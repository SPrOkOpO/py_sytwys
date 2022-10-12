todo
====

bieżące
-------
    *   !!! zweryfikować metodę wczytaj() pod kątem zgodności z nowym
        kodem, wykorzystującym klasę Dzialki
    *   usunąć błąd opisany w 2.1.2
    
planowane 
---------
    *   reorganizacja klasy sytwys
        -   rozdzielenie na składniki - klasy z pliku sytwys_elements.py    
    *   następnie reorganizacja klasy sytwysGUIgid
    *   dopracowanie funkcji divide_into_rows()

changelog
=========

2022.10.12 v. 2.1.13
--------------------
  * kG: implementacja klasy KontoGeodety (częściowa):
    - generowanie pliku kg.txt
    - generowanie pliku AutoHotKey, automatyzującego wypełnianie formularza kG
    - do zrobienia: generowanie pliku dz_ergo.txt

2022.09.13 v. 2.1.12
--------------------
  * inw: tekst `?-?-?` jako domyślny nr decyzji i jej data
  * inw: dodanie brakującego nawiasu wokół określenia obiektu budowlanego
  * gui: w widgetach text zmieniono sposób zawijania tekstu - był domyślny
         wrap=tk.CHAR, a jest wrap=tk.WORD (usunięto rówocześnie wywołanie funkcji
         divide_into_rows(self.sw.mdcp.kp_uwagi2, 90) - funkcja jest niedopracowana)

2022.01.25 v. 2.1.11
--------------------
  * zmiana w instrukcji inicjującej rok polegajaca na z zastąpieniu stałej wartości
    funkcją zwracajacą aktualny rok: g.v_sw_idZgl_rok.set(get_RRRR())

2021.10.08 v. 2.1.10
--------------------
    * SytwysGUIgrid.py zapisz_1():
        - automatyzacja rysowania nagłówka tytułu (MAPA DO ... albo GEODEZYJNA ...)
          - dodano plik tytNagl.txt

2021.09.09 v. 2.1.9
-------------------
    *   SytwysGUIgrid.py zapisz_1():
        -   zmiana układu wysokościowego na PL-EVRF2007-NH (z PL-KRON86-NH) 

2021.07.11 v. 2.1.8
-------------------
    *   SytwysGUIgrid.py comboBox `Typ` (kG_cele_pracy):
        -   zmieniono kolejność mdcp i inw (teraz typ inw jest widoczny po 
            rozwinięciu listy) 

2021.06.25 v. 2.1.7
-------------------
    *   w klasie dzialki (spLib\sytwys\dzialki.py) poprawiono usuwania z napisu
        zawierającego listę działek, zbędnych napisów: dodano  do ich listy `i` 
        oraz zmieniono kolejność na liście `zbedny_napis_dzialka` tak, aby 
        dłuższe słowa były na początku

2021.05.18 v. 2.1.5
-------------------
    *   w module teryt dodano dwa obręby z 2404

2021.05.16 v. 2.1.5
-------------------
    *   w klasie dzialki (spLib\sytwys\dzialki.py) dodano usuwanie z napisu
        zawierającego listę działek, uciązliwego skrótu `dz.` (i jego 
        wariantów)
    *   wprowadzenie jednolitej zasady nazywania obrębów "dublujących się" 
        w różych j. ew.: do nazwy obrębu dodać suffix `-nazwa_jew[0:2]`
    *   poprawki w słowniku dictObr_nazwaObrWpisana2teryt wynikające 
        z wdrożenia powyższej zasady

2021.02.20 v. 2.1.4
-------------------
    <2.1.4 użycie argparse, wdrożenie trybu uruchamiania>
    *   dodanie obróbki argumentów (z użyciem argparse)
        -   główny cel, to umożliwienie wczytywania pliku sw_info podczas
            uruchamiania programu
        -   dodatkowo umożliwia to wprowadzenie trybów pracy nowa/aktualizacja,
            co wykorzystano do wdrożenia dwu trybów: [nowa, aktualizacja]
        -   możliwe, że wdrożenie trybów wyeliminowało błąd opisany w uwagach
            do wersji 2.1.2

2021.02.04 v. 2.1.3
-------------------
    *   plik kg.txt: dodano frazę do wyboru obiektów (w qgis-ie) wyrażeniem
         "idDzialki" IN (
            '240609_2.0005.145/1',
            '240609_2.0005.145/3',
            '240609_2.0005.145/4'
            )

2021.02.01 v. 2.1.2
-------------------
    *   zdiagnozowanie błędu polegającego na braku aktualizacji plików kG po
        zmianie danych
        -   problem występuje na przełomie miesięcy i polega na tym, że:
            -   struktura sw jest zakładana w styczniu - katalog ma nazwę 
                1049_kh_2101_...
            -   jeżeli zmiany wprowadzane są w lutym i uzyta została funkcja
                inicjuj, to tworzy on zmienną zawierającą nazwę katalogu
                z aktualnym miesiącem ..._2102_..., co przy próbie zapisu 
                plików kG powoduje oczywisty błąd No such file or dir
        >>  należy zmienić program tak, aby rozróżniał sytuację tworzenia
            nowej roboty od zmian do istniejącej
    *   Uwaga! Nie dokonano zmian w kodzie.

2020.01.31 v. 2.1.1
-------------------
    *   wdrożenie obsługi zgłoszeń bez mapy (wykaz synchronizacyjny)
        -   dodano typ imdcp-ws
        -   katalog sw otrzymuje sufiks "wykSyn"
    *   zmiana sposobu działania combobox-u typ
        -   wprowadzono obsługę zdarzenia <<ComboboxSelected>>
        -   funkcja obsługująca zdarzenie ustala wykonawcę na podstawie typu
            (poprzednio było odwrotnie, ale był tylko jeden typ prawny)

2020.12.28 v. 2.1.0
-------------------
    *   ostateczne wyeliminowanie pól dot. inwentaryzacji z klasy Sytwys
    *   zmiana sposobu działania funkcji zapisz - przed zapisem pobierane 
        są dane z kontrolek (dotychczas odbywało się to w sposób pośredni
        i - jako pisane w pośpiechu i z małym doświadczeniem - niechlujny)
    *   przekształcenie chBtn "ust 5" w "§ 16 pkt 1"
    *   działka/działki w tytule

2020.12.28 v. 2.0.10
-------------------
    *   merge wersja_2 to master (local)

2020.12.27 v. 2.0.9
-------------------
    *   moduł Dzialki
        *   przeniesienie funkcji sortujacej numery działek z klasy Dzialki
            poza definicje klas - jest niezależną funkcją
        *   klasa Dzialki() - drobne poprawki
    *   SytwysGUIgrid.py metoda zapisz():
        *   dodano drukowanie daty "1 rok+" w pliku kg.txt
    *   SytwysGUIgrid.py metoda inicjuj():
        *   zaimplementowanie oczyszczanie i sortowanie nrów działek
            z wykorzystaniem klasy Dzialki()
    *   kontynuacja zastępowania istniejącego kodu, dot. działek, kodem
        wykorzystującym klasę Dzialki() w:
        -   metodzie inicjuj()
        -   metodzie zapisz()
        -   klasie Sytwys
    
2020.12.23 v. 2.0.8
-------------------
    *   w module dzialki.py zaimplementowano skuteczną funkcję sortowania
        nr-ów działek

2020.12.21 v. 2.0.7
-------------------
    *   generowanie tekstów do wypełniania konta geodety (we własnym pliku):
        mdcp 01_4 Zagórze 1571
        01_4 Zagórze 1571
        *   na razie w treści klasy SytwysGUIgrid() >> wyizolować
    *   przeniesienie części kodu (głównie nowotworzonego) do biblioteki
        LibSP\sytwys
        *   nowe klasy Dzialka i Dzialki, KontoGeodety
        *   zapoczątkowanie wykorzystania własnych modułów z LibSP
    *   zesłownikowanie i implementacja aktualnych celów prac geodezyjnych     

2020.10.10 v. 2.0.6
-------------------
    *   zmiana treści uwag ze względu na zmianę przepisów
        *   usunięcie z klasy Sytwys zbędnych pól mdcp_... (obecnie są w klasie MDCP)
        *   usunięcie użycia tych pól także z klasy SytwysGUIgrid
        *   utworzenie funkcji divide_into_rows(), dzielącej teksty wyswietlane
            w kontrolkach tekstowych tx_mdcp_...
            *   funkcja nie działa idealnie - patrz docstring 
    
2020.09.28 v. 2.0.5
-------------------
    *   klasa sytwys
        *   dodano atrybut sw_dzialki_lst 
            (lista numerów działek)
        *   dodano atrybut sw_dzialki_ergo_lst 
            (lista numerów działek z terytem do zakresu ergo)
        *   dodano dwie metody generujące powyższe listy
        *   dodano atrybut sw_plikDz_ergo_abspath
            (pełna ścieżka pliku dz_ergo.txt)
        *   drobne zmiany związane z tworzeniem scieżki pliku dz_ergo.txt
        
    *   klasa SytwysGUIgrid
        *   zmodyfikowano metodę zapisz:
            - na początku: generuje listy działek
            - na końcu: tworzy plik ...\kG\dz_ergo.txt
        
2020.09.27 v. 2.0.4
-------------------
    *   klasa sytwys
        *   poprawka umożliwiająca tworzenie robót o numerach większych
            niż 1000
        *   tworzenie katalogu kG
        *   poprawka w treści uwag: ... "granic" działki ...    