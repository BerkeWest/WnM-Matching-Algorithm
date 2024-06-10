import pandas as pd
import numpy as np
import openpyxl
from user import User

cities_to_district = {
    "Istanbul": ["Eyüp", "Tarabya", "Sarıyer", "4. Levent", "Levent", "Kağıthane", "Beşiktaş", "Şişli", "Mecidiyeköy", "Üsküdar", "Kadıköy", "Taksim", "Kartal", "Tuzla"],
    "Ankara": ["Etimesgut", "Yenimahalle", "Çankaya", "Keçiören", "Altındağ" "Akyurt","Kalecik"],
    "Izmir": ["Foça","Menemen","Karşıyaka","Bornova","Buca","Narlıdere","Güzelbahçe","Urla","Çeşme"],
    "Antalya": ["Kaş","Kale","Finike","Kumluca","Kemer","Konyaaltı","Muratpaşa","Manavgat","Alanya"],
    "Bursa": ["Karacabey","Mudanya","Gemlik","Orhangazi","İznik","Yenişehir","İnegöl"],
    "Adana": ["Karataş","Yumurtalık","Ceyhan","İmamoğlu","Kozan","Aladağ","Feke","Saimbeyli"],
    "Gaziantep": ["Nurdağı","Şehitkamil","Yavuzeli","Nizip","Karkamış","Oğuzeli"],
    "Samsun": ["Alaçam","Bafra","Havza","Ladik","Asarcik","Ayvacık","Salıpazarı"],
    "Konya": ["Beyşehir", "Seydişehir", "Bozkır", "Akören", "Çumra", "Karatay"],
    "Trabzon": ["Çarşıbaşı", "Akcaabat", "Ortahisar", "Yomra", "Arsin", "Araklı", "Sürmene", "Of"],
    "Tekirdağ": ["Süleymanpaşa", "Çorlu", "Malkara", "Çerkezköy", "Şarköy"],
    "Edirne": ["Havsa", "Uzunköprü", "Keşan", "İpsala", "Enez"],
    "Mugla": ["Bodrum", "Milas", "Yatağan", "Ula", "Marmaris", "Köyceğiz", "Dalaman", "Fethiye"],
    "Canakkale": ["Yenice", "Biga", "Lapseki", "Çanakkale Merkez","Ezine", "Ayvacık"],
    "Eskisehir": ["Tepebasi", "Odunpazari", "Seyitgazi", "Çifteler", "Mahmudiye","Sivrihisar"],
    "Mersin": ["Anamur", "Bozyazı", "Gülnar", "Silifke","Erdemli", "Tarsus"],
    "Sakarya": ["Serdivan", "Adapazari", "Sapanca", "Arifiye", "Erenler", "Karapürçek", "Akyazı"],
    "Van": ["Erciş", "Muradiye", "Çaldıran", "Özalp","Saray","Başkale"],
    "Kocaeli": ["Darıca", "Gebze", "Dilovası", "Körfez", "Derince", "İzmit", "Kartepe"],
    "Diyarbakir": ["Kulp", "Lice", "Hani", "Dicle","Ergani", "Çüngüş"],
    "Denizli": ["Çameli","Acıpayam","Tavas","Serinhisar","Bozkurt","Çivril"],
    "Erzurum": ["Aşkale", "Çat", "Palandöken", "Tekman", "Hınıs", "Karayazı", "Horasan"],
    "Kayseri": ["Pınarbaşı", "Sarız", "Tomarza", "Develi","Yahyâlı", "Yeşilhisar"]
}

def prioritizeField():
    if priority == 1:
        return 0.07
    elif priority == 0:
        return 0
    elif priority == 5:
        return -0.005
    else:
        return -0.01

def prioritizeInt():
    if priority == 2:
        return 0.014
    elif priority == 0:
        return 0
    elif priority == 5:
        return -0.001
    else:
        return -0.01

def prioritizePurpose():
    if priority == 3:
        return 0.07
    elif priority == 0:
        return 0
    elif priority == 5:
        return -0.005
    else:
        return -0.01

def prioritizeDistrict():
    if priority == 4:
        return 0.07
    elif priority == 0:
        return 0
    elif priority == 5:
        return -0.005
    else:
        return -0.01
    
def prioritizeRating():
    if priority == 5:
        return 0.05
    else:
        return 0

user_id = int(input("Please enter your user ID: "))
print()

df = pd.read_excel('WnM_data_excel.xlsx')

user= User(user_id,df)

priority=user.getPriority()

def calculate_similarity(user, match_user):
    sim = 0

    if (user.getUniOnly() == 1 and match_user.getUniStatus()==0) or (user.getUniStatus()==0 and match_user.getUniOnly()==1):
        match_user.updateSimilarity(sim)

    else:
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
        sim = sim + 0.10 + prioritizeField()
    if user.getPurpose()==match_user.getPurpose():
        sim = sim + 0.10 + prioritizePurpose()

    u_ints = user.getInterests()
    m_ints = match_user.getInterests()

    for i in range(0,4):
        for j in range(0,4):
            if u_ints[i] == m_ints[j]:
                if j >= i:
                    sim = sim + (0.21 - (i * 0.025)) - ((j-i) * 0.02) + prioritizeInt()
                else:
                    sim = sim + (0.21 - (i * 0.025)) - ((j-i) * 0.01) + prioritizeInt()
    
    sim = sim * (match_user.getRating()/5 + (0.20 + prioritizeRating()))
    return sim
    
def bothMatch(user, match_user):
    sim = 0
    sim1 = f2fMatch(user, match_user)
    sim2 = onlineMatch(user, match_user)
    sim = max(sim1, sim2)
    return sim
    
def f2fMatch(user, match_user):
    sim = 0
    if user.getCity() == match_user.getCity():
        if user.getField() == match_user.getField():
            sim = sim + 0.08 + prioritizeField()

        if user.getPurpose() == match_user.getPurpose():
            sim = sim + 0.08 + prioritizePurpose()

        dist_list = cities_to_district[user.getCity()]
        ud = dist_list.index(user.getDistrict())
        md = dist_list.index(match_user.getDistrict())
        sim = sim + 0.14 - ((0.14/(len(dist_list))) * (abs(ud - md)/2)) + prioritizeDistrict()


        u_ints = user.getInterests()
        m_ints = match_user.getInterests()

        for i in range(0,4):
            for j in range(0,4):
                if u_ints[i] == m_ints[j]:
                    if j >= i:
                        sim = sim + (0.19 - (i * 0.025)) - ((j-i) * 0.02) + prioritizeInt()
                    else:
                        sim = sim + (0.19 - (i * 0.025)) - ((j-i) * 0.01) + prioritizeInt()
    
        sim = sim * (match_user.getRating()/5 + (0.20 + prioritizeRating()))
        return sim
    
    else:
        return sim

dictionary = {}

for id in range (1,5000):
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
    if i > 10:
        break

    print()
    print(f"-------------- PAGE {i+1} --------------")
    for j in pages[i]:
        print(j["data"],j["similarity"])
    input("")