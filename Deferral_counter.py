import pandas as pd

record_B737 = {
    'TN':['ATK', 'ATN', 'AOW', 'AYK', 'ANN', 'ASJ','AYT', 'ANN', 'ASK','ATK', 'ANO', 'ASJ'],
    'Cat':['D','A','A','B','C','C','D','A','D','B','A','C'],
    'FID':[1212,1214,1123,1242,1242,1532,1253,1423,1423,1214,1212,1214],
    'Skill':['AMT', 'CBN', 'AMT', 'CBN', 'CBN','AMT', 'CBN', 'AMT', 'AMT', 'CBN', 'AMT', 'CBN']
}

record_B777 = {
    'TN':['ABN', 'AQN', 'AOP', 'AYB', 'ABN', 'AOP','AYA', 'AQN', 'AKG','AYW', 'AYW', 'AOP'],
    'Cat':['D','B','C','A','C','D','A','B','D','B','D','C'],
    'FID':[1212,1214,1123,1242,1242,1532,1253,1423,1423,1214,1212,1214],
    'Skill':['AMT', 'CBN', 'AMT', 'CBN', 'CBN','AMT', 'CBN', 'AMT', 'AMT', 'CBN', 'AMT', 'CBN']
}

B737_inop_ac = ['AOW'] #inoperational a/c
B737_passenger = ['AOW', 'AYK', 'ANN', 'ASJ', 'AYT', 'ANN', 'ASK', 'ANO', 'ASJ']
B737_cargo = ['ATK', 'ATN']

B777_inop_ac = ['AOW'] #inoperational a/c
B777_passenger = [ 'AYB', 'ABN', 'AOP','AYA', 'AQN', 'AKG','AYW', 'AYW', 'AYB']
B777_cargo = ['ABN', 'AQN', 'AOP']
######################################


class Mel_counter:
    def __init__(self, fleet,ac_data, inop_ac, cargo, passenger):
        self.fleet = fleet
        self.ac_data = ac_data
        self.inop_ac = inop_ac
        self.cargo = cargo
        self.passanger = passenger

    def count(self):
        _dataframe = pd.DataFrame(self.ac_data, columns=['TN', 'Cat', 'FID', 'Skill'])
        dataframe = _dataframe[~_dataframe['TN'].isin(self.inop_ac)]
        
        PassDF = dataframe[dataframe['TN'].isin(self.passanger)] #passanger a/c
        CargoDF = dataframe[dataframe['TN'].isin(self.cargo)] #cargo a/c


        _AMT = PassDF[PassDF['Skill'] =='AMT'] #take out AMT Skill to count
        AMT = _AMT.drop_duplicates('FID')
        AMT_count = AMT.groupby("Cat")['TN'].count()

        _CBN = PassDF[PassDF['Skill'] =='CBN'] #take out AMT Skill to count
        CBN = _CBN.drop_duplicates('FID')
        CBN_count = CBN.groupby("Cat")['TN'].count()

        #print(AMT_count.value_counts)


        print("    AMT-"+self.fleet)
        print("......................")
        print(AMT_count.to_string(index=True, header=False).strip())
        print("......................")

        print("    CBN-"+self.fleet)
        print("......................")
        print(CBN_count.to_string(index=True, header=False).strip())
        print("......................")
        

class Mel_counter2:
    def __init__(self, fleet,ac_data, inop_ac):
        self.fleet = fleet
        self.ac_data = ac_data
        self.inop_ac = inop_ac

    def count(self):
        _dataframe = pd.DataFrame(self.ac_data, columns=['TN', 'Cat', 'FID', 'Skill'])
        dataframe = _dataframe[~_dataframe['TN'].isin(self.inop_ac)]
        

        _AMT = dataframe[dataframe['Skill'] =='AMT'] #take out AMT Skill to count
        AMT = _AMT.drop_duplicates('FID')
        AMT_count = AMT.groupby("Cat")['TN'].count()

        _CBN = dataframe[dataframe['Skill'] =='CBN'] #take out AMT Skill to count
        CBN = _CBN.drop_duplicates('FID')
        CBN_count = CBN.groupby("Cat")['TN'].count()

        #print(AMT_count.value_counts)


        print("    AMT-"+self.fleet)
        print("......................")
        print(AMT_count.to_string(index=True, header=False).strip())
        print("......................")

        print("    CBN-"+self.fleet)
        print("......................")
        print(CBN_count.to_string(index=True, header=False).strip())
        print("......................")
        



######################################

b737 = Mel_counter("b737", record_B737, B737_inop_ac, B737_cargo, B737_passenger)
b777 = Mel_counter("b777",record_B777, B777_inop_ac, B777_cargo, B777_passenger)
b787 = Mel_counter2("b787",record_B777, B777_inop_ac)

b737.count()
b777.count()
b787.count()








