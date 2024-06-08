import pandas as pd
import numpy as np
import openpyxl
from user import User

user_id = int(input("Please enter the user id: "))

df = pd.read_excel('WnM_data_excel.xlsx')

user= User(user_id,df)
print(user.data)

def calculate_similarity(user, match_user):
    if (user.getAllow()==1 and match_user.getAllow()==1) or (user.getGender() == match_user.getGender()):
        print("ok")
        pref = meetPreference(user, match_user)
        if pref == 0:
            match_user.updateSimilarity(0)
        elif pref == 1:
            of2fMatch(user, match_user)
        elif pref == 2:
            onlineMatch(user, match_user)
        else:
            f2fMatch(user, match_user)
    else: 
        match_user.updateSimilarity(0)

def meetPreference(user1, user2):
    online=False
    f2f=False
    if user1.getOnline()==1 and user2.getOnline()==1:
        online=True
    if user1.getF2F()==1 and user2.getF2F()==1:
        f2f=True
    if online and f2f:
        return 1
    elif online == True and f2f == False:
        return 2
    elif f2f == True and online == False:
        return 3
    else:
        return 0

def onlineMatch(user1, user2):
    print("on")
    
def of2fMatch(user1, user2):
    print("of2f")
    
def f2fMatch(user1, user2):
    print("f2f")
    
def similarityScoring(user1, user2):
    print("score")

for id in range (1,1000):
    if id != user_id:
        match_user = User(id,df)
        calculate_similarity(user, match_user)
    else:
        continue