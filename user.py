class User:
    def __init__(self, user_id, df):
        self.user_id = user_id
        self.data = []
        self.similarity = 0
        row = df[df['id'] == self.user_id]

        if not row.empty:
            row = row.iloc[0]
            self.data.append(row["id"])
            self.data.append(row["name"])
            self.data.append(row["surname"])
            self.data.append(row["email"])
            self.data.append(row["birthDate"])
            self.data.append(row["allowOppositeGender"])
            self.data.append(row["gender"])
            self.data.append(row["field"])
            self.data.append(row["interest1"])
            self.data.append(row["interest2"])
            self.data.append(row["interest3"])
            self.data.append(row["interest4"])
            self.data.append(row["interest5"])
            self.data.append(row["attendsUni"])
            self.data.append(row["university"])
            self.data.append(row["workplace"])
            self.data.append(row["purpose"])
            self.data.append(row["online"])
            self.data.append(row["f2f"])
            self.data.append(row["country"])
            self.data.append(row["city"])
            self.data.append(row["district"])
            self.data.append(row["joinDate"])
            self.data.append(row["rating"])
            self.data.append(row["uniOnly"])
            self.data.append(row["priority"])

    def getId(self):
        return self.data[0]
    
    def getAllow(self):
        return self.data[5]
    
    def getGender(self):
        return self.data[6]
    
    def getField(self):
        return self.data[7]
    
    def getUniStatus(self):
        return self.data[13]
    
    def getUni(self):
        return self.data[14]
    
    def getPurpose(self):
        return self.data[16]
    
    def getOnline(self):
        return self.data[17]
    
    def getF2F(self):
        return self.data[18]
    
    def getCity(self):
        return self.data[20]
    
    def getDistrict(self):
        return self.data[21]
    
    def getRating(self):
        return self.data[23]
    
    def getUniOnly(self):
        return self.data[24]
    
    def getPriority(self):
        return self.data[25]
    
    def getSimilarity(self):
        return self.similarity
    
    def getInterests(self):
        return self.data[8:13]
    
    def updateSimilarity(self, sim):
        self.similarity = sim