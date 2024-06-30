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
    def __init__(self, ac_name, inop_ac, cargo, passenger):
        self.ac_name = ac_name
        self.inop_ac = inop_ac
        self.cargo = cargo
        self.passanger = passenger

    def count(self):
        _dataframe = pd.DataFrame(self.ac_name, columns=['TN', 'Cat', 'FID', 'Skill'])
        dataframe = _dataframe[~_dataframe['TN'].isin(self.inop_ac)]
        PassDF = dataframe[dataframe['TN'].isin(self.passanger)] #passanger a/c
        CargoDF = dataframe[dataframe['TN'].isin(self.cargo)] #cargo a/c
        _AMT = PassDF[PassDF['Skill'] =='AMT'] #take out AMT Skill to count
        AMT = _AMT.drop_duplicates('FID')
        AMT_CAT_A = AMT[AMT['Cat'] =='A']['Cat'].count()
        AMT_CAT_B = AMT[AMT['Cat'] =='B']['Cat'].count()
        AMT_CAT_C = AMT[AMT['Cat'] =='C']['Cat'].count()
        AMT_CAT_D = AMT[AMT['Cat'] =='D']['Cat'].count()



        _CBN = PassDF[PassDF['Skill'] == 'CBN'] #take out CBN Skill to count
        CBN = _CBN.drop_duplicates('FID')

        CBN_CAT_A = CBN[CBN['Cat'] == 'A']['Cat'].count()
        CBN_CAT_B = CBN[CBN['Cat'] == 'B']['Cat'].count()
        CBN_CAT_C = CBN[CBN['Cat'] == 'C']['Cat'].count()
        CBN_CAT_D = CBN[CBN['Cat'] == 'D']['Cat'].count()

        return [
            AMT_CAT_A,
            AMT_CAT_B,
            AMT_CAT_C,
            AMT_CAT_D]
######################################

b737 = Mel_counter(record_B737, B737_inop_ac, B737_cargo, B737_passenger)
b777 = Mel_counter(record_B777, B777_inop_ac, B777_cargo, B777_passenger)

counts_77 = b777.count()
counts_37 = b737.count()







