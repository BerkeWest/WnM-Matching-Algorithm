import pandas as pd
import numpy as np
import openpyxl
from user import User

user_id = int(input("Please enter the user id: "))

df = pd.read_excel('WnM_data_excel.xlsx')

user= User(user_id,df)

def calculate_similarity(user, match_user):
    sim = 0

    if (user.getAllow()==1 and match_user.getAllow()==1) or (user.getGender() == match_user.getGender()):
        pref = meetPreference(user, match_user)
        if pref == 0:
            match_user.updateSimilarity(sim)
        elif pref == 1:
            sim = bothMatch(user, match_user)
            match_user.updateSimilarity(sim)
        elif pref == 2:
            sim = onlineMatch(user, match_user)
            match_user.updateSimilarity(sim)
        else:
            sim = f2fMatch(user, match_user)
            match_user.updateSimilarity(sim)
    else:
        match_user.updateSimilarity(sim)

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
    sim = 0
    if user.getField()==match_user.getField():
        sim = sim + 0.10
    if user.getPurpose()==match_user.getPurpose():
        sim = sim + 0.10
    
    u_ints = user.getInterests()
    m_ints = match_user.getInterests()

    for i in range(0,4):
        for j in range(0,4):
            if u_ints[i] == m_ints[j]:
                if j >= i:
                    sim = sim + (0.21 - (i * 0.025)) - ((j-i) * 0.02)
                else:
                    sim = sim + (0.21 - (i * 0.025)) - ((j-i) * 0.01)
    
    sim = sim * (match_user.getRating()/5 + 0.20)
    return sim
    
def bothMatch(user, match_user):
    sim = 0
    if user.getCity() == match_user.getCity():
        sim1 = f2fMatch(user, match_user)
        sim2 = onlineMatch(user, match_user)
        sim = max(sim1, sim2)
        return sim
    else:
        sim = onlineMatch(user, match_user)
        return sim
    
def f2fMatch(user, match_user):
    sim = 0
    if user.getCity() == match_user.getCity():
        if user.getField() == match_user.getField():
            sim = sim + 0.08

        if user.getPurpose() == match_user.getPurpose():
            sim = sim + 0.08

        if user.getDistrict() == match_user.getDistrict():
            sim = sim + 0.14

        u_ints = user.getInterests()
        m_ints = match_user.getInterests()

        for i in range(0,4):
            for j in range(0,4):
                if u_ints[i] == m_ints[j]:
                    if j >= i:
                        sim = sim + (0.19 - (i * 0.025)) - ((j-i) * 0.02)
                    else:
                        sim = sim + (0.19 - (i * 0.025)) - ((j-i) * 0.01)
    
        sim = sim * (match_user.getRating()/5 + 0.20)
        return sim
    
    else:
        return sim

dictionary = {}

for id in range (1,1000):
    if id == user_id:
        continue
        
    match_user = User(id,df)
    calculate_similarity(user, match_user)
    similarity = match_user.getSimilarity()
    if similarity != 0:
        dictionary[match_user.getId()] = similarity

sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

sublists = [list(sorted_dict.items())[i:i+10] for i in range(0, len(sorted_dict.items()), 10)]

pages = []
for i in sublists:
    pages.append([{"data": User(data[0], df).data, "similarity": data[1]} for data in i])

for i in range(len(pages)):
    print(f"-------------- PAGE {i+1} --------------")
    for j in pages[i]:
        print(j["data"],j["similarity"])