import xml.etree.ElementTree as xml
import time


def WriteXML (fileName,leftLenght,rightLenght):
    file = fileName + ".xml"

    root=xml.Element("Lenghts")
    ll=xml.Element("Left_Line")
    rl=xml.Element("Right_Line")

    root.append(ll)                     #Bu komutla ll yi rootun alt elementi oldu
    root.append(rl)                     #Bu komutla rl yi rootun alt elementi oldu

    amount1=xml.SubElement(ll,"Amount")
    amount1.text=str(leftLenght)

    amount2 = xml.SubElement(rl, "Amount")
    amount2.text =str(rightLenght)

    tree=xml.ElementTree(root)

    with open(file,"wb") as files:
        tree.write(files)

def ReadXML (fileName):
    file=fileName+".xml"
    try:
        tree = xml.parse(file)
    except:
        time.sleep(0.01)
        tree = xml.parse(file)
    root = tree.getroot()

    tag = root.tag

    attr = root.attrib

    for c in root.findall("Left_Line"):
        att = c.attrib

        leftlenght = c.find("Amount").text
        print("Amount Left :", leftlenght)

    for c in root.findall("Right_Line"):
        att = c.attrib

        rightlenght = c.find("Amount").text
        print("Amount Right :", rightlenght)

    return float(leftlenght),float(rightlenght)
