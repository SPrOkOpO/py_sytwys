#-*- coding: windows-1250 -*-


class FunkcjePlanu():
    """
    funkcje planu i ich opisy

    -   w fazie projektowej nie jestem zdecydowany na typ atrybut�w;
        by� mo�e oba typy b�d� przydatne
    """
    def __init__(self):
        # �r�d�owe dane z ustn - funkcje (mog� by� zdublowane)
        # - pobrane z dgna za pomoc� makra fun>inf (sw_funkcja2plikInf.bas)
        # - to makro dopisuje do pliku sw_XXX_info.txt wiersze postaci:
        #   [oPlan_fA_01]=MN,RM,DG
        self.funkcje_z_uStn = list()
        self.funkcje_lst = list()
        self.opisy_lst = list()
        self.funkcje_mstr = ''
        self.opisy_mstr = ''

    def import_ustn_data(self):
        """
        dane z ustn porz�dkuje i wype�nia nimi atrybuty dot. funkcji
        """
        pass




class OpracowaniePlanistyczne(object):
    '''
    klasa do obs�ugi opracowania planistycznego
    -   planu zagospodarowania
    -   decyzji o warunkach zabudowy
    
    
    na razie tylko dostarcza zmiennych do odczytu i zapisu symboli funkcji 
    terenu w pliku sw_XXX_info.txt
    
    >>  na obecnym etapie da si� latwo zrobi� makro do pod��czenia pod polecenie
        inf>fun w p500A.sbm
    >>  mozna te� dorobi� podobn� obs�ug� opis�w, w tym celu trzeba:
        -   zrobi� pole tekstowe do edycji tych opis�w
        -   doda� obs�ug� zapisu i odczytu do/z pliku sw_info    
    ?>  zastanowi� si� nad opisami, kt�re nie mieszcz� si� w jedne linii
    
        
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
        