#-*- coding: windows-1250 -*-
#
#   Utworzenie w katalogu syswys podkatalogu dla    nowej   roboty
#
#---------------------------------------------------------------------
import sys
import os
import datetime
import shutil
#shutil.__doc__
str( shutil)
import tkinter  as  tk
import tkinter.ttk as ttk
import argparse
import pprint

# import zasobów własnych programu
#---------------------------------------------------------------------
import teryt
#teryt.__doc__
str( teryt)
import sytwys
import SytwysGUIgrid

import dictConstants
#import dictErrors
sys.path.append(r"i:\aPy\LibSP")
import spprint


def get_RRMM():
    '''
        funkcja zwraca  string RRMM (1903), potrzebny   do  utworzenia
        sciezki dla katalogu    sw
    '''
    x = datetime.datetime.now()
    rrmm = x.strftime("%y%m")
    return rrmm

def get_RRRR():
    '''
        funkcja zwraca  string RRMM (1903), potrzebny   do  utworzenia
        sciezki dla katalogu    sw
    '''
    x = datetime.datetime.now()
    return x.strftime("%Y")


def main():
    # args parsing
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--tryb',
                    choices=['nowa', 'aktualizacja'],
                    help='tryb pracy [nowa, aktualizacja]')
    ap.add_argument('-d', '--swbasedir', help='katalog sw')
    ap.add_argument('-i', '--swinfo', help='ścieżka do pliku sw_info_....txt')
    ap.add_argument('-n', '--nrsw', help='numer sw')
    args = ap.parse_args()
    spprint.print_header('Argumenty')
    pprint.pprint(vars(args))
    spprint.print_footer('Argumenty')

    # deb
    # ap.print_help()
    # ap.print_usage()

    # utworzenie instancji klasy Teryt i Sytwys
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    t = teryt.Teryt()
    sw = sytwys.Sytwys()

    prompt = "Podaj dane do utworzenia podkatalogu w SW"
    nrWersji = dictConstants.dictConstants["NR_WERSJI"]
    title = "SytWys info " + nrWersji
    master = tk.Tk(screenName=prompt)
    master.title(title)
    master.geometry("1500x900+100+50")
    g = SytwysGUIgrid.SytwysGUIgrid(master, sw, t)

    # opracowanie argumentow z  linii   poleceń
    # - potrzebne,  zeby uzyskac info   o parametrach uruchomienia, np.:
    # - argument 1: katalog bieżący
    # ?> TO JEST PRAWDOPODOBNIE ZBĘDNE
    # -------------------------------------------------------
    # listaArg = sys.argv[0].split('" "')
    # dirBiezacy_fullPath = listaArg[0]
    # if dirBiezacy_fullPath[-1] == '"':
    #     dirBiezacy_fullPath = dirBiezacy_fullPath[0:len(dirBiezacy_fullPath) - 1]

    # ustalenie nru dla nowej roboty, albo uzycie przekazanego podczas
    # uruchomienia
    # ---------------------------------------------------------------------
    if args.tryb == 'nowa':
        sw.ustalNrSW(dictConstants.dictConstants["GC_DIR_LICZNIK"])
        # testowe wypełnienie kontrolek entry
        sw.sw_numer_str = str(sw.sw_numer)
        sw.sw_wykonawca = "kp"
        g.v_sw_numer.set(sw.sw_numer_str)
        g.v_sw_wykonawca.set(sw.sw_wykonawca)
        g.v_sw_obreb.set("Nowa Wieś-Kl")
        g.v_sw_dzialki.set("309, 310 3 , 2000/1, 4, ")
        g.v_sw_typ.set("mdcp")
        # g.v_sw_idZgl.set( "GKK.6640.X.2019")       # <== do likwidacji
        g.v_sw_idZgl_jrwa.set("GKK.6640")
        g.v_sw_idZgl_nr.set("")
        g.v_sw_idZgl_rok.set(get_RRRR())
        g.v_sw_ust5.set(1)
        g.v_sw_ust6.set(1)
        g.v_sw_skala.set("500")

        # stara wersja
        g.tx_mdcp_kp_uwagi1.insert(tk.END, sw.mdcp.kp_uwagi1)
        g.tx_mdcp_kp_uwagi2.insert(tk.END, sw.mdcp.kp_uwagi2)
        g.tx_mdcp_kp_uwagi3.insert(tk.END, sw.mdcp.kp_uwagi3)
        g.tx_mdcp_kp_uwagi4.insert(tk.END, sw.mdcp.kp_uwagi4)
        g.tx_mdcp_kp_uwagi5.insert(tk.END, sw.mdcp.kp_uwagi5)
        g.tx_mdcp_kp_uwagi6.insert(tk.END, sw.mdcp.kp_uwagi6)

        sw.sw_dir_nazwa = sw.sw_numer_str + "_" + sw.sw_wykonawca + "_"
        g.v_sw_dir_nazwa.set(sw.sw_dir_nazwa)
        sw_plikInfo_fullPath = ""
        sw_plikNr_nazwa = ""
        sw_plikNr_fullPath = ""
        sw_dzialka1 = ""
    else:
        sw.sw_numer = args.nrsw
        if not os.path.exists(args.swinfo):
            raise Exception
        g.wczytaj(plik_swinfo_path=args.swinfo)

    master.mainloop()
    # master.wait_window(master)
    # ---[   koniec pracy w  oknie   ]------------------------------------


if __name__ == "__main__":
    main()
