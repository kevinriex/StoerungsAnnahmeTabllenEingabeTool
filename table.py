import terminaltables as tt

class StoerungsTable:
    def __init__(self) -> None:
        pass

    def  printT(data, header):
        print(tt.AsciiTable(data,header).table)
    
    def dataT(data,header):
        return tt.AsciiTable(data,header).table

    def all(data, header):
        print("Ihre Störung:\n")
        print(tt.AsciiTable(data,header).table)