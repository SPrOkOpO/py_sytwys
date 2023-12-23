#-*- coding: windows-1250 -*-


# słownik stałych
#---------------------------------------------------------------------
dictConstants = {
        "NR_WERSJI"             : "2.3.3"
        ,"GC_DIR_SYTWYS"        : "t:\\sytwys\\"                    
        ,"GC_DIR_LICZNIK"       : "t:\\sytwys\\AAB__licznik\\"      
        }


def debugList_dictionary():
    print( "\nSłownik dictConstants:")
    for key, val in dictConstants.items():
        print( "%15s : %s" % (key, val))