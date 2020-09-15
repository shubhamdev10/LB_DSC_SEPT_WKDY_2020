#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Declare a boolean value and store it in a variable. 

a =True
b= bool(a)

#Check the type and print the id of the same.

print(b, type(b), id(b))


# In[2]:


#Take one boolean value between 0 - 256.
#Assign it to two different variables.
a =1
b=1

#Check the id of both the variables. It should come same. Check why?
print(id(a))
print(id(b))


# In[4]:


#Arithmatic Operations on boolean data
#Take two different boolean values.
a =0
b=1
#Store them in two different variables.



#Do below operations on them:-
    #Find sum of both values
print('addition =', a+b)

    #Find differce between them
print('difference =',a-b)    

    #Find the product of both.
print ('multiplication =', a*b)

    #Find value after dividing first value with second value
print ('value after dividing first num with second number =', a/b)
    
    #Find the remainder after dividing first value with second value
print('Remainder =', a%b)
    
    #Find the quotient after dividing first value with second value
print ('Quotient =', a//b)
    
    #Find the result of first value to the power of second value.
print ( 'power', a**b)        










    


# In[6]:


#Comparison Operators on boolean values
#Take two different boolean values.
#Store them in two different variables.

a =0
b=1
#Do below operations on them:-
    #Compare these two values with below operator:-
        #Greater than, '>'
print(a>b)
        #less than, '<'
print(a<b)
        #Greater than or equal to, '>='
print(a>=b)
        #Less than or equal to, '<='    
print(a<=b)
#Observe their output(return type should be boolean)


# In[7]:


#Equality Operator
#Take two different boolean values.
#Store them in two different variables.

a =0
b=1

#Equuate them using equality operator (==, !=)


#Equuate them using equality operator (==, !=)
print(a==b)
print(a!=b)
#Observe the output(return type should be boolean)


# In[8]:


#Logical operators
#Observe the output of below code
#Cross check the output manually

print(True and True)        #----------------------------------------->Output is True
print(False and True)        #----------------------------------------->Output is False
print(True and False)        #----------------------------------------->Output is False
print(False and False)       #----------------------------------------->Output is False

print(True or True)          #----------------------------------------->Output is True
print(False or True)         #----------------------------------------->Output is True
print(True or False)         #----------------------------------------->Output is True
print(False or False)        #----------------------------------------->Output is False

print(not True)              #----------------------------------------->Output is False
print(not False)             #----------------------------------------->Output is True


# In[9]:


#Bitwise Operators
#Do below operations on the values provided below:-
    #Bitwise and(&) -----------------------------------------> True, True    -------> Output is True
    


    #Bitwise or(|)  -----------------------------------------> True, False   -------> Output is True



    #Bitwise(^)     -----------------------------------------> True, False   -------> Output is True

  

    #Bitwise negation(~) ------------------------------------> True          -------> Output is -2

   

    #Bitwise left shift  ------------------------------------> True,2        -------> Output is 4



    #Bitwise right shift ------------------------------------> True,2        -------> Output is 0



#Cross check the output manually










# In[10]:


#What is the output of expression inside print statement. Cross check before running the program.
a = True
b = True
print(a is b)          #True or False?   #true
print(a is not b)      #True or False? false

a = False
b = False
print(a is b)          #True or False? true
print(a is not b)      #True or False? false


# In[11]:


#Membership operation
#in, not in are two membership operators and it returns boolean value

print(True in [10,10.20,10+20j,'Python', True])
print(False in (10,10.20,10+20j,'Python', False))
print(True in {1,2,3, True})
print(True in {True:100, False:200, True:300})
print(False in {True:100, False:200, True:300})


# In[ ]:




