# import numpy as np

# N = int(input())

# ls = list(map(int,input().split()))

 arr = np.array(ls,dtype=float)
 print(arr[::-1])

 import numpy as np

 ls = list(map(int,input().split()))
 arr= np.array(ls)
 arr.shape=3,3
 print(arr)
 import numpy

 numpy.set_printoptions(sign=' ')
 print(numpy.eye(*map(int, input().split())))

 import numpy as np

 a = np.array([1,2,3,4], float)
 b = np.array([5,6,7,8], float)

 print (a + b)           
 print (np.add(a, b))          

 print (a - b)                     
 print (np.subtract(a, b))      

 print (a * b)                     
 print (np.multiply(a, b))      

 print (a / b)                     
 print (np.divide(a, b))     

 print (a % b)                    
 print (np.mod(a, b))           

 print (a**b)                      
 print (np.power(a, b))

 import numpy as np

 my_array = np.array([[1,2,3],
                         [4,5,6]])
 print (np.transpose(my_array))

 import numpy as np 

 a,b=map(int, input().split())
 lst1=list(map(int, input().split()))
 lst2=list(map(int, input().split()))
 m1= np.array(lst1).reshape(a,b)
 m2= np.array(lst2).reshape(a,b)
 out1=np.add(m1,m2)
 out2=np.subtract(m1,m2)
 out3=np.float_divide(m1,m2)
 out4=np.multiply(m1,m2)
 out5=np.power(m1,m2)
 print(out1)
 print(out2)
 print(out3)
 print(out4)
 print(out5)

 import numpy as np

 r,c = map(int, input().split())
 a=[]
 for i in range(0,r):
     b=list(map(int, input().split()))
     a.append(b)
 arr= np.array(a)
 print(arr.T)
 print(arr.flatten())
