


# słownik stałych
#---------------------------------------------------------------------
dictConstants = {
    "NR_WERSJI" : "2.5.2",
    "GC_DIR_SYTWYS" : "t:\\sytwys",
    "GC_DIR_LICZNIK" : "t:\\sytwys\\AAB__licznik",
    'GC_EMPTY_STRATEG_DATABASE_DIR': r't:\STRATEG\BAZA_pusta',
    'GC_EWMAPA_BAZA_INIFILE': r'i:\STRATEG\PROGRAMY\EWMAPA\Users\user\baza.ini'
    }


def debugList_dictionary():
    print("\nSłownik dictConstants:")
    for key, val in dictConstants.items():
        print("%15s : %s" % (key, val))
