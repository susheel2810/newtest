'''
Created on Apr 21, 2017

@author: LENOVO
'''

if __name__ == '__main__':
    file=open("C:\\Users\\LENOVO\\sushi.txt","r")
    print(file.read())
    print(file.tell())
    for line in file:
        print(line)
        
    print("File Name:" +file.name)
    print("Mode:"+file.mode)
    print("File Closed:"+str(file.closed))
    file.close()
    
