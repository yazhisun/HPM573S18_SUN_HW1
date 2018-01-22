# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:08:17 2018

@author: Administrator
"""
#
#Create a list, named yours, to store my favorite schools:
#‘Yale’, ‘MIT’, and ‘Berkeley’; and create a list, named mine, to store 3 of your favorite schools whatever
#they are. Use the + operator to create a new list, named ours1, to represent our favorite schools:
#ours1 = mine + yours
#Now, create another list, name ours2, to again represent our favorite schools but this time use:
#ours2 = []
#ours2.append(mine)
#ours2.append(yours)
#Answer these questions:
#1. Print ours1 and ours2. Describe how ours1 and ours2 differ from each other.
#2. Change the second element of yours to something else and again print ours1 and ours2.
#Explain why changing yours would changes ours2 but not ours1.

yours=['Yale','MIT','Berkeley']
mine=['Yale','UW','Princeton']
ours1=mine+yours
ours2=[]
ours2.append(mine)
ours2.append(yours)

#q1 
print(ours1)
print(ours2)
#ours2 includes two lists as elements, while ours1 includes 6 strings as elements

#q2
mine[1]='Brown'
print(ours1)
print(ours2)
#ours2 is an alias for the combination of mine and yours. if we change any element in ours2,
#it will change in ours2. ours1 is a new list