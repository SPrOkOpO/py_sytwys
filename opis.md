todo
====

bieżące
-------
    *   !!! zweryfikować metodę wczytaj() pod kątem zgodności z nowym
        kodem, wykorzystującym klasę Dzialki
    *   otwieranie z uStn połączone z wczytaniem odpowiedniego pliku
        swInfo
    
planowane 
---------
    *   reorganizacja klasy sytwys
        -   rozdzielenie na składniki - klasy z pliku sytwys_elements.py    
    *   następnie reorganizacja klasy sytwysGUIgid
    *   dopracowanie funkcji divide_into_rows()


changelog
=========

2020.12.28 v. 2.1.1
-------------------
    *   wdrożenie obsługi zgłoszeń bez mapy (wykaz synchronizacyjny)
        -   dodano typ imdcp-sw
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