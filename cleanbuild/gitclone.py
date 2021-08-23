import os,glob,shutil
import pathlib
import configparser
import git
import sys
from git import Repo
#import log


#@log.log_error()
def main():
    
    parser = configparser.ConfigParser()
    
       #print (parser.read('release.ini'))
    var1 = str(sys.argv[1])
    parser.read(var1)
    Dest_loc = str(sys.argv[2])       	#Enter the path where the repository need to be cloned./pull
    entries = os.listdir(Dest_loc)
    for sect in parser.sections():
        
        print('Section:', sect)
        for v in parser.items(sect):
            
            raw_commit = v[0].split(',')
            commitId = raw_commit[0]
            repo_name=raw_commit[1]           
            if(repo_name in entries):
                my_repo = git.Repo(Dest_loc + repo_name)
                print('Remotes:')
                for remote in my_repo.remotes:
                    print(f'- {remote.name} {remote.url}')
                    print(my_repo.git.reset('--hard'))
                    print(my_repo.remotes.origin.pull('master'))
                    print(my_repo.git.checkout(commitId))
                    print("Repo pulled successfully")                                              
            else:
                
                baseUrlPath = v[1]
                gitId       = raw_commit[2]
                full_path  = gitId+ ":"+baseUrlPath
                path = Dest_loc + repo_name      
                repo=git.Repo.clone_from(full_path, path)
                repo.git.checkout(commitId)
                print("Repo cloned  successfully..!")
       

if __name__ == '__main__':
    
    main()                 
                                      
      
   
                  
               

