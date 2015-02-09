import json, requests, lxml
import os
from bs4 import BeautifulSoup
import shutil

print "Enter the round number : "
CF = raw_input()

url = "http://codeforces.com/contest/"+CF+"/problems"
data = requests.get(url)

soup = BeautifulSoup(data.text)
        
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
    
    if (os.path.exists(CF+"/"+chr(ord('A')+counter))):
        print "Folder Exists"
    else:
        os.makedirs(CF+"/"+chr(ord('A')+counter))

    shutil.copyfile("f.bat",CF+"/"+chr(ord('A')+counter)+"/f.bat")
    shutil.copyfile("template.cpp", CF+"/"+chr(ord('A')+counter)+"/prog.cpp" )
    
    detach_dir = CF+"/"+chr(ord('A')+counter)+"/"
    att_path = os.path.join(detach_dir, chr(ord('A')+counter)+".cpp")
    counter+=1
    incounter = 1
    for item in div.findAll('pre'):
        if incounter%2 == 1:
            att_path = os.path.join(detach_dir, "in"+str(incounter/2)+".txt")
            print att_path
            f = open(att_path, 'wb')
        else:
            att_path = os.path.join(detach_dir, "out"+str((incounter/2)-1)+".txt")
            print att_path
            f = open(att_path, 'wb')
        incounter+=1
        item = str(item).replace("<pre>", "")
        item = str(item).replace("</pre>", "")
        item = str(item).replace("<br/>", "\n")
        f.write(item)