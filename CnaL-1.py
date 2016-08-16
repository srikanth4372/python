
import datetime as dt

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

p = int(input("Value of N? "))
tic = dt.datetime.now()
if p <= 0:
   print("Plese enter a correct position -----")
   exit()
else:
   for i in range(p+1):
   	 a =recur_fibo(i)
toc = dt.datetime.now()
print ("Nth position of Fibonacci sequence is %s and time taken is %s microseconds" %(a,(toc-tic).microseconds))

