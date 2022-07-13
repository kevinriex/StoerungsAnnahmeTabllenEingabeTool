from os import write
import terminaltables as tt
from table import StoerungsTable as st

def test():
    data = [['Kundennummer','Vertragsnummer','Kategorie','ONT Typ','LEDs'],['12345','54321','Internet','Alcatel','Grün Grün Aus Orange Aus Aus']]
    #data = [['Heading1', 'Heading2'],['row1 column1', 'row1 column2'],['row2 column1', 'row2 column2'],['row3 column1', 'row3 column2']]
    table = tt.AsciiTable(data,'Störungsannahme').table
    print(table)

def main():
    data = [['Kategorie','ONT Typ','LEDs'],['Internet','Alcatel','Grün Grün Aus Orange Aus Aus']]
    st.printT(data,"K12345 | V54321")

def printall():
    data1header = ['Kundennummer','Vertragsnummer','Vorname','Nachname','Handynummer','Adresse','Stadtteil']
    data2header = ['Paket','Geschwindigkeit Down','Geschwindigkeit Up'] 
    data3header = ['Typ','LEDs']
    data4header = ['Typ','LEDs','Unsere?','Änderungen?']
    data5header = ['Speedtest','Strom ONT', 'Stom FB', 'Werksreset FB']

    data1data = ['12345','54321','Max','Mustermann','01234567890','Musterstraße 4','Fibreland']
    data2data = ['GL M','200','100']
    data3data = ['Alcatel','Grün Grün Aus Orange Aus Aus']
    data4data = ['7560','Grün Grün Aus Aus Aus','Ja!','Ja!']
    data5data = ['Ja!','Ja!','Ja!','Ja!']

    data1 = [data1header, data1data]
    data2 = [data2header, data2data]
    data3 = [data3header, data3data]
    data4 = [data4header, data4data]
    data5 = [data5header, data5data]
    st.all(data1,"Kundendaten")
    st.printT(data2,"Vertragsdaten")
    st.printT(data3, "ONT Daten")
    st.printT(data4, "")
    st.printT(data5, "")

    f = open("./out.txt","w",encoding="UTF-8")
    f.write(st.dataT(data1,"Kundendaten"))
    f.write("\n")
    f.write(st.dataT(data2,"Vertragsdaten"))
    f.write("\n")
    f.write(st.dataT(data3, "ONT Daten"))
    f.write("\n")
    f.write(st.dataT(data4, "FB Daten"))
    f.write("\n")
    f.write(st.dataT(data5, "Was wurde gemacht?"))
    f.close()

printall()
#main()