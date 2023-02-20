import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("emp.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    expert = doc.getElementsByTagName("expertise")
    print(len(expert))
    for skill in expert:
        print(skill.getAttribute("name"))
        
    newSkill = doc.createElement("expertise")
    newSkill.setAttribute('name',".net")
    doc.firstChild.appendChild(newSkill)
    expert = doc.getElementsByTagName("expertise")
    for skill in expert:
        print(skill.getAttribute("name"))
    
main()