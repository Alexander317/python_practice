import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

verbCounter = 0
conjCounter = 0

for child in root.findall('text'):
    paragraphs = child.find('paragraphs')
    for paragraph in paragraphs:
        sentences = paragraph.findall('sentence')
        for sentence in sentences:
            text = sentence.find('source')
            tokens = sentence.find('tokens')
            for token in tokens:
                word = token.attrib['text']
                vs = token.findall('tfr')
                for v in vs:
                    ls = v.find('v')
                    for l in ls:
                        gs = l.findall('g')
                        if word == 'может':
                            if gs[0].attrib['v'] == 'CONJ':
                                conjCounter += 1
                            elif gs[0].attrib['v'] == 'VERB':
                                verbCounter += 1

print("'может' as conj: ", conjCounter)
print("'может' as verb: ", verbCounter)
