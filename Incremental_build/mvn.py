import os
import time
import sys
import shutil
#import log

#@log.log_error()
def main():
    directory = str(sys.argv[1])   				        #Enter the repository available path 
    dest = str(sys.argv[2])						#Enter the Target folder path where the build binary going to deploy
    for filename in os.listdir(directory):
        #print(filename)
        v=directory + "\\" +filename
        os.chdir(v)
        for i in os.listdir(v):
            if i == "pom.xml":
                os.system('cmd /k "mvn clean package -DskipTests && exit"')
                #print("build successfuly..!")  
                var2 =v+'\\target'
                os.system("Robocopy "+var2+" "+dest+" *.jar *.war")
                      
if __name__ == '__main__':
    main()
    
    
    

    
