import uuid
import xml.etree.ElementTree as elementTree
from xml.sax.saxutils import unescape

class RelationParser:
    source, target, c4_description, c4_tech = "", "", "", ""
    c4_type = "Relationship"
    plant_uml_type = ""
    label, style, hash_id = "", "", ""
    c4_technology_div = "&lt;div style=&quot;text-align: center&quot;&gt;[%c4Technology%]&lt;/div&gt;"
    def __init__(self, source, target, c4_description="", c4_tech=""):
        self.source = source
        self.target = target
        self.c4_description = c4_description
        self.c4_tech = c4_tech
        c4_technology_div = self.c4_technology_div if self.c4_tech else ""
        self.label = unescape('&lt;div style=&quot;text-align: left&quot;&gt;&lt;div style=&quot;text-align: center&quot;&gt;&lt;b&gt;%c4Description%&lt;/b&gt;&lt;/div&gt;'+ c4_technology_div +'&lt;/div&gt;')
        self.style = "endArrow=blockThin;html=1;fontSize=10;fontColor=#404040;strokeWidth=1;endFill=1;strokeColor=#828282;elbow=vertical;metaEdit=1;endSize=14;startSize=14;jumpStyle=arc;jumpSize=16;rounded=0;"
        self.hash_id = uuid.uuid4().hex

    def __str__(self):
        return self.source + " -> " + self.c4_description + " -> " + self.target + "\n" + self.c4_tech + " -> " + self.hash_id

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_c4_description(self):
        return self.c4_description

    def get_c4_technology(self):
        return self.c4_tech

    def get_label(self):
        return self.label

    def get_style(self):
        return self.style

    def get_c4_type(self):
        return self.c4_type

    def get_hash_id(self):
        return self.hash_id

    def set_source(self, source):
        self.source = source

    def set_target(self, target):
        self.target = target

    def get_plant_uml_type(self):
        return self.plant_uml_type

    def get_xml_object(self):
        object_xml = elementTree.Element("object", placeholders="1", c4Type=self.get_c4_type(), c4Technology=self.get_c4_technology(), c4Description=self.get_c4_description(), label=self.get_label(), id=self.get_hash_id())
        mx_cell = elementTree.SubElement(object_xml, "mxCell",
                                        style=self.get_style(),
                                        parent="1",source=self.get_source(), target=self.get_target(), edge="1")
        mx_geometry = elementTree.SubElement(mx_cell, "mxGeometry", width="240", relative="1")
        mx_geometry.attrib['as'] = "geometry"
        mx_point = elementTree.SubElement(mx_geometry, "mxPoint", x="140", y="230")
        mx_point.attrib['as'] = "sourcePoint"
        mx_point = elementTree.SubElement(mx_geometry, "mxPoint", x="140", y="230")
        mx_point.attrib['as'] = "targetPoint"
        return object_xml

class Rel_U(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel_U"

class Rel_D(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel_D"

class Rel_R(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel_R"

class Rel_L(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel_L"

class Rel(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel"

class Rel_Back(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel_Back"

class Rel_Neighbor(RelationParser):
    def __init__(self, source, target, c4_description="", c4_tech=""):
        RelationParser.__init__(self, source, target, c4_description, c4_tech)
        self.plant_uml_type = "Rel_Neighbor"
