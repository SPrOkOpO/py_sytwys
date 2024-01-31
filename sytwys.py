#-*- coding: windows-1250 -*-

import os
import sys
import re

from tkinter import messagebox

import sytwys_elements
sys.path.append(r"i:\aPy\LibSP")
sys.path.append(r"i:\aPy\LibSP\sytwys")
import dzialki

"""
#-####################################################################
    grupuje dane zwi�zane z robot� sw
    klasa jest obecnie zbyt rozbudowana i wymaga przeprogramowania
    
    plan zmian
    ----------
    +   przemieszczenie danych do klas bardziej wyspecjalizowanych
        -   Inwentaryzacja
        -   PlikSWinfo 
    
    ToDO - must have:
    >>  

    ToDO - w razie nud�w:
    >>  

######################################################################
"""


class Sytwys( object):
    """
    obs�uga roboty  s-w


    """
    def __init__(self):

        # sta�e,    ale na razie jako   zwykle pola
        self.DIR_TABELKI         =  "\\tabelki\\"
        self.DIR_TABELKI_100     =  "\\tabelki\\100_oryg\\"

        # zmienne dot.  roboty
        self.sw_numer           = -1
        self.sw_numer_str       = ""
        self.sw_wykonawca       = ""
        self.sw_obreb           = ""
        self.sw_obrebDir        = ""

        self.sw_dzialki         = ""
        self.sw_dzialki_lst     = list()
        self.sw_dzialki_ergo_lst = list()
        self.sw_dzialka1        = ""
        self.sw_dzialki_obj = dzialki.Dzialki()

        self.sw_typ             = ""
        self.sw_idZgl           = ""
        self.sw_idZgl_jrwa      = ""
        self.sw_idZgl_nr        = ""
        self.sw_idZgl_rok       = ""
        self.sw_skala           = ""

        # inw. - new ver
        self.inw = sytwys_elements.Inwentaryzacja()
        self.inw.set_default()
        # old ver
        # self.sw_inw_obiekt          = ""
        # self.sw_inw_obiektDoUwag    = ""
        # self.sw_inw_nrZal           = ""
        # self.sw_inw_decZnak         = ""
        # self.sw_inw_decData         = ""

        # mdcp - new ver
        self.mdcp = sytwys_elements.MDCP()

        # !!! to jest stara wersja !!!
        #
        # --->  aktualna jest w pliku sytwys_elements.py - klasa MDCP
        #
        # self.sw_mdcp_ust5 = 1
        # self.sw_mdcp_ust6 = 1
        # self.sw_mdcp_ust5_str = "1"
        # self.sw_mdcp_ust6_str = "1"
        # self.sw_mdcp_kp_uwagi1 = "Mapa utworzona na podstawie arkusza ..."
        # self.sw_mdcp_kp_uwagi2 = "Dane dotycz�ce granic dzia�ki ..., ujawn..."
        # self.sw_mdcp_kp_uwagi3 = "Dla obszaru w granicach projektowanej inwestycji budowlanej brak obci��e� z tytu�u s�u�ebno�ci \ngruntowych (�80 ust. 4. rozp. MSWiA z dnia 9 listopada 2011 r.)."
        # self.sw_mdcp_kp_uwagi4 = "Dla terenu obj�tego opracowaniem brak opracowa� planistycznych."
        # self.sw_mdcp_kp_uwagi5 = "Granice nieruchomo�ci oznaczono kolorem zielonym."
        # self.sw_mdcp_kp_uwagi6  = "Nie wyklucza si� istnienia w terenie innych, niewykazanych na niniejszej mapie, urz�dze� \npodziemnych."
        # self.sw_mdcp_kp_uwagi6 = "Nie wyklucza si� istnienia w terenie innych, niewykazanych na niniejszej mapie, urz�dze� \npodziemnych, kt�re nie by�y zg�oszone do inwentaryzacji lub o kt�rych brak jest informacji\nw instytucjach bran�owych."
        #
        # self.sw_mdcp_kp_uwagi1_fraza1 = "Mapa utworzona na podstawie arkusza "
        # self.sw_mdcp_kp_uwagi1_fraza2 = " mapy zasadniczej oraz pomiaru aktualizacyjnego id. zg�. "
        #
        # self.sw_mdcp_kp_uwagi2_fraza1 = "Dane dotycz�ce granic dzia�ki "
        # self.sw_mdcp_kp_uwagi2_fraza2 = ", ujawnione w PZGiK, "
        # self.sw_mdcp_kp_uwagi2_fraza3 = "przepis�w �79, ust. 5 i 6 rozp. MSWiA z dnia 9 listopada 2011 r."


        # dane do libre
        self.sw_libre_wykon = ""
        self.sw_libre_opis  = ""

        # sekcje
        # s�ownik sekcji
        # - zawiera dwa (na razie) rodzaje kluczy
        #       -   na pojedyncze god�a
        #               key: [sw_godlo_01]
        #               val: 6.143.45.22.2
        #       -   na wiersze z tekstem do wstawienia do opisu
        #               key: [sw_wiersz_01]
        #               val: 234.76801, 234.76802, 234.76803,
        
        self.sw_dicSekcje       = {}
        self.sw_godlo_01        = ""
        self.sw_godlo_02        = ""
        self.sw_godlo_03        = ""
        self.sw_godlo_04        = ""
        self.sw_godlo_05        = ""
        self.sw_godlo_06        = ""
        self.sw_godlo_07        = ""
        self.sw_godlo_08        = ""
        self.sw_godlo_09        = ""
        self.sw_godlo_10        = ""
        self.sw_godlo_11        = ""
        self.sw_godlo_12        = ""
        self.sw_godlo_13        = ""
        self.sw_godlo_14        = ""
        self.sw_godlo_15        = ""
        self.sw_godlo_16        = ""
        self.sw_godlo_17        = ""
        self.sw_godlo_18        = ""
        self.sw_godlo_19        = ""
        self.sw_godlo_20        = ""
                
        self.sw_sekcje          = ""
        self.sw_sekcje_tytul    = "Sekcje mapy zas. uk�. 2000: "
        self.sw_lstSekcje       = []
        

        self.plik_sw_info = sytwys_elements.PlikSWinfo()

        # �cie�ki
        # sta�e,    ale na razie jako   zwykle pola
        self.FILE_TYTNAGL  =  "tytNagl.txt"
        self.FILE_TYTUL  =  "tytul.txt"
        self.FILE_UWAGI  =  "uwagi.txt"
        self.FILE_GODLA  =  "godla2swInfo.txt"
        self.FILE_DZIALKI_ERGO = "dz_ergo.txt"
        self.FILE_KG_ERGO = "kg.txt"
        self.FILE_KG_AHK = "kg.ahk"

        self.sw_dir_nazwa           = ""
        self.sw_plikInfo_fullPath   = ""
        self.sw_plikTytNagl_fullPath  = ""
        self.sw_plikTytul_fullPath  = ""
        self.sw_plikUwagi_fullPath  = ""
        self.sw_plikGodla2swInfo_fullPath  = ""
        self.sw_plikNr_nazwa        = ""
        self.sw_plikNr_fullPath     = ""
        self.sw_plikDz_ergo_abspath = ""
        self.sw_plikDz_kg_abspath = ""

        self.struktura_sw = sytwys_elements.StrukturaKatalogow()

    def setNazwyPlikow_tytul_uwagi(self):
        """
        z danej �cie�ki pliku info tworzy �cie�ki do plik�w
        - "tytNagl"
        - "tytu�"
        - "uwagi"
        =====================================================================
        """
        
        """ 
        cz�� wywiadowcza:
        p = r't:\sytwys\15_kp_2401_BialaG_21'
        print( "---[ path ]--------------------------------------------------------")
        print( "p = %s" % (p))
        print( "%s" % (os.path.basename( p)))
        print( "%s" % (os.path.dirname( p)))
        print( "join = %s" % ( os.path.join( os.path.dirname( p), os.path.basename( p))))
        print( "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        """
        p = self.sw_plikInfo_fullPath
        self.sw_plikTytNagl_fullPath = os.path.join(os.path.dirname(p), self.FILE_TYTNAGL)
        self.sw_plikTytul_fullPath  = os.path.join( os.path.dirname(p), self.FILE_TYTUL)
        self.sw_plikUwagi_fullPath  = os.path.join( os.path.dirname(p), self.FILE_UWAGI)
        self.sw_plikGodla2swInfo_fullPath  = os.path.join( os.path.dirname(p), self.FILE_GODLA)
        # w katalogu ...\kG:
        #self.sw_plikDz_ergo_abspath = os.path.join(os.path.dirname(p), self.sw_dictDirs["kG"])
        self.sw_plikDz_ergo_abspath = os.path.join(self.struktura_sw.sw_dictDirs["kG"], self.FILE_DZIALKI_ERGO)
        self.sw_plikDz_kg_abspath = os.path.join(self.struktura_sw.sw_dictDirs["kG"], self.FILE_KG_ERGO)
        # deb
        #print("def setNazwyPlikow_tytul_uwagi( self):")
        #print( " *1* godla2swInfo.txt= >%s<" % (self.sw.sw_plikGodla2swInfo_fullPath))
        
        
    
    def ustalNrSW( self, adir_licznik, dir_sytwys):
        """
         ustalenie  numeru dla nowej roboty s-w
         -  polega na sprawdzeniu, jaki jest ostatni plik
            w katalogu DIR_LICZNIK i odczytanie jego nru
            t:\sytwys\AAB__licznik\16___kp_2401_Bagna_55.nr
         - dodatkowo sprawdzany jest ostatni katalog sw
           - ta metoda mo�e by� zawodna w sytuacji, kiedy robota o najwy�szym
             numerze zosta�a ju� zako�czona i przeniesiona do archiwum


         adir_licznik :: katalog z plikami licznikowymi
        =====================================================================
        """
        # deb - zawarto�� katalogu:
        # fileList = [f for f in os.listdir(adir_licznik)]
        # [print(f) for f in fileList]
        # print('----1')

        # lista numer�w wyekstrachowanych z nazw plik�w i katalog�w
        # - pliki maj� nazwy typu:
        #   16___kp_2401_Bagna_55.nr
        #   ostatni numer = 16
        num_list = [int(f.split('_')[0]) for f in os.listdir(adir_licznik)]
        self.sw_numer = max(num_list) + 1

        # numer dekodowany z nazwy katalogu sytwys
        # 15_kp_2401_BialaG_21
        # ?> tutaj jest zastosowany myk, polegaj�cy na ograniczeniu zawarto�ci
        #    listy do nazw, kt�re:
        #    - maj� cztery znaki w cz�ci pierwszej przed znakiem `_` - tak
        #      jest w przypadku nazw katalog�w sw
        #    - pierwszy znak cz�ci pierwszej, to `1`
        file_name_pattern = re.compile(r'\d{1,4}_[a-z]{2}_\d{4}_.+')
        num_list = [int(f.split('_')[0])
                    for f
                    in os.listdir(dir_sytwys)
                    if re.fullmatch(file_name_pattern, f)]
        sw_numer_alternative = max(num_list) + 1

        # deb
        print(f'{self.sw_numer=} vs {sw_numer_alternative=}')

        if self.sw_numer != sw_numer_alternative:
            msg = f'{self.sw_numer=}\n{sw_numer_alternative=}\n'
            msg += f'Y: zatwierdzi� numer {self.sw_numer=}\n'
            msg += f'N: zatwierdzi� numer {sw_numer_alternative=}\n'
            msg += f'C: raise Exception()?'
            response = messagebox.askquestion(
                'Problem z numerwem sw',
                msg, type=messagebox.YESNOCANCEL, )
            if response == messagebox.YES:
                # deb
                print(f"1 Wybrany numer licznika dla roboty: {self.sw_numer}")
            elif response == messagebox.NO:
                self.sw_numer = sw_numer_alternative
                print(f"1 Wybrany numer licznika dla roboty: {self.sw_numer}")
            else:
                raise Exception()
        # deb
        print(f"2 Numer licznika dla roboty: {self.sw_numer}")

    def update_dzialki(self, terytF_obr, teryt_jew, nazwa_obr):
        """
        aktualizuje listy numer�w dzia�ek
        - funkcja u�yta w metodzie zapisz()
        - jako �r�d�a danych o dzia�kach u�ywa obiektu sw.dzialki_obj
          - jest on aktualizowany w metodzie inicjuj()
          - zak�adamy, �e w momencie wywo�ania matody zapisz() dzia�ki
            wy�wietlone w swoim polu i przechowywane w obiekcie dzialki_obj
            s� aktualne
        """
        self.sw_dzialki = self.sw_dzialki_obj.sorted_string_nr_prz_sp
        self.sw_dzialki_lst = self.sw_dzialki_obj.lista_nr_sorted
        self.sw_dzialki_obj.source_obr_nazwa = nazwa_obr
        self.sw_dzialki_obj.source_jew_teryt_do_kG = teryt_jew
        self.sw_dzialka1 = self.sw_dzialki_obj.dzialka1

        """
        tworzy list� dzia�ek w formacie wymaganym przez Ergo podczas
        tworzenia zakresu zam�wienia/zg�oszenia z pliku
        -   format:
            999999_9.9999.dz1

        terytF_obr (z instancji teryt)
        "999999_9.9999"
        """
        self.sw_dzialki_ergo_lst.clear()
        for dz in self.sw_dzialki_lst:
            s = f'{terytF_obr}.{dz}'
            self.sw_dzialki_ergo_lst.append(s)
        # deb
        for dz in self.sw_dzialki_ergo_lst:
            print(f'(ergo:) {dz = }')

    def set_defaults(self):
        """
        nadaje niekt�rym atrybutom domy�lne warto�ci, w�a�ciwe dla nowej robooty

        !!! funkcja w stanie pocz�tkowym
        """
        self.sw_numer_str = str(self.sw_numer)
        self.sw_wykonawca = "kp"
        self.sw_obreb = "Nowa Wie�-Kl"
        self.sw_obrebDir = ""

        self.sw_dzialki         = "309, 310 3 , 2000/1, 4, "
        self.sw_dzialki_lst     = list()
        self.sw_dzialki_ergo_lst = list()
        self.sw_dzialka1        = ""
        self.sw_dzialki_obj = dzialki.Dzialki()

        self.sw_typ             = ""
        self.sw_idZgl           = ""
        self.sw_idZgl_jrwa      = ""
        self.sw_idZgl_nr        = ""
        self.sw_idZgl_rok       = ""
        self.sw_skala           = ""
