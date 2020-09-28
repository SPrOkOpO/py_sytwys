todo
====

bieżące
-------
*   otwieranie z uStn połączone z wczytaniem odpowiedniego pliku
    swInfo
    
planowane 
---------
*   reorganizacja klasy sytwys
    -   rozdzielenie na składniki - klasy z pliku sytwys_elements.py    
*   następnie reorganizacja klasy sytwysGUIgid


changelog
=========

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