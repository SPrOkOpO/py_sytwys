
class FunkcjePlanu():
    """
    funkcje planu i ich opisy

    -   w fazie projektowej nie jestem zdecydowany na typ atrybutów;
        być może oba typy będą przydatne
    """
    def __init__(self):
        # źródłowe dane z ustn - funkcje (mogą być zdublowane)
        # - pobrane z dgna za pomocą makra fun>inf (sw_funkcja2plikInf.bas)
        # - to makro dopisuje do pliku sw_XXX_info.txt wiersze postaci:
        #   [oPlan_fA_01]=MN,RM,DG
        self.funkcje_z_uStn = list()
        self.funkcje_lst = list()
        self.opisy_lst = list()
        self.funkcje_mstr = ''
        self.opisy_mstr = ''

    def import_ustn_data(self):
        """
        dane z ustn porządkuje i wypełnia nimi atrybuty dot. funkcji
        """
        pass




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
        