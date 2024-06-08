import pandas as pd
import numpy as np
import openpyxl
from user import User

user_id = int(input("Please enter the user id: "))

df = pd.read_excel('WnM_data_excel.xlsx')

user= User(user_id,df)
print(user.data)

match_list = []

def calculate_similarity(user, match_user):
    if (user.getAllow()==1 and match_user.getAllow()==1) or (user.getGender() == match_user.getGender()):
        pref = meetPreference(user, match_user)
        if pref == 0:
            match_user.updateSimilarity(0)
        elif pref == 1:
            bothMatch(user, match_user)
        elif pref == 2:
            onlineMatch(user, match_user)
        else:
            f2fMatch(user, match_user)
    else:
        match_user.updateSimilarity(0)

def meetPreference(user, match_user):
    online=False
    f2f=False

    if user.getOnline()==1 and match_user.getOnline()==1:
        online=True
    
    if user.getF2F()==1 and match_user.getF2F()==1:
        f2f=True
    
    if online and f2f:
        return 1

    elif online == True and f2f == False:
        return 2
    
    elif f2f == True and online == False:
        return 3
    
    else:
        return 0

def onlineMatch(user, match_user):
    print("online")
    
def bothMatch(user, match_user):
    print("BOTH")
    
def f2fMatch(user, match_user):
    print("face-to-face")
    if user.getCity() == match_user.getCity():
        print("Can Match")
        match_user.updateSimilarity(5)
    else:
        match_user.updateSimilarity(0)

for id in range (1,1000):
    if id == user_id:
        continue
        
    match_user = User(id,df)
    calculate_similarity(user, match_user)
    if match_user.getSimilarity()!=0:
        match_list.append(match_user.data)
    
print("Here are your matches!")
for i in range (0,len(match_list)):
    print(match_list[i])