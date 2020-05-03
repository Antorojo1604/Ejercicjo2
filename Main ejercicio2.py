from Lista import Lista

def  opcion0 ():
   print ( "Adiós" )
        
def  opcion1 ():
   print ( "Código de la opción 1" )
    

def  opcion2 ():
    print ( "Código de la opción 2" )




def  opcion3 ():
    print ( "Código de la opción 3" )

conmutador  = {
   0 : opcion0 ,
   1 : opcion1 ,
   2 : opcion2 ,
   3 : opcion3
}

def interruptor ( argumento ):
   func  =  conmutador . get ( argumento , lambda : print ( "Opción incorrecta" ))
   func ()

   
if __name__=='__main__':
    l=Lista()
    l.testViajero()
    print(l)
    n=input('Ingrese numero de viajero')
    indice = l.buscarViajero(n)
    #l.MENU(n1)
    no=l.getViajero( )
    
    bandera  =  False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print ( "" )
        print ( "0 Salir" )
        print ( "1 Opción 1" )
        print ( "2 Opción 2" )
        print ( "3 Opción 3" )
        opcion =  int ( input ( "Ingrese una opción:" ))
        interruptor ( opcion )
        bandera  =  int ( opcion ) == 0





    



    

