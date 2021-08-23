import os
import sys
#import log

#@log.log_error()
def main():
    MYDIR = str(sys.argv[1])
    os.chdir(MYDIR)    
    CHECK_FOLDER = os.path.isdir(MYDIR)
    if CHECK_FOLDER == True:
        print("Target folder already exists.") 
    else:
        os.makedirs("Target")
        print("Target folder created: ", MYDIR)
           

if __name__ == '__main__':
    main()
    
