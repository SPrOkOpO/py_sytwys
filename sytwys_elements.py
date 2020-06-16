import os
import shutil

import dictConstants

class StrukturaKatalogow:
    #def __init__(self, sw_dir_abspath, sw_wykonawca, sw_numer_str):
    def __init__(self):
        # po uruchomieniu programu nie są znane argumenty: sw_dir_abspath,
        # sw_wykonawca, sw_numer_str, więc zainicjowanie struktury w __init__
        # nie ma sensu
        self.sw_dir_abspath = ''
        self.sw_wykonawca = ''
        self.sw_numer_str = ''
        self.sw_obrebDir = ''
        # słownik z katalogami s-w
        self.sw_dictDirs = {
            "dane_ergo": "",
            "dane_wyk": "",
            "dane_wyk_oryg": "",
            "mz_nr_v7": "",
            "mz_nr_v8": "",
            "mz_nr_v8__v7": "",
            "mz_nr_v8__v7_bac": "",
            "orient": "",
            "tabelki": "",
            "tabelki__100_oryg": "",
            "txt": "",
            "wyslane": "",
            "z_dxf": "",
            "z_dxf_1": "",
            "z_dxf_2": "",
            "z_dxf_3": "",
            "z_dxf_1__zbedne": "",
            "z_dxf_2__zbedne": "",
            "z_dxf_3__zbedne": "",
            "zz_backup": "",
            "zz_wersjeNieakt": "",
            "kG":'',

            "rasC_sytwys": ""
        }


    def inicjujStrukture( self):
        '''
            dot. struktury katalogów i plików sw
            przypisanie odpowiednich wartości do słownika katalogów
        '''
        self.sw_dictDirs["dane_ergo"             ] = self.sw_dir_abspath   + "\\dane_ergo\\"
        self.sw_dictDirs["dane_wyk"              ] = self.sw_dir_abspath   + "\\dane-" + self.sw_wykonawca + "\\"
        self.sw_dictDirs["dane_wyk_oryg"         ] = self.sw_dictDirs[ "dane_wyk"] + "_oryg\\"
        self.sw_dictDirs["mz_nr_v7"              ] = self.sw_dir_abspath   + "\\mz_" + self.sw_numer_str   + "_v7\\"
        self.sw_dictDirs["mz_nr_v8"              ] = self.sw_dir_abspath   + "\\mz_" + self.sw_numer_str   + "_v8\\"
        self.sw_dictDirs["mz_nr_v8__v7"          ] = self.sw_dictDirs[ "mz_nr_v8"] + "v7"
        self.sw_dictDirs["mz_nr_v8__v7_bac"      ] = self.sw_dictDirs[ "mz_nr_v8"] + "v7_bac"
        self.sw_dictDirs["orient"                ] = self.sw_dir_abspath   + "\\orient\\"
        self.sw_dictDirs["tabelki"               ] = self.sw_dir_abspath   + "\\tabelki\\"
        self.sw_dictDirs["tabelki__100_oryg"     ] = self.sw_dir_abspath   + "\\tabelki\\100_oryg\\"
        self.sw_dictDirs["txt"                   ] = self.sw_dir_abspath   + "\\txt\\"
        self.sw_dictDirs["wyslane"               ] = self.sw_dir_abspath   + "\\wyslane\\"
        self.sw_dictDirs["z_dxf"                 ] = self.sw_dir_abspath   + "\\z_dxf\\"
        self.sw_dictDirs["z_dxf_1"               ] = self.sw_dictDirs[ "z_dxf"] +    "\\1\\"
        self.sw_dictDirs["z_dxf_2"               ] = self.sw_dictDirs[ "z_dxf"] +    "\\2\\"
        self.sw_dictDirs["z_dxf_3"               ] = self.sw_dictDirs[ "z_dxf"] +    "\\3\\"
        self.sw_dictDirs["z_dxf_1__zbedne"       ] = self.sw_dictDirs[ "z_dxf_1"]    + "zbedne\\"
        self.sw_dictDirs["z_dxf_2__zbedne"       ] = self.sw_dictDirs[ "z_dxf_2"]    + "zbedne\\"
        self.sw_dictDirs["z_dxf_3__zbedne"       ] = self.sw_dictDirs[ "z_dxf_3"]    + "zbedne\\"
        self.sw_dictDirs["zz_backup"             ] = self.sw_dir_abspath   + "\\zz_backup\\"
        self.sw_dictDirs["zz_wersjeNieakt"       ] = self.sw_dir_abspath   + "\\zz_wersjeNieakt\\"
        self.sw_dictDirs["kG"                    ] = self.sw_dir_abspath   + "\\kG\\"

        self.sw_dictDirs["rasC_sytwys"           ] = "t:\\&&RasC\\sytwys\\" + self.sw_numer_str + "_" + self.sw_obrebDir

    def deb_listujStrukture( self):
        '''
            debugowanie
            -   listing całego  katalogu
        '''
        print( "---[ sw_dictDirs ]------------------------------------------------")
        for x   in  self.sw_dictDirs:
            print( x + "=" + self.sw_dictDirs[x])
        print( "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    def utworzStrukture(self):
        '''
        >>  trzeba dorobić:
            -   sprawdzenie, czy te katalogi istnieją
            -   funkcję, która skasuje błędnie założoną strukturę

        '''
        # utworzenie struktury katalogów
        # -------------------------------------------------------
        os.makedirs(self.sw_dictDirs["dane_ergo"])
        os.makedirs(self.sw_dictDirs["dane_wyk"])
        os.makedirs(self.sw_dictDirs["dane_wyk_oryg"])
        os.makedirs(self.sw_dictDirs["mz_nr_v7"])
        os.makedirs(self.sw_dictDirs["mz_nr_v8"])
        os.makedirs(self.sw_dictDirs["mz_nr_v8__v7"])
        os.makedirs(self.sw_dictDirs["mz_nr_v8__v7_bac"])
        os.makedirs(self.sw_dictDirs["orient"])
        os.makedirs(self.sw_dictDirs["tabelki"])
        os.makedirs(self.sw_dictDirs["tabelki__100_oryg"])
        os.makedirs(self.sw_dictDirs["txt"])
        os.makedirs(self.sw_dictDirs["wyslane"])
        os.makedirs(self.sw_dictDirs["z_dxf"])
        os.makedirs(self.sw_dictDirs["z_dxf_1"])
        os.makedirs(self.sw_dictDirs["z_dxf_2"])
        os.makedirs(self.sw_dictDirs["z_dxf_3"])
        os.makedirs(self.sw_dictDirs["z_dxf_1__zbedne"])
        os.makedirs(self.sw_dictDirs["z_dxf_2__zbedne"])
        os.makedirs(self.sw_dictDirs["z_dxf_3__zbedne"])
        os.makedirs(self.sw_dictDirs["zz_backup"])
        os.makedirs(self.sw_dictDirs["zz_wersjeNieakt"])
        os.makedirs(self.sw_dictDirs["kG"])

        if os.path.exists(self.sw_dictDirs["rasC_sytwys"]) == False:
            os.makedirs(self.sw_dictDirs["rasC_sytwys"])

        # kopiowanie plików do mz...v7
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        sourceFile = "c:\\USSP\\SEED\\seed_ctBialy_u2k_go50_1cm_mzKlobuck_geoRef.dgn"
        targetDir = self.sw_dictDirs["mz_nr_v7"]
        shutil.copy(sourceFile, os.path.join(targetDir, "a_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "b_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "s_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "y_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "z_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "#_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "1_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "2_v7.dgn"))
        shutil.copy(sourceFile, os.path.join(targetDir, "3_v7.dgn"))

        # kopiowanie plików do mz...v8
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        sourceFile = "c:\\USSP\\SEED\\v8_2004\\zDXF_v8_poziomy-v7.dgn"
        targetDir = self.sw_dictDirs["mz_nr_v8"]
        shutil.copy(sourceFile, os.path.join(targetDir, "zDXF_v8.dgn"))
        targetDir = self.sw_dictDirs["mz_nr_v8"]
        shutil.copy(sourceFile, os.path.join(targetDir, "zDXF_v8_pusty.dgn"))

        # utworzenie pliku #_pikiety_XXX.dgn
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        sourceFile = "t:\\sytwys_T\\zzz_wzor_mdcp\\mdcp2k\\#_mdcp2k.dgn"
        targetDir = self.sw_dir_abspath
        plikPikiety_nazwa = "#_pikiety_" + self.sw_numer_str + ".dgn"
        shutil.copy(sourceFile, os.path.join(targetDir, plikPikiety_nazwa))


class PlikSWinfo():
    """
    separacja obsługi pliku sw_XXX_info.txt oraz danych w nim zapisanych
    """
    def __init__(self):
        self.abspath = ''


class Inwentaryzacja():
    def __init__(self):
        self.obiekt = ''
        self.obiekt_do_uwag = ''
        self.nr_zal = ''
        self.dec_znak = ''
        self.dec_data = ''

    def set_default(self):
        self.obiekt = 'budynku mieszkalnego wraz z przyłączami'
        self.obiekt_do_uwag = 'budynku mieszkalnego'
        self.nr_zal = '1'
        self.dec_znak = 'GPN.6730.140.2018.UC'
        self.dec_data = '2018'

    def set_empty(self):
        self.obiekt = ''
        self.obiekt_do_uwag = ''
        self.nr_zal = ''
        self.dec_znak = ''
        self.dec_data = ''


class MDCP():
    def __init__(self):
        self.ust5 = 1
        self.ust6 = 1
        self.ust5_str = "1"
        self.ust6_str = "1"
        self.kp_uwagi1 = "Mapa utworzona na podstawie arkusza ..."
        self.kp_uwagi2 = "Dane dotyczące działki ..., ujawn..."
        self.kp_uwagi3 = "Dla obszaru w granicach projektowanej inwestycji budowlanej brak obciążeń z tytułu służebności \ngruntowych (§80 ust. 4. rozp. MSWiA z dnia 9 listopada 2011 r.)."
        self.kp_uwagi4 = "Dla terenu objętego opracowaniem brak opracowań planistycznych."
        self.kp_uwagi5 = "Granice nieruchomości oznaczono kolorem zielonym."
        # self.kp_uwagi6  = "Nie wyklucza się istnienia w terenie innych, niewykazanych na niniejszej mapie, urządzeń \npodziemnych."
        self.kp_uwagi6 = "Nie wyklucza się istnienia w terenie innych, niewykazanych na niniejszej mapie, urządzeń \npodziemnych, które nie były zgłoszone do inwentaryzacji lub o których brak jest informacji\nw instytucjach branżowych."

        self.uwagi1_fraza1 = "Mapa utworzona na podstawie arkusza "
        self.uwagi1_fraza2 = " mapy zasadniczej oraz pomiaru aktualizacyjnego id. zgł. "

        self.uwagi2_fraza1 = "Dane dotyczące działki "
        self.uwagi2_fraza2 = ", ujawnione w PZGiK, "
        self.uwagi2_fraza3 = "przepisów §79, ust. 5 i 6 rozp. MSWiA z dnia 9 listopada 2011 r."

        '''
        Mapa utworzona na podstawie arkusza 6.144.30.07.4.1, 6.144.30.07.4.2 mapy zasadniczej oraz 
        pomiaru aktualizacyjnego id. zgł. GKN.6640.446.2019

        Dane dotyczące granic działki 309, 310, ujawnione w PZGiK, spełniają warunki przepisów §79, ust.  
        5 i 6 rozp. MSWiA z dnia 9 listopada 2011 r.

        Dla obszaru w granicach projektowanej inwestycji budowlanej brak obciążeń z tytułu służebności 
        gruntowych (§80 ust. 4. rozp. MSWiA z dnia 9 listopada 2011 r.)

        Dla terenu objętego opracowaniem brak opracowań planistycznych.

        Granice nieruchomości oznaczono kolorem zielonym. 

        Nie wyklucza się istnienia w terenie innych niewykazanych na niniejszej mapie urządzeń 
        podziemnych. 
        '''
