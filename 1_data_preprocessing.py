import os
import xml.etree.ElementTree as ET
def read_data(read_dir,write_dir):
    f = open(write_dir, 'w')
    print('start reading...')
    for filename in os.listdir(read_dir):
        print(filename)
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(read_dir, filename)
        tree = ET.parse(fullname)
        root = tree.getroot()
        for abstract in root.iter('AbstractText'):
            label, NlmCategory,text='','',''
            if abstract.attrib and abstract.text and 'Label' in abstract.attrib and 'NlmCategory' in abstract.attrib:
                label = abstract.attrib['Label'].encode('utf-8')
                f.write(label + ',')
                NlmCategory = abstract.attrib['NlmCategory'].encode('utf-8')
                f.write(NlmCategory + ',"')
                text = abstract.text.replace('\"','').replace('\'','').encode('utf-8')
                f.write(text + '"\n')
    f.close()

if __name__ == "__main__":
    read_dir = '/Users/qingping/Documents/Argumentative_Zoning/Pubmed_data/updated/xml'
    write_dir = '/Users/qingping/Documents/Argumentative_Zoning/Pubmed_data/updated_labeled/labeled_all.csv'
    print("hahaha, thats for sure \"honey\"".replace('\"','').replace('\'','').encode('utf-8'))
    read_data(read_dir,write_dir)