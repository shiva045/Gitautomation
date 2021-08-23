# Importing difflib
import difflib
import sys
import os

source_path = str(sys.argv[1])
dest_path = str(sys.argv[2])
Tg_loc = str(sys.argv[3])

def main():
        with open(source_path) as file_1: 
                with open(dest_path) as file_2:
                        difference = set(file_2).difference(file_1)
                        difference.discard('\n')
                        with open(Tg_loc ,'w') as file_out:
                                for line in difference:
                                        file_out.write(line)
                                

def prepend_line(file_name, line):
    dummy_file = "file_name " + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)

if __name__ == '__main__': 
    main()
    prepend_line(Tg_loc, "d03ba23e,MACK_LIB,http://192.168.10.130/MACK_NYK/MACK_LIB.git")
            
