#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Declare an int value and store it in a variable. 

a = int(15)

#Check the type and print the id of the same.
print(a, type(a), id(a))


# In[12]:


#Take one int value between 0 - 256.
#Assign it to two different variables.
a=15
b=15
#Check the id of both the variables. It should come same. Check why?

print(id(a))
print(id(b))


#Take one int value either less than -5 or greater than 256.
#Assign it to two different variables.
a=500
b=500
print(id(a))
print(id(b))
#Check the id of both the variables. It should come different.Check why?



# In[13]:


#Arithmatic Operations on integers
#Take two different intger values.
#Store them in two different variables.
a=15
b=20
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


# In[14]:


#Comparison Operators on integers
#Take two different intger values.
#Store them in two different variables.
#Do below operations on them:-
    #Compare se two numbers with below operator:-
        #Greater than, '>'
print(a>b)        

        #Smaller than, '<'
print(a<b)
        #Greater than or equal to, '>='
print(a>=b)
        #Less than or equal to, '<='
print(a<=b)
#Observe their output(return type should be boolean)


# In[15]:


#Equality Operator
#Take two different intger values.
#Store them in two different variables.
a = 1.5
b=1.2
#Equuate them using equality operator (==, !=)
print(a==b)
print(a!=b)
#Observe the output(return type should be boolean)


# In[16]:


#Logical operators
#Observe the output of below code
#Cross check the output manually

print(10 and 20)       #----------------------------------------->Output is 20
print(0 and 20)        #----------------------------------------->Output is 0
print(20 and 0)        #----------------------------------------->Output is 0
print(0 and 0)         #----------------------------------------->Output is 0

print(10 or 20)        #----------------------------------------->Output is 10
print(0 or 20)         #----------------------------------------->Output is 20
print(20 or 0)         #----------------------------------------->Output is 20
print(0 or 0)          #----------------------------------------->Output is 0

print(not 10)          #----------------------------------------->Output is False
print(not 0)           #----------------------------------------->Output is True


# In[ ]:


#Bitwise Operators
#Do below operations on the values provided below:-
    #Bitwise and(&) -----------------------------------------> 10, 20   -------> Output is 0
    #Bitwise or(|)  -----------------------------------------> 10, 20   -------> Output is 30
    #Bitwise(^)     -----------------------------------------> 10, 20   -------> Output is 30
    #Bitwise negation(~) ------------------------------------> 10       -------> Output is -11
    #Bitwise left shift  ------------------------------------> 10,2     -------> Output is 40
    #Bitwise right shift ------------------------------------> 10,2     -------> Output is 2
#Cross check the output manually


# In[17]:


#What is the output of expression inside print statement. Cross check before running the program.
a = 10
b = 10
print(a is b)          #True or False? true
print(a is not b)      #True or False? false

a = 1000
b = 1000
print(a is b)          #True or False? false
print(a is not b)      #True or False? true


# In[18]:


#What is the output of expression inside print statement. Cross check before running the program. =20
print(10+(10*32)//2**5&20+(~(-10))<<2)


# In[21]:


#Membership operation
#in, not in are two membership operators and it returns boolean value

print('2' in 'Python2.7.8') 
print(10 in [10,10.20,10+20j,'Python'])
print(10 in (10,10.20,10+20j,'Python'))
print(2 in {1,2,3})
print(3 in {1:100, 2:200, 3:300})
print(10 in range(20))


# In[ ]:


#An integer can be represented in binary, octal or hexadecimal form.
#Declare one binary, one octal and one hexadecimal value and store them in three different variables.
#Convert 9876 to its binary, octal and hexadecimal equivalent and print their corresponding value.


# In[22]:


#What will be the outut of following:-
a = 0b1010000
print(a)

b = 0o7436
print(b)

c = 0xfade
print(c)

print(bin(80))

print(oct(3870))

print(hex(64222))

print(bin(0b1010000))

print(bin(0xfade))

print(oct(0xfade))

print(oct(0o7436))

print(hex(0b1010000))

print(hex(0xfade))

