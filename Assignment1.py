#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q6)You can turn a word into pig-Latin using the following two rules (simplified): 
• If the word starts with a consonant, move that letter to the end and append 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'. 
• If the word starts with a vowel, simply append 'way' to the end of the word. For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant). 
Write a function pig() that takes a word (i.e., a string) as input and returns its pig- Latin form. Your function should still work if the input word contains upper case characters. Your output should always be lower case however.


# In[21]:


# list of vowels
vowels = ['a','e','i','o','u']
def pig(word):
    
    #checking if the word starts with vowel or not
    if word[0].lower() in vowels:
        print(word.lower() + 'way')
    else:
        first_letter = word[0]
        print(word[1:].lower()+first_letter.lower()+'ay')


# In[ ]:


Q7)File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.


# In[1]:


def bldcount(bloodtype1):
    
    #reading the file
    x = open(bloodtype1,'r')
    words = x.readline()
    lst = []
    blood_types = ['A','B','AB','O','OO']
    
    #Spliting the words and storing them in a list
    lst.append(words.split(" "))
    
    #checking the count for each blood type
    for blood_type in blood_types:
        print("There are {} patients of blood type {}.".format(lst[0].count(blood_type),blood_type))


# In[4]:


bldcount('bloodtype1.rtf')


# In[ ]:


Q8)Write a function curconv() that takes as input: 

a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro) 
an amount 
and then converts and returns the amount in US dollars.


# In[17]:


def curconv(currency1,amount):
    currencies = {}
    
    #reading the file
    cur_file = open('currrency1.rtf')
    lines = cur_file.readlines()
    
    #storing the currency in the key and it's corresponding $ value and name in value.
    for x in lines:
        currencies[x[:3].strip()] = x[4:].split("\t")
    value = currencies[currency1][0].strip()
    print(amount * float(value))


# In[18]:


curconv('EUR', 100)


# In[ ]:


Q9) Each of the following will cause an exception (an error). Identify what type of exception each will cause.

Solution : 
Error	Error Message
Trying to add incompatible variables, as in adding 6 + ‘a’	Unsupported type
Referring to the 12th item of a list that has only 10 items	Out of index
Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)	domain error
Using an undeclared variable, such as print(x) when x has not been defined	variable not defined
Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.	No such directory found


# In[22]:


6 + 'a'


# In[23]:


list = [1,2,3,4,5,6,7,8,9,10]

show = list[12]
print(show)


# In[24]:


import math
math.sqrt(-1.0)


# In[25]:


str = 'Data Programming'
print(x)


# In[26]:


f = open("dataprogramming.txt")


# In[ ]:


Q.No.10 Encryption is the process of hiding the meaning of a text by substituting letters in the message with other letters, according to some system. If the process is successful, no one but the intended recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the encryption, even if some details of the encryption are unknown (for example, if an encrypted message has been intercepted). The first step of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. Assume that the string letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters.


# In[29]:


def frequencies(text):
    
    #set of alphabets
    alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    total_characters = []
    alpha_dict = {}
    #picking character from every word of input and appending it to total_character list.
    for word in text:
        for char in word:
            if char.isalpha():
                total_characters.append(char)
    #checking if the alphabet is present in the total_character list than assigning it it's count otherwise 0
    for char in alphabets:
        if char in total_characters:
            alpha_dict[char] = total_characters.count(char)
        else:
            alpha_dict[char] = 0
            
    #printing out the values(count) of the alphabets present in the total_character list
    print(list(alpha_dict.values()))


# In[30]:


frequencies('The quick red fox got bored and went home.')


# In[ ]:




