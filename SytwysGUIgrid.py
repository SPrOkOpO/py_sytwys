#-*- coding: windows-1250 -*-


from tkinter import filedialog
from tkinter import messagebox

import tkinter  as  tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import sys
#import teryt as ter
import datetime
import os
import re as re
from tkinter.constants import ACTIVE

import dictConstants
import OpracowaniePlanistyczne as oPlan
import sekcja

sys.path.append(r"i:\aPy\LibSP")
#sys.path.append(r"i:\aPy\LibSP\sytwys")
import kG_cele_pracy
import kGeodety
import spdatetime
import dzialki


class SytwysGUIgrid( tk.Frame):
    def __init__( self, master, sw, teryt):
        '''
            do konstruktora przekazuj� wska�niki:
            -   master: do nadrz�dnej ramki, czyli okna aplikacji;
            -   sw:     do obiektu klasy Sytwys;
            -   teryt:  do obiektu klasy Teryt;
            �eby z wn�trza klasy m�c si� odwo�ywac do p�l i metod obiekt�w
            sw i teryt
        '''
        super( SytwysGUIgrid, self).__init__(master)
        self.grid()

        self.master_frame = master
        self.sw = sw
        self.t = teryt
        self.oPlan = oPlan.OpracowaniePlanistyczne()
        self.godlaX = sekcja.ListaSekcji()
        self.rowGr1 = 0
        self.rowGr2 = self.rowGr1 + 16
        self.rowGr3 = self.rowGr1 + 9

        # font dla widget�w tekst
        # --------------------------------------------------------------------------
        self.font = tkFont.Font(family="Courier New", size=8)

        # zmienne tekstowe dla kontrolek    entry
        # --------------------------------------------------------------------------


        # zmienne zwi�zane z klas� Sytwys
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.v_sw_numer             = tk.StringVar()
        self.v_sw_wykonawca         = tk.StringVar()
        self.v_sw_typ               = tk.StringVar()
        self.v_sw_skala             = tk.StringVar()
        self.v_sw_obreb             = tk.StringVar()
        self.v_sw_obrebListBox      = tk.StringVar()
        self.v_sw_dzialki           = tk.StringVar()
        self.v_sw_idZgl_jrwa        = tk.StringVar()
        self.v_sw_idZgl_nr          = tk.StringVar()
        self.v_sw_idZgl_rok         = tk.StringVar()

        # dot. inwent.
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.v_sw_inw_obiekt        = tk.StringVar()
        self.v_sw_inw_obiektDoUwag  = tk.StringVar()
        self.v_sw_inw_nrZal         = tk.StringVar()
        self.v_sw_inw_decZnak       = tk.StringVar()
        self.v_sw_inw_decData       = tk.StringVar()

        self.v_sw_inw_obiekt.set(self.sw.inw.obiekt)
        self.v_sw_inw_obiektDoUwag.set(self.sw.inw.obiekt_do_uwag)
        self.v_sw_inw_nrZal.set(self.sw.inw.nr_zal)
        self.v_sw_inw_decZnak.set(self.sw.inw.dec_znak)
        self.v_sw_inw_decData.set(self.sw.inw.dec_data)

        # zmienne zwi�zane z klas� Teryt
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.v_sw_powiat_teryt      = tk.StringVar()
        self.v_sw_powiat_nazwa      = tk.StringVar()
        self.v_sw_jEw_teryt         = tk.StringVar()
        self.v_sw_jEw_nazwa         = tk.StringVar()
        self.v_sw_obreb_teryt       = tk.StringVar()
        self.v_sw_obreb_nazwa       = tk.StringVar()
        self.v_sw_obreb_dir         = tk.StringVar()
        self.v_sw_libre_wykon       = tk.StringVar()
        self.v_sw_libre_opis        = tk.StringVar()
        self.v_sw_dir_nazwa         = tk.StringVar()

        self.v_sw_mdcp_kp_uwagi1    = tk.StringVar()
        self.v_sw_mdcp_kp_uwagi2    = tk.StringVar()
        self.v_sw_mdcp_kp_uwagi3    = tk.StringVar()
        self.v_sw_mdcp_kp_uwagi4    = tk.StringVar()
        self.v_sw_mdcp_kp_uwagi5    = tk.StringVar()
        self.v_sw_mdcp_kp_uwagi6    = tk.StringVar()

        self.v_sw_typ.set("mdcp")
        self.v_sw_ust5              = tk.IntVar()
        self.v_sw_ust6              = tk.IntVar()
        self.v_sw_ust5_str          = tk.StringVar()
        self.v_sw_ust6_str          = tk.StringVar()

        self.GC_DIR_SYTWYS = "t:\\sytwys\\"
        self.GC_DIR_LICZNIK = "t:\\sytwys\\AAB__licznik\\"

        self.dicWierszePliku = {}

        # 6 ramek
        # LTop      RTop
        # LMiddle   RMiddle
        # LBottom   RBottom
        self.frameTL = tk.Frame( master, bg="thistle1")
        self.frameML = tk.Frame( master, bg="khaki")
        self.frameBL = tk.Frame( master, bg="thistle3")

        self.frameTL.grid( row=0, column=0, sticky="W")
        self.frameML.grid( row=1, column=0, sticky="W")
        self.frameBL.grid( row=2, column=0, sticky="W")

        self.frameTR = tk.Frame( master)
        self.frameMR = tk.Frame( master)
        self.frameTR.grid( row=0, column=5, sticky="NW")
        self.frameMR.grid( row=1, column=5, sticky="NW")


        '''
        self.tx_mdcp_kp_uwagi1
        self.tx_mdcp_kp_uwagi2
        self.tx_mdcp_kp_uwagi3
        self.tx_mdcp_kp_uwagi4
        self.tx_mdcp_kp_uwagi5
        '''

        self.createWidgets_frameTL()
        self.createWidgets_frameML()
        self.createWidgets_frameBL()
        self.createWidgets_frameTR()
        self.createWidgets_frameMR()
        # self.createWidgets_frameBR()

        # self.inicjuj()
        # self.wczytaj()

    def eventHandler_entry_obreb(self, event):
        # wyczyszczenie powi�zanego ListBoxu
        lista = ""
        self.v_sw_obrebListBox.set( lista)

        obr = self.v_sw_obreb.get()
        # obr = self.e3.get()
        if len( obr) >= 3:
            print("event + tekst %s" % (obr))
            '''
            if obr in self.t.dictObr_nazwaObrWpisana2teryt:
                print( "Obr�b %s jest w s�owniku" % ( obr))
            else:
                print( "Obr�bu %s NIE MA w s�owniku" % ( obr))
            '''
            liczbaKluczy = 0
            lista = ""
            listaTerytow = []
            for k in self.t.dictObr_nazwaObrWpisana2teryt.keys():
                # print( "k=%s" % ( k))
                # klucz = "XXX"
                klucz = k[0:len( obr)]
                if klucz == obr:
                    liczbaKluczy += 1
                    print("klucz %i: %s, teryt: %s" % (liczbaKluczy, obr, self.t.dictObr_nazwaObrWpisana2teryt[k]))
                    listaTerytow.append(self.t.dictObr_nazwaObrWpisana2teryt[k])

            # print( "event + obrCzesc: %s, liczba kluczy: %i" % ( obr, liczbaKluczy))


            listaTerytow.sort()
            listaUnikalnych = []
            for teryt in listaTerytow:
                if teryt in listaUnikalnych:
                    pass
                else:
                    listaUnikalnych.append( teryt)
            for teryt in listaUnikalnych:
                lista = lista + " " + teryt
            self.v_sw_obrebListBox.set( lista)

    def eventHandler_entry_wykonawca(self, event):
        """
        >> usun�� ten eventHandler - ma dzia�ac odwrotny
        """
        wykonawca = self.v_sw_wykonawca.get()
        if wykonawca == "kh":
            self.v_sw_typ.set( "mppn")

    def eventHandler_combobox_celpracy(self, event):
        celpracy = self.v_sw_typ.get()
        if celpracy in ['inw', 'mdcp']:
            self.v_sw_wykonawca.set('kp')
        else:
            self.v_sw_wykonawca.set('kh')

    def createWidgets_frameTL(self):
        #self.rowGr1 = 0
        lab_sw_numer            = tk.Label( self.frameTL, text="Nr "            , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 0)
        lab_sw_wykonawca        = tk.Label( self.frameTL, text="Wykonawca"      , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 1)
        lab_sw_typ              = tk.Label( self.frameTL, text="Typ"            , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 2)
        lab_sw_skala            = tk.Label( self.frameTL, text="Skala (mian.)"  , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 3)
        lab_sw_obreb            = tk.Label( self.frameTL, text="Obreb "         , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 4)
        lab_sw_obrebLBox        = tk.Label( self.frameTL, text="Obreb - teryty" , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 5)
        lab_sw_dzialki          = tk.Label( self.frameTL, text="Dzialki "       , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 6)
        lab_sw_idZgl            = tk.Label( self.frameTL, text="IdZgl "         , anchor="w", width=20).grid(column=0, row=self.rowGr1 + 8)

        e1  = tk.Entry( self.frameTL, justify="left",   width=10    , textvariable  = self.v_sw_numer       , bg="greenyellow")
        e2  = tk.Entry( self.frameTL, justify="left",   width=10    , textvariable  = self.v_sw_wykonawca   )
        # zb�dny: e2.bind( "<FocusOut>", self.eventHandler_entry_wykonawca)

        # typ
        # ttyp = ( "mdcp", "inw", "podz", "inny") <-- tak by�o przed kG...
        combobox = ttk.Combobox(self.frameTL, textvariable=self.v_sw_typ, state="readonly",
                                values=kG_cele_pracy.kG_cele_pracy)
                                #  postcommand=self.eventHandler_combobox_celpracy)
                                #, label_text="Typ"
                                #, labelpos="wn", listbox_width=8, dropdown=0, \
                                #scrolledlist_items=ttyp)
        # combobox["values"] = ttyp
        #combobox.bind("<FocusOut>", self.eventHandler_combobox_celpracy)
        combobox.bind('<<ComboboxSelected>>', self.eventHandler_combobox_celpracy)

        e7  = tk.Entry( self.frameTL, justify="left",   width=10    , textvariable  = self.v_sw_skala       )

        # entry OBR�B
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # -
        self.e3 = tk.Entry( self.frameTL, justify="left",   width=40    , textvariable  = self.v_sw_obreb       )
        # e3.bind('<Button-1>', self.eventHandler_entry_obreb)
        self.e3.bind('<Key>', self.eventHandler_entry_obreb)

        # listBox dla obr�b�w
        self.listBox_obr = tk.Listbox( self.frameTL, height=4, width=15, listvariable=self.v_sw_obrebListBox)

        e4  = tk.Entry( self.frameTL, justify="left",   width=60 , textvariable = self.v_sw_dzialki )
        # e5 = tk.Entry( self.frameTL, justify="left",   width=10    , textvariable  = self.v_sw_typ     )

        # id Zg�
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # do likwidacji:
        # e6 = tk.Entry( self.frameTL, justify="left",   width=40    , textvariable  = self.v_sw_idZgl       )
        e6_1    = tk.Entry( self.frameTL, justify="left",   width=15 , textvariable = self.v_sw_idZgl_jrwa  )
        e6_2    = tk.Entry( self.frameTL, justify="left",   width=6 , textvariable  = self.v_sw_idZgl_nr        )
        e6_3    = tk.Entry( self.frameTL, justify="left",   width=6 , textvariable  = self.v_sw_idZgl_rok   )

        e1.grid(            row=self.rowGr1 + 0, column=1, sticky="W")
        e2.grid(            row=self.rowGr1 + 1, column=1, sticky="W")
        combobox.grid(      row=self.rowGr1 + 2, column=1, sticky="W")

        e7.grid(            row=self.rowGr1 + 3, column=1, sticky="W")
        self.e3.grid(       row=self.rowGr1 + 4, column=1, sticky="W")
        self.listBox_obr.grid(  row=self.rowGr1 + 5, column=1, sticky="W", columnspan=4)

        e4.grid(            row=self.rowGr1 + 6, column=1, sticky="W", columnspan=4)
        # e5.grid(   row=rowGr1 + 22, column=1, sticky="W")
        # e6.grid(   row=self.rowGr1 + 6, column=1, sticky="W")
        e6_1.grid(          row=self.rowGr1 + 8, column=1, sticky="W")
        e6_2.grid(          row=self.rowGr1 + 8, column=2, sticky="W")
        e6_3.grid(          row=self.rowGr1 + 8, column=3, sticky="W")


        # self.v_sw_ust6.set = 1
        lab_tx_mdcp_kp_ust56    = tk.Label( self.frameTL, text="� 16 pkt 1"    , anchor="w", width=20).grid(row=self.rowGr1 + 7, sticky="W")
        for etykieta, row, col, status, variable in [
                ("dane spe�niaj� wymogi", 7, 1, tk.NORMAL, self.v_sw_ust5),
                ("ust. 6", 7, 2, tk.DISABLED, self.v_sw_ust6)
                ]:
            tk.Checkbutton( self.frameTL, text=etykieta, variable=variable, state=status).grid( row=row, column=col, sticky="W")

        # kontrolki zwi�zane z inwentaryzacj�
        # self.rowGr3 = self.rowGr1 + 8
        lab_sw_inw_obiekt       = tk.Label( self.frameTL, text="inw_obiekt "    , anchor="w", width=20).grid(row=self.rowGr3 + 0)
        lab_sw_inw_obiektDoUwag = tk.Label( self.frameTL, text="inw_obiekt do uwag "    , anchor="w", width=20).grid(row=self.rowGr3 + 1)
        lab_sw_inw_nrZal        = tk.Label( self.frameTL, text="inw_nrZal   "   , anchor="w", width=20).grid(row=self.rowGr3 + 2)
        lab_sw_inw_decZnak      = tk.Label( self.frameTL, text="inw_decZnak"    , anchor="w", width=20).grid(row=self.rowGr3 + 3)
        lab_sw_inw_decData      = tk.Label( self.frameTL, text="inw_decData"    , anchor="w", width=20).grid(row=self.rowGr3 + 4)

        e_sw_inw_obiekt         = tk.Entry( self.frameTL,   justify="left", width=60, textvariable  = self.v_sw_inw_obiekt          , bg="white")
        e_sw_inw_obiektDoUwag   = tk.Entry( self.frameTL,   justify="left", width=60, textvariable  = self.v_sw_inw_obiektDoUwag    , bg="white")
        e_sw_inw_nrZal          = tk.Entry( self.frameTL,   justify="left", width=10, textvariable  = self.v_sw_inw_nrZal           , bg="white")
        e_sw_inw_decZnak        = tk.Entry( self.frameTL,   justify="left", width=40, textvariable  = self.v_sw_inw_decZnak         , bg="white")
        e_sw_inw_decData        = tk.Entry( self.frameTL,   justify="left", width=40, textvariable  = self.v_sw_inw_decData         , bg="white")

        e_sw_inw_obiekt.grid        ( row=self.rowGr3 + 0, column=1, sticky="W", columnspan=4)
        e_sw_inw_obiektDoUwag.grid  ( row=self.rowGr3 + 1, column=1, sticky="W", columnspan=4)
        e_sw_inw_nrZal.grid     ( row=self.rowGr3 + 2, column=1, sticky="W", columnspan=4)
        e_sw_inw_decZnak.grid   ( row=self.rowGr3 + 3, column=1, sticky="W", columnspan=4)
        e_sw_inw_decData.grid   ( row=self.rowGr3 + 4, column=1, sticky="W")

    def createWidgets_frameML(self):
        # self.rowGr2 = self.rowGr1 + 9

        lab_sw_powiat_teryt = tk.Label( self.frameML, text="Powiat teryt"   , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 0)
        lab_sw_powiat_nazwa = tk.Label( self.frameML, text="powiat_nazwa"   , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 1)
        lab_sw_jEw_teryt    = tk.Label( self.frameML, text="jEw_teryt"      , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 2)
        lab_sw_jEw_nazwa    = tk.Label( self.frameML, text="jEw_nazwa"      , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 3)
        lab_sw_obreb_teryt  = tk.Label( self.frameML, text="obreb_teryt"    , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 4)
        lab_sw_obreb_nazwa  = tk.Label( self.frameML, text="obreb_nazwa "   , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 5)
        lab_sw_obreb_dir    = tk.Label( self.frameML, text="obreb_dir"      , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 6)

        lab_sw_libre_wykon  = tk.Label( self.frameML, text="libre wykon "   , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 7)
        lab_sw_libre_opis   = tk.Label( self.frameML, text="libre opis "    , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 8)
        lab_sw_dir_nazwa    = tk.Label( self.frameML, text="dir nazwa"      , anchor="w", width=20).grid(column=0, row=self.rowGr2 + 9)

        # definicje kontrolek entry
        e_sw_powiat_teryt    = tk.Entry( self.frameML, justify="left", width=20, textvariable  = self.v_sw_powiat_teryt,   bg="chartreuse2")
        e_sw_powiat_nazwa    = tk.Entry( self.frameML, justify="left", width=40, textvariable  = self.v_sw_powiat_nazwa,   bg="greenyellow")
        e_sw_jEw_teryt       = tk.Entry( self.frameML, justify="left", width=20, textvariable  = self.v_sw_jEw_teryt    ,  bg="chartreuse2")
        e_sw_jEw_nazwa       = tk.Entry( self.frameML, justify="left", width=40, textvariable  = self.v_sw_jEw_nazwa    ,  bg="greenyellow")
        e_sw_obreb_teryt     = tk.Entry( self.frameML, justify="left", width=20, textvariable  = self.v_sw_obreb_teryt ,   bg="chartreuse2")
        e_sw_obreb_nazwa     = tk.Entry( self.frameML, justify="left", width=40, textvariable  = self.v_sw_obreb_nazwa ,   bg="greenyellow")
        e_sw_obreb_dir       = tk.Entry( self.frameML, justify="left", width=40, textvariable  = self.v_sw_obreb_dir    ,  bg="turquoise3")

        e_sw_libre_wykon     = tk.Entry( self.frameML, justify="left", width=10, textvariable  = self.v_sw_libre_wykon, bg="turquoise")
        e_sw_libre_opis      = tk.Entry( self.frameML, justify="left", width=60, textvariable  = self.v_sw_libre_opis  , bg="turquoise")
        e_sw_dir_nazwa       = tk.Entry( self.frameML, justify="left", width=60, textvariable  = self.v_sw_dir_nazwa   , bg="navajowhite")

        e_sw_powiat_teryt.grid(row=self.rowGr2 + 0, column=1,  sticky="W")
        e_sw_powiat_nazwa.grid(row=self.rowGr2 + 1, column=1,  sticky="W")
        e_sw_jEw_teryt.grid(   row=self.rowGr2 + 2, column=1,  sticky="W")
        e_sw_jEw_nazwa.grid(   row=self.rowGr2 + 3, column=1,  sticky="W")
        e_sw_obreb_teryt.grid( row=self.rowGr2 + 4, column=1,  sticky="W")
        e_sw_obreb_nazwa.grid( row=self.rowGr2 + 5, column=1,  sticky="W")
        e_sw_obreb_dir.grid(   row=self.rowGr2 + 6, column=1,  sticky="W")

        e_sw_libre_wykon.grid(  row=self.rowGr2 +  7, column=1, sticky="W")
        e_sw_libre_opis.grid(   row=self.rowGr2 +  8, column=1, sticky="W", columnspan=4)
        e_sw_dir_nazwa.grid(    row=self.rowGr2 +  9, column=1, sticky="W", columnspan=4)


    def createWidgets_frameBL( self):
        butNowaRobota  = tk.Button( self.frameBL, text='Nowa robota',  width =15, command=self.nowaRobota)
        butInicjuj  = tk.Button( self.frameBL, text='Inicjuj',  width =15, command=self.inicjuj)
        butWczytaj  = tk.Button( self.frameBL, text='Wczytaj swInfo',   width =15, command=self.wczytaj)
        butOK       = tk.Button( self.frameBL, text='Zapisz swInfo',        width =15, command=self.zapisz)
        butCancel   = tk.Button( self.frameBL, text='Zako�cz',  width =15,  command=self.btn_rezygnacja, bg="salmon")
        butNowaRobota.grid( row=0, column=0, pady=2, columnspan=1)
        butInicjuj.grid(    row=0, column=1, pady=2, columnspan=1)
        butOK.grid(         row=1, column=1, pady=3, columnspan=1)
        butWczytaj.grid(    row=0, column=2, pady=4, columnspan=1)
        butCancel.grid(     row=1, column=2, pady=4, columnspan=1)


    def createWidgets_frameTR(self):
        lab_tx_sekcje = tk.Label(   self.frameTR, text="sekcje:"    , anchor="w", width=20).grid(row=0, column=0, sticky="W")

        butSekcje   = tk.Button( self.frameTR, text='Gen sekcje',   width =15,  command=self.btn_gen_sekcje, bg="salmon")
        butSekcje.grid( row=0, column=1, pady=0, columnspan=1)

        self.tx_sekcje          = tk.Text( self.frameTR, height=7, width=100, tabs=3, font=self.font)
        self.tx_sekcje.grid     ( row=1, column=0, sticky="W", columnspan=3)


    def createWidgets_frameMR(self):
        lab_tx_mdcp_kp_uwagi    = tk.Label( self.frameMR, text="mdcp_kp_uwagi:" , anchor="w", width=20).grid(row=1, column=0, sticky="W")

        butUwagi1   = tk.Button( self.frameMR, text='Gen u1',   width =15,  command=self.btn_gen_uwagi1, bg="salmon")
        butUwagi2   = tk.Button( self.frameMR, text='Gen u2',   width =15,  command=self.btn_gen_uwagi2, bg="salmon")
        butUwagi3   = tk.Button( self.frameMR, text='Gen u3',   width =15,  command=self.btn_gen_uwagi3, bg="salmon")
        butUwagi1.grid( row=1, column=1, pady=0, columnspan=1)
        butUwagi2.grid( row=1, column=2, pady=0, columnspan=1)
        butUwagi3.grid( row=1, column=3, pady=0, columnspan=1)

        self.tx_mdcp_kp_uwagi1      = tk.Text( self.frameMR, height=6, width=100, tabs=3, font=self.font)
        '''
        lab_tx_mdcp_kp_ust56    = tk.Label( self.frameMR, text="mdcp_kp_ust. 5 i 6:"    , anchor="w", width=20).grid(row=2, sticky="W")
        for etykieta, row, col, status, variable in [ \
            ( "5", 3, 0, tk.NORMAL, v_sw_ust5), ( "6", 3, 1, tk.NORMAL, v_sw_ust6) \
            ]:
            tk.Checkbutton( self.frameMR, text=etykieta, variable=variable, state=status).grid( row=row, column=col, sticky="W")
        '''
        self.tx_mdcp_kp_uwagi2      = tk.Text( self.frameMR, height=6, width=100, tabs=3, font=self.font)
        self.tx_mdcp_kp_uwagi3      = tk.Text( self.frameMR, height=3, width=100, tabs=3, font=self.font)
        self.tx_mdcp_kp_uwagi3.tag_configure('Arial8', font=('Arial', 8))
        self.tx_mdcp_kp_uwagi3.tag_configure('bold_italics', font=('Arial', 16, 'bold', 'italic'))
        self.tx_mdcp_kp_uwagi3.tag_add( 'bold_italics', 1.0, tk.END)
        self.tx_mdcp_kp_uwagi3.tag_add( 'Arial8', 1.0, tk.END)
        # self.tx_mdcp_kp_uwagi3.tag_configure( 'bold_italics', font= 'Arial, 8, bold, italic')
        # self.tx_mdcp_kp_uwagi3.tag_configure( font='Arial, 8, bold')

        self.tx_mdcp_kp_uwagi4      = tk.Text( self.frameMR, height=8, width=100, tabs=3, font=self.font)
        self.tx_mdcp_kp_uwagi5      = tk.Text( self.frameMR, height=2, width=100, tabs=3, font=self.font)
        self.tx_mdcp_kp_uwagi5.tag_configure('bold_italics', font=('Arial', 16, 'bold', 'italic'))
        self.tx_mdcp_kp_uwagi5.tag_add( 'bold_italics', 1.0, tk.END)
        self.tx_mdcp_kp_uwagi6      = tk.Text( self.frameMR, height=2, width=100, tabs=3, font=self.font)

        self.tx_mdcp_kp_uwagi1.grid ( row=2, column=0, sticky="W", columnspan=4)
        self.tx_mdcp_kp_uwagi2.grid ( row=3, column=0, sticky="W", columnspan=4)
        self.tx_mdcp_kp_uwagi3.grid ( row=4, column=0, sticky="W", columnspan=4)
        self.tx_mdcp_kp_uwagi4.grid ( row=5, column=0, sticky="W", columnspan=4)
        self.tx_mdcp_kp_uwagi5.grid ( row=6, column=0, sticky="W", columnspan=4)
        self.tx_mdcp_kp_uwagi6.grid ( row=7, column=0, sticky="W", columnspan=4)

    def nowaRobota(self):
        '''
        skanuje katalog z plikami licznika i ustala numer dla nowej roboty
        -   ma zastosowanie w przypadku rejestracji kilku rob�t po kolei - nie trzeba uruchamiac
            programu dla kazdej roboty
        '''
        self.sw.ustalNrSW(dictConstants.dictConstants["GC_DIR_LICZNIK"])
        self.sw.sw_numer_str = str(self.sw.sw_numer)
        self.v_sw_numer.set(self.sw.sw_numer_str)

    def odczytaj_dane_z_gui(self):
        """
        pobiera dane z gui i zapisuje w odpowiednich polach
        """

        self.sw.sw_numer = self.v_sw_numer.get()
        self.sw.sw_wykonawca = self.v_sw_wykonawca.get()
        self.sw.sw_typ = self.v_sw_typ.get()
        self.sw.sw_skala = self.v_sw_skala.get()

        # tu ma by� obr�b
        # cho� na razie nie ma, a chyba dzia�a dobrze

        # oczyszczenie i posortowanie dzia�ek i wype�nienie p�l dot. dzia�ek
        self.sw.sw_dzialki_obj.source_string_nr = self.v_sw_dzialki.get()
        self.sw.sw_dzialki_obj.init_instance()
        self.sw.update_dzialki(self.t.terytF_obr, self.t.teryt_jew, self.t.nazwa_obr)
        self.v_sw_dzialki.set(self.sw.sw_dzialki_obj.sorted_string_nr_prz_sp)

        # zast�pi� jednym ChBoxem "spe�niaj�"
        self.sw.mdcp.ust5 = "%s" % self.v_sw_ust5.get()
        self.sw.mdcp.ust6 = "%s" % self.v_sw_ust6.get()

        # id zg�.
        self.sw.sw_idZgl_jrwa = self.v_sw_idZgl_jrwa.get()
        self.sw.sw_idZgl_nr = self.v_sw_idZgl_nr.get()
        self.sw.sw_idZgl_rok = self.v_sw_idZgl_rok.get()
        self.sw.sw_idZgl = '.'.join([self.v_sw_idZgl_jrwa.get(), self.v_sw_idZgl_nr.get(), self.v_sw_idZgl_rok.get()])

        # dane dot. inwentaryzacji
        if self.v_sw_typ.get() == "inw":
            # old ver
            # self.sw.sw_inw_obiekt       = self.v_sw_inw_obiekt.get()
            # self.sw.sw_inw_obiektDoUwag = self.v_sw_inw_obiektDoUwag.get()
            # self.sw.sw_inw_nrZal        = self.v_sw_inw_nrZal.get()
            # self.sw.sw_inw_decZnak      = self.v_sw_inw_decZnak.get()
            # self.sw.sw_inw_decData      = self.v_sw_inw_decData.get()
            # new ver - obiekt Inwentaryzacja
            self.sw.inw.obiekt         = self.v_sw_inw_obiekt.get()
            self.sw.inw.obiekt_do_uwag = self.v_sw_inw_obiektDoUwag.get()
            self.sw.inw.nr_zal         = self.v_sw_inw_nrZal.get()
            self.sw.inw.dec_znak       = self.v_sw_inw_decZnak.get()
            self.sw.inw.dec_data       = self.v_sw_inw_decData.get()
        else:
            # new
            self.sw.inw.set_empty()
            self.v_sw_inw_obiekt.set        (self.sw.inw.obiekt        )
            self.v_sw_inw_obiektDoUwag.set  (self.sw.inw.obiekt_do_uwag)
            self.v_sw_inw_nrZal.set         (self.sw.inw.nr_zal        )
            self.v_sw_inw_decZnak.set       (self.sw.inw.dec_znak      )
            self.v_sw_inw_decData.set       (self.sw.inw.dec_data      )

        # dane do excela - cz�� teryt
        self.t.terytF_pow = self.v_sw_powiat_teryt.get()
        self.t.nazwa_pow = self.v_sw_powiat_nazwa.get()
        self.t.terytF_jew = self.v_sw_jEw_teryt.get()
        self.t.nazwa_jew = self.v_sw_jEw_nazwa.get()
        self.t.terytF_obr = self.v_sw_obreb_teryt.get()
        self.t.nazwa_obr = self.v_sw_obreb_nazwa.get()

        self.v_sw_obreb_dir.set( self.t.nazwaDir_obr)
        # dane do excela - cz�� libre
        self.sw.sw_obrebDir = self.v_sw_obreb_dir.get()
        self.sw.sw_libre_wykon = self.v_sw_libre_wykon.get()
        self.sw.sw_libre_opis = self.v_sw_libre_opis.get()
        self.sw.sw_dir_nazwa = self.v_sw_dir_nazwa.get()

        # sekcje i uwagi
        self.sw.sw_sekcje_tytul = self.tx_sekcje.get( 1.0, tk.END)
        self.sw.mdcp.kp_uwagi1 = self.tx_mdcp_kp_uwagi1.get( 1.0, tk.END)
        self.sw.mdcp.kp_uwagi2 = self.tx_mdcp_kp_uwagi2.get( 1.0, tk.END)
        self.sw.mdcp.kp_uwagi3 = self.tx_mdcp_kp_uwagi3.get( 1.0, tk.END)
        self.sw.mdcp.kp_uwagi4 = self.tx_mdcp_kp_uwagi4.get( 1.0, tk.END)
        self.sw.mdcp.kp_uwagi5 = self.tx_mdcp_kp_uwagi5.get( 1.0, tk.END)
        self.sw.mdcp.kp_uwagi6 = self.tx_mdcp_kp_uwagi6.get( 1.0, tk.END)

    def inicjuj(self):
        '''
        na  podstawie wprowadzonych danych wype�nia odpowiednie pola

        1)  najpierw ustalenie wybranego obr�bu
            (jest to jednocze�nie inicjalizacja p�l terytu i nazw p/g/o)
            -   sprawdzenie, czy obr�b jest wpisany jednoznacznie
                a)  to sprawdzenie odbywa si� poprzez ustalenie liczby teryt�w
                    w ListBoxie obr�bu
                -   je�eli jest jeden teryt, to nie trzeba nic robi�
                b)  je�eli jest wi�cej ni� jeden teryt, to trzeba pobra� teryt
                    wybrany w ListBoxie, a je�eli �aden nie jest wybrany, to wy�wietli�
                    MsgBox z wezwaniem do usera

        NIE TWORZY KATALOGU s-w! To robi funkcja zapisz().
        '''

        # 1a,b)
        if self.listBox_obr.size() > 1:
            obrTerytFull = self.listBox_obr.get(ACTIVE)
            if len( obrTerytFull) < 3:
                tk.messagebox.showinfo("Err", "Wska� teryt obr�bu w ListBoxie!")

            # obrNazwa = self.t.dictObr_teryt2nazwa[ obrTerytFull]
        else:
            obrTerytFull = self.t.dictObr_nazwaObrWpisana2teryt[ self.v_sw_obreb.get()]

        # 1)
        if self.t.setTerytyFrom_obrTerytFull(obrTerytFull) != 0:
            tk.messagebox.showinfo("Err", "Inicjacja nieudana - b��dny obr�b")
            return -1

        # self.sw.sw_plikInfo_fullPath
        global sw_plikNr_fullPath
        global sw_plikNr_nazwa

        self.sw.sw_wykonawca = self.v_sw_wykonawca.get()

        # oczyszczenie i posortowanie dzia�ek i wype�nienie p�l dot. dzia�ek
        self.sw.sw_dzialki_obj.source_string_nr = self.v_sw_dzialki.get()
        self.sw.sw_dzialki_obj.init_instance()
        self.sw.update_dzialki(self.t.terytF_obr, self.t.teryt_jew, self.t.nazwa_obr)
        self.v_sw_dzialki.set(self.sw.sw_dzialki_obj.sorted_string_nr_prz_sp)

        self.sw.sw_typ              = self.v_sw_typ.get()
        self.sw.sw_idZgl            = '.'.join([self.v_sw_idZgl_jrwa.get(), self.v_sw_idZgl_nr.get(), self.v_sw_idZgl_rok.get()])
        self.sw.sw_skala            = self.v_sw_skala.get()
        self.sw.mdcp.ust5        = "%s" % self.v_sw_ust5.get()
        self.sw.mdcp.ust6        = "%s" % self.v_sw_ust6.get()

        print ( "self.sw.mdcp.ust5 = " + self.sw.mdcp.ust5)
        print ( "self.sw.mdcp.ust6 = " + self.sw.mdcp.ust6)

        if self.v_sw_typ.get() == "inw":
            # old ver
            # self.sw.sw_inw_obiekt       = self.v_sw_inw_obiekt.get()
            # self.sw.sw_inw_obiektDoUwag = self.v_sw_inw_obiektDoUwag.get()
            # self.sw.sw_inw_nrZal        = self.v_sw_inw_nrZal.get()
            # self.sw.sw_inw_decZnak      = self.v_sw_inw_decZnak.get()
            # self.sw.sw_inw_decData      = self.v_sw_inw_decData.get()
            # new ver - obiekt Inwentaryzacja
            self.sw.inw.obiekt         = self.v_sw_inw_obiekt.get()
            self.sw.inw.obiekt_do_uwag = self.v_sw_inw_obiektDoUwag.get()
            self.sw.inw.nr_zal         = self.v_sw_inw_nrZal.get()
            self.sw.inw.dec_znak       = self.v_sw_inw_decZnak.get()
            self.sw.inw.dec_znak       = self.v_sw_inw_decData.get()
        else:
            # new
            self.sw.inw.set_empty()
            # old
            # self.sw.sw_inw_obiekt       = ""
            # self.sw.sw_inw_obiektDoUwag = ""
            # self.sw.sw_inw_nrZal        = ""
            # self.sw.sw_inw_decZnak      = ""
            # self.sw.sw_inw_decData      = ""

            self.v_sw_inw_obiekt.set      (self.sw.inw.obiekt        )
            self.v_sw_inw_obiektDoUwag.set(self.sw.inw.obiekt_do_uwag)
            self.v_sw_inw_nrZal.set       (self.sw.inw.nr_zal        )
            self.v_sw_inw_decZnak.set     (self.sw.inw.dec_znak      )
            self.v_sw_inw_decData.set     (self.sw.inw.dec_data      )

        self.sw.sw_libre_wykon = self.sw.sw_numer_str + self.sw.sw_wykonawca
        self.sw.sw_libre_opis = self.t.nazwaDir_obr + " dz. " + self.sw.sw_dzialka1
        if self.v_sw_typ.get() == "inw":
            self.sw.sw_libre_opis = self.sw.sw_libre_opis + " " + "inw"
        elif self.v_sw_typ.get() == 'imdcp-ws':
            self.sw.sw_libre_opis = self.sw.sw_libre_opis + " " + "wykSyn"

        # obr_terytFull  = dictObr_nazwaObrWpisana2teryt[    self.v_sw_obreb.get()]
        # self.t.terytFull = obr_terytFull
        # print( "obr_terytFull=" +  obr_terytFull)
        # print( "dictObr_teryt2nazwaDir[    obr_terytFull]=" + dictObr_teryt2nazwaDir[ obr_terytFull])

        # nazwa obr. do nazwy katalogu
        self.sw.sw_obrebDir = self.t.nazwaDir_obr
        tytstr = self.sw.sw_wykonawca + "_" + self.get_RRMM() + "_" + self.t.nazwaDir_obr
        tytstr = tytstr + "_" + self.sw.sw_dzialka1
        if self.v_sw_typ.get() == "inw":
            tytstr = tytstr + "_" + "inw"
        if self.v_sw_typ.get() == 'imdcp-ws':
            tytstr = tytstr + "_" + "wykSyn"
        self.sw.sw_dir_nazwa = self.GC_DIR_SYTWYS + self.sw.sw_numer_str + "_" + tytstr
        if not os.path.exists(self.sw.sw_plikInfo_fullPath):
            self.sw.sw_plikInfo_fullPath = self.sw.sw_dir_nazwa + "\\sw_" + self.sw.sw_numer_str + "_info.txt"
            self.sw.sw_plikNr_nazwa = self.sw.sw_numer_str + "___" + tytstr
            self.sw.sw_plikNr_fullPath = self.GC_DIR_LICZNIK + self.sw.sw_plikNr_nazwa + ".nr"
        print("1 sw_dir_nazwa=" + self.sw.sw_dir_nazwa)
        print("1 sw_plikInfo_fullPath=" + self.sw.sw_plikInfo_fullPath)
        print("1 sw_plikNr_fullPath=" + self.sw.sw_plikNr_fullPath)

        # wype�nienie kontrolek entry   aktualnymi danymi
        # - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   -
        # teryty    i nazwy
        self.v_sw_powiat_teryt.set( self.t.terytF_pow)
        self.v_sw_jEw_teryt.set( self.t.terytF_jew)
        self.v_sw_obreb_teryt.set( self.t.terytF_obr)

        self.v_sw_powiat_nazwa.set( self.t.nazwa_pow)
        self.v_sw_jEw_nazwa.set( self.t.nazwa_jew)
        self.v_sw_obreb_nazwa.set( self.t.nazwa_obr)

        self.v_sw_obreb_dir.set( self.t.nazwaDir_obr)

        # libre
        self.v_sw_libre_wykon.set(self.sw.sw_libre_wykon)
        self.v_sw_libre_opis.set(self.sw.sw_libre_opis)

        # �ciezka dir
        self.v_sw_dir_nazwa.set(self.sw.sw_dir_nazwa)

        self.sw.inicjujStrukture(self.sw.sw_dir_nazwa)   # old
        self.sw.struktura_sw.sw_dir_abspath = self.sw.sw_dir_nazwa
        self.sw.struktura_sw.inicjujStrukture() # new
        self.sw.struktura_sw.deb_listujStrukture()

    def btn_rezygnacja(self):
        # print( "Rezygnacja")
        self.master_frame.destroy
        sys.exit()

    def zapisz(self):
        self.odczytaj_dane_z_gui()
        self.zapisz_1()

    def zapisz_1(self):
        """
        -   tworzy katalog s-w
        -   wype�nia go struktur� s-w
        -   tworzy i otwiera plik sw_NNN_info.txt
        -   zapisuje do niego:
            -   dane teryt - wszystkie pola klasy (opr�cz s�ownik�w oczywi�cie)
            -   dane sw

        """

        # aktualizacja list dzia�ek
        self.sw.update_dzialki(self.t.terytF_obr, self.t.teryt_jew, self.t.nazwa_obr)

        # global sw_plikInfo_fullPath
        global sw_plikNr_fullPath
        global sw_plikNr_nazwa

        # utworzenie katalogu w GC_DIR_SYTWYS - je�eli nie istnieje
        if not os.path.exists(self.sw.sw_plikInfo_fullPath):
            print("sw_dir_nazwa=" + self.sw.sw_dir_nazwa)
            print("sw_plikInfo_fullPath=" + self.sw.sw_plikInfo_fullPath)
            # os.mkdir( sw_dir_nazwa, 0777)
            os.makedirs(self.sw.sw_dir_nazwa)
            self.sw.utworzStrukture()
            # os.path.isdir("C:\First\Second\Third")
            f = open(self.sw.sw_plikNr_fullPath,   "w")
            f.write(self.sw.sw_plikNr_nazwa)
            f.close()

        # zapisanie danych do pliku sw_*_info.txt
        with open(self.sw.sw_plikInfo_fullPath, "w") as f:

            # dane klasy Teryt
            f.write("[t_terytFull]=" + self.t.terytFull + "\n")
            f.write("[t_terytF_woj]=" + self.t.terytF_woj + "\n")
            f.write("[t_terytF_pow]=" + self.t.terytF_pow + "\n")
            f.write("[t_terytF_jew]=" + self.t.terytF_jew + "\n")
            f.write("[t_terytF_obr]=" + self.t.terytF_obr + "\n")

            f.write("[t_teryt_woj]=" + self.t.teryt_woj + "\n")
            f.write("[t_teryt_pow]=" + self.t.teryt_pow + "\n")
            f.write("[t_teryt_jew]=" + self.t.teryt_jew + "\n")
            f.write("[t_teryt_obr]=" + self.t.teryt_obr + "\n")

            f.write("[t_nazwa_woj]=" + self.t.nazwa_woj + "\n")
            f.write("[t_nazwa_pow]=" + self.t.nazwa_pow + "\n")
            f.write("[t_nazwa_jew]=" + self.t.nazwa_jew + "\n")
            f.write("[t_nazwa_obr]=" + self.t.nazwa_obr + "\n")

            f.write("[t_nazwa_uStn_woj]=" + self.t.nazwa_uStn_woj + "\n")
            f.write("[t_nazwa_uStn_pow]=" + self.t.nazwa_uStn_pow + "\n")
            f.write("[t_nazwa_uStn_jew]=" + self.t.nazwa_uStn_jew + "\n")
            f.write("[t_nazwa_uStn_obr]=" + self.t.nazwa_uStn_obr + "\n")

            f.write("[t_nazwaDir_obr]=" + self.t.nazwaDir_obr + "\n")

            # dane klasy Sytwys
            self.sw.sw_typ = self.v_sw_typ.get()
            self.sw.sw_idZgl = ".".join([self.v_sw_idZgl_jrwa.get(), self.v_sw_idZgl_nr.get(), self.v_sw_idZgl_rok.get()])
            self.sw.sw_idZgl_jrwa   = self.v_sw_idZgl_jrwa.get()
            self.sw.sw_idZgl_nr     = self.v_sw_idZgl_nr.get()
            self.sw.sw_idZgl_rok    = self.v_sw_idZgl_rok.get()
            f.write("[sw_numer]="           + str(self.sw.sw_numer)        + "\n")
            f.write("[sw_numer_str]="       + self.sw.sw_numer_str          + "\n")
            f.write("[sw_wykonawca]="       + self.sw.sw_wykonawca          + "\n")
            f.write("[sw_typ]="             + self.sw.sw_typ                + "\n")
            f.write("[sw_skala]="           + self.sw.sw_skala              + "\n")
            f.write("[sw_dzialki]="         + self.sw.sw_dzialki            + "\n")
            f.write("[sw_dzialka1]="        + self.sw.sw_dzialka1           + "\n")

            f.write("[sw_idZgl]="           + self.sw.sw_idZgl              + "\n")
            f.write("[sw_idZgl_jrwa]="      + self.sw.sw_idZgl_jrwa         + "\n")
            f.write("[sw_idZgl_nr]="        + self.sw.sw_idZgl_nr           + "\n")
            f.write("[sw_idZgl_rok]="       + self.sw.sw_idZgl_rok          + "\n")

            f.write("[sw_obrebDir]="        + self.sw.sw_obrebDir           + "\n")
            f.write("[sw_dir_nazwa]="       + self.sw.sw_dir_nazwa          + "\n")
            f.write("[sw_mdcp_ust5]=%d\n"  % ( self.v_sw_ust5.get()))
            f.write("[sw_mdcp_ust6]=%d\n"  % ( self.v_sw_ust6.get()))
            # print ( "self.v_sw_ust5_str.get() = %d\n") % ( self.v_sw_ust5.get())
            # print ( "self.v_sw_ust6_str.get() = %d\n") % ( self.v_sw_ust6.get())

            # inw
            f.write("[sw_inw_obiekt]="       + self.v_sw_inw_obiekt.get()      + "\n")
            f.write("[sw_inw_obiektDoUwag]=" + self.v_sw_inw_obiektDoUwag.get()+ "\n")
            f.write("[sw_inw_nrZal]="        + self.v_sw_inw_nrZal.get()       + "\n")
            f.write("[sw_inw_decZnak]="      + self.v_sw_inw_decZnak.get()     + "\n")
            f.write("[sw_inw_decData]="      + self.v_sw_inw_decData.get()     + "\n")

            # libre
            f.write("[sw_libre_wykon]="    + self.sw.sw_libre_wykon    + "\n")
            f.write("[sw_libre_opis]="     + self.sw.sw_libre_opis     + "\n")

            # pZag
            f.write("[oPlan_fA_01]=" + self.oPlan.funAkt_01 + "\n")
            f.write("[oPlan_fA_02]=" + self.oPlan.funAkt_02 + "\n")
            f.write("[oPlan_fA_03]=" + self.oPlan.funAkt_03 + "\n")
            f.write("[oPlan_fA_04]=" + self.oPlan.funAkt_04 + "\n")
            f.write("[oPlan_fA_05]=" + self.oPlan.funAkt_05 + "\n")
            f.write("[oPlan_fA_06]=" + self.oPlan.funAkt_06 + "\n")
            f.write("[oPlan_fA_07]=" + self.oPlan.funAkt_07 + "\n")
            f.write("[oPlan_fA_08]=" + self.oPlan.funAkt_08 + "\n")
            f.write("[oPlan_fA_09]=" + self.oPlan.funAkt_09 + "\n")
            f.write("[oPlan_fA_10]=" + self.oPlan.funAkt_10 + "\n")
            f.write("[oPlan_fA_11]=" + self.oPlan.funAkt_11 + "\n")
            f.write("[oPlan_fA_12]=" + self.oPlan.funAkt_12 + "\n")
            f.write("[oPlan_fA_13]=" + self.oPlan.funAkt_13 + "\n")
            f.write("[oPlan_fA_14]=" + self.oPlan.funAkt_14 + "\n")
            f.write("[oPlan_fA_15]=" + self.oPlan.funAkt_15 + "\n")

            # sekcje
            for key, val in self.sw.sw_dicSekcje.items():
                f.write("%s=%s\n" % (key, val))

            # zapisanie danych wieloliniowych
            # 1) pobranie z textu
            # 2) obci�cie
            # 3) zapisanie do pliku info
            # 4) zapisanie do pliku tytu�
            # 5) zapisanie do pliku uwagi
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # 1)
            # self.sw.sw_sekcje = self.tx_sekcje.get( 1.0, tk.END)
            self.sw.sw_sekcje_tytul = self.tx_sekcje.get( 1.0, tk.END)
            self.sw.mdcp.kp_uwagi1 = self.tx_mdcp_kp_uwagi1.get( 1.0, tk.END)
            self.sw.mdcp.kp_uwagi2 = self.tx_mdcp_kp_uwagi2.get( 1.0, tk.END)
            self.sw.mdcp.kp_uwagi3 = self.tx_mdcp_kp_uwagi3.get( 1.0, tk.END)
            self.sw.mdcp.kp_uwagi4 = self.tx_mdcp_kp_uwagi4.get( 1.0, tk.END)
            self.sw.mdcp.kp_uwagi5 = self.tx_mdcp_kp_uwagi5.get( 1.0, tk.END)
            self.sw.mdcp.kp_uwagi6 = self.tx_mdcp_kp_uwagi6.get( 1.0, tk.END)
            # 2)
            # self.sw.sw_sekcje = self.sw.sw_sekcje.strip()
            self.sw.sw_sekcje_tytul = self.sw.sw_sekcje_tytul.strip()
            self.sw.mdcp.kp_uwagi1 = self.sw.mdcp.kp_uwagi1.strip()
            self.sw.mdcp.kp_uwagi2 = self.sw.mdcp.kp_uwagi2.strip()
            self.sw.mdcp.kp_uwagi3 = self.sw.mdcp.kp_uwagi3.strip()
            self.sw.mdcp.kp_uwagi4 = self.sw.mdcp.kp_uwagi4.strip()
            self.sw.mdcp.kp_uwagi5 = self.sw.mdcp.kp_uwagi5.strip()
            self.sw.mdcp.kp_uwagi6 = self.sw.mdcp.kp_uwagi6.strip()
            # 3)
            f.write( "[sw_sekcje]="             + self.sw.sw_sekcje + "\n")
            f.write( "[sw_sekcje_tytul]="       + self.sw.sw_sekcje_tytul + "\n")
            f.write( "[sw.mdcp.kp_uwagi1]="     + self.sw.mdcp.kp_uwagi1 + "\n")
            f.write( "[sw.mdcp.kp_uwagi2]="     + self.sw.mdcp.kp_uwagi2 + "\n")
            f.write( "[sw.mdcp.kp_uwagi3]="     + self.sw.mdcp.kp_uwagi3 + "\n")
            f.write( "[sw.mdcp.kp_uwagi4]="     + self.sw.mdcp.kp_uwagi4 + "\n")
            f.write( "[sw.mdcp.kp_uwagi5]="     + self.sw.mdcp.kp_uwagi5 + "\n")
            f.write( "[sw.mdcp.kp_uwagi6]="     + self.sw.mdcp.kp_uwagi6 + "\n")

        # 4)
        # utworzenie pliku tytul.txt i uwagi.txt
        self.sw.setNazwyPlikow_tytul_uwagi()

        # tytul.txt
        with open(self.sw.sw_plikTytul_fullPath, "w") as f2:
            f2.write(self.t.nazwa_uStn_woj + "\n")
            f2.write(self.t.nazwa_uStn_pow + "\n")
            f2.write(self.t.nazwa_uStn_jew + "\n")
            f2.write(self.t.nazwa_uStn_obr + "\n")
            if len(self.sw.sw_dzialki_ergo_lst) < 2:
                f2.write("Dzia�ka: " + self.sw.sw_dzialki + "\n")
            else:
                f2.write("Dzia�ki: " + self.sw.sw_dzialki + "\n")
            f2.write("Uk�ad wsp�rz�dnych p�askich prostok�tnych: PL-2000/18" + "\n")
            f2.write("Geodezyjny uk�ad wysoko�ciowy: PL-KRON86-NH" + "\n")
            f2.write(self.sw.sw_sekcje_tytul + "\n")
            f2.write("Skala 1:" + self.sw.sw_skala + "\n")
            f2.write("Id. zg�.: " + self.sw.sw_idZgl + "\n")
            if self.sw.sw_typ == "inw":
                f2.write("\n")
                f2.write(f"Usytuowanie obiektu budowlanego {self.sw.inw.obiekt_do_uwag} zgodne\n")
                f2.write(f"z projektem zagospodarowania terenu (za��cznik nr {self.sw.inw.nr_zal} do decyzji\n")
                # na ko�cu musi by� spacja, bo z niewiadomych wzgl�d�w macro nie tworzy
                # ostatniego wiersza z ostatnim znakiem (bez spacji nie narysuje si� kropka)
                f2.write("o znaku %s z dnia %s r.). " % (self.sw.inw.dec_znak, self.sw.inw.dec_data))
            else:
                print(f'deb: {self.sw.sw_typ=}')

        # uwagi.txt
        with open(self.sw.sw_plikUwagi_fullPath, "w") as f2:
            f2.write(self.sw.mdcp.kp_uwagi1 + "\n\n")
            f2.write(self.sw.mdcp.kp_uwagi2 + "\n\n")
            f2.write(self.sw.mdcp.kp_uwagi3 + "\n\n")
            f2.write(self.sw.mdcp.kp_uwagi4 + "\n\n")
            f2.write(self.sw.mdcp.kp_uwagi5 + "\n\n")
            f2.write(self.sw.mdcp.kp_uwagi6 + "\n\n")

        # utworzenie pliku dz.txt z dzia�kami do zakresu ergo
        try:
            with open(self.sw.sw_plikDz_ergo_abspath, 'w') as f:
                for dz in self.sw.sw_dzialki_ergo_lst:
                    f.write(dz + '\n')
        except:
            print("ERR b��d zapisu listy dzia�ek do ergo do pliku")
            print(f'B��d {sys.exc_info()[0]}')
            print(f'B��d {sys.exc_info()[1]}')

        # utworzenie pliku do zg�oszenia ergo (kg.txt)
        # - dodano odst�p mi�dzy wierszami - �atwiej zaznacza� mysz�
        try:
            with open(self.sw.sw_plikDz_kg_abspath, 'w') as f:
                # nazwa obiektu
                f.write(self.sw.sw_typ + ' ')
                f.write(self.sw.sw_dzialki_obj.source_jew_teryt_do_kG + ' ')
                f.write(self.sw.sw_dzialki_obj.source_obr_nazwa + ' ')
                f.write(self.sw.sw_dzialki_obj.sorted_string_nr_prz_sp + '\n\n')
                # opis po�o�enia
                f.write(self.sw.sw_dzialki_obj.source_jew_teryt_do_kG + ' ')
                f.write(self.sw.sw_dzialki_obj.source_obr_nazwa + ' ')
                f.write(self.sw.sw_dzialki_obj.sorted_string_nr_prz_sp + '\n\n')
                # data zakonczenia
                f.write(spdatetime.date_after(1, 0, 0).isoformat() + '\n')
        except:
            print("ERR b��d zapisu pliku kg.txt")
            print(f'B��d {sys.exc_info()[0]}')
            print(f'B��d {sys.exc_info()[1]}')

        print("zapisano")
        # na razie trzeba zamkn��, �eby program nie g�upia�
        # self.master_frame.destroy
        # sys.exit()


    def wczytaj(self):
        """

        """

        # otwarcie pliku sw_*_info.txt
        # - na razie za pomoc� okna dialogowego
        # >> zrobi� przekazywanie �cie�ki pliku do otwarcia jako argumentu
        #    przekazywanego podczas uruchamiania programu
        # =========================================================================
        # global sw_plikInfo_fullPath
        # self.sw.sw_plikInfo_fullPath = "t:\\sytwys\\826_kp_1904_Biezen_7-24\\sw_826_info.txt"
        self.sw.sw_plikInfo_fullPath = tk.filedialog.askopenfilename(
                initialdir=dictConstants.dictConstants["GC_DIR_SYTWYS"],
                title="Wybierz plik swInfo",
                filetypes=(("swInfo files", "*.txt"), ("all files", "*.*"))
                )
        self.sw.setNazwyPlikow_tytul_uwagi()
        if not os.path.exists(self.sw.sw_plikInfo_fullPath):
            komunikat = "Plik %s nie istnieje" % self.sw.sw_plikInfo_fullPath
            tk.messagebox.showinfo("Err", komunikat)
            return -1

        # - odczytanie danych z pliku info
        # - i zapisanie ich s�owniku dicWierszePliku
        # =========================================================================
        with open( self.sw.sw_plikInfo_fullPath, "r") as f:
        # with open( plikInfo_826, "r") as f:
            for wiersz in f:
                wLen = len( wiersz)
                # print( "%s" % wiersz[:-1])

                s = wiersz.strip()
                lstWiersz = s.split("=")
                if len(lstWiersz) == 2:
                    s = ">%s< >%s<\n" % (lstWiersz[0], lstWiersz[1])
                    # print( s)
                    klucz = lstWiersz[0]
                    self.dicWierszePliku[ klucz] = lstWiersz[1]
                elif len( lstWiersz) == 1:
                    self.dicWierszePliku[ klucz] = self.dicWierszePliku[ klucz] + "\n" + lstWiersz[0]
                else:
                    print("ERR")

                # self.dicWierszePliku.insert( wiersz)
                # print( "%s" % self.dicWierszePliku)
            # deb
            # print( self.dicWierszePliku)

        # aktualizacja zmiennych danymi ze s�ownika dicWierszePliku
        # =========================================================================
        for key, val in self.dicWierszePliku.items():
            if key == "[t_terytFull]"           : self.t.terytFull          = val
            if key == "[t_terytF_woj]"          : self.t.terytF_woj         = val
            if key == "[t_terytF_pow]"          : self.t.terytF_pow         = val
            if key == "[t_terytF_jew]"          : self.t.terytF_jew         = val
            if key == "[t_terytF_obr]"          : self.t.terytF_obr         = val
            if key == "[t_teryt_woj]"           : self.t.teryt_woj          = val
            if key == "[t_teryt_pow]"           : self.t.teryt_pow          = val
            if key == "[t_teryt_jew]"           : self.t.teryt_jew          = val
            if key == "[t_teryt_obr]"           : self.t.teryt_obr          = val
            if key == "[t_nazwa_woj]"           : self.t.nazwa_woj          = val
            if key == "[t_nazwa_pow]"           : self.t.nazwa_pow          = val
            if key == "[t_nazwa_jew]"           : self.t.nazwa_jew          = val
            if key == "[t_nazwa_obr]"           : self.t.nazwa_obr          = val
            if key == "[t_nazwa_uStn_woj]"      : self.t.nazwa_uStn_woj     = val
            if key == "[t_nazwa_uStn_pow]"      : self.t.nazwa_uStn_pow     = val
            if key == "[t_nazwa_uStn_jew]"      : self.t.nazwa_uStn_jew     = val
            if key == "[t_nazwa_uStn_obr]"      : self.t.nazwa_uStn_obr     = val
            if key == "[t_nazwaDir_obr]"        : self.t.nazwaDir_obr       = val

            if key == "[sw_numer]"              : self.sw.sw_numer          = int( val)
            if key == "[sw_numer_str]"          : self.sw.sw_numer_str      = val
            if key == "[sw_wykonawca]"          : self.sw.sw_wykonawca      = val
            if key == "[sw_typ]"                : self.sw.sw_typ            = val
            if key == "[sw_skala]"              : self.sw.sw_skala          = val

            # aktualizacja dzia�ek
            # - string z numerami odczytany z pliku
            # ?> czy tutaj jest potrzebna aktualizacja obiektu sw.sw_dzialki_obj
            #    NIE, bo tu tylko odczytujemy dane z pliku
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            if key == "[sw_dzialki]"            : self.sw.sw_dzialki = val
            if key == "[sw_dzialka1]"           : self.sw.sw_dzialka1       = val

            # if key == "[sw_idZgl]"              : self.sw.sw_idZgl          = val
            if key == "[sw_idZgl_jrwa]"         : self.sw.sw_idZgl_jrwa     = val
            if key == "[sw_idZgl_nr]"           : self.sw.sw_idZgl_nr       = val
            if key == "[sw_idZgl_rok]"          : self.sw.sw_idZgl_rok      = val

            if key == "[sw_obrebDir]"           : self.sw.sw_obrebDir       = val
            if key == "[sw_dir_nazwa]"          : self.sw.sw_dir_nazwa      = val
            if key == "[sw_mdcp_ust5]"          : self.sw.mdcp.ust5      = val
            if key == "[sw_mdcp_ust6]"          : self.sw.mdcp.ust6      = val

            if key == "[sw_inw_obiekt]"         : self.sw.inw.obiekt         = val
            if key == "[sw_inw_obiektDoUwag]"   : self.sw.inw.obiekt_do_uwag = val
            if key == "[sw_inw_nrZal]"          : self.sw.inw.nr_zal         = val
            if key == "[sw_inw_decZnak]"        : self.sw.inw.dec_znak       = val
            if key == "[sw_inw_decData]"        : self.sw.inw.dec_data       = val

            if key == "[sw_libre_wykon]"        : self.sw.sw_libre_wykon    = val
            if key == "[sw_libre_opis]"         : self.sw.sw_libre_opis     = val

            if key == "[sw_sekcje]"             : self.sw.sw_sekcje         = val
            if key == "[sw_sekcje_tytul]"       : self.sw.sw_sekcje_tytul   = val

            # do zmiany
            # print( key[0:7])
            if key[0:7] == "[godlo_":
                if key == "[godlo_01]"              : self.sw.sw_godlo_01       = val
                if key == "[godlo_02]"              : self.sw.sw_godlo_02       = val
                if key == "[godlo_03]"              : self.sw.sw_godlo_03       = val
                if key == "[godlo_04]"              : self.sw.sw_godlo_04       = val
                if key == "[godlo_05]"              : self.sw.sw_godlo_05       = val
                if key == "[godlo_06]"              : self.sw.sw_godlo_06       = val
                if key == "[godlo_07]"              : self.sw.sw_godlo_07       = val
                if key == "[godlo_08]"              : self.sw.sw_godlo_08       = val
                if key == "[godlo_09]"              : self.sw.sw_godlo_09       = val
                if key == "[godlo_10]"              : self.sw.sw_godlo_10       = val
                if key == "[godlo_11]"              : self.sw.sw_godlo_11       = val
                if key == "[godlo_12]"              : self.sw.sw_godlo_12       = val
                if key == "[godlo_13]"              : self.sw.sw_godlo_13       = val
                if key == "[godlo_14]"              : self.sw.sw_godlo_14       = val
                if key == "[godlo_15]"              : self.sw.sw_godlo_15       = val
                if key == "[godlo_16]"              : self.sw.sw_godlo_16       = val
                if key == "[godlo_17]"              : self.sw.sw_godlo_17       = val
                if key == "[godlo_18]"              : self.sw.sw_godlo_18       = val
                if key == "[godlo_19]"              : self.sw.sw_godlo_19       = val
                if key == "[godlo_20]"              : self.sw.sw_godlo_20       = val

            if key == "[oPlan_fA_01]"           : self.oPlan.funAkt_01      = val
            if key == "[oPlan_fA_02]"           : self.oPlan.funAkt_02      = val
            if key == "[oPlan_fA_03]"           : self.oPlan.funAkt_03      = val
            if key == "[oPlan_fA_04]"           : self.oPlan.funAkt_04      = val
            if key == "[oPlan_fA_05]"           : self.oPlan.funAkt_05      = val
            if key == "[oPlan_fA_06]"           : self.oPlan.funAkt_06      = val
            if key == "[oPlan_fA_07]"           : self.oPlan.funAkt_07      = val
            if key == "[oPlan_fA_08]"           : self.oPlan.funAkt_08      = val
            if key == "[oPlan_fA_09]"           : self.oPlan.funAkt_09      = val
            if key == "[oPlan_fA_10]"           : self.oPlan.funAkt_10      = val
            if key == "[oPlan_fA_11]"           : self.oPlan.funAkt_11      = val
            if key == "[oPlan_fA_12]"           : self.oPlan.funAkt_12      = val
            if key == "[oPlan_fA_13]"           : self.oPlan.funAkt_13      = val
            if key == "[oPlan_fA_14]"           : self.oPlan.funAkt_14      = val
            if key == "[oPlan_fA_15]"           : self.oPlan.funAkt_15      = val

            if key == "[sw_mdcp_kp_uwagi1]"     : self.sw.mdcp.kp_uwagi1 = val
            if key == "[sw_mdcp_kp_uwagi2]"     : self.sw.mdcp.kp_uwagi2 = val
            if key == "[sw_mdcp_kp_uwagi3]"     : self.sw.mdcp.kp_uwagi3 = val
            if key == "[sw_mdcp_kp_uwagi4]"     : self.sw.mdcp.kp_uwagi4 = val
            if key == "[sw_mdcp_kp_uwagi5]"     : self.sw.mdcp.kp_uwagi5 = val
            if key == "[sw_mdcp_kp_uwagi6]"     : self.sw.mdcp.kp_uwagi6 = val

        # aktualizacja zmiennych zwi�zanych z widgetami
        # =========================================================================
        self.v_sw_numer         .set( self.sw.sw_numer_str          )
        self.v_sw_wykonawca     .set( self.sw.sw_wykonawca          )
        self.v_sw_typ           .set( self.sw.sw_typ                )
        self.v_sw_skala         .set( self.sw.sw_skala              )
        self.v_sw_obreb         .set( self.t.nazwa_obr              )
        # tu powinien by� obr�b-teryt
        # self.v_sw_obrebListBox
        self.v_sw_dzialki       .set( self.sw.sw_dzialki            )
        self.v_sw_ust5.set(int(self.sw.mdcp.ust5))
        self.v_sw_ust6.set(int(self.sw.mdcp.ust6))
        # self.v_sw_idZgl         .set( self.sw.sw_idZgl              )   #<== do likwidacji
        self.v_sw_idZgl_jrwa    .set( self.sw.sw_idZgl_jrwa         )
        self.v_sw_idZgl_nr      .set( self.sw.sw_idZgl_nr           )
        self.v_sw_idZgl_rok     .set( self.sw.sw_idZgl_rok          )

        self.v_sw_powiat_teryt  .set( self.t.terytF_pow     )
        self.v_sw_powiat_nazwa  .set( self.t.nazwa_pow      )
        self.v_sw_jEw_teryt     .set( self.t.terytF_jew     )
        self.v_sw_jEw_nazwa     .set( self.t.nazwa_jew      )
        self.v_sw_obreb_teryt   .set( self.t.teryt_obr      )
        self.v_sw_obreb_nazwa   .set( self.t.nazwa_obr      )
        self.v_sw_obreb_dir     .set( self.t.nazwaDir_obr   )

        self.v_sw_libre_wykon   .set( self.sw.sw_libre_wykon        )
        self.v_sw_libre_opis    .set( self.sw.sw_libre_opis         )
        self.v_sw_dir_nazwa     .set( self.sw.sw_dir_nazwa          )

        self.v_sw_inw_obiekt        .set(self.sw.inw.obiekt        )
        self.v_sw_inw_obiektDoUwag  .set(self.sw.inw.obiekt_do_uwag)
        self.v_sw_inw_nrZal         .set(self.sw.inw.nr_zal        )
        self.v_sw_inw_decZnak       .set(self.sw.inw.dec_znak      )
        self.v_sw_inw_decData       .set(self.sw.inw.dec_data      )

        # self.v_sw_mdcp_kp_uwagi1.set( self.sw.sw_mdcp_kp_uwagi1   )
        # self.v_sw_mdcp_kp_uwagi2.set( self.sw.sw_mdcp_kp_uwagi2   )
        # self.v_sw_mdcp_kp_uwagi3.set( self.sw.sw_mdcp_kp_uwagi3   )
        # self.v_sw_mdcp_kp_uwagi4.set( self.sw.sw_mdcp_kp_uwagi4   )
        # self.v_sw_mdcp_kp_uwagi5.set( self.sw.sw_mdcp_kp_uwagi5   )
        # self.v_sw_typ.set( self.sw_sw_typ)
        # print( self.sw.sw_mdcp_ust5)
        # print( self.sw.sw_mdcp_ust6)


        # god�a i text sekcje
        # utworzenie listy sekcji i s�ownika sekcji
        # -------------------------------------------------------------------------
        # deb - wczytana zmienna
        print("---[ self.sw.sw_sekcje po wczytaniu ]-----------------------------")
        print("%s\n" % (self.sw.sw_sekcje))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        self.tx_sekcje.delete( 1.0, tk.END)
        if len( self.sw.sw_sekcje_tytul) > 0:
            self.tx_sekcje.insert( tk.END, self.sw.sw_sekcje_tytul)

        # utworzenie listy i s�ownika sekcji
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        print("---[ utworzenie listy i s�ownika sekcji ]------------------------")
        self.sw.sw_dicSekcje.clear()
        del self.sw.sw_lstSekcje[0:]
        for key, val in self.dicWierszePliku.items():
            if key.startswith( "[godlo_") > 0:
                self.sw.sw_lstSekcje.append( val)
                self.sw.sw_dicSekcje[ key] = val
        self.sw.sw_lstSekcje.sort()
        print("self.sw.sw_lstSekcje po utworzeniu:\n")
        print("%s\n" % (self.sw.sw_lstSekcje))
        print("self.sw.sw_dicSekcje po utworzeniu:\n")
        print(self.sw.sw_dicSekcje)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


        # uwagi 1
        # wpisanie wczytanych uwag do widgetu text
        # -------------------------------------------------------------------------
        print("---[ self.sw.sw_mdcp_kp_uwagi1 po wczytaniu ]---------------------")
        print("%s\n" % (self.sw.mdcp.kp_uwagi1))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        self.tx_mdcp_kp_uwagi1.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi2.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi3.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi4.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi5.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi6.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi1.insert( tk.END, self.sw.mdcp.kp_uwagi1)
        self.tx_mdcp_kp_uwagi2.insert( tk.END, self.sw.mdcp.kp_uwagi2)
        self.tx_mdcp_kp_uwagi3.insert( tk.END, self.sw.mdcp.kp_uwagi3)
        self.tx_mdcp_kp_uwagi4.insert( tk.END, self.sw.mdcp.kp_uwagi4)
        self.tx_mdcp_kp_uwagi5.insert( tk.END, self.sw.mdcp.kp_uwagi5)
        self.tx_mdcp_kp_uwagi6.insert( tk.END, self.sw.mdcp.kp_uwagi6)

        # self.master_frame.destroy
        # sys.exit()

    def btn_gen_sekcje( self):
        '''
        -   wczytanie gode� z pliku "godla2swInfo.txt" do obiektu sekcje
        -   utworzenie s�ownika gode� postaci:
                    [godlo_03]=6.142.28.02.2.2
        -   utworzenie propozycji tre�ci tekstu sw.sw_sekcje
        '''
        # deb
        # self.sw.sw_plikGodla2swInfo_fullPath = "t:\sytwys\883_rg_1909_BorZapilski-kan_inw\godla2swInfo.txt"
        # print( "godla2swInfo.txt= >%s<" % (self.sw.sw_plikGodla2swInfo_fullPath))

        if not os.path.exists(self.sw.sw_plikGodla2swInfo_fullPath):
            komunikat = "Plik %s nie istnieje" % self.sw.sw_plikGodla2swInfo_fullPath
            tk.messagebox.showinfo("Err", komunikat)
            return -1

        with open (self.sw.sw_plikGodla2swInfo_fullPath) as f:
            # if self.godlaX.g_lista.len() > 0:
            self.godlaX.oproznijListe()
            self.godlaX.drukujListe("---[ godla przed wczytaniem z pliku ]-------")
            for wiersz in f:
                self.godlaX.dodajSekcje( wiersz[:-1])

        # for wiersz
        # print( self.godlaX.g_lista)
        self.godlaX.drukujListe("---[ godla po wczytaniu ]-------")
        self.godlaX.drukujSlownik("---[ slownik gode� po wczytaniu ]-------")

        # utworzenie tekstu sw_sekcje
        #
        self.sw.sw_sekcje = ""
        '''
        -   wiersze numerowane od "0"
        -   i == nr god�a w wierszu
        -   j == nr kolejny god�a
        -   sStart == trzy spacje na pocz. wiersz, poza wierszem 0
        '''
        i = 0
        j = 0
        iOstatnia = len( self.godlaX.g_lista)
        liczbaSekcjiWWierszu = 4
        wierszSekcji = ""
        nrWiersza = 0
        sStart = ""
        for s in self.godlaX.g_lista:
            i += 1
            j += 1
            sEnd = ""
            if (nrWiersza > 0) and (i == 1):
                sStart = "   "
            else:
                sStart = ""
            if i == liczbaSekcjiWWierszu:
                sEnd = "\n"
                i = 0
                nrWiersza += 1
            if j != iOstatnia:
                sPrzecinek = ", "
            else:
                sEnd = ""
                sPrzecinek = ""
            # deb
            # print( "i=%d, iOstatnia=%d >%s<>%s<\n" % ( i, iOstatnia, sPrzecinek, sEnd))
            wierszSekcji = wierszSekcji + s + sPrzecinek + sEnd
            self.sw.sw_sekcje = self.sw.sw_sekcje + sStart + s + sPrzecinek + sEnd
            # zapisanie wiersza w s�owniku sekcji
            # self.sw.sw_dicSekcje[]

        if iOstatnia < (liczbaSekcjiWWierszu - 1):
            self.sw.sw_sekcje_tytul = "Sekcje mapy zas. uk�. 2000: " + self.sw.sw_sekcje
        else:
            self.sw.sw_sekcje_tytul = "Sekcje mapy zas. uk�. 2000:\n" + self.sw.sw_sekcje
        # print( "self.sw.sw_lstSekcje po utworzeniu z gode�:\n")
        # print( "%s\n" % (self.sw.sw_lstSekcje))
        print("self.sw.sw_sekcje po utworzeniu z gode�:\n")
        print("%s\n" % (self.sw.sw_sekcje))

        self.tx_sekcje.delete(1.0, tk.END)
        self.tx_sekcje.insert(tk.END, self.sw.sw_sekcje_tytul)


#        # WERSJA WCZE�NIEJSZA
#        # utworzenie tekstu sw_sekcje
#        i = 0
#        j = 0
#        iOstatnia = len( self.sw.sw_lstSekcje)
#        liczbaSekcjiWWierszu = 3
#        self.sw.sw_sekcje = ""
#        wierszSekcji = ""
#        for s in self.sw.sw_lstSekcje:
#            i += 1
#            j += 1
#            sEnd = ""
#            if i == liczbaSekcjiWWierszu:
#                sEnd = "\n"
#                i = 0
#            if j != iOstatnia:
#                sPrzecinek = ", "
#            else:
#                sEnd = ""
#                sPrzecinek = ""
#            #deb
#            #print( "i=%d, iOstatnia=%d >%s<>%s<\n" % ( i, iOstatnia, sPrzecinek, sEnd))
#            wierszSekcji = wierszSekcji + s + sPrzecinek + sEnd
#            self.sw.sw_sekcje = self.sw.sw_sekcje + s + sPrzecinek + sEnd
#            # zapisanie wiersza w s�owniku sekcji
#            #self.sw.sw_dicSekcje[]
#
#        self.sw.sw_sekcje_tytul = "Sekcje mapy zas. uk�. 2000: " + self.sw.sw_sekcje
#        print( "self.sw.sw_lstSekcje po utworzeniu z gode�:\n")
#        print( "%s\n" % (self.sw.sw_lstSekcje))
#        print( "self.sw.sw_sekcje po utworzeniu z gode�:\n")
#        print( "%s\n" % (self.sw.sw_sekcje))
#
#
#        self.tx_sekcje.delete( 1.0, tk.END)
#        self.tx_sekcje.insert( tk.END, self.sw.sw_sekcje_tytul)

    def btn_gen_uwagi1(self):
        # utworzenie uwag

        # utworzenie stringu idZgl
        self.sw.sw_idZgl_jrwa = self.v_sw_idZgl_jrwa.get()
        self.sw.sw_idZgl_nr = self.v_sw_idZgl_nr.get()
        self.sw.sw_idZgl_rok = self.v_sw_idZgl_rok.get()
        s = '.'.join([self.sw.sw_idZgl_jrwa, self.sw.sw_idZgl_nr, self.sw.sw_idZgl_rok])

        self.sw.mdcp.kp_uwagi1 = "Mapa utworzona na podstawie arkusza "
        self.sw.mdcp.kp_uwagi1 += self.sw.sw_sekcje
        self.sw.mdcp.kp_uwagi1 += " mapy zasadniczej oraz pomiaru aktualizacyjnego id. zg�. "
        self.sw.mdcp.kp_uwagi1 += s + "."

        self.sw.mdcp.kp_uwagi1 = self.divide_into_rows(self.sw.mdcp.kp_uwagi1, 90)
        # deb
        print(f'{self.sw.mdcp.kp_uwagi1 = }')

        self.tx_mdcp_kp_uwagi1.delete(1.0, tk.END)
        self.tx_mdcp_kp_uwagi1.insert(tk.END, self.sw.mdcp.kp_uwagi1)

    def btn_gen_uwagi2(self):
        # utworzenie uwag
        self.sw.sw_dzialki = self.v_sw_dzialki.get()
        self.sw.mdcp.ust5 = "%s" % self.v_sw_ust5.get()
        self.sw.mdcp.ust6 = "%s" % self.v_sw_ust6.get()
        self.sw.mdcp.kp_uwagi2 = "Dane dotycz�ce granic dzia�ki "
        self.sw.mdcp.kp_uwagi2 += self.sw.sw_dzialki + ", ujawnione w PZGiK,"
        if self.sw.mdcp.ust5 == "1":
            self.sw.mdcp.kp_uwagi2 += " spe�niaj� wymogi dok�adno�ciowe dla znak�w i punkt�w granicznych, okre�lone"
        else:
            self.sw.mdcp.kp_uwagi2 += " nie spe�niaj� wymog�w dok�adno�ciowych dla znak�w i punkt�w granicznych, okre�lonych"
        self.sw.mdcp.kp_uwagi2 += " w � 16 pkt 1 rozporz�dzenia Ministra Rozwoju"
        self.sw.mdcp.kp_uwagi2 += " z dnia 18 sierpnia 2020 r., DzU 2020 poz. 1429."

        self.sw.mdcp.kp_uwagi2 = self.divide_into_rows(self.sw.mdcp.kp_uwagi2, 90)

        self.tx_mdcp_kp_uwagi2.delete( 1.0, tk.END)
        self.tx_mdcp_kp_uwagi2.insert( tk.END, self.sw.mdcp.kp_uwagi2)

    def btn_gen_uwagi3(self):
        self.sw.mdcp.kp_uwagi3 = 'Dla obszaru w granicach projektowanej inwestycji budowlanej brak obci��e�'
        self.sw.mdcp.kp_uwagi3 += ' z tytu�u s�u�ebno�ci gruntowych (� 30 ust. 2 pkt 4 rozporz�dzenia'
        self.sw.mdcp.kp_uwagi3 += ' Ministra Rozwoju z dnia 18 sierpnia 2020 r., DzU 2020 poz. 1429).'

        self.sw.mdcp.kp_uwagi3 = self.divide_into_rows(self.sw.mdcp.kp_uwagi3, 90)

        self.tx_mdcp_kp_uwagi3.delete(1.0, tk.END)
        self.tx_mdcp_kp_uwagi3.insert(tk.END, self.sw.mdcp.kp_uwagi3)

        # self.tx_mdcp_kp_uwagi3.tag_add( 'bold_italics', 1.0, tk.END)
        # self.tx_mdcp_kp_uwagi3.tag_add( 'Arial8', 1.0, tk.END)
        # pass

    #
    #     self.sw.mdcp.kp_uwagi4 += 'Dla terenu obj�tego pomiarem brak opracowa� planistycznych (� 30 ust. 2 pkt 3 rozporz�dzenia'
    #     self.sw.mdcp.kp_uwagi4 += 'Ministra Rozwoju z dnia 18 sierpnia 2020 r., DzU 2020 poz. 1429).'


    def get_RRMM(self):
        '''
            funkcja zwraca  string RRMM (1903), potrzebny   do  utworzenia
            sciezki dla katalogu    sw
        '''
        x = datetime.datetime.now()
        rrmm = x.strftime("%y%m")
        return rrmm

    def divide_into_rows(self, text, max_length):
        """
        podzia� na linie po ok. 90 znak�w
        podzia� polega na wstawieniu znak�w \n
        - wymaga dopracowania
        - dzieli na chama w p� s�owa, je�eli tak wypadnie

            text        :: tekst do podzia�u
            max_length  ::
        """
        i = 0
        s = ''
        poprzedni_znak = ''
        for letter in text:
            # deb print(f'{letter = }_')
            if i < max_length:
                s += letter
                poprzedni_znak = letter
            else:
                s += letter
                s += '\n'
                i = 0
                poprzedni_znak = ''
            i += 1
        return s

    # koniec __init__()
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
