import terminaltables as tt

data = [['Kundennummer','Vertragsnummer','Kategorie','ONT Typ','LEDs']['1','2','3','4','5']]
table = tt.AsciiTable(data,'Störungsannahme')
print(table)