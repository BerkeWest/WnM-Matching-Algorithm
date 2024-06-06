import pandas as pd
import numpy as np
import openpyxl
from user import User

user_id = int(input("Please enter the user id: "))

df = pd.read_excel('data.xlsx')

user= User(user_id,df)

while True:
    try:
        id=1
        if id != user_id:
            match_user = User(id,df)
            calculate_similarity(user, match_user)
            id++
        elif:
            id++
    except KeyError:
        break
    except IndexError:
        break

def calculate_similarity(user, match_user):
    userAOG = allowsOppositeGender(user)
    mUserAOG = allowsOppositeGender(match_user)
    if (userAOG and mUserAOG) or 

def allowsOppositeGender(user):
    return user.allowOppositeGender