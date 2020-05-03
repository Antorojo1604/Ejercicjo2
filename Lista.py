from Viajero import ViajeroFrecuente
import csv

class Lista:
    ___Lista=[]
    
    def __init__(self):
        self.__lista=[]
        
    def agregarViajero (self, viajero):
        self.__lista.append(viajero)
        
    def testViajero (self):
        archivo=open('D:/antonela/facultad/programacion orientada a objetos/poo.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                nr=int(fila[0])
                print (nr)
                dni=fila[1]
                print (dni)
                nom=fila[2]
                print(nom)
                ap=fila[3]
                print(ap)
                am=fila[4]
                print(am)
                viajero=ViajeroFrecuente(nr,dni,nom,ap,am)
                self.agregarViajero(viajero)
                
        archivo.close()
                
    def buscarViajero (self,n):
        i=0
        print (i)
        unViajero=self.__lista[i]
        num=unViajero.getnrodeViajero()
        print (num)
        print (n)
        if n==num:
            print("el numero se encotro")
        else:
            print("no se encuentra el numero")
        #while ((n!=num)&(i<18)):
             #print ("hola")
             #i=i+1
             #unViajero=self.__lista[i]
             #print (unViajero)
             #print (i)
       
        print ("sali de la iteracion")    
        if i== 18:
            print(" no se eencuentra el viajero en la lista")
            return -1
        else:
            print(" Se encotro el viajero que busca")
            return i
    def __str__ (self):
        s=""
        for viajero in self.__lista:
         s+=str(viajero)+'\n'
        return s

    
   