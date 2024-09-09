import xml.etree.ElementTree as elementTree
import networkx as nx
import importlib
import re

from parser.ComponentParser import ComponentParser
from parser.RelationParser import RelationParser

component_dictionary = ('Person', 'Person_Ext',
                        'System', 'SystemDb',  'SystemDb', 'SystemDb', 'System_Ext', 'SystemDb_Ext', 'SystemQueue_Ext',
                        'Container', 'ContainerDb', 'ContainerQueue', 'Container_Ext', 'ContainerDb_Ext', 'ContainerQueue_Ext',
                        'Component', 'ComponentDb', 'ComponentQueue', 'Component_Ext', 'ComponentDb_Ext', 'ComponentQueue_Ext')
relation_dictionary = ('Rel_U', 'Rel_D', 'Rel_R', 'Rel_L', 'Rel', 'Rel_Back', 'Rel_Neighbor')


class DrawioParser:
    component_list = {}
    relation_list = []
    # Criar um grafo
    graph_components = nx.Graph()
    # Tamanho da escala para ajustar os componentes (aumentando ou diminuindo, os objetos ficam distantes ou próximos, respectivamente)
    scale = 700
    def __init__(self):
        pass

    def add_component(self, object_class):
        self.component_list[object_class.get_type()] = object_class

    def add_relation(self, object_class):
        self.relation_list.append(object_class)

    def __str__(self):
        result = ''
        for index, object_class in self.component_list.items():
            result += str(object_class) + "\n"
        return result


    def parser(self, path_file_plantuml):
        self.component_list = {}
        self.relation_list = []
        plant_uml_file = open(path_file_plantuml)
        plant_uml_content = plant_uml_file.read()
        for line in plant_uml_content.splitlines():
            line = line.strip()
            line_list = [p.strip() for p in re.split("[,()](?=(?:(?:[^\"]*\"){2})*[^\"]*$)", line) if p.strip()]
            new_line = ""
            index = 0
            for line_striped in line_list:
                line_list[index] = line_striped.replace('$', '').replace('"', '') if line_striped[
                                                                                     0:1] == '"' or index == 0 or line_striped[
                                                                                                                  1:4] == 'tags' else f'{line_striped.replace("$", "")}'.replace(
                    '"', "")
                if index == 0:
                    if line_list[index] in component_dictionary or line_list[index] in relation_dictionary:
                        new_line += line_list[index] + "("
                    else:
                        break
                else:
                    if index == len(line_list) - 1:
                        end_word = ')'
                    else:
                        end_word = ','

                    new_line += line_list[index] + end_word
                index += 1
                if index == len(line_list):
                    module_name = 'parser.ComponentParser' if line.startswith(
                        component_dictionary) else 'parser.RelationParser'
                    module = importlib.import_module(module_name)
                    class_name = line_list[0]
                    if module_name == 'parser.ComponentParser':
                        plant_uml_type = line_list[1]
                        c4_name = line_list[2] if len(line_list) >= 3 else ''
                        c4_description = line_list[3] if len(line_list) >= 4 else ''
                        c4_tech = line_list[4] if len(line_list) >= 5 else ''
                        tags = line_list[5].replace('tags', '').replace('=', '').replace('"', '').strip() if len(
                            line_list) >= 6 else ''
                        # print(class_name, c4_name, c4_tech, c4_description, tags)
                        instance: ComponentParser = getattr(module, class_name)(plant_uml_type=plant_uml_type,
                                                                                c4_name=c4_name,
                                                                                c4_description=c4_description,
                                                                                c4_tech=c4_tech,
                                                                                tags=tags)
                        self.add_component(instance)
                    else:
                        source = line_list[1]
                        target = line_list[2] if len(line_list) >= 3 else ''
                        c4_description = line_list[3] if len(line_list) >= 4 else ''
                        c4_tech = line_list[4] if len(line_list) >= 5 else ''
                        # print(class_name, source, target, c4_tech, c4_description)
                        instance: ComponentParser = getattr(module, class_name)(source=source, target=target,
                                                                                c4_description=c4_description,
                                                                                c4_tech=c4_tech)
                        self.add_relation(instance)

    def generate_drawio(self, path_file_drawio=None):
        mx_file = elementTree.Element('mxfile', host="drawio-plugin",
                                     agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                                     modified="2024-09-05T17:59:54.214Z", version="22.1.22",
                                     etag="u7vjfVFp5oDaGUMwaua2", type="embed")
        diagram = elementTree.SubElement(mx_file, "diagram", name="Página", id="zIcZK3G4L6XBM3bqiY_4")
        mx_graph_model = elementTree.SubElement(diagram, "mxGraphModel", dx="838", dy="799", grid="1", gridSize="10",
                                              guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                              pageScale="1", pageWidth=str(int(self.scale*2.2)), pageHeight=str(int(self.scale*2.2)), math="0", shadow="0")
        root = elementTree.SubElement(mx_graph_model, "root")
        elementTree.SubElement(root, "mxCell", id="0")
        elementTree.SubElement(root, "mxCell", id="1", parent="0")

        # Adiciona os objetos no grafo
        for object_class in self.component_list.values():
            self.graph_components.add_node(object_class)

        # Adiciona a relação entre eles
        for relation in self.relation_list:
            relation : RelationParser = relation
            source : ComponentParser = self.component_list[relation.get_source()]
            target : ComponentParser = self.component_list[relation.get_target()]
            self.graph_components.add_edge(source, target)

        # Reposiciona os elementos, escala x e y (que vai de -1 até 1)
        pos = nx.spring_layout(self.graph_components)
        # Atualiza o objeto na lista de componentes
        for obj, arr in pos.items():
            arr = arr * self.scale
            arr = arr + self.scale
            component : ComponentParser = obj
            component.set_x(int(arr[0]))
            component.set_y(int(arr[1]))
            self.component_list[component.get_type()] = component

        # Adiciona os componentes com X e Y ajustados no xml do Drawio
        for object_class in self.component_list.values():
            object_xml = object_class.get_xml_object()
            root.append(object_xml)

        # Adiciona as setas de relação
        for relation in self.relation_list:
            relation : RelationParser = relation
            source : ComponentParser = self.component_list[relation.get_source()]
            target : ComponentParser = self.component_list[relation.get_target()]
            self.graph_components.add_edge(source, target)
            relation.set_source(source.get_hash_id())
            relation.set_target(target.get_hash_id())
            object_xml = relation.get_xml_object()
            root.append(object_xml)

        tree = elementTree.ElementTree(mx_file)
        if path_file_drawio:
            tree.write(path_file_drawio)
            return None
        else:
            return elementTree.tostring(mx_file, encoding='unicode')
