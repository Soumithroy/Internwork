import time
from datetime import datetime, date, time, timedelta

import ast 
def MissingDates(thisdict):
    #creating list of keys and values
    keylist = list()
    valuelist=list()

    #creating updated list of missing keys and values
    upkey=list()
    upvalue=list()
    
    #converting keys to date and storing in the keylist   
    for i in thisdict.keys():
        keylist.append(datetime.strptime(i, '%Y-%m-%d'))
        #storing the values from dictionary into value list
        valuelist.append(thisdict[i])
    
    #accessing adjacent keys to find the missing days
    for i in range(len(keylist)-1):
        diff=keylist[i+1]-keylist[i];
        #checking if there are any missing days
        if (diff.days)>1:
            firstday=keylist[i];
            firstvalue=int(valuelist[i]);
            #calculating the average
            avg=(int(valuelist[i+1])-int(valuelist[i]))/(diff.days);

            #adding missing dates
            for j in range(1,diff.days):
                #adding missing date key to upkey list
                firstday+=timedelta(days=1)
                upkey.insert(j,str(firstday));
                #adding missing value to upvalue list
                firstvalue=firstvalue+avg;
                upvalue.insert(j,int(firstvalue));
                
    #adding missing key-value from lists to dictionary
    for key in upkey: 
        for value in upvalue: 
            thisdict[key] = value 
            upvalue.remove(value) 
            break
    #sorting on basis of keyss
    for i in sorted (thisdict.keys()):  
        print((i, thisdict[i]), end =" ")            
    

class_list = dict()

# initializing string and taking input from user 
test_string = input('Enter date(yyyy-mm-dd) & value in dictionary format i.e {"key":value}:-') 
    
# using ast.literal_eval() test_string to dictionary 
class_list = ast.literal_eval(test_string) 
MissingDates(class_list);

    

    
