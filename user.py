
class User:
    similarity=0
    
    def __init__(self, user_id, df):
        self.user_id = user_id
        row = df.index[df['id'] == self.user_id]
        self.name = df.loc[row,"name"]
        self.surname = df.loc[row,"surname"]
        self.email = df.loc[row,"email"]
        self.birthDate = df.loc[row,"birthDate"]
        self.allowOppositeGender = df.loc[row,"allowOppositeGender"]
        self.gender = df.loc[row,"gender"]
        self.field = df.loc[row,"field"]
        self.interest1 = df.loc[row,"interest1"]
        self.interest2 = df.loc[row,"interest2"]
        self.interest3 = df.loc[row,"interest3"]
        self.interest4 = df.loc[row,"interest4"]
        self.interest5 = df.loc[row,"interest5"]
        self.attendsUni = df.loc[row,"attendsUni"]
        self.university = df.loc[row,"university"]
        self.workplace = df.loc[row,"workplace"]
        self.purpose = df.loc[row,"purpose"]
        self.online = df.loc[row,"online"]
        self.f2f = df.loc[row,"f2f"]
        self.country = df.loc[row,"country"]
        self.city = df.loc[row,"city"]
        self.district = df.loc[row,"district"]
        self.joinDate = df.loc[row,"joinDate"]
        self.rating = df.loc[row,"rating"]
    
    def getAllow(self):
        return self.allowOppositeGender
    
    def getGender(self):
        return self.gender
        
    def getOnline(self):
        return self.online
    
    def getF2F(self):
        return self.f2f
    
    def getUniStatus(self):
        return self.attendsUni
    
    def updateSimilarity(self, sim):
        self.similarity=sim
        return self.similarity

