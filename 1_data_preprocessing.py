import os
import xml.etree.ElementTree as ET
def read_data(read_dir,write_dir):
    f = open(write_dir, 'w')
    for filename in os.listdir(read_dir):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(read_dir, filename)
        tree = ET.parse(fullname)
        root = tree.getroot()
        for abstract in root.iter('AbstractText'):
            label, NlmCategory,text='','',''
            if abstract.attrib:
                label = abstract.attrib['Label'] if 'Label' in abstract.attrib else 'NA'
                NlmCategory = abstract.attrib['NlmCategory'] if 'NlmCategory' in abstract.attrib else 'NA'
                text = abstract.text.encode('utf-8')
                f.write(label + ','+ NlmCategory + ',"' + text + '"\n')
    f.close()

if __name__ == "__main__":
    read_dir = '/Users/qingping/Documents/Research/Dissertation/Argument_Sentence_Classification/Pubmed/raw_xml_data'
    write_dir = '/Users/qingping/Documents/Research/Dissertation/Argument_Sentence_Classification/Pubmed/labeled_data/labeled_all.csv'
    read_data(read_dir,write_dir)