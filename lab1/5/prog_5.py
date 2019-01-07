# 5. Assume that we have a folder with name ‘mix-files’, which contains many sub folders. 
# Each sub folders may contain ‘n’ number of different types of files (.java, .py, .c, .txt, .html … etc). 
# Write python script which identifies different types of files under all sub folders of ‘mix-files’ folder. 
# After identifying different types of file, create sub folders for each type of files and move the corresponding type of files that folders ie.  
# ‘.c’ files to ‘c-folder’, .java files to ‘java-folder’ etc.

import os

def main():

    for root, dirs, files in os.walk("mix-files", topdown=False):
        for name in files:
            filename, extention = os.path.splitext(name)

            #create extention dir if not present
            extention = extention.strip('.')
            if not os.path.exists(extention):
                os.makedirs(extention)
                
            os.rename(os.path.join(root, name), os.path.join(extention, name))

if __name__ == "__main__":
    main()