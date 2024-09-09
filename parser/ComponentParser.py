import uuid
import xml.etree.ElementTree as elementTree
from xml.sax.saxutils import unescape

class ComponentParser:
    c4type, plant_uml_type, c4_name, c4_description, tags, label, style = "", "", "", "", "", "", ""
    c4_tech = ""
    hash_id = ""
    width=240
    height=120
    x = 0
    y = 0
    def __init__(self, plant_uml_type, c4_name, c4_description="", tags="", c4_tech=""):
        self.plant_uml_type = plant_uml_type
        self.c4_name = c4_name
        self.c4_description = c4_description
        self.tags = tags
        self.hash_id = uuid.uuid4().hex
        self.c4_tech = c4_tech

    def __str__(self):
        return self.c4type + "(" + self.plant_uml_type + ",'" + self.c4_name + "','" + self.c4_description + "','" + self.tags + "','" + self.c4_tech + "')"

    def get_type(self):
        return self.plant_uml_type

    def get_c4_type(self):
        return self.c4type

    def get_c4_name(self):
        return self.c4_name

    def get_c4_technology(self):
        return self.c4_tech

    def get_c4_description(self):
        return self.c4_description

    def get_label(self):
        return self.label

    def get_style(self):
        return self.style

    def get_hash_id(self):
        return self.hash_id

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_xml_object(self):
        object_xml = elementTree.Element("object", placeholders="1", c4Name=self.get_c4_name(), c4Type=self.get_c4_type(),
                                         c4Description=self.get_c4_description(), label=self.get_label(), c4Technology=self.get_c4_technology(),
                                         id=self.get_hash_id())
        mx_cell = elementTree.SubElement(object_xml, "mxCell",
                                        style=self.get_style(),
                                        parent="1", vertex="1")
        mx_geometry = elementTree.SubElement(mx_cell, "mxGeometry", x=str(self.x), y=str(self.y), width=str(self.width), height=str(self.height))
        mx_geometry.attrib['as'] = "geometry"
        return object_xml


class Person(ComponentParser):
    def __init__(self, plant_uml_type, c4_name, c4_description="", tags="", c4_tech=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Person"
        self.label = unescape(
            '&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "html=1;fontSize=11;dashed=0;whiteSpace=wrap;fillColor=#083F75;strokeColor=#06315C;fontColor=#ffffff;shape=mxgraph.c4.person2;align=center;metaEdit=1;points=[[0.5,0,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0]];resizable=0;"
        self.width = 200
        self.height = 180

class Person_Ext(ComponentParser):
    def __init__(self, plant_uml_type, c4_name, c4_description="", tags="", c4_tech=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Person"
        self.label = unescape('&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "html=1;fontSize=11;dashed=0;whiteSpace=wrap;fillColor=#6C6477;strokeColor=#4D4D4D;fontColor=#ffffff;shape=mxgraph.c4.person2;align=center;metaEdit=1;points=[[0.5,0,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0]];resizable=0;"
        self.width = 200
        self.height = 180

class System(ComponentParser):
    def __init__(self, plant_uml_type, c4_name, c4_description="", tags="", c4_tech=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Software System"
        self.label = unescape('&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#1061B0;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#0D5091;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class System_Ext(ComponentParser):
    def __init__(self, plant_uml_type, c4_name, c4_description="", tags="", c4_tech=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Software System"
        self.label = unescape('&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#cccccc&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#736782;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class Container(ComponentParser):
    def __init__(self, plant_uml_type, c4_name, c4_tech="", c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Container"
        self.label = unescape('&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#E6E6E6&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;fontSize=11;labelBackgroundColor=none;fillColor=#23A2D9;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#0E7DAD;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class ContainerDb(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech="", c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Container"
        self.label = unescape('&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%:&amp;nbsp;%c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;&lt;font color=&quot;#E6E6E6&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "shape=cylinder3;size=15;whiteSpace=wrap;html=1;boundedLbl=1;rounded=0;labelBackgroundColor=none;fillColor=#23A2D9;fontSize=12;fontColor=#ffffff;align=center;strokeColor=#0E7DAD;metaEdit=1;points=[[0.5,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.5,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];resizable=0;"
        self.width = 240
        self.height = 120

class Component(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech, c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Component"
        self.label = unescape('label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#63BEF2;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class Component_Ext(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech, c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Component"
        self.label = unescape('label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class ComponentDb(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech, c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Component"
        self.label = unescape('label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#63BEF2;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class ComponentDb_Ext(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech, c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Component"
        self.label = unescape('label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class ComponentQueue(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech, c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Component"
        self.label = unescape('label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#63BEF2;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120

class ComponentQueue_Ext(ComponentParser):
    c4_tech = ""
    def __init__(self, plant_uml_type, c4_name, c4_tech, c4_description="", tags=""):
        ComponentParser.__init__(self, plant_uml_type, c4_name, c4_description, tags, c4_tech=c4_tech)
        self.c4type = "Component"
        self.label = unescape('label="&lt;font style=&quot;font-size: 16px&quot;&gt;&lt;b&gt;%c4Name%&lt;/b&gt;&lt;/font&gt;&lt;div&gt;[%c4Type%: %c4Technology%]&lt;/div&gt;&lt;br&gt;&lt;div&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;%c4Description%&lt;/font&gt;&lt;/div&gt;')
        self.style = "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;points=[[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];"
        self.width = 240
        self.height = 120


