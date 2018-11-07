import os
import sys
import xml.etree.ElementTree as et
import re

base_path = os.path.dirname(os.path.realpath(__file__))


xml_file = os.path.join(base_path, sys.argv[1])
#inintialize
parseFile = open (xml_file,'r')
data = parseFile.read()
parseFile.close()
data_list = list(data)
for i in range(len(data_list)):
    if data_list[i] == '&':
        data_list[i] = ' '
    elif data_list[i] == ';':
        data_list[i] = ' '
data_1 = ''.join(str(x)for x in data_list)

#root is now the root of xml file
root = et.fromstring(data_1)

#terms
newfile = open('terms.txt','w')
search = ['author','title','journal','booktitle','publisher']
for child in root:
        for i in search:
            terms = child.findall(i)
            for a in terms:
                a_text = a.text
                a_text.strip()
                a_list = re.findall(r"[\w']+",a_text)
                if a_list:
                    for j in range(len(a_list)):
                            match = a_list[j]
                            if match:
                                if ((i == 'author') and (len(match)>2)):
                                    output = 'a-'+match.lower()+':'+child.attrib['key']+'\n'
                                    newfile.write(output)
                                    #print(output)
                                elif (i == 'title')and (len(match)>2):
                                    output = 't-'+match.lower()+':'+child.attrib['key']+'\n'
                                    newfile.write(output)
                                    #print(output)
                                elif (len(match.lower())>2):
                                    output = 'o-'+match.lower()+':'+child.attrib['key']+'\n'
                                    newfile.write(output)
                                    #print(output)
                                else:
                                    pass
            
newfile.close()


#years
newfile = open('years.txt','w')
for child in root.iter(tag = 'article'):
    yearnum = child.find('year').text
    attrib = child.attrib
    ouptut = yearnum+':'+attrib['key']+'\n'
    newfile.write(ouptut)
    
for child in root.iter(tag = 'inproceedings'):
    yearnum = child.find('year').text
    attrib = child.attrib
    ouptut = yearnum+':'+attrib['key']+'\n'
    newfile.write(ouptut)
newfile.close()


#recs
parseFile = open(xml_file,'r')
line = parseFile.readlines()
parseFile.close()
newfile = open('recs.txt','w')
cnt = 1
for child in root:
    output = child.attrib['key']+':'+line[cnt]
    cnt+=1
    newfile.write(output)
newfile.close()