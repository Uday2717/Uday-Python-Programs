file=open("tops1.txt","w")
file.write("This is file write operation using python")
file.close()
print("File Written successfully")
print("*************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*************************************")

file=open("tops1.txt","a")
file.write("This file is now appended.")
file.close()
print("File Appended Successfully")
print("*************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()

