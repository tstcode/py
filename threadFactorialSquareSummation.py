import threading

def cal_sqre(*num): 
    for n in num:
        print(' Square is : ', n * n)  
  
def cal_fact(*num):
    for n in num:    
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print("factorial of",n,"=",fact)
  
arr=eval(input("Enter numbers"))
t1 = threading.Thread( target = cal_sqre, args =arr)
t2 = threading.Thread( target = cal_fact, args =arr)  
t1.start()
t2.start()
t1.join()
t2.join()
