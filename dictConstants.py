#-*- coding: windows-1250 -*-


# s�ownik sta�ych
#---------------------------------------------------------------------
dictConstants = {
        "NR_WERSJI"             : "2.3.3"
        ,"GC_DIR_SYTWYS"        : "t:\\sytwys\\"                    
        ,"GC_DIR_LICZNIK"       : "t:\\sytwys\\AAB__licznik\\"      
        }


def debugList_dictionary():
    print( "\nS�ownik dictConstants:")
    for key, val in dictConstants.items():
        print( "%15s : %s" % (key, val))