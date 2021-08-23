import os,glob
import git
import pathlib
import sys
from git import Repo

def main():
    repo_name=str(sys.argv[1])
    repo_url =str(sys.argv[2])
    clone_path =str(sys.argv[3])
    commitId=str(sys.argv[4])
    entries = os.listdir(clone_path)
    if(repo_name in entries):
        my_repo = git.Repo(clone_path + repo_name)
        print(my_repo.remotes.origin.pull('master'))
        print(my_repo.git.checkout(commitId))
        print("Repo pulled successfully")  
    else:
        path = clone_path + repo_name
        repo=git.Repo.clone_from(repo_url, path)
        repo.git.checkout(commitId)
        print("Repo cloned  successfully..!")
    



if __name__ == '__main__':
    main()            
