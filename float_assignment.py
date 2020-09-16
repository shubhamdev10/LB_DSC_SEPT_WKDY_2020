#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Declare a float value and store it in a variable. 

a = 1.5



#Check the type and print the id of the same.

print(a, type(a), id(a))


# In[6]:


#Arithmatic Operations on float
#Take two different float values.
#Store them in two different variables.
a = 1.5
b=1.2
#Do below operations on them:-
    #Find sum of both numbers
print('addition =', a+b)
    #Find differce between them
print('difference =',a-b)    
    #Find the product of both numbers.
print ('multiplication =', a*b)
    #Find value after dividing first num with second number
print ('value after dividing first num with second number =', a/b)
    #Find the remainder after dividing first number with second number
print('Remainder =', a%b)
    #Find the quotient after dividing first number with second number
print ('Quotient =', a//b)
    #Find the result of first num to the power of second number.
print ( 'power', a**b)    


# In[9]:


#Comparison Operators on float
#Take two different float values.
#Store them in two different variables.
a = 1.5
b=1.2

#Do below operations on them:-
    #Compare these two numbers with below operator:-
        #Greater than, '>'
print(a>b)        

        #Smaller than, '<'
print(a<b)
        #Greater than or equal to, '>='
print(a>=b)
        #Less than or equal to, '<='
print(a<=b)
#Observe their output(return type should be boolean)









# In[10]:


#Equality Operator
#Take two different float values.
#Store them in two different variables.
a = 1.5
b=1.2
#Equuate them using equality operator (==, !=)
print(a==b)
print(a!=b)
#Observe the output(return type should be boolean)







# In[11]:


#Logical operators
#Observe the output of below code
#Cross check the output manually

print(10.20 and 20.30)       #both are true and second value taken >Output is 20.3
print(0.0 and 20.30)         #First is false so first value taken->Output is 0.0
print(20.30 and 0.0)         #Goes to till second and second value is false so second is taken>Output is 0.0
print(0.0 and 0.0)           #First is false so first value is taken->Output is 0.0

print(10.20 or 20.30)        #First is True so first value is taken>Output is 10.2
print(0.0 or 20.30)          #Goes to till second and second is true second value is taken->Output is 20.3
print(20.30 or 0.0)          #First is True so first value is taken->Output is 20.3
print(0.0 or 0.0)            #Goes to till second and secod is also false and second value is taken>Output is 0.0

print(not 10.20)             #-Not of true is false->Output is False
print(not 0.0)               #Not of false is True>Output is True


# In[12]:


#What is the output of expression inside print statement. Cross check before running the program.
a = 10.20
b - 10.20
print(a is b)          #True or False? True 10.20<256
print(a is not b)      #True or False? False


# Why the Id of float values are different when the same value is assigned to two different variables
# ex: a = 10.5 b=10.5. but id will be same if I assign the variable having float i.e. a=c then both a anc c's
# Id are same


# In[ ]:


#Bitwise operation is not applicable between instances of float.
## Why the Id of float values are different when the same value is assigned to two different variables
## ex: a = 10.5 b=10.5. but id will be same if I assign the variable having float i.e. a=c then both a anc c's
## Id are same
#Object reusability concept is not applicable on float values.


# In[13]:


#Membership operation
#in, not in are two membership operators and it returns boolean value

print('2.7' in 'Python2.7.8')              #True
print(10.20 in [10,10.20,10+20j,'Python']) #True
print(10.20 in (10,10.20,10+20j,'Python')) # True
print(20.30 in {1,20.30,30+40j})           # True
print(2.3 in {1:100, 2.3:200, 30+40j:300}) # True
print(10 in range(20))                     # True

