import pandas as pd
import numpy as np
import openpyxl
from user import User

user_id = int(input("Please enter the user id: "))

df = pd.read_excel('data.xlsx')

user= User(user_id,df)

def calculate_similarity(user, match_user):
    if (user.allowOppositeGender and match_user.allowOppositeGender) or (user.gender == match_user.gender):
        print("es")

while True:
    id=1
    if id != user_id:
        match_user = User(id,df)
        calculate_similarity(user, match_user)
        id = id + 1
    elif id > 1000:
        break
    else:
        id = id + 1