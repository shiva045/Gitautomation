import os,glob
import git
import pathlib
import sys
from git import Repo

def main():
    var1 = str(sys.argv[1])
    Dest_loc = str(sys.argv[2])
    entries = os.listdir(Dest_loc)
    with open(var1) as file_1:
        for i in file_1.readlines():
            var1 = i.split(',')
            commitId = var1[0].strip()
            repo_name= var1[1].strip()
            repo_url = var1[2].strip()
            if(repo_name in entries):
                my_repo = git.Repo(Dest_loc + repo_name)
                print(my_repo.git.reset('--hard'))
                print(my_repo.remotes.origin.pull('master'))
                print(my_repo.git.checkout(commitId))
                print("Repo pulled successfully")  
            else:
                path = Dest_loc + repo_name
                repo=git.Repo.clone_from(repo_url, path)
                repo.git.checkout(commitId)
                print("Repo cloned  successfully..!")

if __name__ == '__main__':
    main()         
