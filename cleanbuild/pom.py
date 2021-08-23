from xml.dom import minidom
import xml.dom.minidom as md
import xml.dom.minidom
import glob
import os
from lxml import etree
import sys
#import log

#@log.log_error()
def main():
    ver_name= str(sys.argv[1])       				    
    lib_path= str(sys.argv[2])						
    dir_path=str(sys.argv[3])    
    for filename in os.listdir(dir_path):        
        var2=dir_path + "\\" + filename
        for i in os.listdir(var2):           
            if i == "pom.xml":                
                fullname= os.path.join(var2, i)
                data=md.parse(fullname)               
                alltag = data.getElementsByTagName("vdspath")
                if(alltag.length > 0):                    
                    data.getElementsByTagName("version")[0].childNodes[ 0 ].nodeValue = ver_name
                    data.getElementsByTagName("vdspath")[0].childNodes[ 0 ].nodeValue = lib_path 
                    data.getElementsByTagName("productlibpath")[0].childNodes[ 0 ].nodeValue = lib_path
                    data.getElementsByTagName("commonlibpath")[0].childNodes[ 0 ].nodeValue = lib_path
                else:                    
                    data.getElementsByTagName("version")[0].childNodes[ 0 ].nodeValue = ver_name
                    data.getElementsByTagName("productlibpath")[0].childNodes[ 0 ].nodeValue = lib_path
                    data.getElementsByTagName("commonlibpath")[0].childNodes[ 0 ].nodeValue = lib_path
                with open(fullname,"w")as fs:                   
                    fs.write(data.toxml())
                    fs.close()
                      
    print("file updated successfully..!")        

       
       
if __name__=="__main__":
    main();
