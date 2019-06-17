'''
A program to demonstrate the creation of a directory and a file in it and the performing read write operations on the file using os library
'''


import os
print(os.getcwd)

class createfile:
    path=""
    __file_name=''
    __input_text=''
    def read_and_create(self):
        '''
        an extra '\' is used to change the original meaning of '\'
        '''
        self.path="C:\\Users\\Aryan Kumar\\Desktop\\PythonProgramming\\new1" 
        # 777 is used to grant read ,write,execute permission to all 
        os.mkdir(self.path,777)
        os.chdir(self.path)
        self.__file_name=input("Enter the file name, you want to create: ")
        f=open(self.__file_name,'w')
        self.__input_text=input("Enter the text : ")
        f.write(self.__input_text)
        f.close()

    def read_file_content(self):
        x=open(self.__file_name,'r')
        print(x.read())


o=createfile()
o.read_and_create()
o.read_file_content()
