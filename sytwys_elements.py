import sys
import os
import shutil
import configparser

lib_abspaths = [r'i:\aPy\LibSP',
                ]
for path in lib_abspaths:
    if path not in sys.path:
        sys.path.append(path)
import spos


class StrukturaKatalogow:
    """

    """
    def __init__(self, dictConstants):
        # kopia słownika stałych globalnych, z którego potrzebne są
        # - "GC_DIR_SYTWYS"         : "t:\\sytwys",
        # - 'GC_EMPTY_STRATEG_DATABASE_DIR': r't:\STRATEG\BAZA_pusta',
        self.dictConstants = dictConstants
        self.empty_strateg_database = self.dictConstants['GC_EMPTY_STRATEG_DATABASE_DIR']
        self.ewmapa_baza_ini = self.dictConstants['GC_EWMAPA_BAZA_INIFILE']

        self.sw_dir_abspath = ''
        self.sw_wykonawca = ''
        self.sw_numer_str = ''
        self.sw_obrebDir = ''
        # słownik z katalogami s-w
        self.sw_dictDirs = dict()


    def inicjujStrukture(self,
                         sw_dir_abspath,
                         sw_wykonawca,
                         sw_numer_str,
                         sw_obrebDir,
                         ):
        """
            dot. struktury katalogów i plików sw
            przypisanie odpowiednich wartości do słownika katalogów
        """
        # atrybuty potrzebne do tworzenia ścieżek i wpisów do baza.ini
        # ---------------------------------------------------------------------
        self.sw_dir_abspath = sw_dir_abspath
        self.sw_wykonawca = sw_wykonawca
        self.sw_numer_str = sw_numer_str
        self.sw_obrebDir = sw_obrebDir
        self.ewmapa_baza_id_str = f'Baza_{self.sw_numer_str}{self.sw_wykonawca}'
        # deb
        print(f'\t{self.sw_dir_abspath=}')
        print(f'\t{self.sw_wykonawca=}')
        print(f'\t{self.sw_numer_str=}')
        print(f'\t{self.sw_obrebDir=}')


        # słownik ścieżek
        # ---------------------------------------------------------------------
        self.sw_dictDirs["baza"] = self.sw_dir_abspath + "\\BAZA_" + self.sw_numer_str + self.sw_wykonawca
        self.sw_dictDirs["dane_ergo"        ] = self.sw_dir_abspath   + "\\dane_ergo\\"

        self.sw_dictDirs["dane_wyk"         ] = self.sw_dir_abspath   + "\\dane-" + self.sw_wykonawca + "\\"
        self.sw_dictDirs["dane_wyk_oryg"    ] = self.sw_dictDirs[ "dane_wyk"] + "_oryg\\"

        self.sw_dictDirs["dxf"] = self.sw_dir_abspath + "\\dxf\\"
        self.sw_dictDirs["gml_1_do_modyf"] = self.sw_dir_abspath + "\\gml_1_do_modyf\\"
        self.sw_dictDirs["gml_2_eksport"] = self.sw_dir_abspath + "\\gml_2_eksport\\"

        self.sw_dictDirs["mz_nr_v7"         ] = self.sw_dir_abspath   + "\\mz_" + self.sw_numer_str + "_v7\\"
        self.sw_dictDirs["mz_nr_v8"         ] = self.sw_dir_abspath   + "\\mz_" + self.sw_numer_str + "_v8\\"
        self.sw_dictDirs["mz_nr_v8__v7"     ] = self.sw_dictDirs[ "mz_nr_v8"] + "v7"
        self.sw_dictDirs["mz_nr_v8__v7_bac" ] = self.sw_dictDirs[ "mz_nr_v8"] + "v7_bac"
        self.sw_dictDirs["orient"           ] = self.sw_dir_abspath   + "\\orient\\"
        self.sw_dictDirs["tabelki"          ] = self.sw_dir_abspath   + "\\tabelki\\"
        self.sw_dictDirs["tabelki__100_oryg"] = self.sw_dir_abspath   + "\\tabelki\\100_oryg\\"
        self.sw_dictDirs["txt"              ] = self.sw_dir_abspath   + "\\txt\\"
        self.sw_dictDirs["wyslane"          ] = self.sw_dir_abspath   + "\\wyslane\\"
        self.sw_dictDirs["z_dxf"            ] = self.sw_dir_abspath   + "\\z_dxf\\"
        self.sw_dictDirs["z_dxf_1"          ] = self.sw_dictDirs[ "z_dxf"] +    "\\1\\"
        self.sw_dictDirs["z_dxf_2"          ] = self.sw_dictDirs[ "z_dxf"] +    "\\2\\"
        self.sw_dictDirs["z_dxf_3"          ] = self.sw_dictDirs[ "z_dxf"] +    "\\3\\"
        self.sw_dictDirs["z_dxf_1__zbedne"  ] = self.sw_dictDirs[ "z_dxf_1"]    + "zbedne\\"
        self.sw_dictDirs["z_dxf_2__zbedne"  ] = self.sw_dictDirs[ "z_dxf_2"]    + "zbedne\\"
        self.sw_dictDirs["z_dxf_3__zbedne"  ] = self.sw_dictDirs[ "z_dxf_3"]    + "zbedne\\"
        self.sw_dictDirs["zz_backup"        ] = self.sw_dir_abspath   + "\\zz_backup\\"
        self.sw_dictDirs["zz_wersjeNieakt"  ] = self.sw_dir_abspath   + "\\zz_wersjeNieakt\\"
        self.sw_dictDirs["kG"               ] = self.sw_dir_abspath   + "\\kG\\"

        self.sw_dictDirs["rasC_sytwys"      ] = ("t:\\&&RasC\\sytwys\\"
                                                 + self.sw_numer_str
                                                 + "_" + self.sw_obrebDir)

    def deb_listujStrukture( self):
        '''
            debugowanie
            -   listing całego  katalogu
        '''
        print("---[ sw_dictDirs ]------------------------------------------------")
        for x in self.sw_dictDirs:
            print(x + "=" + self.sw_dictDirs[x])
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    def utworzStrukture(self):
        """
        >>  trzeba dorobić:
            -   sprawdzenie, czy te katalogi istnieją
            -   funkcję, która skasuje błędnie założoną strukturę

        """
        # utworzenie struktury katalogów
        # - w kat. sw
        # - w &rasC (dla zakresu)
        # -------------------------------------------------------
        for k,v in self.sw_dictDirs.items():
            os.makedirs(v)

        if not os.path.exists(self.sw_dictDirs["rasC_sytwys"]):
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

        # przygotowanie pustej bazy danych
        # - kopiowanie plików
        # - dodanie bazy do pliku konfiguracyjnego ewmapy
        #   [baza]
        #   Baza_152kp=Baza_152kp
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        spos.copy_directory_tree(self.empty_strateg_database, self.sw_dictDirs["baza"])

        # Create a ConfigParser object
        config = configparser.ConfigParser()
        config.optionxform = str  # Preserve case sensitivity for keys

        # Read the existing INI file
        config.read(self.ewmapa_baza_ini, encoding="cp1250")

        # Ensure the `[baza]` section exists, and add the line
        if "baza" not in config:
            config["baza"] = {}
        config["baza"][self.ewmapa_baza_id_str] = self.ewmapa_baza_id_str

        # Add the `[BAZA_152kp]` section
        config[self.ewmapa_baza_id_str] = {
            'Dzialki': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\egib.fdb,,,,0,',
            'Kontury klasyfikacyjne1': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\egib.fdb,,{self.ewmapa_baza_id_str} - kontury,,,,',
            'Uzytki gruntowe1': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\egib.fdb,,{self.ewmapa_baza_id_str} - użytki,,,,',
            'Kat1': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\gesut.fdb:GESUT',
            'Kat1Nazwa': 'GESUT',
            'Kat2': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\bdot500.fdb:BDOT500',
            'Kat2Nazwa': 'BDOT500',

            'Kat3': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\egib.fdb:BUDYNKI',
            'Kat3Nazwa': f'Budynki',
            'Kat4': f'fb:127.0.0.1:{self.sw_dictDirs["baza"]}\\egib.fdb:ADRESY',
            'Kat4Nazwa': f'Adresy',
            'Kat5': f'{self.sw_dictDirs["baza"]}\\sp_warstwy\\',
            'Kat5Nazwa': f'sp_warstwy',
            'Kat6': f'{self.sw_dictDirs["baza"]}\\sp_dxf\\',
            'Kat6Nazwa': f'sp_dxf',
            'Menu aktywności1': f'GESUT,I:\\STRATEG\\PROGRAMY\\EWMAPA\\Gesut_2021\\gesut_2021.mnu',
            'Menu aktywności2': f'GESUT - projektowane,I:\\STRATEG\\PROGRAMY\\EWMAPA\\Gesut_2021\\gesut2021_proj.mnu',
            'Menu aktywności3': f'BDOT500,I:\\STRATEG\\PROGRAMY\\EWMAPA\\Bdot500_2021\\bdot500_2021.mnu',
            'Menu aktywności4': f'EGIB,I:\\STRATEG\\PROGRAMY\\EWMAPA\\Egib\\egib.mnu',
            'Szrafury1': f'{self.sw_dictDirs["baza"]}\\Szrafury,{self.ewmapa_baza_id_str}',
            'Operaty': f'{self.sw_dictDirs["baza"]}\\Operaty',
            'Kartoteka z danymi dla interfejsow': f'{self.sw_dictDirs["baza"]}\\',
            'Identyfikator bazy dla interfejsow': f'{self.ewmapa_baza_id_str}',
            'Rastry': f'{self.sw_dictDirs["baza"]}\\Rastry',
            'Sterowanie': f'{self.ewmapa_baza_id_str}',
            'Parametry przecięcia baz': f'',
            'Baza budynków': f'',
            'Kod budynków': f'',
            'Kat7': f'{self.sw_dictDirs["baza"]}\\sp_wydruk\\',
            'Kat7Nazwa': f'sp_wydruk',
            'Kat9': f'{self.sw_dictDirs["baza"]}\\sp_wydruk_dxf',
            'Kat9Nazwa': f'sp_wydruk_dxf',

















        }

        # Write the updated configuration back to the file
        with open(self.ewmapa_baza_ini, "w", encoding="cp1250") as configfile:
            config.write(configfile)
            print(f"Updated INI file saved at: {self.empty_strateg_database}")


        # utworzenie pliku #_pikiety_XXX.dgn
        # currently unnecessary
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # sourceFile = "t:\\sytwys_T\\zzz_wzor_mdcp\\mdcp2k\\#_mdcp2k.dgn"
        # targetDir = self.sw_dir_abspath
        # plikPikiety_nazwa = "#_pikiety_" + self.sw_numer_str + ".dgn"
        # shutil.copy(sourceFile, os.path.join(targetDir, plikPikiety_nazwa))


class PlikSWinfo:
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
        self.dec_znak = '?-?-?'
        self.dec_data = '?-?-?'

    def set_empty(self):
        self.obiekt = ''
        self.obiekt_do_uwag = ''
        self.nr_zal = ''
        self.dec_znak = ''
        self.dec_data = ''


class MDCP:
    def __init__(self):
        self.ust5 = 1
        self.ust6 = 1
        self.ust5_str = "1"
        self.ust6_str = "1"
        self.kp_uwagi1 = "Mapa utworzona na podstawie arkusza ..."
        self.kp_uwagi2 = "Dane dotyczące granic działki ..., ujawn..."
        self.kp_uwagi3 = "Dla obszaru w granicach projektowanej inwestycji budowlanej brak obciążeń z tytułu służebności \ngruntowych (§ 30 ust. 2 pkt 4 rozporządzenia Ministra Rozwoju z dnia 18 sierpnia 2020 r.,\nDzU 2020 poz. 1429)."
        self.kp_uwagi4 = 'Dla terenu objętego pomiarem brak opracowań planistycznych (§ 30 ust. 2 pkt 3 rozporządzenia\nMinistra Rozwoju z dnia 18 sierpnia 2020 r., DzU 2020 poz. 1429).'
        self.kp_uwagi5 = "Granice nieruchomości oznaczono kolorem zielonym."
        # self.kp_uwagi6  = "Nie wyklucza się istnienia w terenie innych, niewykazanych na niniejszej mapie, urządzeń \npodziemnych."
        self.kp_uwagi6 = "Nie wyklucza się istnienia w terenie innych, niewykazanych na niniejszej mapie, urządzeń \npodziemnych, które nie były zgłoszone do inwentaryzacji lub o których brak jest informacji\nw instytucjach branżowych."

        self.uwagi1_fraza1 = "Mapa utworzona na podstawie arkusza "
        self.uwagi1_fraza2 = " mapy zasadniczej oraz pomiaru aktualizacyjnego id. zgł. "

        self.uwagi2_fraza1 = "Dane dotyczące działki "
        self.uwagi2_fraza2 = ", ujawnione w PZGiK, "
        self.uwagi2_fraza3 = "przepisów §79, ust. 5 i 6 rozp. MSWiA z dnia 9 listopada 2011 r."

        # wersja nowa (od 2020)
        # DzU 2020 poz. 1429
        # Rozporządzenie Ministra Rozwoju z dnia 18 sierpnia 2020 r. w sprawie standardów technicznych
        # wykonywania geodezyjnych pomiarów sytuacyjnych i wysokościowych oraz opracowywania
        # i przekazywania wyników tych pomiarów do państwowego zasobu geodezyjnego i kartograficznego

        '''
        Mapa utworzona na podstawie arkusza 6.144.30.07.4.1, 6.144.30.07.4.2 mapy zasadniczej oraz 
        pomiaru aktualizacyjnego id. zgł. GKN.6640.446.2019

        Dane dotyczące granic działki 309, 310, ujawnione w PZGiK, spełniają wymogi dokładnościowe
        dla znaków i punktów granicznych określone w § 16 pkt 1 rozporządzenia Ministra Rozwoju  
        z dnia 18 sierpnia 2020 r., DzU 2020 poz. 1429.

        Dla obszaru w granicach projektowanej inwestycji budowlanej brak obciążeń z tytułu służebności 
        gruntowych (§ 30 ust. 2 pkt 4 rozporządzenia Ministra Rozwoju z dnia 18 sierpnia 2020 r., 
        DzU 2020 poz. 1429).

        Dla terenu objętego pomiarem brak opracowań planistycznych (§ 30 ust. 2 pkt 3 rozporządzenia 
        Ministra Rozwoju z dnia 18 sierpnia 2020 r., DzU 2020 poz. 1429).

        Granice nieruchomości oznaczono kolorem zielonym. 

        Nie wyklucza się istnienia w terenie innych niewykazanych na niniejszej mapie urządzeń 
        podziemnych. 
        '''

        # wersja stara
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
