#-*- coding: windows-1250 -*-


class Sekcja( object):
    '''
    sekcja mapy
    
    '''
    def __init__( self, agodlo):
        '''
        
        '''
        godlo = agodlo
        skala = 0
        ukladWsp = ""
        #pktLD = 
        #pktPG =
        
        
class ListaSekcji( object):
    '''
    lista:
    -   zawiera posortowaną liste godeł
    
    słownik:
    -   ułatwia wydruk
    -   ma postać:
            [godlo_01]=6.142.28.02.2.1
            [godlo_02]=6.142.28.02.2.3
            [godlo_03]=6.142.28.02.2.2
        
    # godla2swInfo.txt            
    '''
    def __init__(self):        
        self.g_lista = []
        self.g_liczbaSekcjiNaLiscie = 0
        self.g_slownik = {}
        
    def dodajSekcje( self, agodlo):
        '''
        -   sprawdzenie, czy sekcja jest już na liście
        -   jeżeli nie, to dodanie sekcji
        -   posortowanie listy
        
        '''
        if self.g_lista.count( agodlo) == 0:
            self.g_lista.append( agodlo)
            self.g_lista.sort()
            self.generujSlownik()
            

    def oproznijListe( self):
        '''
        -   usunięcie wszystkich elementów z listy
        
        '''
        del self.g_lista[0:]

    def drukujListe( self, atytul):
        if len(atytul) > 0:
            print( atytul)
        for s in self.g_lista:
            print( "%s" % (s))
                     
    def generujSlownik( self):
        self.g_slownik.clear()
        i = 0
        for godlo in self.g_lista:
            key = "[godlo_%02d]" % ( i)
            self.g_slownik[key] = godlo
            i += 1

    def drukujSlownik( self, atytul):
        if len(atytul) > 0:
            print( atytul)
        for k, v in self.g_slownik.items():
            print( "%s=%s" % (k, v))
    
    def komponujGodlaDoTytulu( self):
        pass