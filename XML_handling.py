import xml.etree.ElementTree as ET

#parse the xml file
ref = ET.parse("C:\\Users\\Prateek.THINKPAD\\Downloads\\file.xml")

#get the root node of the xml file
node = ref.getroot()
#printing the root note tag
print(node.tag)

#printing the child node tag of root node
print(node.getchildren()[0].tag)

#printing the text value of child node tag of root node
print(node.getchildren()[0].getchildren()[1].text)
#second child node of root
print(node.getchildren()[0].getchildren()[1].tag)
print(node.getchildren()[0].getchildren()[2].text)

#large xml file with multiple nodes
file_ref = ET.parse("C:\\Users\\Prateek.THINKPAD\\Downloads\\file_xml.xml")
root_node = file_ref.getroot()
store_in_list = []
#getting all the data from xml and storing it in form of list or dict
for element in root_node.getchildren():
    dictionary = {}
    for subelement in element.getchildren():
        dictionary[subelement.tag] = subelement.text
    store_in_list.append(dictionary)
print(store_in_list)