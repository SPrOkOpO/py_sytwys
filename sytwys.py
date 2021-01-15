#-*- coding: windows-1250 -*-

import os
import sys
#import datetime
import shutil

import sytwys_elements
sys.path.append(r"i:\aPy\LibSP")
sys.path.append(r"i:\aPy\LibSP\sytwys")
import dzialki

"""
#-####################################################################
    grupuje dane związane z robotą sw
    klasa jest obecnie zbyt rozbudowana i wymaga przeprogramowania
    
    plan zmian
    ----------
    +   przemieszczenie danych do klas bardziej wyspecjalizowanych
        -   Inwentaryzacja
        -   PlikSWinfo 
    
    ToDO - must have:
    >>  

    ToDO - w razie nudów:
    >>  

######################################################################
"""




class   Sytwys( object):
    '''
    obsługa roboty  s-w


    '''
    def __init__( self):

        # stałe,    ale na razie jako   zwykle pola
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
        # self.sw_mdcp_kp_uwagi2 = "Dane dotyczące granic działki ..., ujawn..."
        # self.sw_mdcp_kp_uwagi3 = "Dla obszaru w granicach projektowanej inwestycji budowlanej brak obciążeń z tytułu służebności \ngruntowych (§80 ust. 4. rozp. MSWiA z dnia 9 listopada 2011 r.)."
        # self.sw_mdcp_kp_uwagi4 = "Dla terenu objętego opracowaniem brak opracowań planistycznych."
        # self.sw_mdcp_kp_uwagi5 = "Granice nieruchomości oznaczono kolorem zielonym."
        # self.sw_mdcp_kp_uwagi6  = "Nie wyklucza się istnienia w terenie innych, niewykazanych na niniejszej mapie, urządzeń \npodziemnych."
        # self.sw_mdcp_kp_uwagi6 = "Nie wyklucza się istnienia w terenie innych, niewykazanych na niniejszej mapie, urządzeń \npodziemnych, które nie były zgłoszone do inwentaryzacji lub o których brak jest informacji\nw instytucjach branżowych."
        #
        # self.sw_mdcp_kp_uwagi1_fraza1 = "Mapa utworzona na podstawie arkusza "
        # self.sw_mdcp_kp_uwagi1_fraza2 = " mapy zasadniczej oraz pomiaru aktualizacyjnego id. zgł. "
        #
        # self.sw_mdcp_kp_uwagi2_fraza1 = "Dane dotyczące granic działki "
        # self.sw_mdcp_kp_uwagi2_fraza2 = ", ujawnione w PZGiK, "
        # self.sw_mdcp_kp_uwagi2_fraza3 = "przepisów §79, ust. 5 i 6 rozp. MSWiA z dnia 9 listopada 2011 r."


        # dane do libre
        self.sw_libre_wykon = ""
        self.sw_libre_opis  = ""

        # sekcje
        # słownik sekcji
        # - zawiera dwa (na razie) rodzaje kluczy
        #       -   na pojedyncze godła
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
        self.sw_sekcje_tytul    = "Sekcje mapy zas. ukł. 2000: "
        self.sw_lstSekcje       = []
        

        self.plik_sw_info = sytwys_elements.PlikSWinfo()

        # ścieżki
        # stałe,    ale na razie jako   zwykle pola
        self.FILE_TYTUL  =  "tytul.txt"
        self.FILE_UWAGI  =  "uwagi.txt"
        self.FILE_GODLA  =  "godla2swInfo.txt"
        self.FILE_DZIALKI_ERGO = "dz_ergo.txt"
        self.FILE_KG_ERGO = "kg.txt"

        self.sw_dir_nazwa           = ""
        self.sw_plikInfo_fullPath   = ""
        self.sw_plikTytul_fullPath  = ""
        self.sw_plikUwagi_fullPath  = ""
        self.sw_plikGodla2swInfo_fullPath  = ""
        self.sw_plikNr_nazwa        = ""
        self.sw_plikNr_fullPath     = ""
        self.sw_plikDz_ergo_abspath = ""
        self.sw_plikDz_kg_abspath = ""

        self.struktura_sw = sytwys_elements.StrukturaKatalogow()
        # słownik z katalogami s-w
        self.sw_dictDirs = {
            "dane_ergo"                     : "",
            "dane_wyk"                      : "",
            "dane_wyk_oryg"                 : "",
            "mz_nr_v7"                      : "",
            "mz_nr_v8"                      : "",
            "mz_nr_v8__v7"                  : "",
            "mz_nr_v8__v7_bac"              : "",
            "orient"                        : "",
            "tabelki"                       : "",
            "tabelki__100_oryg"             : "",
            "txt"                           : "",
            "wyslane"                       : "",
            "z_dxf"                         : "",
            "z_dxf_1"                       : "",
            "z_dxf_2"                       : "",
            "z_dxf_3"                       : "",
            "z_dxf_1__zbedne"               : "",
            "z_dxf_2__zbedne"               : "",
            "z_dxf_3__zbedne"               : "",
            "zz_backup"                     : "",
            "zz_wersjeNieakt"               : "",
            "kG": "",

            "rasC_sytwys"                   : ""
        }
    
    # koniec __init__()
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
        
    def setNazwyPlikow_tytul_uwagi( self):
        '''
        z danej ścieżki pliku info tworzy ścieżki do plików "tytuł" i "uwagi"
        =====================================================================
        '''
        
        ''' 
        część wywiadowcza:
        p = "t:\\sytwys\\826_kp_1904_Biezen_7-24\\sw_826_info.txt"
        print( "---[ path ]--------------------------------------------------------")
        print( "p = %s" % (p))
        print( "%s" % (os.path.basename( p)))
        print( "%s" % (os.path.dirname( p)))
        print( "join = %s" % ( os.path.join( os.path.dirname( p), os.path.basename( p))))
        print( "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        '''
        p = self.sw_plikInfo_fullPath
        self.sw_plikTytul_fullPath  = os.path.join( os.path.dirname( p), self.FILE_TYTUL)
        self.sw_plikUwagi_fullPath  = os.path.join( os.path.dirname( p), self.FILE_UWAGI)
        self.sw_plikGodla2swInfo_fullPath  = os.path.join( os.path.dirname( p), self.FILE_GODLA)
        # w katalogu ...\kG:
        #self.sw_plikDz_ergo_abspath = os.path.join(os.path.dirname(p), self.sw_dictDirs["kG"])
        self.sw_plikDz_ergo_abspath = os.path.join(self.sw_dictDirs["kG"], self.FILE_DZIALKI_ERGO)
        self.sw_plikDz_kg_abspath = os.path.join(self.sw_dictDirs["kG"], self.FILE_KG_ERGO)
        # deb
        #print("def setNazwyPlikow_tytul_uwagi( self):")
        #print( " *1* godla2swInfo.txt= >%s<" % (self.sw.sw_plikGodla2swInfo_fullPath))
        
        
    
    def ustalNrSW( self, adir_licznik):
        '''
         ustalenie  numeru dla nowej roboty s-w
         -  polega na sprawdzeniu, jaki jest ostatni plik
            w katalogu DIR_LICZNIK i odczytanie jego nru
            t:\sytwys\AAB__licznik\909___kp_2001_Bagna_55_inw.nr

         adir_licznik :: katalog z plikami licznikowymi
        =====================================================================
        '''
        # deb - zawartość katalogu:
        # fileList = [f for f in os.listdir(adir_licznik)]
        # [print(f) for f in fileList]
        # print('----1')

        # lista numerów wyekstrachowanych z nazw plików i katalogów
        num_list = [f.split('_')[0] for f in os.listdir(adir_licznik)]
        self.sw_numer = -1
        for nr_str in num_list:
            # deb
            # print(f'{nr_str = }')
            if int(nr_str) > self.sw_numer:
                self.sw_numer = int(nr_str)
        self.sw_numer = self.sw_numer + 1
        #deb
        print( "Numer licznika dla roboty: %d" % (self.sw_numer))


    def inicjujStrukture( self, asw_dir_nazwa):
        '''
            dot. struktury katalogów i plików sw
            przypisanie odpowiednich wartości do słownika katalogów
        '''
        self.sw_dictDirs[   "dane_ergo"             ] = asw_dir_nazwa   + "\\dane_ergo\\"
        self.sw_dictDirs[   "dane_wyk"              ] = asw_dir_nazwa   + "\\dane-" + self.sw_wykonawca + "\\"
        self.sw_dictDirs[   "dane_wyk_oryg"         ] = self.sw_dictDirs[ "dane_wyk"] + "_oryg\\"
        self.sw_dictDirs[   "mz_nr_v7"              ] = asw_dir_nazwa   + "\\mz_" + self.sw_numer_str   + "_v7\\"
        self.sw_dictDirs[   "mz_nr_v8"              ] = asw_dir_nazwa   + "\\mz_" + self.sw_numer_str   + "_v8\\"
        self.sw_dictDirs[   "mz_nr_v8__v7"          ] = self.sw_dictDirs[ "mz_nr_v8"] + "v7"
        self.sw_dictDirs[   "mz_nr_v8__v7_bac"      ] = self.sw_dictDirs[ "mz_nr_v8"] + "v7_bac"
        self.sw_dictDirs[   "orient"                ] = asw_dir_nazwa   + "\\orient\\"
        self.sw_dictDirs[   "tabelki"               ] = asw_dir_nazwa   + self.DIR_TABELKI
        self.sw_dictDirs[   "tabelki__100_oryg"     ] = asw_dir_nazwa   + self.DIR_TABELKI_100
        self.sw_dictDirs[   "txt"                   ] = asw_dir_nazwa   + "\\txt\\"
        self.sw_dictDirs[   "wyslane"               ] = asw_dir_nazwa   + "\\wyslane\\"
        self.sw_dictDirs[   "z_dxf"                 ] = asw_dir_nazwa   + "\\z_dxf\\"
        self.sw_dictDirs[   "z_dxf_1"               ] = self.sw_dictDirs[ "z_dxf"] +    "\\1\\"
        self.sw_dictDirs[   "z_dxf_2"               ] = self.sw_dictDirs[ "z_dxf"] +    "\\2\\"
        self.sw_dictDirs[   "z_dxf_3"               ] = self.sw_dictDirs[ "z_dxf"] +    "\\3\\"
        self.sw_dictDirs[   "z_dxf_1__zbedne"       ] = self.sw_dictDirs[ "z_dxf_1"]    + "zbedne\\"
        self.sw_dictDirs[   "z_dxf_2__zbedne"       ] = self.sw_dictDirs[ "z_dxf_2"]    + "zbedne\\"
        self.sw_dictDirs[   "z_dxf_3__zbedne"       ] = self.sw_dictDirs[ "z_dxf_3"]    + "zbedne\\"
        self.sw_dictDirs[   "zz_backup"             ] = asw_dir_nazwa   + "\\zz_backup\\"
        self.sw_dictDirs[   "zz_wersjeNieakt"       ] = asw_dir_nazwa   + "\\zz_wersjeNieakt\\"
        self.sw_dictDirs[   "kG"                    ] = asw_dir_nazwa   + "\\kG\\"

        self.sw_dictDirs[   "rasC_sytwys"           ] = "t:\\&&RasC\\sytwys\\" + self.sw_numer_str + "_" + self.sw_obrebDir
    
    
    def deb_listujStrukture( self):
        '''
            debugowanie
            -   listing całego  katalogu
        '''
        print( "---[ sw_dictDirs ]------------------------------------------------")
        for x   in  self.sw_dictDirs:
            print( x + "=" + self.sw_dictDirs[x])
        print( "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


    def utworzStrukture(    self):
        '''
        >>  trzeba dorobić: 
            -   sprawdzenie, czy te katalogi istnieją
            -   funkcję, która skasuje błędnie założoną strukturę
        
        '''   
        # utworzenie struktury katalogów
        #-------------------------------------------------------
        os.makedirs(self.sw_dictDirs[ "dane_ergo"          ])
        os.makedirs(self.sw_dictDirs[ "dane_wyk"           ])
        os.makedirs(self.sw_dictDirs[ "dane_wyk_oryg"      ])
        os.makedirs(self.sw_dictDirs[ "mz_nr_v7"           ])
        os.makedirs(self.sw_dictDirs[ "mz_nr_v8"           ])
        os.makedirs(self.sw_dictDirs[ "mz_nr_v8__v7"       ])
        os.makedirs(self.sw_dictDirs[ "mz_nr_v8__v7_bac"   ])
        os.makedirs(self.sw_dictDirs[ "orient"             ])
        os.makedirs(self.sw_dictDirs[ "tabelki"            ])
        os.makedirs(self.sw_dictDirs[ "tabelki__100_oryg"  ])
        os.makedirs(self.sw_dictDirs[ "txt"                ])
        os.makedirs(self.sw_dictDirs[ "wyslane"            ])
        os.makedirs(self.sw_dictDirs[ "z_dxf"              ])
        os.makedirs(self.sw_dictDirs[ "z_dxf_1"            ])
        os.makedirs(self.sw_dictDirs[ "z_dxf_2"            ])
        os.makedirs(self.sw_dictDirs[ "z_dxf_3"            ])
        os.makedirs(self.sw_dictDirs[ "z_dxf_1__zbedne"    ])
        os.makedirs(self.sw_dictDirs[ "z_dxf_2__zbedne"    ])
        os.makedirs(self.sw_dictDirs[ "z_dxf_3__zbedne"    ])
        os.makedirs(self.sw_dictDirs[ "zz_backup"          ])
        os.makedirs(self.sw_dictDirs[ "zz_wersjeNieakt"    ])
        os.makedirs(self.sw_dictDirs["kG"])

        if os.path.exists( self.sw_dictDirs[ "rasC_sytwys"]) == False:
            os.makedirs( self.sw_dictDirs[ "rasC_sytwys"        ])

        # kopiowanie plików do mz...v7
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        sourceFile = "c:\\USSP\\SEED\\seed_ctBialy_u2k_go50_1cm_mzKlobuck_geoRef.dgn"
        targetDir = self.sw_dictDirs[ "mz_nr_v7"]
        shutil.copy( sourceFile, os.path.join( targetDir, "a_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "b_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "s_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "y_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "z_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "#_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "1_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "2_v7.dgn"))
        shutil.copy( sourceFile, os.path.join( targetDir, "3_v7.dgn"))

        # kopiowanie plików do mz...v8
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        sourceFile = "c:\\USSP\\SEED\\v8_2004\\zDXF_v8_poziomy-v7.dgn"
        targetDir = self.sw_dictDirs[ "mz_nr_v8"]
        shutil.copy( sourceFile, os.path.join( targetDir, "zDXF_v8.dgn"))
        targetDir = self.sw_dictDirs[ "mz_nr_v8"]
        shutil.copy( sourceFile, os.path.join( targetDir, "zDXF_v8_pusty.dgn"))

        # utworzenie pliku #_pikiety_XXX.dgn
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        sourceFile = "t:\\sytwys_T\\zzz_wzor_mdcp\\mdcp2k\\#_mdcp2k.dgn"
        targetDir = self.sw_dir_nazwa
        plikPikiety_nazwa = "#_pikiety_" + self.sw_numer_str + ".dgn"
        shutil.copy( sourceFile, os.path.join( targetDir, plikPikiety_nazwa))

    def update_dzialki(self, terytF_obr, teryt_jew, nazwa_obr):
        """
        aktualizuje listy numerów działek
        - funkcja użyta w metodzie zapisz()
        - jako źródła danych o działkach używa obiektu sw.dzialki_obj
          - jest on aktualizowany w metodzie inicjuj()
          - zakładamy, że w momencie wywołania matody zapisz() działki
            wyświetlone w swoim polu i przechowywane w obiekcie dzialki_obj
            są aktualne
        """
        self.sw_dzialki = self.sw_dzialki_obj.sorted_string_nr_prz_sp
        self.sw_dzialki_lst = self.sw_dzialki_obj.lista_nr_sorted
        self.sw_dzialki_obj.source_obr_nazwa = nazwa_obr
        self.sw_dzialki_obj.source_jew_teryt_do_kG = teryt_jew
        self.sw_dzialka1 = self.sw_dzialki_obj.dzialka1

        """
        tworzy listę działek w formacie wymaganym przez Ergo podczas
        tworzenia zakresu zamówienia/zgłoszenia z pliku
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

