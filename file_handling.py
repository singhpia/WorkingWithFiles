#to print contents of file in same directory
file_handle = open("file.txt") #creates object <class TextIOWrapper>
print(type(file_handle))
dir(file_handle)
#access content of file line by line
#using loop
n=1
print(file_handle)
for line in file_handle:
    print("Line {0} of file is \n{1}".format(n,line))
    n+=1
file_var = file_handle.read() #passes all contents of file in one go in form of string <class str>
print("content of file_var\n",file_var) #sends content of file to python console

#another way of printing file is-
file_handle2 = open("file.txt").read() # <class str>
print(type(file_handle2))
print("content of file_handle2\n",file_handle2)

#access content of file line by line

#using readline()
new = open("file.txt",'r')
file_var2 = new.readline()
# print("Line 1st is {0}".format(file_var2))
print("file_var2 ",file_var2)

#using readlines
file_var3 = new.readlines(8)
print(file_var3)

#creating a new file using w
create_file = open("file2.txt",'w')
create_file.write('my name is Priya Singh\n This is a sample text file.')
print(create_file)
#opening file in append and read mode
create_file = open("file2.txt",'a+')
#appending content to existing file using append and read mode
print(create_file.write("\nadd this too"))
#printing contents of file
print("after adding content printing - ",create_file.readlines())
#returning the cursor location
print(create_file.tell())
#bringing the cursor to beginning of file
print(create_file.seek(0))
print(create_file.read())

#automatic memory deallocation via with open function:
with open('file3.txt','a+') as file_ref:
    print(type(file_ref))
    file_ref.write("this is an added line via with open")

with open('file3.txt') as file_ref:
    a = file_ref.read()
    print(a)