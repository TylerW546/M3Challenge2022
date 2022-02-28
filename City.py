class City:
    Years = [2000, 2005, 2010, 2015, 2019, 2020, 2021]
    Fields = ["Mining, logging, construction",
                    "Manufacturing",
                    "Trade, transportation, and utilities",
                    "Information",
                    "Financial activities",
                    "Professional and business services",
                    "Education and health services",
                    "Information",
                    "Leisure and hospitality",
                    "Other services",
                    "Government"]
    
    def __init__(self, name, inputString):
        self.table = []
        
        self.table = inputString.split("\n")
        for i in range(len(self.table)):
            self.table[i] = self.table[i].split("\t")
            for j in range(len(self.table[i])):
                self.table[i][j] = int(self.table[i][j])
    
    def regression(self):
        for field in range(len(self.table)):
            x = City.Years
            y = self.table[field]
            
            m, b = polyfit(x, y, 1)
            
        
        
        
        
        


class Field:
    def __init__(self, name):
        pass
        
  
      