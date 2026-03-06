try:
    srcfile=open("readfrom.txt","r")
    temp=srcfile.readline()
    print(temp)
    print("before seeking:",srcfile.tell())
    srcfile.seek(0)
    print("after seeking:",srcfile.tell())
    temp2=srcfile.readlines()
    print(temp2)
    srcfile.seek(0)
    temp3=srcfile.read()
    print(temp3)

    destfile=open("writeto.txt","a")
    destfile.flush()
except FileNotFoundError:
    print("file doesn't exist on Disk!")
srcfile.close()
destfile.close()
