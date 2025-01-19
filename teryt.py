class   Teryt( object):
    '''
    Obsługa TERYT

    konwencje nazewnicze
    --------------------
        -   nazwy   jedn.   administracyjnych
            : woj, pow, jew, obr
        -   cechy:
            : nw        ==  nazwa
            : tr        ==  teryt

    properties
    ----------
    -   poziom
        :   określa,    czego   dotyczy dana instancja (woj, pow, jew,  obr
        :   0 - nieokreslone
            1 - woj
            ...
            4 - obreb

    methods:
    --------
    '''
    def __init__( self):
        #pass
        # pola prywatne (nazwa ma "__" na pocz.):
        #__private_field = 'top secret'

        # poziom    teryt   ==  rodzaj jednostki
        self.poziom = 0

        # kody teryt
        self.terytFull  = "99"
        self.terytF_woj = "99"
        self.terytF_pow = "9999"
        self.terytF_jew = "999999_9"
        self.terytF_obr = "999999_9.9999"
        self.teryt_woj  = "99"
        self.teryt_pow  = "9999"
        self.teryt_jew  = "99_9"
        self.teryt_obr  = "9999"

        # nazwa bez czlonu określajacego    rodzaj jednostki (poziom)
        # np.: nazwa_pow = "kłobucki"
        self.nazwa_woj  = "wNN"
        self.nazwa_pow  = "pNN"
        self.nazwa_jew  = "jNN"
        self.nazwa_obr  = "oNN"

        # napisy    do  uStn
        self.nazwa_uStn_woj = "wNN"
        self.nazwa_uStn_pow = "pNN"
        self.nazwa_uStn_jew = "999999_9,.jNN"
        self.nazwa_uStn_obr = "9999 oNN"

        # nazwa obr do  utworzenia katalogu
        self.nazwaDir_obr   = "NN"

        # słowniki powiatów
        self.dictPow =  {
            "2404" :    "częstochowski",
            "2406" :    "kłobucki",
            "2409" :    "myszkowski",
            "2464" :    "Częstochowa"
        }

        # słownik jEw
        self.dictJEw =  {
            # powiat    kłobucki
            "240601_4" : "Kłobuck - miasto",
            "240601_5" : "Kłobuck - obszar wiejski",
            "240602_4" : "Krzepice - miasto",
            "240602_5" : "Krzepice - obszar wiejski",
            "240603_2" : "Lipie",
            "240604_2" : "Miedźno",
            "240605_2" : "Opatów",
            "240606_2" : "Panki",
            "240607_2" : "Popów",
            "240608_2" : "Przystajń",
            "240609_2" : "Wręczyca Wielka",

            # powiat    częstochowski
            "240401_4" : "Blachownia - miasto",
            "240401_5" : "Blachownia - obszar wiejski",
            "240402_2" : "Dąbrowa Zielona",
            "240403_2" : "Janów",
            "240404_2" : "Kamienica Polska",
            "240405_2" : "Kłomnice",
            "240407_2" : "Konopiska",
            "240411_2" : "Mykanów",
            "240412_2" : "Olsztyn",
            "240415_2" : "Rędziny",
            
            # M. Częstochowa
            "246401_1" : "Częstochowa",
                
                
            "999999_9" : "koniec wyścigu"
        }


        # słownik do zamiany    terytu na nazwę obrębu
        self.dictObr_teryt2nazwa =  {
            "240601_4.0001" :   "Brody Malina",
            "240601_4.0002" :   "Kłobuck",
            "240601_4.0003" :   "Niwa Skrzeszów",
            "240601_4.0004" :   "Osoki - Pustkowie",
            "240601_4.0005" :   "Przybyłów",
            "240601_4.0006" :   "Smugi",
            "240601_4.0007" :   "Zagórze",
            "240601_4.0008" :   "Zakrzew",

            "240601_5.0001" :   "Biała Dolna",
            "240601_5.0002" :   "Biała Górna",
            "240601_5.0003" :   "Borowianka",
            "240601_5.0004" :   "Gruszewnia",
            "240601_5.0005" :   "Kamyk",
            "240601_5.0006" :   "Kopiec",
            "240601_5.0007" :   "Lgota",
            "240601_5.0008" :   "Libidza",
            "240601_5.0009" :   "Łobodno",
            "240601_5.0010" :   "Nowa Wieś",
            "240601_5.0011" :   "Rybno",

            "240602_4.0001" :   "Krzepice",
            "240602_4.0002" :   "Kuków",
            "240602_4.0003" :   "Kuźniczka",

            "240602_5.0001" :   "Dankowice",
            "240602_5.0002" :   "Lutrowskie",
            "240602_5.0003" :   "Podłęże Królewskie",
            "240602_5.0004" :   "Starokrzepice",
            "240602_5.0005" :   "Szarki",
            "240602_5.0006" :   "Zajączki Pierwsze",
            "240602_5.0007" :   "Zajączki Drugie",

            "240603_2.0001" :   "Albertów",
            "240603_2.0002" :   "Brzózki",
            "240603_2.0003" :   "Danków",
            "240603_2.0004" :   "Grabarze",
            "240603_2.0005" :   "Julianów",
            "240603_2.0006" :   "Kleśniska",
            "240603_2.0007" :   "Lindów",
            "240603_2.0008" :   "Lipie",
            "240603_2.0009" :   "Łyźniaki",
            "240603_2.0010" :   "Napoleon",
            "240603_2.0011" :   "Natolin",
            "240603_2.0012" :   "Parzymiechy",
            "240603_2.0013" :   "Rębielice Szlacheckie",
            "240603_2.0014" :   "Rozalin",
            "240603_2.0015" :   "Stanisławów",
            "240603_2.0016" :   "Szyszków",
            "240603_2.0017" :   "Wapiennik",
            "240603_2.0018" :   "Zbrojewsko",
            "240603_2.0019" :   "Zimnowoda",

            "240604_2.0001" :   "Borowa",
            "240604_2.0002" :   "Izbiska",
            "240604_2.0003" :   "Kołaczkowice",
            "240604_2.0004" :   "Mazówki",
            "240604_2.0005" :   "Miedźno",
            "240604_2.0006" :   "Mokra",
            "240604_2.0007" :   "Ostrowy",
            "240604_2.0008" :   "Suchany",
            "240604_2.0009" :   "Wapiennik",
            "240604_2.0010" :   "Władysławów",

            "240605_2.0001" :   "Iwanowice Duże",
            "240605_2.0002" :   "Iwanowice Małe",
            "240605_2.0003" :   "Naboków",
            "240605_2.0004" :   "Opatów",
            "240605_2.0005" :   "Waleńczów",
            "240605_2.0006" :   "Wilkowiecko",
            "240605_2.0007" :   "Złochowice",
            "240605_2.0008" :   "Zwierzyniec I",
            "240605_2.0009" :   "Zwierzyniec II",

            "240606_2.0001" :   "Aleksandrów",
            "240606_2.0002" :   "Cyganka",
            "240606_2.0003" :   "Jaciska",
            "240606_2.0004" :   "Janiki",
            "240606_2.0005" :   "Kałmuki",
            "240606_2.0006" :   "Kawki",
            "240606_2.0007" :   "Konieczki",
            "240606_2.0008" :   "Koski",
            "240606_2.0009" :   "Kostrzyna II",
            "240606_2.0010" :   "Kotary",
            "240606_2.0011" :   "Panki",
            "240606_2.0012" :   "Praszczyki",
            "240606_2.0013" :   "Zwierzyniec III",
            "240606_2.0014" :   "Żerdzina",

            "240607_2.0001" :   "Annolesie",
            "240607_2.0002" :   "Brzózki",
            "240607_2.0003" :   "Dąbrowa",
            "240607_2.0004" :   "Dąbrówka",
            "240607_2.0005" :   "Dębie",
            "240607_2.0006" :   "Florianów",
            "240607_2.0007" :   "Kamieńszczyzna",
            "240607_2.0008" :   "Lelity",
            "240607_2.0009" :   "Marianów",
            "240607_2.0010" :   "Nowa Wieś",
            "240607_2.0011" :   "Płaczki",
            "240607_2.0012" :   "Popów",
            "240607_2.0013" :   "Rębielice Królewskie",
            "240607_2.0014" :   "Wąsosz Dolny",
            "240607_2.0015" :   "Wąsosz Górny",
            "240607_2.0016" :   "Więcki",
            "240607_2.0017" :   "Zawady",
            "240607_2.0018" :   "Zbory",

            "240608_2.0001" :   "Antonów",
            "240608_2.0002" :   "Bagna",
            "240608_2.0003" :   "Bór Zajaciński",
            "240608_2.0004" :   "Brzeziny",
            "240608_2.0005" :   "Dąbrowa",
            "240608_2.0006" :   "Górki",
            "240608_2.0007" :   "Kamińsko",
            "240608_2.0008" :   "Kostrzyna I",
            "240608_2.0009" :   "Kuźnica Nowa",
            "240608_2.0010" :   "Kuźnica Stara",
            "240608_2.0011" :   "Ługi Radły",
            "240608_2.0012" :   "Michalinów",
            "240608_2.0013" :   "Mrówczak",
            "240608_2.0014" :   "Podłęże Szlacheckie",
            "240608_2.0015" :   "Przystajń",
            "240608_2.0016" :   "Siekierowizna",
            "240608_2.0017" :   "Stany",
            "240608_2.0018" :   "Wilcza Góra",
            "240608_2.0019" :   "Wrzosy",

            "240609_2.0001" :   "Bieżeń",
            "240609_2.0002" :   "Borowe",
            "240609_2.0003" :   "Bór Zapilski",
            "240609_2.0004" :   "Brzezinki",
            "240609_2.0005" :   "Czarna Wieś",
            "240609_2.0006" :   "Długi Kąt",
            "240609_2.0007" :   "Golce",
            "240609_2.0008" :   "Grodzisko",
            "240609_2.0009" :   "Hutka",
            "240609_2.0010" :   "Jezioro",
            "240609_2.0011" :   "Kalej",
            "240609_2.0012" :   "Klepaczka",
            "240609_2.0013" :   "Kuleje",
            "240609_2.0014" :   "Nowiny",
            "240609_2.0015" :   "Pierzchno",
            "240609_2.0016" :   "Piła I",
            "240609_2.0017" :   "Piła II",
            "240609_2.0018" :   "Puszczew",
            "240609_2.0019" :   "Szarlejka",
            "240609_2.0020" :   "Truskolasy",
            "240609_2.0021" :   "Węglowice",
            "240609_2.0022" :   "Wręczyca Mała",
            "240609_2.0023" :   "Wręczyca Wielka",
            "240609_2.0024" :   "Wydra",
            "240609_2.0025" :   "Zamłynie",

            # powiat cz.
            "240401_4.0001" :   "Blachownia",
            "240401_4.0002" :   "Błaszczyki",
            
            "240401_5.0002" :   "Gorzelnia",

            "240411_2.0016":    "Kuźnica Lechowa",

            "240412_2.0001" :   "Biskupice",
            "240412_2.0006" :   "Przymiłowice",

            # M. Częstochowa
            "246401_1"      : "Częstochowa",
            
            "246401_1.0395" :   "395",
                
            "246401_1.0420" :   "420-Brzeziny Małe",
                
            
            "999999_9.9999" :   "koniec wyścigu"
        }

        # słownik do zamiany nazwy wpisanej do entry-sw_obreb na terytFull
        # - zasada dla nazw obrębów powtarzających się w różnych j. ew.:
        #   do nazwy dodać suffix: myślnik + dwuliterowy skrót j. ew.
        #   np. Nowa Wieś-Kl, Dąbrowa-Po
        # ---------------------------------------------------------------------
        self.dictObr_nazwaObrWpisana2teryt = {
         "Brody Malina"                   : "240601_4.0001",
         "BrodyMalina"                    : "240601_4.0001",
         "Kłobuck"                        : "240601_4.0002",
         "Klobuck"                        : "240601_4.0002",
         "Niwa Skrzeszów"                 : "240601_4.0003",
         "NiwaSkrzeszów"                  : "240601_4.0003",
         "Osoki - Pustkowie"              : "240601_4.0004",
         "Osoki-Pustkowie"                : "240601_4.0004",
         "Osoki Pustkowie"                : "240601_4.0004",
         "OsokiPustkowie"                 : "240601_4.0004",
         "Przybyłów"                      : "240601_4.0005",
         "Przybylow"                      : "240601_4.0005",
         "Smugi"                          : "240601_4.0006",
         "Zagórze"                        : "240601_4.0007",
         "Zagorze"                        : "240601_4.0007",
         "Zakrzew"                        : "240601_4.0008",

         "Biała Dolna"                    : "240601_5.0001",
         "BiałaD"                         : "240601_5.0001",
         "Biała Górna"                    : "240601_5.0002",
         "BiałaG"                         : "240601_5.0002",
         "Borowianka"                     : "240601_5.0003",
         "Gruszewnia"                     : "240601_5.0004",
         "Kamyk"                          : "240601_5.0005",
         "Kopiec"                         : "240601_5.0006",
         "Lgota"                          : "240601_5.0007",
         "Libidza"                        : "240601_5.0008",
         "Łobodno"                        : "240601_5.0009",
         "Nowa Wieś-Kl"                   : "240601_5.0010",
         "Nowa Wieś K"                    : "240601_5.0010",
         "Nowa Wieś-K"                    : "240601_5.0010",
         "Nowa WieśK"                     : "240601_5.0010",
         "Rybno"                          : "240601_5.0011",

         "Krzepice"                       : "240602_4.0001",
         "Kuków"                          : "240602_4.0002",
         "Kuźniczka"                      : "240602_4.0003",

         "Dankowice"                      : "240602_5.0001",
         "Lutrowskie"                     : "240602_5.0002",
         "Podłęże Królewskie"             : "240602_5.0003",
         "PodłężeK"                       : "240602_5.0003",
         "Starokrzepice"                  : "240602_5.0004",
         "Szarki"                         : "240602_5.0005",
         "Zajączki I"                     : "240602_5.0006",
         "Zajączki II"                    : "240602_5.0007",
         "Zajączki Pierwsze"              : "240602_5.0006",
         "Zajączki Drugie"                : "240602_5.0007",

         "Albertów"                       : "240603_2.0001",
         "Brzózki-Li"                     : "240603_2.0002",
         "Brzózki L"                      : "240603_2.0002",
         "Brzózki-L"                      : "240603_2.0002",
         "Danków"                         : "240603_2.0003",
         "Grabarze"                       : "240603_2.0004",
         "Julianów"                       : "240603_2.0005",
         "Kleśniska"                      : "240603_2.0006",
         "Lindów"                         : "240603_2.0007",
         "Lipie"                          : "240603_2.0008",
         "Łyźniaki"                       : "240603_2.0009",
         "Napoleon"                       : "240603_2.0010",
         "Natolin"                        : "240603_2.0011",
         "Parzymiechy"                    : "240603_2.0012",
         "Rębielice Szlacheckie"          : "240603_2.0013",
         "Rozalin"                        : "240603_2.0014",
         "Stanisławów"                    : "240603_2.0015",
         "Szyszków"                       : "240603_2.0016",
         "Wapiennik-Li"                   : "240603_2.0017",
         "Wapiennik-L"                    : "240603_2.0017",
         "Wapiennik L"                    : "240603_2.0017",
         "Zbrojewsko"                     : "240603_2.0018",
         "Zimnowoda"                      : "240603_2.0019",

         "Borowa"                         : "240604_2.0001",
         "Izbiska"                        : "240604_2.0002",
         "Kołaczkowice"                   : "240604_2.0003",
         "Mazówki"                        : "240604_2.0004",
         "Miedźno"                        : "240604_2.0005",
         "Mokra"                          : "240604_2.0006",
         "Ostrowy"                        : "240604_2.0007",
         "Suchany"                        : "240604_2.0008",
         "Wapiennik-Mi"                   : "240604_2.0009",
         "Wapiennik M"                    : "240604_2.0009",
         "Władysławów"                    : "240604_2.0010",

         "Iwanowice Duże"                 : "240605_2.0001",
         "Iwanowice Małe"                 : "240605_2.0002",
         "Naboków"                        : "240605_2.0003",
         "Opatów"                         : "240605_2.0004",
         "Waleńczów"                      : "240605_2.0005",
         "Wilkowiecko"                    : "240605_2.0006",
         "Złochowice"                     : "240605_2.0007",
         "Zwierzyniec I"                  : "240605_2.0008",
         "Zwierzyniec II"                 : "240605_2.0009",

         "Aleksandrów"                    : "240606_2.0001",
         "Cyganka"                        : "240606_2.0002",
         "Jaciska"                        : "240606_2.0003",
         "Janiki"                         : "240606_2.0004",
         "Kałmuki"                        : "240606_2.0005",
         "Kawki"                          : "240606_2.0006",
         "Konieczki"                      : "240606_2.0007",
         "Koski"                          : "240606_2.0008",
         "Kostrzyna II"                   : "240606_2.0009",
         "Kotary"                         : "240606_2.0010",
         "Panki"                          : "240606_2.0011",
         "Praszczyki"                     : "240606_2.0012",
         "Zwierzyniec III"                : "240606_2.0013",
         "Żerdzina"                       : "240606_2.0014",

         "Annolesie"                      : "240607_2.0001",
         "Brzózki-Po"                     : "240607_2.0002",
         "Dąbrowa-Po"                     : "240607_2.0003",
         "Dąbrówka"                       : "240607_2.0004",
         "Dębie"                          : "240607_2.0005",
         "Florianów"                      : "240607_2.0006",
         "Kamieńszczyzna"                 : "240607_2.0007",
         "Lelity"                         : "240607_2.0008",
         "Marianów"                       : "240607_2.0009",
         "Nowa Wieś-Po"                   : "240607_2.0010",
         "Nowa Wieś P"                    : "240607_2.0010",
         "Nowa WieśP"                     : "240607_2.0010",
         "Płaczki"                        : "240607_2.0011",
         "Popów"                          : "240607_2.0012",
         "Rębielice Królewskie"           : "240607_2.0013",
         "Wąsosz Dolny"                   : "240607_2.0014",
         "Wąsosz Górny"                   : "240607_2.0015",
         "Więcki"                         : "240607_2.0016",
         "Zawady"                         : "240607_2.0017",
         "Zbory"                          : "240607_2.0018",

         "Antonów"                        : "240608_2.0001",
         "Bagna"                          : "240608_2.0002",
         "Bór Zajaciński"                 : "240608_2.0003",
         "Brzeziny"                       : "240608_2.0004",
         "Dąbrowa-Pr"                     : "240608_2.0005",
         "Górki"                          : "240608_2.0006",
         "Kamińsko"                       : "240608_2.0007",
         "KostrzynaI"                     : "240608_2.0008",
         "Kostrzyna I"                    : "240608_2.0008",
         "Kuźnica Nowa"                   : "240608_2.0009",
         "Kuźnica Stara"                  : "240608_2.0010",
         "Ługi Radły"                     : "240608_2.0011",
         "Michalinów"                     : "240608_2.0012",
         "Mrówczak"                       : "240608_2.0013",
         "Podłęże Szlacheckie"            : "240608_2.0014",
         "Przystajń"                      : "240608_2.0015",
         "Siekierowizna"                  : "240608_2.0016",
         "Stany"                          : "240608_2.0017",
         "Wilcza Góra"                    : "240608_2.0018",
         "Wrzosy"                         : "240608_2.0019",

         "Bieżeń"                         : "240609_2.0001",
         "Borowe"                         : "240609_2.0002",
         "Bór Zapilski"                   : "240609_2.0003",
         "Brzezinki"                      : "240609_2.0004",
         "Czarna Wieś"                    : "240609_2.0005",
         "CzarnaW"                        : "240609_2.0005",
         "Długi Kąt"                      : "240609_2.0006",
         "DługiKąt"                       : "240609_2.0006",
         "DługiK"                         : "240609_2.0006",
         "Golce"                          : "240609_2.0007",
         "Grodzisko"                      : "240609_2.0008",
         "Hutka"                          : "240609_2.0009",
         "Jezioro"                        : "240609_2.0010",
         "Kalej"                          : "240609_2.0011",
         "Klepaczka"                      : "240609_2.0012",
         "Kuleje"                         : "240609_2.0013",
         "Nowiny"                         : "240609_2.0014",
         "Pierzchno"                      : "240609_2.0015",
         "Piła I"                         : "240609_2.0016",
         "Piła II"                        : "240609_2.0017",
         "Puszczew"                       : "240609_2.0018",
         "Szarlejka"                      : "240609_2.0019",
         "Truskolasy"                     : "240609_2.0020",
         "Węglowice"                      : "240609_2.0021",
         "Wręczyca Mała"                  : "240609_2.0022",
         "WręczycaM"                      : "240609_2.0022",
         "Wręczyca Wielka"                : "240609_2.0023",
         "WręczycaW"                      : "240609_2.0023",
         "Wydra"                          : "240609_2.0024",
         "Zamłynie"                       : "240609_2.0025",

         # inne powiaty
         "Blachownia"                     : "240401_4.0001",
         "Błaszczyki"                     : "240401_4.0002",

         "Gorzelnia"                      : "240401_5.0002",
         "Kuźnica Lechowa": "240411_2.0016",

         "Biskupice"                      : "240412_2.0001",
         "Przymiłowice"                   : "240412_2.0006",

            # M. Częstochowa
         "Częstochowa"                    : "246401_1",   


         "koniec wyścigu"                 : "999999_9.9999"
         }

        # słownik do zamiany    terytu na nazwę obr.    do  utworzenia
        # katalogu (bez znaków diaktrycznych)
        self.dictObr_teryt2nazwaDir =   {
            "240601_4.0001" :   "BrodyM",
            "240601_4.0002" :   "Klobuck",
            "240601_4.0003" :   "NiwaSk",
            "240601_4.0004" :   "OsokiP",
            "240601_4.0005" :   "Przybylow",
            "240601_4.0006" :   "Smugi",
            "240601_4.0007" :   "Zagorze",
            "240601_4.0008" :   "Zakrzew",

            "240601_5.0001" :   "BialaD",
            "240601_5.0002" :   "BialaG",
            "240601_5.0003" :   "Borowianka",
            "240601_5.0004" :   "Gruszewnia",
            "240601_5.0005" :   "Kamyk",
            "240601_5.0006" :   "Kopiec",
            "240601_5.0007" :   "Lgota",
            "240601_5.0008" :   "Libidza",
            "240601_5.0009" :   "Lobodno",
            "240601_5.0010" :   "NowaWies-Kl",
            "240601_5.0011" :   "Rybno",

            "240602_4.0001" :   "Krzepice",
            "240602_4.0002" :   "Kukow",
            "240602_4.0003" :   "Kuzniczka",

            "240602_5.0001" :   "Dankowice",
            "240602_5.0002" :   "Lutrowskie",
            "240602_5.0003" :   "PodlezeKrol",
            "240602_5.0004" :   "Starokrzepice",
            "240602_5.0005" :   "Szarki",
            "240602_5.0006" :   "Zajaczki1",
            "240602_5.0007" :   "Zajaczki2",

            "240603_2.0001" :   "Albertow",
            "240603_2.0002" :   "Brzozki",
            "240603_2.0003" :   "Dankow",
            "240603_2.0004" :   "Grabarze",
            "240603_2.0005" :   "Julianow",
            "240603_2.0006" :   "Klesniska",
            "240603_2.0007" :   "Lindow",
            "240603_2.0008" :   "Lipie",
            "240603_2.0009" :   "Lyzniaki",
            "240603_2.0010" :   "Napoleon",
            "240603_2.0011" :   "Natolin",
            "240603_2.0012" :   "Parzymiechy",
            "240603_2.0013" :   "RebieliceSz",
            "240603_2.0014" :   "Rozalin",
            "240603_2.0015" :   "Stanislawow",
            "240603_2.0016" :   "Szyszkow",
            "240603_2.0017" :   "Wapiennik-L",
            "240603_2.0018" :   "Zbrojewsko",
            "240603_2.0019" :   "Zimnowoda",

            "240604_2.0001" :   "Borowa",
            "240604_2.0002" :   "Izbiska",
            "240604_2.0003" :   "Kolaczkowice",
            "240604_2.0004" :   "Mazowki",
            "240604_2.0005" :   "Miedzno",
            "240604_2.0006" :   "Mokra",
            "240604_2.0007" :   "Ostrowy",
            "240604_2.0008" :   "Suchany",
            "240604_2.0009" :   "Wapiennik-M",
            "240604_2.0010" :   "Wladyslawow",

            "240605_2.0001" :   "IwanowiceD",
            "240605_2.0002" :   "IwanowiceM",
            "240605_2.0003" :   "Nabokow",
            "240605_2.0004" :   "Opatow",
            "240605_2.0005" :   "Walenczow",
            "240605_2.0006" :   "Wilkowiecko",
            "240605_2.0007" :   "Zlochowice",
            "240605_2.0008" :   "Zwierzyniec1",
            "240605_2.0009" :   "Zwierzyniec2",

            "240606_2.0001" :   "Aleksandrow",
            "240606_2.0002" :   "Cyganka",
            "240606_2.0003" :   "Jaciska",
            "240606_2.0004" :   "Janiki",
            "240606_2.0005" :   "Kalmuki",
            "240606_2.0006" :   "Kawki",
            "240606_2.0007" :   "Konieczki",
            "240606_2.0008" :   "Koski",
            "240606_2.0009" :   "Kostrzyna2",
            "240606_2.0010" :   "Kotary",
            "240606_2.0011" :   "Panki",
            "240606_2.0012" :   "Praszczyki",
            "240606_2.0013" :   "Zwierzyniec3",
            "240606_2.0014" :   "Zerdzina",

            "240607_2.0001" :   "Annolesie",
            "240607_2.0002" :   "Brzozki",
            "240607_2.0003" :   "Dabrowa",
            "240607_2.0004" :   "Dabrowka",
            "240607_2.0005" :   "Debie",
            "240607_2.0006" :   "Florianow",
            "240607_2.0007" :   "Kamienszczyzna",
            "240607_2.0008" :   "Lelity",
            "240607_2.0009" :   "Marianow",
            "240607_2.0010" :   "NowaWies-Pop",
            "240607_2.0011" :   "Placzki",
            "240607_2.0012" :   "Popow",
            "240607_2.0013" :   "RebieliceKrol",
            "240607_2.0014" :   "WasoszD",
            "240607_2.0015" :   "WasoszG",
            "240607_2.0016" :   "Wiecki",
            "240607_2.0017" :   "Zawady",
            "240607_2.0018" :   "Zbory",

            "240608_2.0001" :   "Antonow",
            "240608_2.0002" :   "Bagna",
            "240608_2.0003" :   "BorZajacinski",
            "240608_2.0004" :   "Brzeziny",
            "240608_2.0005" :   "Dabrowa",
            "240608_2.0006" :   "Gorki",
            "240608_2.0007" :   "Kaminsko",
            "240608_2.0008" :   "Kostrzyna1",
            "240608_2.0009" :   "KuznicaN",
            "240608_2.0010" :   "KuznicaS",
            "240608_2.0011" :   "LugiRadly",
            "240608_2.0012" :   "Michalinow",
            "240608_2.0013" :   "Mrowczak",
            "240608_2.0014" :   "PodlezeSz",
            "240608_2.0015" :   "Przystajn",
            "240608_2.0016" :   "Siekierowizna",
            "240608_2.0017" :   "Stany",
            "240608_2.0018" :   "WilczaGora",
            "240608_2.0019" :   "Wrzosy",

            "240609_2.0001" :   "Biezen",
            "240609_2.0002" :   "Borowe",
            "240609_2.0003" :   "BorZapilski",
            "240609_2.0004" :   "Brzezinki",
            "240609_2.0005" :   "CzarnaWies",
            "240609_2.0006" :   "DlugiKat",
            "240609_2.0007" :   "Golce",
            "240609_2.0008" :   "Grodzisko",
            "240609_2.0009" :   "Hutka",
            "240609_2.0010" :   "Jezioro",
            "240609_2.0011" :   "Kalej",
            "240609_2.0012" :   "Klepaczka",
            "240609_2.0013" :   "Kuleje",
            "240609_2.0014" :   "Nowiny",
            "240609_2.0015" :   "Pierzchno",
            "240609_2.0016" :   "Pila1",
            "240609_2.0017" :   "Pila2",
            "240609_2.0018" :   "Puszczew",
            "240609_2.0019" :   "Szarlejka",
            "240609_2.0020" :   "Truskolasy",
            "240609_2.0021" :   "Weglowice",
            "240609_2.0022" :   "WreczycaM",
            "240609_2.0023" :   "WreczycaW",
            "240609_2.0024" :   "Wydra",
            "240609_2.0025" :   "Zamlynie",

            # powiat cz.
            "240401_4.0001" :   "Blachownia",
            "240401_4.0002" :   "Blaszczyki",

            "240401_5.0002" :   "Gorzelnia",

            "240411_2.0016": "KuznicaLechowa",

            "240412_2.0001" :   "Biskupice",
            "240412_2.0006" :   "Przymilowice",

            # M. Częstochowa
            "246401_1":   "CzM",
                    
            "999999_9.9999" :   "koniec wyścigu"
        }


        # słownik do zamiany    nazwy   obrębu na teryt
        # UWAGA!!!
        # Ten słownik jest nieprzydatny, bo powtarzają sie w nim klucze
        '''
        self.dictObr_nazwa2teryt =  {
            "Brody Malina"                      : "240601_4.0001",
            "Kłobuck"                           : "240601_4.0002",
            "Niwa Skrzeszów"                    : "240601_4.0003",
            "Osoki - Pustkowie"                 : "240601_4.0004",
            "Przybyłów"                         : "240601_4.0005",
            "Smugi"                             : "240601_4.0006",
            "Zagórze"                           : "240601_4.0007",
            "Zakrzew"                           : "240601_4.0008",
                                                    
            "Biała Dolna"                       : "240601_5.0001",
            "Biała Górna"                       : "240601_5.0002",
            "Borowianka"                        : "240601_5.0003",
            "Gruszewnia"                        : "240601_5.0004",
            "Kamyk"                             : "240601_5.0005",
            "Kopiec"                            : "240601_5.0006",
            "Lgota"                             : "240601_5.0007",
            "Libidza"                           : "240601_5.0008",
            "Łobodno"                           : "240601_5.0009",
            "Nowa Wieś"                         : "240601_5.0010",
            "Rybno"                             : "240601_5.0011",
                                                    
            "Krzepice"                          : "240602_4.0001",
            "Kuków"                             : "240602_4.0002",
            "Kuźniczka"                         : "240602_4.0003",
                                                    
            "Dankowice"                         : "240602_5.0001",
            "Lutrowskie"                        : "240602_5.0002",
            "Podłęże Królewskie"                : "240602_5.0003",
            "Starokrzepice"                     : "240602_5.0004",
            "Szarki"                            : "240602_5.0005",
            "Zajączki I"                        : "240602_5.0006",
            "Zajączki II"                       : "240602_5.0007",
                                                    
            "Albertów"                          : "240603_2.0001",
            "Brzózki"                           : "240603_2.0002",
            "Danków"                            : "240603_2.0003",
            "Grabarze"                          : "240603_2.0004",
            "Julianów"                          : "240603_2.0005",
            "Kleśniska"                         : "240603_2.0006",
            "Lindów"                            : "240603_2.0007",
            "Lipie"                             : "240603_2.0008",
            "Łyźniaki"                          : "240603_2.0009",
            "Napoleon"                          : "240603_2.0010",
            "Natolin"                           : "240603_2.0011",
            "Parzymiechy"                       : "240603_2.0012",
            "Rębielice Szlacheckie"             : "240603_2.0013",
            "Rozalin"                           : "240603_2.0014",
            "Stanisławów"                       : "240603_2.0015",
            "Szyszków"                          : "240603_2.0016",
            "Wapiennik"                         : "240603_2.0017",
            "Zbrojewsko"                        : "240603_2.0018",
            "Zimnowoda"                         : "240603_2.0019",
                                                    
            "Borowa"                            : "240604_2.0001",
            "Izbiska"                           : "240604_2.0002",
            "Kołaczkowice"                      : "240604_2.0003",
            "Mazówki"                           : "240604_2.0004",
            "Miedźno"                           : "240604_2.0005",
            "Mokra"                             : "240604_2.0006",
            "Ostrowy"                           : "240604_2.0007",
            "Suchany"                           : "240604_2.0008",
            "Wapiennik"                         : "240604_2.0009",
            "Władysławów"                       : "240604_2.0010",
                                                    
            "Iwanowice Duże"                    : "240605_2.0001",
            "Iwanowice Małe"                    : "240605_2.0002",
            "Naboków"                           : "240605_2.0003",
            "Opatów"                            : "240605_2.0004",
            "Waleńczów"                         : "240605_2.0005",
            "Wilkowiecko"                       : "240605_2.0006",
            "Złochowice"                        : "240605_2.0007",
            "Zwierzyniec I"                     : "240605_2.0008",
            "Zwierzyniec II"                    : "240605_2.0009",
                                                    
            "Aleksandrów"                       : "240606_2.0001",
            "Cyganka"                           : "240606_2.0002",
            "Jaciska"                           : "240606_2.0003",
            "Janiki"                            : "240606_2.0004",
            "Kałmuki"                           : "240606_2.0005",
            "Kawki"                             : "240606_2.0006",
            "Konieczki"                         : "240606_2.0007",
            "Koski"                             : "240606_2.0008",
            "Kostrzyna II"                      : "240606_2.0009",
            "Kotary"                            : "240606_2.0010",
            "Panki"                             : "240606_2.0011",
            "Praszczyki"                        : "240606_2.0012",
            "Zwierzyniec III"                   : "240606_2.0013",
            "Żerdzina"                          : "240606_2.0014",
                                                    
            "Annolesie"                         : "240607_2.0001",
            "Brzózki"                           : "240607_2.0002",
            "Dąbrowa"                           : "240607_2.0003",
            "Dąbrówka"                          : "240607_2.0004",
            "Dębie"                             : "240607_2.0005",
            "Florianów"                         : "240607_2.0006",
            "Kamieńszczyzna"                    : "240607_2.0007",
            "Lelity"                            : "240607_2.0008",
            "Marianów"                          : "240607_2.0009",
            "Nowa Wieś"                         : "240607_2.0010",
            "Płaczki"                           : "240607_2.0011",
            "Popów"                             : "240607_2.0012",
            "Rębielice Królewskie"              : "240607_2.0013",
            "Wąsosz Dolny"                      : "240607_2.0014",
            "Wąsosz Górny"                      : "240607_2.0015",
            "Więcki"                            : "240607_2.0016",
            "Zawady"                            : "240607_2.0017",
            "Zbory"                             : "240607_2.0018",
                                                    
            "Antonów"                           : "240608_2.0001",
            "Bagna"                             : "240608_2.0002",
            "Bór Zajaciński"                    : "240608_2.0003",
            "Brzeziny"                          : "240608_2.0004",
            "Dąbrowa"                           : "240608_2.0005",
            "Górki"                             : "240608_2.0006",
            "Kamińsko"                          : "240608_2.0007",
            "Kostrzyna I"                       : "240608_2.0008",
            "Kuźnica Nowa"                      : "240608_2.0009",
            "Kuźnica Stara"                     : "240608_2.0010",
            "Ługi Radły"                        : "240608_2.0011",
            "Michalinów"                        : "240608_2.0012",
            "Mrówczak"                          : "240608_2.0013",
            "Podłęże Szlacheckie"               : "240608_2.0014",
            "Przystajń"                         : "240608_2.0015",
            "Siekierowizna"                     : "240608_2.0016",
            "Stany"                             : "240608_2.0017",
            "Wilcza Góra"                       : "240608_2.0018",
            "Wrzosy"                            : "240608_2.0019",
                                                    
            "Bieżeń"                            : "240609_2.0001",
            "Borowe"                            : "240609_2.0002",
            "Bór Zapilski"                      : "240609_2.0003",
            "Brzezinki"                         : "240609_2.0004",
            "Czarna Wieś"                       : "240609_2.0005",
            "Długi Kąt"                         : "240609_2.0006",
            "Golce"                             : "240609_2.0007",
            "Grodzisko"                         : "240609_2.0008",
            "Hutka"                             : "240609_2.0009",
            "Jezioro"                           : "240609_2.0010",
            "Kalej"                             : "240609_2.0011",
            "Klepaczka"                         : "240609_2.0012",
            "Kuleje"                            : "240609_2.0013",
            "Nowiny"                            : "240609_2.0014",
            "Pierzchno"                         : "240609_2.0015",
            "Piła I"                            : "240609_2.0016",
            "Piła II"                           : "240609_2.0017",
            "Puszczew"                          : "240609_2.0018",
            "Szarlejka"                         : "240609_2.0019",
            "Truskolasy"                        : "240609_2.0020",
            "Węglowice"                         : "240609_2.0021",
            "Wręczyca Mała"                     : "240609_2.0022",
            "Wręczyca Wielka"                   : "240609_2.0023",
            "Wydra"                             : "240609_2.0024",
            "Zamłynie"                          : "240609_2.0025",
                                                    
            "Blachownia"                        : "240401_4.0001",
            "Błaszczyki"                        : "240401_4.0002",
                                                    
                                                    
            "koniec wyścigu"                    : "999999_9.9999"
        }
        '''
        
    # koniec    __init__()
    # = =   = = =   = = =   = = =   = = =   = = =   = = =   = = =   = = =   = = =   = = =   = = =   = = =

    '''
    @staticmethod
    def setTerytFrom_obrNazwa_static(   astr):
        return setTerytFrom_obrNazwa(   astr)
    '''

    def setTerytyFrom_obrTerytFull( self, aobrTerytFull):
        # sprawdzenie, czy aobrTerytFull jest w słowniku terytów
        if aobrTerytFull in self.dictObr_teryt2nazwa.keys():
            self.terytFull = aobrTerytFull 
            print( "aobrTerytFull=" +   aobrTerytFull)
            print( "dictObr_teryt2nazwaDir[ obr_terytFull]=" +  self.dictObr_teryt2nazwaDir[ self.terytFull])

            self.terytF_woj =   self.terytFull[0:2]
            self.terytF_pow =   self.terytFull[0:4]
            self.terytF_jew =   self.terytFull[0:8]
            self.terytF_obr =   self.terytFull
            self.teryt_woj   =  self.terytFull[0:2]
            self.teryt_pow   =  self.terytFull[2:4]
            self.teryt_jew   =  self.terytFull[4:8]
            self.teryt_obr   =  self.terytFull[9:15]

            self.nazwa_woj  = "śląskie"
            self.nazwa_pow  = self.dictPow[ self.terytF_pow]
            self.nazwa_jew  = self.dictJEw[ self.terytF_jew]
            self.nazwa_obr  = self.dictObr_teryt2nazwa[ self.terytFull]

            self.nazwa_uStn_woj = "Województwo: " + self.nazwa_woj
            self.nazwa_uStn_pow = "Powiat: " + self.nazwa_pow
            self.nazwa_uStn_jew = "Jednostka ewidencyjna: "  + self.terytF_jew[0:6] + "__" + self.terytF_jew[7:9] + ", "   + self.nazwa_jew
            self.nazwa_uStn_obr = "Obręb: " + self.teryt_obr + " " + self.nazwa_obr

            # nazwa obr. do nazwy katalogu
            self.nazwaDir_obr   = self.dictObr_teryt2nazwaDir[ self.terytFull]

            return 0
        else:
            print( "aobrTerytFull >%s< nie został odnaleziony w słowniku" % ( aobrTerytFull))
            return -1
    
    
    # chyba - w tej postaci - zbędna funkcja
    def setTerytFrom_obrNazwa(self, astr):
        '''
            podajemy    nazwę   obrębu, a funkcja   na  tej podstawie ustawia
            wszystkie pola  instancji klasy
        '''
        if  len( astr) > 2:
            #self.terytFull = self.dictObr_nazwaObrWpisana2teryt[ astr]
            print( "self.terytFull=" +  self.terytFull)
            print( "dictObr_teryt2nazwaDir[ obr_terytFull]=" +  self.dictObr_teryt2nazwaDir[ self.terytFull])

            self.terytF_woj =   self.terytFull[0:2]
            self.terytF_pow =   self.terytFull[0:4]
            self.terytF_jew =   self.terytFull[0:8]
            self.terytF_obr =   self.terytFull
            self.teryt_woj   =  self.terytFull[0:2]
            self.teryt_pow   =  self.terytFull[2:4]
            self.teryt_jew   =  self.terytFull[4:8]
            self.teryt_obr   =  self.terytFull[9:15]

            self.nazwa_woj  = "śląskie"
            self.nazwa_pow  = self.dictPow[ self.terytF_pow]
            self.nazwa_jew  = self.dictJEw[ self.terytF_jew]
            self.nazwa_obr  = self.dictObr_teryt2nazwa[ self.terytFull]

            self.nazwa_uStn_woj = "Województwo: " + self.nazwa_woj
            self.nazwa_uStn_pow = "Powiat: "    + self.nazwa_pow
            self.nazwa_uStn_jew = "Jednostka ewidencyjna: "  + self.terytF_jew[0:6] + "__"   + self.terytF_jew[7:9] + ", "   + self.nazwa_jew
            self.nazwa_uStn_obr = "obręb:   " + self.teryt_obr +    " " +   self.nazwa_obr

            # nazwa obr. do nazwy katalogu
            self.nazwaDir_obr   = self.dictObr_teryt2nazwaDir[ self.terytFull]

            return 0
        else:
            print( "Zbyt krótka nazwa obrębu!")
            return -1

    