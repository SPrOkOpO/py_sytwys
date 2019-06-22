#-*- coding: windows-1250 -*-

class	Teryt( object):
	'''
	Obs�uga TERYT

	konwencje nazewnicze
	--------------------
		-	nazwy	jedn.	administracyjnych
			: woj, pow,	jew, obr
		-	cechy:
			: nw		==	nazwa
			: tr		==	teryt

	properties
	----------
	-	poziom
		:	okre�la,	czego	dotyczy dana instancja (woj, pow, jew,	obr
		:	0 - nieokreslone
			1 - woj
			...
			4 - obreb

	methods:
	--------
	'''
	def __init__( self):
		#pass
		# pola prywatne (nazwa ma "__" na pocz.):
		#__private_field = 'top	secret'

		# poziom	teryt	==	rodzaj jednostki
		self.poziom	= 0

		# kody teryt
		self.terytFull	= "99"
		self.terytF_woj =	"99"
		self.terytF_pow =	"9999"
		self.terytF_jew =	"999999_9"
		self.terytF_obr =	"999999_9.9999"
		self.teryt_woj	= "99"
		self.teryt_pow	= "9999"
		self.teryt_jew	= "99_9"
		self.teryt_obr	= "9999"

		# nazwa bez	czlonu okre�lajacego	rodzaj jednostki (poziom)
		# np.: nazwa_pow = "k�obucki"
		self.nazwa_woj	= "wNN"
		self.nazwa_pow	= "pNN"
		self.nazwa_jew	= "jNN"
		self.nazwa_obr	= "oNN"

		# napisy	do	uStn
		self.nazwa_uStn_woj = "wNN"
		self.nazwa_uStn_pow = "pNN"
		self.nazwa_uStn_jew = "999999_9,.jNN"
		self.nazwa_uStn_obr = "9999 oNN"

		# nazwa obr	do	utworzenia katalogu
		self.nazwaDir_obr	= "NN"

		# s�owniki powiat�w
		self.dictPow =	{
			"2404" :	"cz�stochowski",
			"2406" :	"k�obucki",
			"2409" :	"myszkowski",
			"2464" :	"Cz�stochowa"
		}

		# s�ownik jEw
		self.dictJEw =	{
			# powiat	k�obucki
			"240601_4" : "K�obuck -	miasto",
			"240601_5" : "K�obuck -	obszar wiejski",
			"240602_4" : "Krzepice - miasto",
			"240602_5" : "Krzepice - obszar wiejski",
			"240603_2" : "Lipie",
			"240604_2" : "Mied�no",
			"240605_2" : "Opat�w",
			"240606_2" : "Panki",
			"240607_2" : "Pop�w",
			"240608_2" : "Przystaj�",
			"240609_2" : "Wr�czyca Wielka",

			# powiat	cz�stochowski
			"240401_4" : "Blachownia -	miasto",
			"240401_5" : "Blachownia -	obszar wiejski",
			"240403_2" : "Jan�w",
			"240405_2" : "K�omnice",
			"240407_2" : "Konopiska",
			"240411_2" : "Mykan�w",
			"240412_2" : "Olsztyn",
			"240415_2" : "R�dziny",

			"999999_9" : "koniec	wy�cigu"
		}


		# s�ownik do zamiany	terytu na nazw� obr�bu
		self.dictObr_teryt2nazwa =	{
			"240601_4.0001" :	"Brody Malina",
			"240601_4.0002" :	"K�obuck",
			"240601_4.0003" :	"Niwa	Skrzesz�w",
			"240601_4.0004" :	"Osoki -	Pustkowie",
			"240601_4.0005" :	"Przyby��w",
			"240601_4.0006" :	"Smugi",
			"240601_4.0007" :	"Zag�rze",
			"240601_4.0008" :	"Zakrzew",

			"240601_5.0001" :	"Bia�a Dolna",
			"240601_5.0002" :	"Bia�a G�rna",
			"240601_5.0003" :	"Borowianka",
			"240601_5.0004" :	"Gruszewnia",
			"240601_5.0005" :	"Kamyk",
			"240601_5.0006" :	"Kopiec",
			"240601_5.0007" :	"Lgota",
			"240601_5.0008" :	"Libidza",
			"240601_5.0009" :	"�obodno",
			"240601_5.0010" :	"Nowa	Wie�",
			"240601_5.0011" :	"Rybno",

			"240602_4.0001" :	"Krzepice",
			"240602_4.0002" :	"Kuk�w",
			"240602_4.0003" :	"Ku�niczka",

			"240602_5.0001" :	"Dankowice",
			"240602_5.0002" :	"Lutrowskie",
			"240602_5.0003" :	"Pod��e	Kr�lewskie",
			"240602_5.0004" :	"Starokrzepice",
			"240602_5.0005" :	"Szarki",
			"240602_5.0006" :	"Zaj�czki I",
			"240602_5.0007" :	"Zaj�czki II",

			"240603_2.0001" :	"Albert�w",
			"240603_2.0002" :	"Brz�zki",
			"240603_2.0003" :	"Dank�w",
			"240603_2.0004" :	"Grabarze",
			"240603_2.0005" :	"Julian�w",
			"240603_2.0006" :	"Kle�niska",
			"240603_2.0007" :	"Lind�w",
			"240603_2.0008" :	"Lipie",
			"240603_2.0009" :	"�y�niaki",
			"240603_2.0010" :	"Napoleon",
			"240603_2.0011" :	"Natolin",
			"240603_2.0012" :	"Parzymiechy",
			"240603_2.0013" :	"R�bielice Szlacheckie",
			"240603_2.0014" :	"Rozalin",
			"240603_2.0015" :	"Stanis�aw�w",
			"240603_2.0016" :	"Szyszk�w",
			"240603_2.0017" :	"Wapiennik",
			"240603_2.0018" :	"Zbrojewsko",
			"240603_2.0019" :	"Zimnowoda",

			"240604_2.0001" :	"Borowa",
			"240604_2.0002" :	"Izbiska",
			"240604_2.0003" :	"Ko�aczkowice",
			"240604_2.0004" :	"Maz�wki",
			"240604_2.0005" :	"Mied�no",
			"240604_2.0006" :	"Mokra",
			"240604_2.0007" :	"Ostrowy",
			"240604_2.0008" :	"Suchany",
			"240604_2.0009" :	"Wapiennik",
			"240604_2.0010" :	"W�adys�aw�w",

			"240605_2.0001" :	"Iwanowice Du�e",
			"240605_2.0002" :	"Iwanowice Ma�e",
			"240605_2.0003" :	"Nabok�w",
			"240605_2.0004" :	"Opat�w",
			"240605_2.0005" :	"Wale�cz�w",
			"240605_2.0006" :	"Wilkowiecko",
			"240605_2.0007" :	"Z�ochowice",
			"240605_2.0008" :	"Zwierzyniec I",
			"240605_2.0009" :	"Zwierzyniec II",

			"240606_2.0001" :	"Aleksandr�w",
			"240606_2.0002" :	"Cyganka",
			"240606_2.0003" :	"Jaciska",
			"240606_2.0004" :	"Janiki",
			"240606_2.0005" :	"Ka�muki",
			"240606_2.0006" :	"Kawki",
			"240606_2.0007" :	"Konieczki",
			"240606_2.0008" :	"Koski",
			"240606_2.0009" :	"Kostrzyna II",
			"240606_2.0010" :	"Kotary",
			"240606_2.0011" :	"Panki",
			"240606_2.0012" :	"Praszczyki",
			"240606_2.0013" :	"Zwierzyniec III",
			"240606_2.0014" :	"�erdzina",

			"240607_2.0001" :	"Annolesie",
			"240607_2.0002" :	"Brz�zki",
			"240607_2.0003" :	"D�browa",
			"240607_2.0004" :	"D�br�wka",
			"240607_2.0005" :	"D�bie",
			"240607_2.0006" :	"Florian�w",
			"240607_2.0007" :	"Kamie�szczyzna",
			"240607_2.0008" :	"Lelity",
			"240607_2.0009" :	"Marian�w",
			"240607_2.0010" :	"Nowa	Wie�",
			"240607_2.0011" :	"P�aczki",
			"240607_2.0012" :	"Pop�w",
			"240607_2.0013" :	"R�bielice Kr�lewskie",
			"240607_2.0014" :	"W�sosz Dolny",
			"240607_2.0015" :	"W�sosz G�rny",
			"240607_2.0016" :	"Wi�cki",
			"240607_2.0017" :	"Zawady",
			"240607_2.0018" :	"Zbory",

			"240608_2.0001" :	"Anton�w",
			"240608_2.0002" :	"Bagna",
			"240608_2.0003" :	"B�r Zajaci�ski",
			"240608_2.0004" :	"Brzeziny",
			"240608_2.0005" :	"D�browa",
			"240608_2.0006" :	"G�rki",
			"240608_2.0007" :	"Kami�sko",
			"240608_2.0008" :	"Kostrzyna I",
			"240608_2.0009" :	"Ku�nica	Nowa",
			"240608_2.0010" :	"Ku�nica	Stara",
			"240608_2.0011" :	"�ugi	Rad�y",
			"240608_2.0012" :	"Michalin�w",
			"240608_2.0013" :	"Mr�wczak",
			"240608_2.0014" :	"Pod��e	Szlacheckie",
			"240608_2.0015" :	"Przystaj�",
			"240608_2.0016" :	"Siekierowizna",
			"240608_2.0017" :	"Stany",
			"240608_2.0018" :	"Wilcza G�ra",
			"240608_2.0019" :	"Wrzosy",

			"240609_2.0001" :	"Bie�e�",
			"240609_2.0002" :	"Borowe",
			"240609_2.0003" :	"B�r Zapilski",
			"240609_2.0004" :	"Brzezinki",
			"240609_2.0005" :	"Czarna Wie�",
			"240609_2.0006" :	"D�ugi K�t",
			"240609_2.0007" :	"Golce",
			"240609_2.0008" :	"Grodzisko",
			"240609_2.0009" :	"Hutka",
			"240609_2.0010" :	"Jezioro",
			"240609_2.0011" :	"Kalej",
			"240609_2.0012" :	"Klepaczka",
			"240609_2.0013" :	"Kuleje",
			"240609_2.0014" :	"Nowiny",
			"240609_2.0015" :	"Pierzchno",
			"240609_2.0016" :	"Pi�a	I",
			"240609_2.0017" :	"Pi�a	II",
			"240609_2.0018" :	"Puszczew",
			"240609_2.0019" :	"Szarlejka",
			"240609_2.0020" :	"Truskolasy",
			"240609_2.0021" :	"W�glowice",
			"240609_2.0022" :	"Wr�czyca Ma�a",
			"240609_2.0023" :	"Wr�czyca Wielka",
			"240609_2.0024" :	"Wydra",
			"240609_2.0025" :	"Zam�ynie",

			"240401_4.0001" :	"Blachownia",
			"240401_4.0002" :	"B�aszczyki",


			"999999_9.9999" :	"koniec wy�cigu"
		}




		# s�ownik do zamiany	nazwy	wpisanej	do	entry-sw_obreb	na	terytFull
		self.dictObr_nazwaObrWpisana2teryt = {
         "Brody Malina"                   : "240601_4.0001",
         "BrodyMalina"                    : "240601_4.0001",
         "K�obuck"                        : "240601_4.0002",
         "Klobuck"                        : "240601_4.0002",
         "Niwa Skrzesz�w"                 : "240601_4.0003",
         "NiwaSkrzesz�w"                  : "240601_4.0003",
         "Osoki - Pustkowie"              : "240601_4.0004",
         "Osoki-Pustkowie"                : "240601_4.0004",
         "OsokiPustkowie"                 : "240601_4.0004",
         "Przyby��w"                      : "240601_4.0005",
         "Przybylow"                      : "240601_4.0005",
         "Smugi"                          : "240601_4.0006",
         "Zag�rze"                        : "240601_4.0007",
         "Zagorze"                        : "240601_4.0007",
         "Zakrzew"                        : "240601_4.0008",

         "Bia�a Dolna"                    : "240601_5.0001",
         "Bia�aD"                         : "240601_5.0001",
         "Bia�a G�rna"                    : "240601_5.0002",
         "Bia�aG"                         : "240601_5.0002",
         "Borowianka"                     : "240601_5.0003",
         "Gruszewnia"                     : "240601_5.0004",
         "Kamyk"                          : "240601_5.0005",
         "Kopiec"                         : "240601_5.0006",
         "Lgota"                          : "240601_5.0007",
         "Libidza"                        : "240601_5.0008",
         "�obodno"                        : "240601_5.0009",
         "Nowa Wie� K"                    : "240601_5.0010",
         "Nowa Wie�-K"                    : "240601_5.0010",
         "Nowa Wie�K"                     : "240601_5.0010",
         "Rybno"                          : "240601_5.0011",

         "Krzepice"                       : "240602_4.0001",
         "Kuk�w"                          : "240602_4.0002",
         "Ku�niczka"                      : "240602_4.0003",

         "Dankowice"                      : "240602_5.0001",
         "Lutrowskie"                     : "240602_5.0002",
         "Pod��e Kr�lewskie"             : "240602_5.0003",
         "Pod��eK"                       : "240602_5.0003",
         "Starokrzepice"                  : "240602_5.0004",
         "Szarki"                         : "240602_5.0005",
         "Zaj�czki I"                     : "240602_5.0006",
         "Zaj�czki II"                    : "240602_5.0007",

         "Albert�w"                       : "240603_2.0001",
         "Brz�zki"                        : "240603_2.0002",
         "Dank�w"                         : "240603_2.0003",
         "Grabarze"                       : "240603_2.0004",
         "Julian�w"                       : "240603_2.0005",
         "Kle�niska"                      : "240603_2.0006",
         "Lind�w"                         : "240603_2.0007",
         "Lipie"                          : "240603_2.0008",
         "�y�niaki"                       : "240603_2.0009",
         "Napoleon"                       : "240603_2.0010",
         "Natolin"                        : "240603_2.0011",
         "Parzymiechy"                    : "240603_2.0012",
         "R�bielice Szlacheckie"          : "240603_2.0013",
         "Rozalin"                        : "240603_2.0014",
         "Stanis�aw�w"                    : "240603_2.0015",
         "Szyszk�w"                       : "240603_2.0016",
         #"Wapiennik"                      : "240603_2.0017",
         "Wapiennik-L"                    : "240603_2.0017",
         "Wapiennik L"                    : "240603_2.0017",
         "Zbrojewsko"                     : "240603_2.0018",
         "Zimnowoda"                      : "240603_2.0019",

         "Borowa"                         : "240604_2.0001",
         "Izbiska"                        : "240604_2.0002",
         "Ko�aczkowice"                   : "240604_2.0003",
         "Maz�wki"                        : "240604_2.0004",
         "Mied�no"                        : "240604_2.0005",
         "Mokra"                          : "240604_2.0006",
         "Ostrowy"                        : "240604_2.0007",
         "Suchany"                        : "240604_2.0008",
         #"Wapiennik"                      : "240604_2.0009",
         "Wapiennik-M"                    : "240604_2.0009",
         "Wapiennik M"                    : "240604_2.0009",
         "W�adys�aw�w"                    : "240604_2.0010",

         "Iwanowice Du�e"                 : "240605_2.0001",
         "Iwanowice Ma�e"                 : "240605_2.0002",
         "Nabok�w"                        : "240605_2.0003",
         "Opat�w"                         : "240605_2.0004",
         "Wale�cz�w"                      : "240605_2.0005",
         "Wilkowiecko"                    : "240605_2.0006",
         "Z�ochowice"                     : "240605_2.0007",
         "Zwierzyniec I"                  : "240605_2.0008",
         "Zwierzyniec II"                 : "240605_2.0009",

         "Aleksandr�w"                    : "240606_2.0001",
         "Cyganka"                        : "240606_2.0002",
         "Jaciska"                        : "240606_2.0003",
         "Janiki"                         : "240606_2.0004",
         "Ka�muki"                        : "240606_2.0005",
         "Kawki"                          : "240606_2.0006",
         "Konieczki"                      : "240606_2.0007",
         "Koski"                          : "240606_2.0008",
         "Kostrzyna II"                   : "240606_2.0009",
         "Kotary"                         : "240606_2.0010",
         "Panki"                          : "240606_2.0011",
         "Praszczyki"                     : "240606_2.0012",
         "Zwierzyniec III"                : "240606_2.0013",
         "�erdzina"                       : "240606_2.0014",

         "Annolesie"                      : "240607_2.0001",
         "Brz�zki"                        : "240607_2.0002",
         "D�browa"                        : "240607_2.0003",
         "D�br�wka"                       : "240607_2.0004",
         "D�bie"                          : "240607_2.0005",
         "Florian�w"                      : "240607_2.0006",
         "Kamie�szczyzna"                 : "240607_2.0007",
         "Lelity"                         : "240607_2.0008",
         "Marian�w"                       : "240607_2.0009",
         #"NowaWie�"                      : "240607_2.0010",
         "Nowa Wie� P"                    : "240607_2.0010",
         "Nowa Wie�-P"                    : "240607_2.0010",
		 "Nowa Wie�P"					  : "240607_2.0010",
         "P�aczki"                        : "240607_2.0011",
         "Pop�w"                          : "240607_2.0012",
         "R�bielice Kr�lewskie"           : "240607_2.0013",
         "W�sosz Dolny"                   : "240607_2.0014",
         "W�sosz G�rny"                   : "240607_2.0015",
         "Wi�cki"                         : "240607_2.0016",
         "Zawady"                         : "240607_2.0017",
         "Zbory"                          : "240607_2.0018",

         "Anton�w"                        : "240608_2.0001",
         "Bagna"                          : "240608_2.0002",
         "B�r Zajaci�ski"                 : "240608_2.0003",
         "Brzeziny"                       : "240608_2.0004",
         "D�browa"                        : "240608_2.0005",
         "G�rki"                          : "240608_2.0006",
         "Kami�sko"                       : "240608_2.0007",
         "KostrzynaI"                     : "240608_2.0008",
         "Kostrzyna I"                    : "240608_2.0008",
         "Ku�nica Nowa"                   : "240608_2.0009",
         "Ku�nica Stara"                  : "240608_2.0010",
         "�ugi Rad�y"                     : "240608_2.0011",
         "Michalin�w"                     : "240608_2.0012",
         "Mr�wczak"                       : "240608_2.0013",
         "Pod��e Szlacheckie"            : "240608_2.0014",
         "Przystaj�"                      : "240608_2.0015",
         "Siekierowizna"                  : "240608_2.0016",
         "Stany"                          : "240608_2.0017",
         "Wilcza G�ra"                    : "240608_2.0018",
         "Wrzosy"                         : "240608_2.0019",

         "Bie�e�"                         : "240609_2.0001",
         "Borowe"                         : "240609_2.0002",
         "B�r Zapilski"                   : "240609_2.0003",
         "Brzezinki"                      : "240609_2.0004",
         "Czarna Wie�"                    : "240609_2.0005",
         "CzarnaW"                        : "240609_2.0005",
         "D�ugi K�t"                      : "240609_2.0006",
         "D�ugiK�t"                       : "240609_2.0006",
         "D�ugiK"                         : "240609_2.0006",
         "Golce"                          : "240609_2.0007",
         "Grodzisko"                      : "240609_2.0008",
         "Hutka"                          : "240609_2.0009",
         "Jezioro"                        : "240609_2.0010",
         "Kalej"                          : "240609_2.0011",
         "Klepaczka"                      : "240609_2.0012",
         "Kuleje"                         : "240609_2.0013",
         "Nowiny"                         : "240609_2.0014",
         "Pierzchno"                      : "240609_2.0015",
         "Pi�a I"                         : "240609_2.0016",
         "Pi�a II"                        : "240609_2.0017",
         "Puszczew"                       : "240609_2.0018",
         "Szarlejka"                      : "240609_2.0019",
         "Truskolasy"                     : "240609_2.0020",
         "W�glowice"                      : "240609_2.0021",
         "Wr�czyca Ma�a"                  : "240609_2.0022",
         "Wr�czycaM"                      : "240609_2.0022",
         "Wr�czyca Wielka"                : "240609_2.0023",
         "Wr�czycaW"                      : "240609_2.0023",
         "Wydra"                          : "240609_2.0024",
         "Zam�ynie"                       : "240609_2.0025",

         # inne powiaty
         "Blachownia"                     : "240401_4.0001",
         "B�aszczyki"                     : "240401_4.0002",


         "koniec wy�cigu"                 : "999999_9.9999"
         }

		# s�ownik do zamiany	terytu na nazw� obr.	do	utworzenia katalogu
		self.dictObr_teryt2nazwaDir =	{
			"240601_4.0001" :	"BrodyM",
			"240601_4.0002" :	"Klobuck",
			"240601_4.0003" :	"NiwaSk",
			"240601_4.0004" :	"OsokiP",
			"240601_4.0005" :	"Przybylow",
			"240601_4.0006" :	"Smugi",
			"240601_4.0007" :	"Zagorze",
			"240601_4.0008" :	"Zakrzew",

			"240601_5.0001" :	"BialaD",
			"240601_5.0002" :	"BialaG",
			"240601_5.0003" :	"Borowianka",
			"240601_5.0004" :	"Gruszewnia",
			"240601_5.0005" :	"Kamyk",
			"240601_5.0006" :	"Kopiec",
			"240601_5.0007" :	"Lgota",
			"240601_5.0008" :	"Libidza",
			"240601_5.0009" :	"Lobodno",
			"240601_5.0010" :	"NowaWies-Kl",
			"240601_5.0011" :	"Rybno",

			"240602_4.0001" :	"Krzepice",
			"240602_4.0002" :	"Kukow",
			"240602_4.0003" :	"Kuzniczka",

			"240602_5.0001" :	"Dankowice",
			"240602_5.0002" :	"Lutrowskie",
			"240602_5.0003" :	"PodlezeKrol",
			"240602_5.0004" :	"Starokrzepice",
			"240602_5.0005" :	"Szarki",
			"240602_5.0006" :	"Zajaczki1",
			"240602_5.0007" :	"Zajaczki2",

			"240603_2.0001" :	"Albertow",
			"240603_2.0002" :	"Brzozki",
			"240603_2.0003" :	"Dankow",
			"240603_2.0004" :	"Grabarze",
			"240603_2.0005" :	"Julianow",
			"240603_2.0006" :	"Klesniska",
			"240603_2.0007" :	"Lindow",
			"240603_2.0008" :	"Lipie",
			"240603_2.0009" :	"Lyzniaki",
			"240603_2.0010" :	"Napoleon",
			"240603_2.0011" :	"Natolin",
			"240603_2.0012" :	"Parzymiechy",
			"240603_2.0013" :	"RebieliceSz",
			"240603_2.0014" :	"Rozalin",
			"240603_2.0015" :	"Stanislawow",
			"240603_2.0016" :	"Szyszkow",
			"240603_2.0017" :	"Wapiennik-L",
			"240603_2.0018" :	"Zbrojewsko",
			"240603_2.0019" :	"Zimnowoda",

			"240604_2.0001" :	"Borowa",
			"240604_2.0002" :	"Izbiska",
			"240604_2.0003" :	"Kolaczkowice",
			"240604_2.0004" :	"Mazowki",
			"240604_2.0005" :	"Miedzno",
			"240604_2.0006" :	"Mokra",
			"240604_2.0007" :	"Ostrowy",
			"240604_2.0008" :	"Suchany",
			"240604_2.0009" :	"Wapiennik-M",
			"240604_2.0010" :	"Wladyslawow",

			"240605_2.0001" :	"IwanowiceD",
			"240605_2.0002" :	"IwanowiceM",
			"240605_2.0003" :	"Nabokow",
			"240605_2.0004" :	"Opatow",
			"240605_2.0005" :	"Walenczow",
			"240605_2.0006" :	"Wilkowiecko",
			"240605_2.0007" :	"Zlochowice",
			"240605_2.0008" :	"Zwierzyniec1",
			"240605_2.0009" :	"Zwierzyniec2",

			"240606_2.0001" :	"Aleksandrow",
			"240606_2.0002" :	"Cyganka",
			"240606_2.0003" :	"Jaciska",
			"240606_2.0004" :	"Janiki",
			"240606_2.0005" :	"Kalmuki",
			"240606_2.0006" :	"Kawki",
			"240606_2.0007" :	"Konieczki",
			"240606_2.0008" :	"Koski",
			"240606_2.0009" :	"Kostrzyna2",
			"240606_2.0010" :	"Kotary",
			"240606_2.0011" :	"Panki",
			"240606_2.0012" :	"Praszczyki",
			"240606_2.0013" :	"Zwierzyniec3",
			"240606_2.0014" :	"Zerdzina",

			"240607_2.0001" :	"Annolesie",
			"240607_2.0002" :	"Brzozki",
			"240607_2.0003" :	"Dabrowa",
			"240607_2.0004" :	"Dabrowka",
			"240607_2.0005" :	"Debie",
			"240607_2.0006" :	"Florianow",
			"240607_2.0007" :	"Kamienszczyzna",
			"240607_2.0008" :	"Lelity",
			"240607_2.0009" :	"Marianow",
			"240607_2.0010" :	"NowaWies-Pop",
			"240607_2.0011" :	"Placzki",
			"240607_2.0012" :	"Popow",
			"240607_2.0013" :	"RebieliceKrol",
			"240607_2.0014" :	"WasoszD",
			"240607_2.0015" :	"WasoszG",
			"240607_2.0016" :	"Wiecki",
			"240607_2.0017" :	"Zawady",
			"240607_2.0018" :	"Zbory",

			"240608_2.0001" :	"Antonow",
			"240608_2.0002" :	"Bagna",
			"240608_2.0003" :	"BorZajacinski",
			"240608_2.0004" :	"Brzeziny",
			"240608_2.0005" :	"Dabrowa",
			"240608_2.0006" :	"Gorki",
			"240608_2.0007" :	"Kaminsko",
			"240608_2.0008" :	"Kostrzyna1",
			"240608_2.0009" :	"KuznicaN",
			"240608_2.0010" :	"KuznicaS",
			"240608_2.0011" :	"LugiRadly",
			"240608_2.0012" :	"Michalinow",
			"240608_2.0013" :	"Mrowczak",
			"240608_2.0014" :	"PodlezeSz",
			"240608_2.0015" :	"Przystajn",
			"240608_2.0016" :	"Siekierowizna",
			"240608_2.0017" :	"Stany",
			"240608_2.0018" :	"WilczaGora",
			"240608_2.0019" :	"Wrzosy",

			"240609_2.0001" :	"Biezen",
			"240609_2.0002" :	"Borowe",
			"240609_2.0003" :	"BorZapilski",
			"240609_2.0004" :	"Brzezinki",
			"240609_2.0005" :	"CzarnaWies",
			"240609_2.0006" :	"DlugiKat",
			"240609_2.0007" :	"Golce",
			"240609_2.0008" :	"Grodzisko",
			"240609_2.0009" :	"Hutka",
			"240609_2.0010" :	"Jezioro",
			"240609_2.0011" :	"Kalej",
			"240609_2.0012" :	"Klepaczka",
			"240609_2.0013" :	"Kuleje",
			"240609_2.0014" :	"Nowiny",
			"240609_2.0015" :	"Pierzchno",
			"240609_2.0016" :	"Pila1",
			"240609_2.0017" :	"Pila2",
			"240609_2.0018" :	"Puszczew",
			"240609_2.0019" :	"Szarlejka",
			"240609_2.0020" :	"Truskolasy",
			"240609_2.0021" :	"Weglowice",
			"240609_2.0022" :	"WreczycaM",
			"240609_2.0023" :	"WreczycaW",
			"240609_2.0024" :	"Wydra",
			"240609_2.0025" :	"Zamlynie",

			"240401_4.0001" :	"Blachownia",
			"240401_4.0002" :	"Blaszczyki",

			"999999_9.9999" :	"koniec wy�cigu"
		}


		# s�ownik do zamiany	nazwy	obr�bu na teryt
		# UWAGA!!!
		# Ten s�ownik jest nieprzydatny, bo powtarzaj� sie w nim klucze
		'''
		self.dictObr_nazwa2teryt =	{
			"Brody Malina"						: "240601_4.0001",
			"K�obuck"							: "240601_4.0002",
			"Niwa Skrzesz�w"					: "240601_4.0003",
			"Osoki - Pustkowie"				: "240601_4.0004",
			"Przyby��w"							: "240601_4.0005",
			"Smugi"								: "240601_4.0006",
			"Zag�rze"							: "240601_4.0007",
			"Zakrzew"							: "240601_4.0008",
													
			"Bia�a Dolna"						: "240601_5.0001",
			"Bia�a G�rna"						: "240601_5.0002",
			"Borowianka"						: "240601_5.0003",
			"Gruszewnia"						: "240601_5.0004",
			"Kamyk"								: "240601_5.0005",
			"Kopiec"								: "240601_5.0006",
			"Lgota"								: "240601_5.0007",
			"Libidza"							: "240601_5.0008",
			"�obodno"							: "240601_5.0009",
			"Nowa Wie�"							: "240601_5.0010",
			"Rybno"								: "240601_5.0011",
													
			"Krzepice"							: "240602_4.0001",
			"Kuk�w"								: "240602_4.0002",
			"Ku�niczka"							: "240602_4.0003",
													
			"Dankowice"							: "240602_5.0001",
			"Lutrowskie"						: "240602_5.0002",
			"Pod��e Kr�lewskie"				: "240602_5.0003",
			"Starokrzepice"					: "240602_5.0004",
			"Szarki"								: "240602_5.0005",
			"Zaj�czki I"						: "240602_5.0006",
			"Zaj�czki II"						: "240602_5.0007",
													
			"Albert�w"							: "240603_2.0001",
			"Brz�zki"							: "240603_2.0002",
			"Dank�w"								: "240603_2.0003",
			"Grabarze"							: "240603_2.0004",
			"Julian�w"							: "240603_2.0005",
			"Kle�niska"							: "240603_2.0006",
			"Lind�w"								: "240603_2.0007",
			"Lipie"								: "240603_2.0008",
			"�y�niaki"							: "240603_2.0009",
			"Napoleon"							: "240603_2.0010",
			"Natolin"							: "240603_2.0011",
			"Parzymiechy"						: "240603_2.0012",
			"R�bielice Szlacheckie"			: "240603_2.0013",
			"Rozalin"							: "240603_2.0014",
			"Stanis�aw�w"						: "240603_2.0015",
			"Szyszk�w"							: "240603_2.0016",
			"Wapiennik"							: "240603_2.0017",
			"Zbrojewsko"						: "240603_2.0018",
			"Zimnowoda"							: "240603_2.0019",
													
			"Borowa"								: "240604_2.0001",
			"Izbiska"							: "240604_2.0002",
			"Ko�aczkowice"						: "240604_2.0003",
			"Maz�wki"							: "240604_2.0004",
			"Mied�no"							: "240604_2.0005",
			"Mokra"								: "240604_2.0006",
			"Ostrowy"							: "240604_2.0007",
			"Suchany"							: "240604_2.0008",
			"Wapiennik"							: "240604_2.0009",
			"W�adys�aw�w"						: "240604_2.0010",
													
			"Iwanowice Du�e"					: "240605_2.0001",
			"Iwanowice Ma�e"					: "240605_2.0002",
			"Nabok�w"							: "240605_2.0003",
			"Opat�w"								: "240605_2.0004",
			"Wale�cz�w"							: "240605_2.0005",
			"Wilkowiecko"						: "240605_2.0006",
			"Z�ochowice"						: "240605_2.0007",
			"Zwierzyniec I"					: "240605_2.0008",
			"Zwierzyniec II"					: "240605_2.0009",
													
			"Aleksandr�w"						: "240606_2.0001",
			"Cyganka"							: "240606_2.0002",
			"Jaciska"							: "240606_2.0003",
			"Janiki"								: "240606_2.0004",
			"Ka�muki"							: "240606_2.0005",
			"Kawki"								: "240606_2.0006",
			"Konieczki"							: "240606_2.0007",
			"Koski"								: "240606_2.0008",
			"Kostrzyna II"						: "240606_2.0009",
			"Kotary"								: "240606_2.0010",
			"Panki"								: "240606_2.0011",
			"Praszczyki"						: "240606_2.0012",
			"Zwierzyniec III"					: "240606_2.0013",
			"�erdzina"							: "240606_2.0014",
													
			"Annolesie"							: "240607_2.0001",
			"Brz�zki"							: "240607_2.0002",
			"D�browa"							: "240607_2.0003",
			"D�br�wka"							: "240607_2.0004",
			"D�bie"								: "240607_2.0005",
			"Florian�w"							: "240607_2.0006",
			"Kamie�szczyzna"					: "240607_2.0007",
			"Lelity"								: "240607_2.0008",
			"Marian�w"							: "240607_2.0009",
			"Nowa Wie�"							: "240607_2.0010",
			"P�aczki"							: "240607_2.0011",
			"Pop�w"								: "240607_2.0012",
			"R�bielice Kr�lewskie"			: "240607_2.0013",
			"W�sosz Dolny"						: "240607_2.0014",
			"W�sosz G�rny"						: "240607_2.0015",
			"Wi�cki"								: "240607_2.0016",
			"Zawady"								: "240607_2.0017",
			"Zbory"								: "240607_2.0018",
													
			"Anton�w"							: "240608_2.0001",
			"Bagna"								: "240608_2.0002",
			"B�r Zajaci�ski"					: "240608_2.0003",
			"Brzeziny"							: "240608_2.0004",
			"D�browa"							: "240608_2.0005",
			"G�rki"								: "240608_2.0006",
			"Kami�sko"							: "240608_2.0007",
			"Kostrzyna I"						: "240608_2.0008",
			"Ku�nica Nowa"						: "240608_2.0009",
			"Ku�nica Stara"					: "240608_2.0010",
			"�ugi Rad�y"						: "240608_2.0011",
			"Michalin�w"						: "240608_2.0012",
			"Mr�wczak"							: "240608_2.0013",
			"Pod��e Szlacheckie"			: "240608_2.0014",
			"Przystaj�"							: "240608_2.0015",
			"Siekierowizna"					: "240608_2.0016",
			"Stany"								: "240608_2.0017",
			"Wilcza G�ra"						: "240608_2.0018",
			"Wrzosy"								: "240608_2.0019",
													
			"Bie�e�"								: "240609_2.0001",
			"Borowe"								: "240609_2.0002",
			"B�r Zapilski"						: "240609_2.0003",
			"Brzezinki"							: "240609_2.0004",
			"Czarna Wie�"						: "240609_2.0005",
			"D�ugi K�t"							: "240609_2.0006",
			"Golce"								: "240609_2.0007",
			"Grodzisko"							: "240609_2.0008",
			"Hutka"								: "240609_2.0009",
			"Jezioro"							: "240609_2.0010",
			"Kalej"								: "240609_2.0011",
			"Klepaczka"							: "240609_2.0012",
			"Kuleje"								: "240609_2.0013",
			"Nowiny"								: "240609_2.0014",
			"Pierzchno"							: "240609_2.0015",
			"Pi�a I"								: "240609_2.0016",
			"Pi�a II"							: "240609_2.0017",
			"Puszczew"							: "240609_2.0018",
			"Szarlejka"							: "240609_2.0019",
			"Truskolasy"						: "240609_2.0020",
			"W�glowice"							: "240609_2.0021",
			"Wr�czyca Ma�a"					: "240609_2.0022",
			"Wr�czyca Wielka"					: "240609_2.0023",
			"Wydra"								: "240609_2.0024",
			"Zam�ynie"							: "240609_2.0025",
													
			"Blachownia"						: "240401_4.0001",
			"B�aszczyki"						: "240401_4.0002",
													
													
			"koniec wy�cigu"					: "999999_9.9999"
		}
		'''
		
	# koniec	__init__()
	# = =	= = =	= = =	= = =	= = =	= = =	= = =	= = =	= = =	= = =	= = =	= = =	= = =

	'''
	@staticmethod
	def setTerytFrom_obrNazwa_static(	astr):
		return setTerytFrom_obrNazwa(	astr)
	'''

	def setTerytyFrom_obrTerytFull( self, aobrTerytFull):
		# sprawdzenie, czy aobrTerytFull jest w s�owniku teryt�w
		if aobrTerytFull in self.dictObr_teryt2nazwa.keys():
			self.terytFull = aobrTerytFull 
			print( "aobrTerytFull=" +	aobrTerytFull)
			print( "dictObr_teryt2nazwaDir[ obr_terytFull]=" +	self.dictObr_teryt2nazwaDir[ self.terytFull])

			self.terytF_woj =	self.terytFull[0:2]
			self.terytF_pow =	self.terytFull[0:4]
			self.terytF_jew =	self.terytFull[0:8]
			self.terytF_obr =	self.terytFull
			self.teryt_woj	 =	self.terytFull[0:2]
			self.teryt_pow	 =	self.terytFull[2:4]
			self.teryt_jew	 =	self.terytFull[4:8]
			self.teryt_obr	 =	self.terytFull[9:15]

			self.nazwa_woj	= "�l�skie"
			self.nazwa_pow	= self.dictPow[ self.terytF_pow]
			self.nazwa_jew	= self.dictJEw[ self.terytF_jew]
			self.nazwa_obr	= self.dictObr_teryt2nazwa[ self.terytFull]

			self.nazwa_uStn_woj = "Wojew�dztwo:	" + self.nazwa_woj
			self.nazwa_uStn_pow = "Powiat: "	+ self.nazwa_pow
			self.nazwa_uStn_jew = "Jednostka	ewidencyjna: "	+ self.terytF_jew[0:6] + "__"	+ self.terytF_jew[7:9] + ", "	+ self.nazwa_jew
			self.nazwa_uStn_obr = "obr�b:	" + self.teryt_obr +	" " +	self.nazwa_obr

			# nazwa obr. do nazwy katalogu
			self.nazwaDir_obr	= self.dictObr_teryt2nazwaDir[ self.terytFull]

			return 0
		else:
			print( "aobrTerytFull >%s< nie zosta� odnaleziony w s�owniku" % ( aobrTerytFull))
			return -1
	
	
	# chyba - w tej postaci - zb�dna funkcja
	def setTerytFrom_obrNazwa(	self,	astr):
		'''
			podajemy	nazw�	obr�bu, a funkcja	na	tej podstawie ustawia
			wszystkie pola	instancji klasy
		'''
		if	len( astr) > 2:
			#self.terytFull	= self.dictObr_nazwaObrWpisana2teryt[ astr]
			print( "self.terytFull=" +	self.terytFull)
			print( "dictObr_teryt2nazwaDir[ obr_terytFull]=" +	self.dictObr_teryt2nazwaDir[ self.terytFull])

			self.terytF_woj =	self.terytFull[0:2]
			self.terytF_pow =	self.terytFull[0:4]
			self.terytF_jew =	self.terytFull[0:8]
			self.terytF_obr =	self.terytFull
			self.teryt_woj	 =	self.terytFull[0:2]
			self.teryt_pow	 =	self.terytFull[2:4]
			self.teryt_jew	 =	self.terytFull[4:8]
			self.teryt_obr	 =	self.terytFull[9:15]

			self.nazwa_woj	= "�l�skie"
			self.nazwa_pow	= self.dictPow[ self.terytF_pow]
			self.nazwa_jew	= self.dictJEw[ self.terytF_jew]
			self.nazwa_obr	= self.dictObr_teryt2nazwa[ self.terytFull]

			self.nazwa_uStn_woj = "Wojew�dztwo:	" + self.nazwa_woj
			self.nazwa_uStn_pow = "Powiat: "	+ self.nazwa_pow
			self.nazwa_uStn_jew = "Jednostka	ewidencyjna: "	+ self.terytF_jew[0:6] + "__"	+ self.terytF_jew[7:9] + ", "	+ self.nazwa_jew
			self.nazwa_uStn_obr = "obr�b:	" + self.teryt_obr +	" " +	self.nazwa_obr

			# nazwa obr. do nazwy katalogu
			self.nazwaDir_obr	= self.dictObr_teryt2nazwaDir[ self.terytFull]

			return 0
		else:
			print( "Zbyt kr�tka nazwa obr�bu!")
			return -1

	