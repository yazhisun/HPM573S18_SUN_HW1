# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:59:38 2018

@author: Administrator
"""

#Problem 5: Dictionaries (Weight 2). Create a dictionary for the months of the year that can be called by
#the number of months (i.e. 1, 2, ..., 12) or the name of months (i.e. January, February, ..., December).
#Write a statement that prints ‘The sixth month is June.’ and another statement that prints
#‘February is month 2.
months={'1':'January', '2':'February', '3':'March', '4':'April', '5':'May',
        '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', 
        '11':'November', '12':'December',
        'January':'1', 'February':'2', 'March':'3', 'April':'4', 'May':'5', 'June':'6', 'July':'7', 'August':'8', 'September':'9',
        'October':'10', 'November':'11', 'December':'12'}
print('The sixth month is '+ months['6'])
print('February is month '+ months['February'])