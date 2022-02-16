import threading

first=input("Enter first filename:")
sec=input("Enter second filename:")

def readfile(fil):
    f = open(fil,"r")
    Content = f.readlines()
    print("Number of lines in file",fil,"is",len(Content))

t1 = threading.Thread( target = readfile, args =(first,))
t2 = threading.Thread( target = readfile, args =(sec,))  
t1.start()
t2.start()
t1.join()
t2.join()
