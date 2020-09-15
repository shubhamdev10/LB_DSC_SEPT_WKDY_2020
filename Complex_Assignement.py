#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Declare a complex number and store it in a variable. 
a=5
b=7

c= complex(a,b)
print(c)

#Check the type and print the id of the same.

print(c, type(c), id(c))


# In[8]:


#Arithmatic Operations on complex number
#Take two different complex number.
#Store them in two different variables.
a= 5+7j
b= 6+8j
#Do below operations on them:-
    #Find sum of both numbers
print('addition =', a+b)
    #Find differce between them
print('difference =',a-b)    
    #Find the product of both numbers.
print ('multiplication =', a*b)
    #Find value after dividing first num with second number
print ('value after dividing first num with second number =', a/b)
     #Find the result of first num to the power of second number.
print ( 'power', a**b)    


# In[ ]:


#Comparison Operation not applicable between instance of complex values
#Object reusability concept is not applicable on complex numebr
# ok


# In[9]:


#Equality Operator
#Take two different complex numbers.
#Store them in two different variables.
a= 5+7j
b= 6+8j
#Equuate them using equality operator (==, !=)
print(a==b)
print(a!=b)
#Observe the output(return type should be boolean)






# In[10]:


#Logical operators
#Observe the output of below code
#Cross check the output manually

print(10+20j and 20+30j)    #20+30j    #----------------------------------------->Output is 20+30j
print(0+0j and 20+30j)      #0+0j    #----------------------------------------->Output is 0j
print(20+30j and 0+0j)      #0+0j   #----------------------------------------->Output is 0j
print(0+0j and 0+0j)        #0+0j   #----------------------------------------->Output is 0j

print(10+20j or 20+30j)     #10+20j   #----------------------------------------->Output is 10+20j
print(0+0j or 20+30j)       #20+30j   #----------------------------------------->Output is 20+30j
print(20+30j or 0+0j)       #20+30j  #----------------------------------------->Output is 20+30j
print(0+0j or 0+0j)         #0+0j   #----------------------------------------->Output is 0j

print(not 10+20j)           #False   #----------------------------------------->Output is False
print(not 0+0j)             #True   #----------------------------------------->Output is True


# In[11]:


#What is the output of expression inside print statement. Cross check before running the program.
a = 10+20j
b = 10+20j
print(a is b)       #False   #True or False?
print(a is not b)   #True   #True or False?


# In[12]:


#Membership operation
#in, not in are two membership operators and it returns boolean value

print('2.7' in 'Python2.7.8')                      #True
print(10+20j in [10,10.20,10+20j,'Python'])        #True
print(10+20j in (10,10.20,10+20j,'Python'))        #True
print(30+40j in {1,20.30,30+40j})                  #True
print(30+40j in {1:100, 2.3:200, 30+40j:300})      #True
print(10 in range(20))                             #True

