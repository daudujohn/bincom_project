import sqlite3

def create_connection():
    conn = sqlite3.connect('bincomdb.sqlite')
    return conn

def validate_pu(pol_unit):
    pol_units = ['Sapele Ward 8 PU _', 'Primary School in Aghara', 'Ishere Primary School  Aghara', 'Igini Primary School', 'Umukwapa poll unit 1', 'Church in Effurun1 Ovie', 'Ishere Primary School Aghara', 'Effurun 2 in Uvwie', 'school in ethiope west', 'agbasa 1', 'Customary Court P.t.i Road', 'effurun 2', 'asumbo town hall1', 'eki-otoi', 'pollling 3 in agbara', 'aghara ii', 'obiteogbon quarters', 'okegbe quarter1', 'gra', 'anocha north', 'gra ward', 'ellu ', 'emami quarter 2', 'emami quarter 1', 'oguanja quarters', 'okegbe quarters 2', 'ajudaibo primary school', 'isoko north', 'hall 2', 'uvwie', 'ughelli', 'cable point i', 'aka avenue', 'sapele', 'ethiope', 'Aniocha North 4', 'aniocha ward 3', 'aniocha ward 4', 'uru standard junction off jakpa rd', 'Oshimili', 'Isoko', 'Ukwuani', 'Effurun', 'aniocha', 'Bomadi', 'Udogbie Village', 'ethiope west ', 'ethiope unit 12', 'kolafiogbene', 'Ndokwa east', 'seimbiri', 'ndokwa', '']
    if pol_unit in pol_units:
        return True
    return False

def validate_lga(lga_name):
    lgas = ['Aniocha North', 'Aniocha - South', 'Ethiope East', 'Ethiope West', 'Ika North - East', 'Ika - South', 'Isoko North', 'Isoko South', 'Ndokwa East', 'Ndokwa West', 'Okpe', 'Oshimili - North', 'Oshimili - South', 'Patani', 'Sapele', 'Udu', 'Ughelli North', 'Ughelli South', 'Ukwuani', 'Uvwie', 'Bomadi', 'Burutu', 'Warri North', 'Warri South', 'Warri South West']
    if lga_name in lgas:
        return True
    return False