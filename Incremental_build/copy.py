import os,glob
import sys
import git
from git import Repo
import subprocess
import pathlib

def main():
    directory = str(sys.argv[1])
    dest = str(sys.argv[2])
    os.system("Robocopy "+directory+" "+dest+"  *.ini")
    

if __name__ == '__main__':
    main()    
