# Infotable

## Kundendaten
- Kundnnummer
- Vertragsnummer
- Vorname
- Nachname
- Adresse
- Stadtteil

## Vertragsdaten
- Paket
- Geschwindigkeit Down
- Geschwindigkeit Up

## ONT Daten
- Typ
- LEDs

## FB Daten
- Typ
- LEDs
- Unsere?
- Änderungen?

## Was wurde gemacht?
- Speedtest
- Strom ONT
- Strom FB
- Werksreset FB

```python
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
```