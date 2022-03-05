

class Occupations():
    OccupationDict = {}
    
    # Pareses the data from the D3 table and brings it into the program.
    def defineOccupations():
        data = open("D3-Inputs/HomeWorkPerJob.txt")
        dataString = data.read().split("\n")
        data.close()
        
        for i in range(len(dataString)):
            dataString[i] = dataString[i].split("\t")
        
        # Push the data to a dict
        for occupationLine in dataString:
            Occupations.OccupationDict[occupationLine[0]] = float(occupationLine[1][:-1])/100
