#-*- coding: windows-1250 -*-

class OpracowaniePlanistyczne(object):
    '''
    klasa do obsługi opracowania planistycznego
    -   planu zagospodarowania
    -   decyzji o warunkach zabudowy
    
    
    na razie tylko dostarcza zmiennych do odczytu i zapisu symboli funkcji 
    terenu w pliku sw_XXX_info.txt
    
    >>  na obecnym etapie da się latwo zrobić makro do podłączenia pod polecenie
        inf>fun w p500A.sbm
    >>  mozna też dorobić podobną obsługę opisów, w tym celu trzeba:
        -   zrobić pole tekstowe do edycji tych opisów
        -   dodać obsługę zapisu i odczytu do/z pliku sw_info    
    ?>  zastanowić się nad opisami, które nie mieszczą się w jedne linii
    
        
    '''
    def __init__(self):
        self.funAkt_01 = ""
        self.funAkt_02 = ""
        self.funAkt_03 = ""
        self.funAkt_04 = ""
        self.funAkt_05 = ""
        self.funAkt_06 = ""
        self.funAkt_07 = ""
        self.funAkt_08 = ""
        self.funAkt_09 = ""
        self.funAkt_10 = ""
        self.funAkt_11 = ""
        self.funAkt_12 = ""
        self.funAkt_13 = ""
        self.funAkt_14 = ""
        self.funAkt_15 = ""
        