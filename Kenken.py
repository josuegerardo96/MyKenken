import tkinter as tk 
from tkinter import messagebox
import webbrowser
import pickle
from tkinter import *
from tkinter import IntVar
from tkinter import StringVar
import random
import pygame
from pygame import mixer

vPrincipal = tk.Tk()
vPrincipal.title("Kenken")
vPrincipal.geometry("800x630")
vPrincipal.config(bg="#F7DC6F")

#...........................................................................GLOBALES......................................................................... 
mixer.init()
avrirConfig = open('kenken_configuracion.dat','rb')
while True:
    try:
        ListConfig = pickle.load(avrirConfig)
    except EOFError:
        break
avrirConfig.close()

if(ListConfig[1]=="ConReloj"):
    MiReloj = True
    MiTimer = False
elif(ListConfig[1]=="ConTimer"):
    MiReloj = False
    MiTimer = True
elif(ListConfig[1]=="SinReloj"):
    MiReloj = False
    MiTimer = False

DificultadJuego = ListConfig[0]
destructor = False

Sonido = ListConfig[2]

PausarReloj = False
PausarTimer = False
MisHoras = "00"
MisMinutos = "00"
MisSegundos = "00"

JuegoFinalizado = False

MostrarEntradaTimer = False

NombreJugador = ""
TiempoJugador = ""

destructorDerelojes = False

TableroDeJuego = ListConfig[3]
TableroFilasColumnas=ListConfig[4]
#-.....................................................................SECCION DE FUNCIONES ...............................................................
if("MenuTable"=="MenuTable"):
    def IrAConfiguracion():
        vMenu = tk.Tk()
        vMenu.geometry("700x600")
        vMenu.title("Configuracion del juego")
        vMenu.config(bg="#F7DC6F")

        class Configuracion:
            def ConDificultadFacil():
                BFacil.config(bg="#2ED60C")
                BIntermedio.config(bg="#E25050")
                BDificil.config(bg="#E25050")

            def ConDificultadIntermedio():
                BFacil.config(bg="#E25050")
                BIntermedio.config(bg="#2ED60C")
                BDificil.config(bg="#E25050")

            def ConDificultadDificil():
                BFacil.config(bg="#E25050")
                BIntermedio.config(bg="#E25050")
                BDificil.config(bg="#2ED60C")   
                if messagebox.showinfo("Error","NO HAY JUEGOS PARA ESTE NIVEL \n se pondrá intermedio",parent=vMenu):
                    Configuracion.ConDificultadIntermedio()
                    BFacil.config(bg="#E25050")
                    BIntermedio.config(bg="#2ED60C")
                    BDificil.config(bg="#E25050")

            def ConReloj():
                global MiReloj
                global MiTimer
                MiReloj = True
                MiTimer = False
                BConReloj.config(bg="#2ED60C")
                BSinReloj.config(bg="#E25050")
                BTimer.config(bg="#E25050")
                EntradaParaHorasTimer.config(state="disabled")
                EntradaParaMinutosTimer.config(state="disabled")
                EntradaParaSegundosTimer.config(state="disabled")
                TimerListo.config(state="disabled")
                MostrarEntradaTimer = False
                avrirConfig = open('kenken_configuracion.dat','rb')
                while True:
                    try:
                        ListConfig = pickle.load(avrirConfig)
                    except EOFError:
                        break
                avrirConfig.close()
                ListConfig.pop(1)
                ListConfig.insert(1,"ConReloj")

                avrir = open('kenken_configuracion.dat','wb')
                pickle.dump(ListConfig,avrir)
                avrir.close()

            def SinReloj():
                global MiReloj
                global MiTimer
                MiReloj = False
                MiTimer = False
                BSinReloj.config(bg="#2ED60C")
                BTimer.config(bg="#E25050")
                BConReloj.config(bg="#E25050")

                EntradaParaHorasTimer.config(state="disabled")
                EntradaParaMinutosTimer.config(state="disabled")
                EntradaParaSegundosTimer.config(state="disabled")
                TimerListo.config(state="disabled")
                MostrarEntradaTimer = False
                avrirConfig = open('kenken_configuracion.dat','rb')
                while True:
                    try:
                        ListConfig = pickle.load(avrirConfig)
                    except EOFError:
                        break
                avrirConfig.close()
                ListConfig.pop(1)
                ListConfig.insert(1,"SinReloj")

                avrir = open('kenken_configuracion.dat','wb')
                pickle.dump(ListConfig,avrir)
                avrir.close()

            def ConTimer():
                global MiReloj
                global MiTimer
                MiReloj = False
                MiTimer = True
                BSinReloj.config(bg="#E25050")
                BTimer.config(bg="#2ED60C")
                BConReloj.config(bg="#E25050")

                EntradaParaHorasTimer.config(state="normal")
                EntradaParaMinutosTimer.config(state="normal")
                EntradaParaSegundosTimer.config(state="normal")
                TimerListo.config(state="normal")   
                MostrarEntradaTimer = True
                avrirConfig = open('kenken_configuracion.dat','rb')
                while True:
                    try:
                        ListConfig = pickle.load(avrirConfig)
                    except EOFError:
                        break
                avrirConfig.close()
                ListConfig.pop(1)
                ListConfig.insert(1,"ConTimer")

                avrir = open('kenken_configuracion.dat','wb')
                pickle.dump(ListConfig,avrir)
                avrir.close()

            def ConSonido():
                global Sonido
                Sonido = "ConSonido"
                BSonidoSi.config(bg="#2ED60C")
                BSonidoNo.config(bg="#E25050")
                avrirConfig = open('kenken_configuracion.dat','rb')
                while True:
                    try:
                        ListConfig = pickle.load(avrirConfig)
                    except EOFError:
                        break
                avrirConfig.close()
                ListConfig.pop(2)
                ListConfig.insert(2,"ConSonido")

                avrir = open('kenken_configuracion.dat','wb')
                pickle.dump(ListConfig,avrir)
                avrir.close()

            def SinSonido():
                global Sonido
                Sonido = "SinSonido"
                BSonidoNo.config(bg="#2ED60C")
                BSonidoSi.config(bg="#E25050")
                avrirConfig = open('kenken_configuracion.dat','rb')
                while True:
                    try:
                        ListConfig = pickle.load(avrirConfig)
                    except EOFError:
                        break
                avrirConfig.close()
                ListConfig.pop(2)
                ListConfig.insert(2,"SinSonido")

                avrir = open('kenken_configuracion.dat','wb')
                pickle.dump(ListConfig,avrir)
                avrir.close()

            def TipoCuadricula(texto):
                global TableroDeJuego
                TableroDeJuego = texto
                avrir = open('kenken_configuracion.dat','rb')
                while True:
                    try:
                        datos = pickle.load(avrir)
                    except EOFError:
                        break
                avrir.close()
                datos.pop(3)
                datos.insert(3,TableroDeJuego)
                avrir = open('kenken_configuracion.dat','wb')
                pickle.dump(datos,avrir)
                avrir.close()

                if(texto=='3x3'):
                    Cuadricula3x3.config(bg="#2ED60C")
                    Cuadricula4x4.config(bg="#E25050")
                    Cuadricula5x5.config(bg="#E25050")
                    Cuadricula6x6.config(bg="#E25050")
                    Cuadricula7x7.config(bg="#E25050")
                    Cuadricula8x8.config(bg="#E25050")
                    Cuadricula9x9.config(bg="#E25050")

                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[6,3])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()
                elif(texto=='4x4'):
                    Cuadricula3x3.config(bg="#E25050")
                    Cuadricula4x4.config(bg="#2ED60C")
                    Cuadricula5x5.config(bg="#E25050")
                    Cuadricula6x6.config(bg="#E25050")
                    Cuadricula7x7.config(bg="#E25050")
                    Cuadricula8x8.config(bg="#E25050")
                    Cuadricula9x9.config(bg="#E25050")
                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[8,4])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()

                elif(texto=='5x5'):
                    Cuadricula3x3.config(bg="#E25050")
                    Cuadricula4x4.config(bg="#E25050")
                    Cuadricula5x5.config(bg="#2ED60C")
                    Cuadricula6x6.config(bg="#E25050")
                    Cuadricula7x7.config(bg="#E25050")
                    Cuadricula8x8.config(bg="#E25050")
                    Cuadricula9x9.config(bg="#E25050")
                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[10,5])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()
                elif(texto=='6x6'):
                    Cuadricula3x3.config(bg="#E25050")
                    Cuadricula4x4.config(bg="#E25050")
                    Cuadricula5x5.config(bg="#E25050")
                    Cuadricula6x6.config(bg="#2ED60C")
                    Cuadricula7x7.config(bg="#E25050")
                    Cuadricula8x8.config(bg="#E25050")
                    Cuadricula9x9.config(bg="#E25050")
                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[12,6])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()
                elif(texto=='7x7'):
                    Cuadricula3x3.config(bg="#E25050")
                    Cuadricula4x4.config(bg="#E25050")
                    Cuadricula5x5.config(bg="#E25050")
                    Cuadricula6x6.config(bg="#E25050")
                    Cuadricula7x7.config(bg="#2ED60C")
                    Cuadricula8x8.config(bg="#E25050")
                    Cuadricula9x9.config(bg="#E25050")
                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[14,7])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()
                elif(texto=='8x8'):
                    Cuadricula3x3.config(bg="#E25050")
                    Cuadricula4x4.config(bg="#E25050")
                    Cuadricula5x5.config(bg="#E25050")
                    Cuadricula6x6.config(bg="#E25050")
                    Cuadricula7x7.config(bg="#E25050")
                    Cuadricula8x8.config(bg="#2ED60C")
                    Cuadricula9x9.config(bg="#E25050")
                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[16,8])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()
                elif(texto=='9x9'):
                    Cuadricula3x3.config(bg="#E25050")
                    Cuadricula4x4.config(bg="#E25050")
                    Cuadricula5x5.config(bg="#E25050")
                    Cuadricula6x6.config(bg="#E25050")
                    Cuadricula7x7.config(bg="#E25050")
                    Cuadricula8x8.config(bg="#E25050")
                    Cuadricula9x9.config(bg="#2ED60C")
                    avrir = open('kenken_configuracion.dat','rb')
                    while True:
                        try:
                            datos = pickle.load(avrir)
                        except EOFError:
                            break
                    avrir.close()
                    datos.pop(4)
                    datos.insert(4,[18,9])
                    avrir = open('kenken_configuracion.dat','wb')
                    pickle.dump(datos,avrir)
                    avrir.close()


        class EntradaTimer:
            def EntradaHoras(evento):
                global MisHoras
                global MisMinutos
                global MisSegundos
                f = EntradaParaHorasTimer.get()
                s = str(f)
                if(s==""):
                    EntradaParaHorasTimer.insert("end","00")
                f = int(f)
                print(s+"gato")
                if(f>3 or f<0):
                    messagebox.showerror("Error","Error, las horas deben ser entre 0 y 3")
                    EntradaParaHorasTimer.focus_set()
                
            def EntradaHoras2(evento):
                if(EntradaParaHorasTimer.get()=="00"):
                    EntradaParaHorasTimer.delete("0","end")

            def EntradaMinutos(evento):
                global MisHoras
                global MisMinutos
                global MisSegundos
                f = EntradaParaMinutosTimer.get()
                s = str(f)
                if(s==""):
                    EntradaParaMinutosTimer.insert("end","00")
                f = int(f)
                if(f>59 or f<0):
                    messagebox.showerror("Error","Error, los minutos deben estar entre 0 y 59")
                    EntradaParaMinutosTimer.focus_set()

            def EntradaMinutos2(evento):
                if(EntradaParaMinutosTimer.get()=="00"):
                    EntradaParaMinutosTimer.delete("0","end")

            def EntradaSegundos(evento):
                global MisHoras
                global MisMinutos
                global MisSegundos
                f= EntradaParaSegundosTimer.get()
                s = str(f)
                if(s==""):
                    EntradaParaSegundosTimer.insert("end","00")
                f = int(f)
                if(f>59 or f<0):
                    messagebox.showerror("Error","Error, los segundos deben estar entre 0 y 59")
                    EntradaParaSegundosTimer.focus_set()
            
            def EntradaSegundos2(evento):
                if(EntradaParaSegundosTimer.get()=="00"):
                    EntradaParaSegundosTimer.delete("0","end")

        def MeterDatos():
            global MisHoras
            global MisMinutos
            global MisSegundos
            global MiReloj
            global MiTimer
            MisHoras = EntradaParaHorasTimer.get()
            MisMinutos = EntradaParaMinutosTimer.get()
            MisSegundos = EntradaParaSegundosTimer.get()
            if(MisHoras=="" or MisMinutos=="" or MisSegundos==""):
                messagebox.showerror("Error","Que ningún espacio en el timer quedé vacío")
                return ""

            if(MisHoras!="00" or MisMinutos!="00" or MisSegundos!="00"):
                MisHoras = int(MisHoras)
                if(MisHoras<10):
                    MisHoras = str(MisHoras)
                    MisHoras = "0"+str(MisHoras)
                else:
                    MisHoras = str(MisHoras)
                MisMinutos = int(MisMinutos)
                if(MisMinutos<10):
                    MisMinutos = str(MisMinutos)
                    MisMinutos = "0"+str(MisMinutos)
                else:
                    MisMinutos = str(MisMinutos)

                MisSegundos = int(MisSegundos)
                if(MisSegundos<10):
                    MisSegundos = str(MisSegundos)
                    MisSegundos = "0"+str(MisSegundos)
                else:
                    MisSegundos = str(MisSegundos)
            elif(MiReloj!=True):
                MiReloj = False
                MiTimer = False

            AparecerReloj()
            vMenu.destroy()

        global DificultadJuego
        global Sonido

        Introduccion = tk.Label(vMenu,bg="#F7DC6F",text="Haga aquí la configuración del juego a su gusto\n si selecciona el cronometro utilice el botón para enviar los datos\n de lo contrario seleccione su opción y cierre la venta :)",pady=20).pack()

        NivelLabel = tk.Label(vMenu,bg="#F7DC6F",text="Nivel:").place(x=50,y=80)

        selecNivel = IntVar()

        if(DificultadJuego == "Facil"):
            BFacil = tk.Button(vMenu,relief="groove",bg="#2ED60C", text="Facil", command=Configuracion.ConDificultadFacil)
            BFacil.place(x=70,y=110)
        else:
            BFacil = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Facil", command=Configuracion.ConDificultadFacil)
            BFacil.place(x=70,y=110)

        if(DificultadJuego == "Intermedio"):
            BIntermedio = tk.Button(vMenu,relief="groove",bg="#2ED60C", text="Intermedio", command=Configuracion.ConDificultadIntermedio)
            BIntermedio.place(x=170,y=110)
        else:
            BIntermedio = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Intermedio", command=Configuracion.ConDificultadIntermedio)
            BIntermedio.place(x=170,y=110)

        BDificil = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Dificil", command=Configuracion.ConDificultadDificil)
        BDificil.place(x=300,y=110)

        RelojLabel = tk.Label(vMenu,bg="#F7DC6F",text="Reloj:").place(x=50,y=190)

        selecReloj = IntVar()
        if(MiReloj==True):
            BConReloj = tk.Button(vMenu,relief="groove",bg="#2ED60C", text="Con reloj", command=Configuracion.ConReloj)
            BConReloj.place(x=70,y=220)
        else:
            BConReloj = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Con reloj", command=Configuracion.ConReloj)
            BConReloj.place(x=70,y=220)
        if(MiReloj==False and MiTimer==False):
            BSinReloj = tk.Button(vMenu,relief="groove",bg="#2ED60C", text="Sin reloj", command=Configuracion.SinReloj)
            BSinReloj.place(x=170,y=220)
        else:
            BSinReloj = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Sin reloj", command=Configuracion.SinReloj)
            BSinReloj.place(x=170,y=220)
        if(MiTimer==True):
            BTimer = tk.Button(vMenu,relief="groove",bg="#2ED60C", text="Timer", command=Configuracion.ConTimer)
            BTimer.place(x=280,y=220)
        else:
            BTimer = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Timer", command=Configuracion.ConTimer)
            BTimer.place(x=280,y=220)

        EntradaParaHorasTimer = tk.Entry(vMenu, width=3, bg="white", font=("Helvetica",20,"italic bold"),bd=0, justify="center")
        EntradaParaHorasTimer.place(x=125,y=280)
        EntradaParaHorasTimer.bind("<FocusOut>",EntradaTimer.EntradaHoras)
        EntradaParaHorasTimer.bind("<FocusIn>",EntradaTimer.EntradaHoras2)
        EntradaParaHorasTimer.insert("end","00")

        EntradaParaMinutosTimer = tk.Entry(vMenu, width=3, bg="white", font=("Helvetica",20,"italic bold"),bd=0, justify="center")
        EntradaParaMinutosTimer.place(x=195,y=280)
        EntradaParaMinutosTimer.bind("<FocusOut>",EntradaTimer.EntradaMinutos)
        EntradaParaMinutosTimer.bind("<FocusIn>",EntradaTimer.EntradaMinutos2)
        EntradaParaMinutosTimer.insert("end","00")

        EntradaParaSegundosTimer = tk.Entry(vMenu, width=3, bg="white", font=("Helvetica",20,"italic bold"),bd=0, justify="center")
        EntradaParaSegundosTimer.place(x=265,y=280)
        EntradaParaSegundosTimer.bind("<FocusOut>",EntradaTimer.EntradaSegundos)
        EntradaParaSegundosTimer.bind("<FocusIn>",EntradaTimer.EntradaSegundos2)
        EntradaParaSegundosTimer.insert("end","00")

        TimerListo = tk.Button(vMenu, relief="groove", bg ="#A1E889", text="Jugar con cronometro", command=MeterDatos, width=18)
        TimerListo.place(x=130,y=350)

        if(MostrarEntradaTimer == False):
            EntradaParaHorasTimer.config(state="disabled")
            EntradaParaMinutosTimer.config(state="disabled")
            EntradaParaSegundosTimer.config(state="disabled")
            TimerListo.config(state="disabled")
            
        else:
            EntradaParaHorasTimer.config(state="normal")
            EntradaParaMinutosTimer.config(state="normal")
            EntradaParaSegundosTimer.config(state="normal")
            TimerListo.config(state="normal")
            

        SonidoLabel = tk.Label(vMenu,bg="#F7DC6F",text="Sonido:").place(x=50,y=400)

        selecSonidoFinal = IntVar()
        if(Sonido == "ConSonido"):
            BSonidoSi = tk.Button(vMenu,relief="groove",bg="#E25050",text="Con sonido", command=Configuracion.ConSonido)
            BSonidoSi.place(x=115,y=430)
        else:
            BSonidoSi = tk.Button(vMenu,relief="groove",bg="#F7DC6F",text="Con sonido", command=Configuracion.ConSonido)
            BSonidoSi.place(x=115,y=430)
        if(Sonido == "SinSonido"):
            BSonidoNo = tk.Button(vMenu,relief="groove",bg="#E25050", text="Sin sonido", command=Configuracion.SinSonido)
            BSonidoNo.place(x=215,y=430)
        else:
            BSonidoNo = tk.Button(vMenu,relief="groove",bg="#F7DC6F", text="Sin sonido", command=Configuracion.SinSonido)
            BSonidoNo.place(x=215,y=430)

        if(DificultadJuego=="Facil"):
            Configuracion.ConDificultadFacil()
        elif(DificultadJuego=="Intermedio"):
            Configuracion.ConDificultadIntermedio()

        if(MiReloj==True):
            Configuracion.ConReloj()
        elif(MiReloj==False and MiTimer == False):
            Configuracion.SinReloj()
        elif(MiTimer==True):
            Configuracion.ConTimer()

        if(Sonido=="ConSonido"):
            Configuracion.ConSonido()
        elif(Sonido=="SinSonido"):
            Configuracion.SinSonido()


        global TableroDeJuego

        labelCua = tk.Label(vMenu, text="En que cuadricula desea jugar: ",bg="#F7DC6F", font=('Helvetica',10,'italic bold'))
        labelCua.place(x=450,y=110)

        Cuadricula3x3 = tk.Button(vMenu,text="3x3",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula3x3['text']))
        Cuadricula3x3.place(x=510,y=140)

        Cuadricula4x4 = tk.Button(vMenu,text="4x4",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula4x4['text']))
        Cuadricula4x4.place(x=510,y=180)

        Cuadricula5x5 = tk.Button(vMenu,text="5x5",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula5x5['text']))
        Cuadricula5x5.place(x=510,y=220)

        Cuadricula6x6 = tk.Button(vMenu,text="6x6",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula6x6['text']))
        Cuadricula6x6.place(x=510,y=260)

        Cuadricula7x7 = tk.Button(vMenu,text="7x7",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula7x7['text']))
        Cuadricula7x7.place(x=510,y=300)

        Cuadricula8x8 = tk.Button(vMenu,text="8x8",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula8x8['text']))
        Cuadricula8x8.place(x=510,y=340)

        Cuadricula9x9 = tk.Button(vMenu,text="9x9",width=10,relief="groove",bg='#E25050',command=lambda: Configuracion.TipoCuadricula(Cuadricula9x9['text']))
        Cuadricula9x9.place(x=510,y=380)

        if(TableroDeJuego=='3x3'):
            Cuadricula3x3.config(bg="#2ED60C")
        elif(TableroDeJuego=='4x4'):
            Cuadricula4x4.config(bg='#2ED60C')
        elif(TableroDeJuego=='5x5'):
            Cuadricula5x5.config(bg="#2ED60C")
        elif(TableroDeJuego=='6x6'):
            Cuadricula6x6.config(bg='#2ED60C')
        elif(TableroDeJuego=='7x7'):
            Cuadricula7x7.config(bg='#2ED60C')
        elif(TableroDeJuego=='8x8'):
            Cuadricula8x8.config(bg="#2ED60C")
        elif(TableroDeJuego=='9x9'):
            Cuadricula9x9.config(bg='#2ED60C')

        vMenu.mainloop()

    class AyudaAlUsuario:
        def IrAlManual():
            webbrowser.open_new(r"https://drive.google.com/open?id=1KDZcxPOQneB4mA43FfZ1Nx2qnRT_4vAX")

        def IrAAcercaDe():            
            vAyuda = tk.Toplevel()
            vAyuda.title("Ayuda")
            vAyuda.geometry("550x300")
            vAyuda.config(bg="#FFF8A6")
            PalabrasParaElUsuario=tk.Label(vAyuda,bg="#FFF8A6",text="Para disfrutar mejor la experiencia del juego\n se recomienda leer el manual de usuario:",pady=28,font=("Arial",13,"italic bold"))
            PalabrasParaElUsuario.pack()
            photodescargar = tk.PhotoImage(file="descargarnube.png")
            BotonDescarga = tk.Button(vAyuda,image=photodescargar,command=AyudaAlUsuario.IrAlManual, bg="#FFF8A6",bd=0, cursor="hand2")
            BotonDescarga.pack()
            LabDes = tk.Label(vAyuda,text="descargar",font=("Arial",9,"italic bold"), bg="#FFF8A6")
            LabDes.pack()


            vAyuda.mainloop()

    class AcercaDelPrograma:
        def Acercade():
            def VolverAlJuegoDesdeAcerca():
                vAcerca.destroy()
            vAcerca = tk.Tk()
            vAcerca.geometry("500x300")
            vAcerca.title("Acerca de")
            vAcerca.config(bg="#FFF8A6")
            NombrePrograma = tk.Label(vAcerca,bg="#FFF8A6",text="Nombre: KenKen",pady=20)
            NombrePrograma.pack()
            versionPrograma = tk.Label(vAcerca,bg="#FFF8A6",text="Versión 1.0",pady=20)
            versionPrograma.pack()
            fechaCreacion = tk.Label(vAcerca,bg="#FFF8A6",text="Fecha de creación: 13 de octubre del 2018",pady=20)
            fechaCreacion.pack()
            NombreAutor = tk.Label(vAcerca,bg="#FFF8A6",text="Autor: Josué Gerardo Gutiérrez Mora",pady=20)
            NombreAutor.pack()
            volverAlJueguito = tk.Button(vAcerca,bd=1, bg="orange", relief="groove", text="Volver al menú", command=VolverAlJuegoDesdeAcerca).pack()
            vAcerca.mainloop()

if("Relojes"=="Relojes"):
    class ActualizarTiempo:
        def __init__(self, master):
            self.FrameTiempo = tk.Frame(master)
            self.FrameTiempo.configure(bg="white",width=95,height=22)
            self.FrameTiempo.place(x=660,y=50)

            self.LabelSegundos = tk.Label(self.FrameTiempo)
            self.LabelSegundos.config(font=("Helvetica",11,"bold italic"),bg="white",text="00")
            self.LabelSegundos.place(x=70)

            self.LabelMinutos = tk.Label(self.FrameTiempo)
            self.LabelMinutos.config(font=("Helvetica",11,"bold italic"),bg="white",text="00")
            self.LabelMinutos.place(x=40)

            self.LabelHoras = tk.Label(self.FrameTiempo)
            self.LabelHoras.config(font=("Helvetica",11,"bold italic"),bg="white",text="00")
            self.LabelHoras.place(x=10)

            self.seg = 0
            self.min = 0
            self.hor = 0

            self.update_Reloj()

        def update_Reloj(self):
            global destructor
            global destructorDerelojes
            if(destructor == True):
                self.seg = 0
                self.min = 0
                self.hor = 0
                destructor = False
            if(destructorDerelojes==True):
                destructorDerelojes = False
                self.FrameTiempo.destroy()
            if(PausarReloj==True):
                self.seg = int(self.seg)
                self.seg = self.seg + 1
                if(self.seg>59):
                    self.min = self.min + 1
                    self.seg = 0
                    if(self.min>59):
                        self.hor= self.hor + 1
                        self.min = 0
                        if(self.hor>23):
                            self.hor = 23
                            self.min = 59
                            self.seg = 59

                segundos = str(self.seg)
                minutos = str(self.min)
                horas = str(self.hor)

                if(self.seg<10):
                    segundos = "0"+str(self.seg)
                if(self.min<10):
                    minutos = "0"+str(self.min)
                if(self.hor<10):
                    horas = "0"+str(self.hor)

                self.LabelSegundos.configure(text=str(segundos))
                self.LabelMinutos.configure(text=str(minutos))
                self.LabelHoras.configure(text=str(horas))
                global MisSegundos
                global MisMinutos
                global MisHoras

                MisHoras = horas
                MisMinutos = minutos
                MisSegundos = segundos
                global TiempoJugador
                TiempoJugador = horas+":"+minutos+":"+segundos

            self.FrameTiempo.after(1000,self.update_Reloj)

        def PausarTiempo():
            global PausarReloj
            global BotonPausarTiempo
            global Bnumero1
            global Bnumero2
            global Bnumero3
            global Bnumero4
            global Bnumero5
            global Bnumero6
            global Bborrador
            if(PausarReloj == False):
                PausarReloj = True
                BotonPausarTiempo.config(text="Pausar",bg="#34FEF5")
                Bnumero1.config(state="normal")
                Bnumero2.config(state="normal")
                Bnumero3.config(state="normal")
                Bnumero4.config(state="normal")
                Bnumero5.config(state="normal")
                Bnumero6.config(state="normal")
                Bborrador.config(state="normal")
                BValidarJuego.config(state="normal")
                BOtroJuego.config(state="normal")
                BReiniciarJuego.config(state="normal")
                BTerminarJuego.config(state="normal")

            else:
                PausarReloj = False
                BotonPausarTiempo.config(text="Continuar", bg="red")
                Bnumero1.config(state="disabled")
                Bnumero2.config(state="disabled")
                Bnumero3.config(state="disabled")
                Bnumero4.config(state="disabled")
                Bnumero5.config(state="disabled")
                Bnumero6.config(state="disabled")
                Bborrador.config(state="disabled")
                BValidarJuego.config(state="disabled")
                BOtroJuego.config(state="disabled")
                BReiniciarJuego.config(state="disabled")
                BTerminarJuego.config(state="disabled")

    class ActualizarTimer:
        def __init__(self, master):
            global MisHoras
            global MisMinutos
            global MisSegundos
            self.FrameTiempo1 = tk.Frame(master)
            self.FrameTiempo1.configure(bg="white",width=95,height=20)
            self.FrameTiempo1.place(x=660,y=50)

            self.LabelSegundos = tk.Label(self.FrameTiempo1)
            self.LabelSegundos.config(font=("Helvetica",11,"bold italic"),bg="white",text=MisSegundos)
            self.LabelSegundos.place(x=70)

            self.LabelMinutos = tk.Label(self.FrameTiempo1)
            self.LabelMinutos.config(font=("Helvetica",11,"bold italic"),bg="white",text=MisMinutos)
            self.LabelMinutos.place(x=40)

            self.LabelHoras = tk.Label(self.FrameTiempo1)
            self.LabelHoras.config(font=("Helvetica",11,"bold italic"),bg="white",text=MisHoras)
            self.LabelHoras.place(x=10)

            self.seg = int(MisSegundos)
            self.min = int(MisMinutos)
            self.hor = int(MisHoras)
            

            self.seg2 = self.seg
            self.min2 = self.min
            self.hor2 = self.hor

            global con314
            con314 = 0
            self.update_Timer()

        def PausarTiempo():
            global PausarTimer
            global Bnumero1
            global Bnumero2
            global Bnumero3
            global Bnumero4
            global Bnumero5
            global Bnumero6
            global Bborrador
            if(PausarTimer == False):
                PausarTimer = True
                Bnumero1.config(state="normal")
                Bnumero2.config(state="normal")
                Bnumero3.config(state="normal")
                Bnumero4.config(state="normal")
                Bnumero5.config(state="normal")
                Bnumero6.config(state="normal")
                Bborrador.config(state="normal")
            else:
                PausarTimer = False
                Bnumero1.config(state="disabled")
                Bnumero2.config(state="disabled")
                Bnumero3.config(state="disabled")
                Bnumero4.config(state="disabled")
                Bnumero5.config(state="disabled")
                Bnumero6.config(state="disabled")
                Bborrador.config(state="disabled")

        def update_Reloj2(self):
            global MisHoras
            global MisMinutos
            global MisSegundos
            global TiempoJugador
            global PausarTimer

            segundos = str(self.seg2)
            minutos = str(self.min2)
            horas = str(self.hor2)

            MisHoras = horas
            MisMinutos = minutos
            MisSegundos = segundos

            if(self.seg2<10):
                segundos = "0"+str(self.seg2)
                MisSegundos = segundos
            if(self.min2<10):
                minutos = "0"+str(self.min2)
                MisMinutos = minutos
            if(self.hor2<10):
                horas = "0"+str(self.hor2)
                MisHoras = horas     

            if(PausarTimer==True):
                self.LabelSegundos.configure(text=str(segundos))
                self.LabelMinutos.configure(text=str(minutos))
                self.LabelHoras.configure(text=str(horas))   
                self.seg2 = self.seg2 + 1
                if(self.seg2>59):
                    self.min2 = self.min2 + 1
                    self.seg2 = 0
                    if(self.min2>59):
                        self.hor2= self.hor2 + 1
                        self.min2 = 0
                        if(self.hor2>23):
                            self.hor2 = 23
                            self.min2 = 59
                            self.seg2 = 59
            
                TiempoJugador = MisHoras+":"+MisMinutos+":"+MisSegundos
            self.FrameTiempo1.after(1000,self.update_Reloj2)

        def update_Timer(self):
            global MisHoras
            global MisMinutos
            global MisSegundos
            global destructor
            global destructorDerelojes

            if(destructorDerelojes==True):
                self.FrameTiempo1.destroy()
                self.LabelHoras.destroy()
                self.LabelMinutos.destroy()
                self.LabelSegundos.destroy()
                F = tk.Frame(vPrincipal,bg="#F7DC6F",width=100,height=20)
                F.place(x=660,y=50)
                destructorDerelojes=False

            if(PausarTimer == True):
                self.seg = self.seg - 1
                if(self.seg<0 and (self.min!=0 or self.hor!=0)):
                    self.seg = 59
                    self.min = self.min-1

                    if(self.min<=0 and self.hor!=0):
                        self.min = 59
                        self.hor = self.hor - 1

                        if(self.min<0):
                            self.hor= self.hor - 1
                            self.min = 59

                            if(self.hor<=0):
                                self.hor = 0

                    elif(self.min<=0):
                        self.min = 0

                elif(self.seg < -1):
                    self.seg = 0
                
                MisHoras = str(self.hor)
                MisMinutos = str(self.min)
                MisSegundos = str(self.seg)
                segundos = str(self.seg)
                minutos = str(self.min)
                horas = str(self.hor)
                if(self.seg<10):
                    segundos = "0"+str(self.seg)
                    MisSegundos = segundos
                if(self.min<10):
                    minutos = "0"+str(self.min)
                    MisMinutos = minutos
                if(self.hor<10):
                    horas = "0"+str(self.hor)
                    MisHoras = horas
                self.LabelSegundos.configure(text=str(segundos))
                self.LabelMinutos.configure(text=str(minutos))
                self.LabelHoras.configure(text=str(horas))

            if(self.seg==0 and self.min==0 and self.hor==0):
                global con314
                if(con314==0):
                    con314 = con314 + 1
                    if messagebox.askyesno("Continuar?","Tiempo expirado ¿desea continuar el mismo juego?"):
                        self.update_Reloj2()
                    else:
                        MisHoras = "00"
                        MisMinutos = "00"
                        MisSegundos = "00"
                        mixer.music.stop()
                        CuadriculaCeldas.place_forget()
                        BIniciarJuego.config(state="normal")
                        BotonIrAConfiguracion.config(state="normal")
                        BotonIrAAcercaDe.config(state="normal")
                        BotonAyuda.config(state="normal")
                        BValidarJuego.config(state="disabled")
                        BOtroJuego.config(state="disabled")
                        BReiniciarJuego.config(state="disabled")
                        BTerminarJuego.config(state="disabled")

                        if(MiTimer==True or MiReloj==True):
                            BotonPausarTiempo.destroy()
                        self.FrameTiempo1.destroy()
                        F = tk.Frame(vPrincipal,bg="#F7DC6F",width=100,height=20)
                        F.place(x=660,y=50)
            else:
                self.FrameTiempo1.after(1000,self.update_Timer)

def validarNombre():
    global NombreJugador
    global MiTimer
    nom = EntradaNombre.get()
    if(len(nom)>30 or len(nom)<3):
        messagebox.showerror("Error en nombre","Debe escribir entre 3 y 30 caracteres")
        EntradaNombre.focus()

    if(len(nom)>=3 and len(nom)<=30):
        BValidarNombre.config(state="disabled")
        BIniciarJuego.config(state="normal")
        EntradaNombre.config(state="disabled",disabledbackground="#3FE108", disabledforeground="#ffffff")  
        NombreJugador = EntradaNombre.get()
        BotonIrAConfiguracion.config(state="normal")
        if(MiTimer == True):
            IrAConfiguracion()

if("Cuadricula"=="Cuadricula"):
    CuadriculaCeldas = tk.Frame()
    widgetEncendido = False

    def CasillaEnfocada(r,c):
        global widget
        global widgetEncendido
        widgetEncendido = True
        widget = CuadriculaCeldas.grid_slaves(row=r, column=c)[0]
        widget.config(bg="#E3FACF")
        wid = CuadriculaCeldas.grid_slaves(row=r-1,column=c)[0]
        wid.config(bg="#E3FACF")

    def CasillaDesenfocada(color,r,c):
        global widgetEncendido
        widgetEncendido=False
        widget = CuadriculaCeldas.grid_slaves(row=r, column=c)[0]
        widget.config(bg=color)
        wid = CuadriculaCeldas.grid_slaves(row=r-1,column=c)[0]
        wid.config(bg=color)

    def insertador(w):
        global widget
        global widgetEncendido
        if(widgetEncendido==True):
            if(w=="Borrar"):
                widget.delete("0","end")
            else:
                widget.delete("0","end")
                widget.insert("end",w)
        else:
            messagebox.showerror("Error","Ninguna casilla seleccionada")


    Bnumero1 = tk.Button(vPrincipal,font=("Helvetica",15), background="#34FEAF",relief="groove", text="1",padx=10,command=lambda: insertador(Bnumero1['text']))
    Bnumero1.place(x=90,y=70)

    Bnumero2 = tk.Button(vPrincipal,font=("Helvetica",15), background="#34FEAF",relief="groove", text="2",padx=10,command=lambda: insertador(Bnumero2['text']))
    Bnumero2.place(x=90,y=130)

    Bnumero3 = tk.Button(vPrincipal,font=("Helvetica",15), background="#34FEAF",relief="groove", text="3",padx=10,command=lambda: insertador(Bnumero3['text']))
    Bnumero3.place(x=90,y=190)

    Bnumero4 = tk.Button(vPrincipal,font=("Helvetica",15), background="#34FEAF",relief="groove", text="4",padx=10,command=lambda: insertador(Bnumero4['text']))
    Bnumero4.place(x=90,y=250)

    Bnumero5 = tk.Button(vPrincipal,font=("Helvetica",15), background="#34FEAF",relief="groove", text="5",padx=10,command=lambda: insertador(Bnumero5['text']))
    Bnumero5.place(x=90,y=310)

    Bnumero6 = tk.Button(vPrincipal,font=("Helvetica",15), background="#34FEAF",relief="groove", text="6",padx=10,command=lambda: insertador(Bnumero6['text']))
    Bnumero6.place(x=90,y=370)

    photo = tk.PhotoImage(file="borrador.png")
    Bborrador = tk.Button(vPrincipal,font=("Helvetica",15), image=photo,background="#34FEAF",relief="groove", text="Borrar",padx=10,command=lambda: insertador(Bborrador['text']))
    Bborrador.place(x=18,y=200)


    def colored(Dic,Coordenadas):
        contaDic=1
        while(contaDic<=len(Dic)):
            ConfCasilla = Dic[contaDic]
            ContaCasi = 0
            while(ContaCasi<len(ConfCasilla)):
                if(ConfCasilla[ContaCasi]==Coordenadas):
                    return ConfCasilla[-1]
                else:
                    ContaCasi = ContaCasi+1
            contaDic = contaDic + 1

    def ColocarNum(Dic,Coordenadas):
        contaDic=1
        while(contaDic<=len(Dic)):
            ConfCasilla = Dic[contaDic]
            if(ConfCasilla[1]==Coordenadas):
                return ConfCasilla[0]
            else:
                contaDic = contaDic+1

    def GeneradorJuego():
        avrir = open('kenken_juegos.dat','rb')
        while True:
            try:
                JuegosDeKenken = pickle.load(avrir)
            except EOFError:
                break
        avrir.close()
        global TableroDeJuego
        if(TableroDeJuego=='3x3'):
            numRandom = random.randint(0,2)
        elif(TableroDeJuego=='4x4'):
            numRandom = random.randint(3,5)
        elif(TableroDeJuego=='5x5'):
            numRandom = random.randint(6,8)
        elif(TableroDeJuego=='6x6'):
            numRandom = random.randint(9,11)
        elif(TableroDeJuego=='7x7'):
            numRandom = random.randint(12,14)
        elif(TableroDeJuego=='8x8'):
            numRandom = random.randint(15,16)
        elif(TableroDeJuego=='9x9'):
            numRandom = random.randint(17,18)
        global JuegoActual
        print(numRandom)
        JuegoActual = JuegosDeKenken[numRandom]
        return JuegoActual

    def GeneradorJuego2(otro):
        avrir = open('kenken_juegos.dat','rb')
        while True:
            try:
                JuegosDeKenken = pickle.load(avrir)
            except EOFError:
                break
        avrir.close()
        global TableroDeJuego
        if(TableroDeJuego=='3x3'):
            numRandom = random.randint(0,2)
        elif(TableroDeJuego=='4x4'):
            numRandom = random.randint(3,5)
        elif(TableroDeJuego=='5x5'):
            numRandom = random.randint(6,8)
        elif(TableroDeJuego=='6x6'):
            numRandom = random.randint(9,11)
        elif(TableroDeJuego=='7x7'):
            numRandom = random.randint(12,14)
        elif(TableroDeJuego=='8x8'):
            numRandom = random.randint(15,16)
        elif(TableroDeJuego=='9x9'):
            numRandom = random.randint(17,18)
        print(numRandom,"Pollo")
        OtroJuegazo = JuegosDeKenken[numRandom]
        if(OtroJuegazo==otro):
            return GeneradorJuego2(otro)
        else:
            return OtroJuegazo

    def Cuadricula(JuegoActual):
        global CuadriculaCeldas
        CuadriculaCeldas = tk.Frame(bg="black",relief="solid",bd=2)
        CuadriculaCeldas.place(x=150,y=60)
        global TableroDeJuego
        if(TableroDeJuego=='3x3'):
            for r in range(6):
                for c in range(3):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic",33))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",42),width=4, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))

        elif(TableroDeJuego=='4x4'):
            for r in range(8):
                for c in range(4):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic",22))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",34),width=4, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))

        elif(TableroDeJuego=='5x5'):
            for r in range(10):
                for c in range(5):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic",16))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",28),width=4, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))

        elif(TableroDeJuego=='6x6'):
            for r in range(12):
                for c in range(6):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic"))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",23),width=4, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))


        elif(TableroDeJuego=='7x7'):
            for r in range(14):
                for c in range(7):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic"))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",17),width=4, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))

        elif(TableroDeJuego=='8x8'):
            for r in range(16):
                for c in range(8):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic",8))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",16),width=4, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))

        elif(TableroDeJuego=='9x9'):
            for r in range(18):
                for c in range(9):
                    if(r==0 or r%2==0):
                        coloreado = colored(JuegoActual,(r+1,c))
                        texto = ColocarNum(JuegoActual,(r+1,c))
                        lavelNumeros = tk.Label(CuadriculaCeldas,text=texto,bg=coloreado,anchor="w", font=("comic",7))
                        lavelNumeros.grid(row=r,column=c,sticky="we",padx=1)
                    else:
                        coloreado = colored(JuegoActual,(r,c))
                        Entrada = tk.Entry(CuadriculaCeldas,font=("Arial",13),width=5, justify="center",bd=0, bg=coloreado)
                        Entrada.grid(row=r,column=c,padx=1,pady=(0,2))

                        Entrada.bind("<FocusIn>",lambda event, r=r, c=c: CasillaEnfocada(r,c))
                        Entrada.bind("<FocusOut>",lambda event,color=coloreado, r=r, c=c: CasillaDesenfocada(color,r,c))
      
def AparecerReloj():
    if(MiReloj==True and MiTimer==False):
        ActualizarTiempo(vPrincipal)
    elif(MiTimer==True and MiReloj==False):
        ActualizarTimer(vPrincipal)

def AparecerPausador():
    global BotonPausarTiempo
    if(MiReloj==True and MiTimer==False):
        BotonPausarTiempo = tk.Button(vPrincipal, text="Pausar", command=ActualizarTiempo.PausarTiempo, bg="#34FEF5",bd=5, relief="groove",width=13,state="normal")
        BotonPausarTiempo.place(x=655,y=80)
    elif(MiTimer==True and MiReloj==False):
        BotonPausarTiempo = tk.Button(vPrincipal, text="Pausar", command=ActualizarTimer.PausarTiempo, bg="#34FEF5",bd=5, relief="groove",width=13,state="normal")
        BotonPausarTiempo.place(x=655,y=80)

class FuncionesTiempo:
    def ListaTiempo(lista):
        primerLista = []
        for i in lista:
            if(i!=("vacio","vacio")):
                dato1 = i[1]
                dato1 = dato1.split(":")
                cadenaN = ""
                for n in dato1:
                    cadenaN = cadenaN+n
                primerLista.append(cadenaN)
        segundaLista = []
        for a in primerLista:
            dato1 = int(a)
            segundaLista.append(dato1)
        segundaLista = sorted(segundaLista)
        TerceraLista = []
        for u in segundaLista:
            datoEnString = str(u)
            TerceraLista.append(datoEnString)

        contador = 0
        cuartaLista = []
        while(contador<len(TerceraLista)):
            while(len(TerceraLista[contador])<6):
                TerceraLista[contador] = "0"+TerceraLista[contador]
            cuartaLista.append(TerceraLista[contador])
            contador = contador +1 

        quintaLista = []
        contador = 0
        while(contador<len(cuartaLista)):
            hora = cuartaLista[contador]
            cadena = ""
            con = 0
            while(con<len(hora)):
                cadena=cadena+hora[con]
                if(con==1):
                    cadena=cadena+":"
                elif(con==3):
                    cadena=cadena+":"
                con=con+1
            quintaLista.append(cadena)
            contador = contador + 1

        return quintaLista
                
    def OrganizarListaTiempo(ListaPuntuaciones):
        global NombreJugador
        nuevasHoras = FuncionesTiempo.ListaTiempo(ListaPuntuaciones)
        ListaFinal = []
        contador = 0
        while(contador<len(nuevasHoras)):
            conta=0
            while(conta<len(ListaPuntuaciones)):
                if(nuevasHoras[contador]==ListaPuntuaciones[conta][1]):
                    ListaFinal.append(ListaPuntuaciones[conta])
                    ListaPuntuaciones.pop(conta)
                    conta = conta + 1
                else:
                    conta=conta+1
            contador = contador+1
        if(len(ListaFinal)<10):
            while(len(ListaFinal)<10):
                ListaFinal.append(("vacio","vacio"))
        elif(len(ListaFinal)>10):
            while(len(ListaFinal)>10):
                ListaFinal.pop(len(ListaFinal)-1)
        return ListaFinal

class Ranking:
    def EstaEnElRanking(lista,NombreJugador):
        NombreJugador = EntradaNombre.get()
        contador = 0
        while(contador<len(lista)):
            if(NombreJugador==lista[contador][0]):
                return True
            contador = contador+1
        return False

    def IngresarAlRanking():
        global NombreJugador
        global TiempoJugador

        global PuestoNombre1
        global PuestoNombre2
        global PuestoNombre3
        global PuestoNombre4
        global PuestoNombre5
        global PuestoNombre6
        global PuestoNombre7
        global PuestoNombre8
        global PuestoNombre9
        global PuestoNombre10

        global PuestoTiempo1
        global PuestoTiempo2
        global PuestoTiempo3
        global PuestoTiempo4
        global PuestoTiempo5
        global PuestoTiempo6
        global PuestoTiempo7
        global PuestoTiempo8
        global PuestoTiempo9
        global PuestoTiempo10

        global JuegoFinalizado
        ListaJugadores = []
        Avrir = open("kenken_top10.dat","rb")
        while True:
            try:
                x = pickle.load(Avrir)
                for i in x:
                    ListaJugadores.append(i)
            except EOFError:
                if(ListaJugadores==[]):
                    ListaJugadores = FuncionesTiempo.OrganizarListaTiempo(ListaJugadores)
                break
        Avrir.close()
        Avrir=open("kenken_top10.dat","wb")
        Avrir.close()

        if(NombreJugador!="" and TiempoJugador!="" and JuegoFinalizado == True):
            ListaJugadores.insert(0,(NombreJugador,TiempoJugador))
            JuegoFinalizado = False
        ListaJugadores = FuncionesTiempo.OrganizarListaTiempo(ListaJugadores)
        """if(Ranking.EstaEnElRanking(ListaJugadores,NombreJugador)==True):
                                    messagebox.showinfo("Felicidades!","Felidades! Eres parte del top 10")
                                    print("Felicidades! Entraste al top 10")"""
        PuestoNombre1 = ListaJugadores[0][0]
        PuestoNombre2 = ListaJugadores[1][0]
        PuestoNombre3 = ListaJugadores[2][0]
        PuestoNombre4 = ListaJugadores[3][0]
        PuestoNombre5 = ListaJugadores[4][0]
        PuestoNombre6 = ListaJugadores[5][0]
        PuestoNombre7 = ListaJugadores[6][0]
        PuestoNombre8 = ListaJugadores[7][0]
        PuestoNombre9 = ListaJugadores[8][0]
        PuestoNombre10 = ListaJugadores[9][0]

        PuestoTiempo1 = ListaJugadores[0][1]
        PuestoTiempo2 = ListaJugadores[1][1]
        PuestoTiempo3 = ListaJugadores[2][1]
        PuestoTiempo4 = ListaJugadores[3][1]
        PuestoTiempo5 = ListaJugadores[4][1]
        PuestoTiempo6 = ListaJugadores[5][1]
        PuestoTiempo7 = ListaJugadores[6][1]
        PuestoTiempo8 = ListaJugadores[7][1]
        PuestoTiempo9 = ListaJugadores[8][1]
        PuestoTiempo10 = ListaJugadores[9][1]

        Avrir = open("kenken_top10.dat","wb")
        pickle.dump(ListaJugadores,Avrir)
        Avrir.close()

def AbrirTop():
    global NombreJugador
    global TiempoJugador

    global PuestoNombre1
    global PuestoNombre2
    global PuestoNombre3
    global PuestoNombre4
    global PuestoNombre5
    global PuestoNombre6
    global PuestoNombre7
    global PuestoNombre8
    global PuestoNombre9
    global PuestoNombre10

    global PuestoTiempo1
    global PuestoTiempo2
    global PuestoTiempo3
    global PuestoTiempo4
    global PuestoTiempo5
    global PuestoTiempo6
    global PuestoTiempo7
    global PuestoTiempo8
    global PuestoTiempo9
    global PuestoTiempo10

    vTabla = tk.Tk()
    vTabla.geometry("500x400")
    vTabla.title("Puntuaciones")
    vTabla.config(bg="#FFFFBF")

    ContenerPuntos = tk.Frame(vTabla, bg="#FFFFBF")
    ContenerPuntos.place(x=80,y=40)
    LlamarAlaClaseParaQueTodoSeAcctualice = Ranking.IngresarAlRanking()
    primo1 = tk.StringVar()
    primo1 = ("1. "+PuestoNombre1)
    primo = tk.Label(ContenerPuntos, width=28, bg="#8DCBFF", text=primo1)
    primo.grid(row=1,column=1, pady=6)
    primo1Tempo = tk.StringVar()
    primo1Tempo=(PuestoTiempo1)
    primoTempo = tk.Label(ContenerPuntos,width=15, bg="#B3FF8D", text=primo1Tempo)
    primoTempo.grid(row=1, column=2, pady=6)

    secondo1 = tk.StringVar()
    secondo1=("2. "+PuestoNombre2)
    secondo = tk.Label(ContenerPuntos, text=secondo1, width=28, bg="#8DCBFF")
    secondo.grid(row=2,column=1, pady=6)
    secondo1Tempo = tk.StringVar()
    secondo1Tempo=(PuestoTiempo2)
    secondoTempo = tk.Label(ContenerPuntos, text=secondo1Tempo,width=15, bg="#B3FF8D")
    secondoTempo.grid(row=2, column=2, pady=6)

    terzo1 = tk.StringVar()
    terzo1=("3. "+PuestoNombre3)
    terzo = tk.Label(ContenerPuntos, text=terzo1, width=28, bg="#8DCBFF")
    terzo.grid(row=3,column=1, pady=6)
    terzo1Tempo = tk.StringVar()
    terzo1Tempo=(PuestoTiempo3)
    terzoTempo = tk.Label(ContenerPuntos, text=terzo1Tempo,width=15, bg="#B3FF8D")
    terzoTempo.grid(row=3, column=2, pady=6)

    quarto1 = tk.StringVar()
    quarto1=("4. "+PuestoNombre4)
    quarto = tk.Label(ContenerPuntos, text=quarto1, width=28, bg="#8DCBFF")
    quarto.grid(row=4,column=1, pady=6)
    quarto1Tempo = tk.StringVar()
    quarto1Tempo=(PuestoTiempo4)
    quartoTempo = tk.Label(ContenerPuntos, text=quarto1Tempo,width=15, bg="#B3FF8D")
    quartoTempo.grid(row=4, column=2, pady=6)

    quinto1 = tk.StringVar()
    quinto1=("5."+PuestoNombre5)
    quinto = tk.Label(ContenerPuntos, text=quinto1, width=28, bg="#8DCBFF")
    quinto.grid(row=5,column=1, pady=6)
    quinto1Tempo = tk.StringVar()
    quinto1Tempo=(PuestoTiempo5)
    quintoTempo = tk.Label(ContenerPuntos, text=quinto1Tempo,width=15, bg="#B3FF8D")
    quintoTempo.grid(row=5, column=2, pady=6)

    sexto1 = tk.StringVar()
    sexto1=("6. "+PuestoNombre6)
    sexto = tk.Label(ContenerPuntos, text=sexto1, width=28, bg="#8DCBFF")
    sexto.grid(row=6,column=1, pady=6)
    sexto1Tempo = tk.StringVar()
    sexto1Tempo=(PuestoTiempo6)
    sextoTempo = tk.Label(ContenerPuntos, text=sexto1Tempo,width=15, bg="#B3FF8D")
    sextoTempo.grid(row=6, column=2, pady=6)

    settimo1 = tk.StringVar()
    settimo1=("7. "+PuestoNombre7)
    settimo = tk.Label(ContenerPuntos, text=settimo1, width=28, bg="#8DCBFF")
    settimo.grid(row=7,column=1, pady=6)
    settimo1Tempo = tk.StringVar()
    settimo1Tempo=(PuestoTiempo7)
    settimoTempo = tk.Label(ContenerPuntos, text=settimo1Tempo,width=15, bg="#B3FF8D")
    settimoTempo.grid(row=7, column=2, pady=6)

    octavo1 = tk.StringVar()
    octavo1=("8. "+PuestoNombre8)
    octavo = tk.Label(ContenerPuntos, text=octavo1, width=28, bg="#8DCBFF")
    octavo.grid(row=8,column=1, pady=6)
    octavo1Tempo = tk.StringVar()
    octavo1Tempo=(PuestoTiempo8)
    octavoTempo = tk.Label(ContenerPuntos, text=octavo1Tempo,width=15, bg="#B3FF8D")
    octavoTempo.grid(row=8, column=2, pady=6)

    nono1 = tk.StringVar()
    nono1=("9. "+PuestoNombre9)
    nono = tk.Label(ContenerPuntos, text=nono1, width=28, bg="#8DCBFF")
    nono.grid(row=9,column=1, pady=6)
    nono1Tempo = tk.StringVar()
    nono1Tempo=(PuestoTiempo9)
    nonoTempo = tk.Label(ContenerPuntos, text=nono1Tempo,width=15, bg="#B3FF8D")
    nonoTempo.grid(row=9, column=2, pady=6)

    decimo1 = tk.StringVar()
    decimo1=("10. "+PuestoNombre10)
    decimo = tk.Label(ContenerPuntos, text=decimo1, width=28, bg="#8DCBFF")
    decimo.grid(row=10,column=1, pady=6)
    decimo1Tempo = tk.StringVar()
    decimo1Tempo=(PuestoTiempo10)
    decimoTempo = tk.Label(ContenerPuntos, text=decimo1Tempo,width=15, bg="#B3FF8D")
    decimoTempo.grid(row=10, column=2, pady=6)

    vTabla.mainloop()

if("Analizar"=="Analizar"):
    def SeRepitenNumeros(lista):
        for i in lista:
            if(lista.count(i)>1):
                return True
        return False

    def AnalizarFilas():
        global TableroFilasColumnas
        for r in range(TableroFilasColumnas[0]):
            lista = []
            for c in range(TableroFilasColumnas[1]):
                if(r!=0 and r%2!=0):
                    DatoEnEntrada = CuadriculaCeldas.grid_slaves(row=r,column=c)[0]
                    DatoEnEntrada = DatoEnEntrada.get()
                    if(DatoEnEntrada!=""):
                        lista.append(DatoEnEntrada)
            if(r!=0 and r%2!=0):
                if(SeRepitenNumeros(lista)==True):
                    return False
        return True

    def AnalizarColumnas():
        global TableroFilasColumnas
        for c in range(TableroFilasColumnas[1]):
            lista = []
            for r in range(TableroFilasColumnas[0]):
                if(r!=0 and r%2!=0):
                    DatoEnEntrada = CuadriculaCeldas.grid_slaves(row=r,column=c)[0]
                    DatoEnEntrada = DatoEnEntrada.get()
                    if(DatoEnEntrada!=""):
                        lista.append(DatoEnEntrada)
            if(r!=0 and r%2!=0):
                if(SeRepitenNumeros(lista)==True):
                    return False
        return True

    def Sumador(num,listaNumeros):
        resultado = 0
        for i in listaNumeros:
            resultado = resultado + i

        if(resultado==num):
            return True
        else:
            return False

    def Multiplicador(num,listaNumeros):
        resultado = 1
        for i in listaNumeros:
            resultado = resultado * i
        if(resultado==num):
            return True
        else:
            return False

    def Restador(num,listaNumeros):
        listaNumeros.sort()
        listaNumeros = listaNumeros[::-1]
        resultado = listaNumeros[0]*2
        for i in listaNumeros:
            resultado = resultado - i
        if(resultado==num):
            return True
        else:
            return False

    def Divisor(num,listaNumeros):
        listaNumeros.sort()
        listaNumeros = listaNumeros[::-1]
        resultado = listaNumeros[0]*listaNumeros[0]
        for i in listaNumeros:
            resultado = resultado / i
        if(resultado==num):
            return True
        else:
            return False

    def Operador(num, operacion, lista):
        num = int(num)
        NumerosPoperacion = []
        cont = 0
        while(cont<len(lista)):
            r = lista[cont][0]
            c = lista[cont][1]
            w = CuadriculaCeldas.grid_slaves(row=r, column=c)[0]
            w = w.get()
            if(w==""):
                return False
            w = int(w)
            NumerosPoperacion.append(w)
            cont = cont + 1
        if(operacion=="x"):
            M=Multiplicador(num,NumerosPoperacion)
            if(M==False):
                return False
        elif(operacion=="+"):
            S=Sumador(num, NumerosPoperacion)
            if(S==False):
                return False
        elif(operacion=="/"):
            D=Divisor(num,NumerosPoperacion)
            if(D==False):
                return False
        elif(operacion=="-"):
            R=Restador(num,NumerosPoperacion)
            if(R==False):
                return False
        elif(operacion==num):
            if(int(operacion)!=w):
                return False
        return True

    def retornaSoloNumero(num):
        c = 0
        numero = ""
        while(c<len(num)):
            if(num[c].isdigit()):
                numero=numero+num[c]
            c = c+1
        return numero

    def AnalisisResultados():
        global JuegoActual
        contador = 1
        while(contador<=len(JuegoActual)):
            AnalisisLinea = JuegoActual[contador]
            cont = 0
            while(cont<len(AnalisisLinea)):
                num = retornaSoloNumero(AnalisisLinea[0])
                operacion = AnalisisLinea[0][-1]
                if(operacion.isdigit()):
                    operacion = num
                lista = []
                co = 0
                while(co<len(AnalisisLinea)):
                    if(type(AnalisisLinea[co])==tuple):
                        lista.append(AnalisisLinea[co])
                    co = co+1
                cont = cont + 1
            EsNoEs = Operador(num, operacion, lista)
            if(EsNoEs==False):
                return False
            contador = contador + 1
        return True

    def AnalisisCompleto():
        global MiReloj
        global MiTimer
        global PausarTimer
        global PausarReloj
        if(AnalizarColumnas()==False):
            if(MiReloj==True):
                PausarReloj = False
            if(MiTimer==True):
                PausarTimer = False
            if messagebox.showerror("Error C","En alguna de las COLUMNAS hay numeros repetidos\n checalo y arreglalo ;D"):
                if(MiReloj==True):
                    PausarReloj = True
                if(MiTimer==True):
                    PausarTimer = True
        else:
            if(AnalizarFilas()==False):
                if(MiReloj==True):
                    PausarReloj = False
                if(MiTimer==True):
                    PausarTimer = False
                if messagebox.showerror("Error F","En alguna de las FILAS hay numeros repetidos\n checalo y arreglalo ;D"):
                    if(MiReloj==True):
                        PausarReloj = True
                    if(MiTimer==True):
                        PausarTimer = True                    
            else:
                if(AnalisisResultados()==False):
                    if(MiReloj==True):
                        PausarReloj = False
                    if(MiTimer==True):
                        PausarTimer = False
                    if messagebox.showerror("Error +-*/","En alguna(s) de las casillas te has equivocado\n y no da el resultado que se pide, buscalo y arreglalo ;D"):
                        if(MiReloj==True):
                            PausarReloj = True
                        if(MiTimer==True):
                            PausarTimer = True                      
                    return False
                else:
                    if(MiReloj==True):
                        PausarReloj = False
                    if(MiTimer==True):
                        PausarTimer = False
                    if(Sonido=="ConSonido"):
                        mixer.music.stop()
                        mixer.music.load("nivelcompletado.mp3")
                        mixer.music.play()
                    messagebox.showinfo("Ganaste","GANASTE!!! MUCHAS FELICIDADES")
                    return True



#-----------------------------------INICIAR COMANDOS PARA BOTONES DE JUEGO------------------------------------------------------
Msj = tk.Label()
def MensajeDeConfiguracion(evento):
    if(BIniciarJuego['state']!="disabled"):
        global Msj
        Msj = tk.Label(vPrincipal,text="Si desea puede ir a la configuracion del juego y cambiar\n los parametros de juego :)", bg="#62E71F")
        Msj.place(x=50,y=430)
        BotonIrAConfiguracion.config(bg="#00FF27")

def DejarMensajeConfiguracion(evento):
        global Msj
        Msj.config(text="",bg="#F7DC6F")
        BotonIrAConfiguracion.config(bg="white")

def IniciarJuego():
    global MiReloj
    global MiTimer
    global MisHoras
    global MisMinutos
    global MisSegundos
    global destructor
    global MiMusica
    global Sonido
    BIniciarJuego.config(state="disabled")
    BValidarJuego.config(state="normal")
    BOtroJuego.config(state="normal")
    BReiniciarJuego.config(state="normal")
    BTerminarJuego.config(state="normal")
    BotonIrAConfiguracion.config(state="disabled")
    BotonAyuda.config(state="disabled")
    BotonIrAAcercaDe.config(state="disabled")

    if(MiReloj==True):
        destructor = True

    if(MiReloj==True):
        AparecerPausador()
        ActualizarTiempo.PausarTiempo()
    elif(MiTimer==True):
        if(MisHoras=="00" and MisMinutos=="00" and MisSegundos=="00"):
            MiTimer=False
            MiReloj=False
        else:
            AparecerPausador()
            ActualizarTimer.PausarTiempo()

    Cuadricula(GeneradorJuego())
    if(MiReloj == True or MiTimer == True):
        AparecerReloj()

    if(Sonido=="ConSonido"):
        mixer.music.load("mario.mp3")
        mixer.music.play(-1)
    
def ValidarJuego():
    global NombreJugador
    global TiempoJugador
    global MiReloj
    global MiTimer
    global BotonPausarTiempo
    global JuegoFinalizado
    global PausarReloj 
    global PausarTimer
    global BotonPausarTiempo
    global MisHoras
    global MisMinutos
    global MisSegundos
    global destructor
    global destructorDerelojes
    if(AnalisisCompleto()==True):
        if(MiReloj==True):
            destructor = True
            destructorDerelojes = True
            MisHoras = "00"
            MisMinutos = "00"
            MisSegundos = "00"
            CuadriculaCeldas.place_forget()
            BIniciarJuego.config(state="normal")
            BotonIrAConfiguracion.config(state="normal")
            BotonIrAAcercaDe.config(state="normal")
            BotonAyuda.config(state="normal")
            BValidarJuego.config(state="disabled")
            BOtroJuego.config(state="disabled")
            BReiniciarJuego.config(state="disabled")
            BTerminarJuego.config(state="disabled")
            if(MiTimer==True or MiReloj==True):
                BotonPausarTiempo.destroy()
            MT = MiTimer
            MR = MiReloj
            MiTimer = False
            MiReloj = False

            if(Sonido=="ConSonido"):
                mixer.music.stop()
            MiTimer = MT
            MiReloj = MR
            
            JuegoFinalizado = True
            AbrirTop()

        elif(MiTimer==True):
            destructor = True
            
            MisHoras = "00"
            MisMinutos = "00"
            MisSegundos = "00"
            CuadriculaCeldas.place_forget()
            BIniciarJuego.config(state="normal")
            BotonIrAConfiguracion.config(state="normal")
            BotonIrAAcercaDe.config(state="normal")
            BotonAyuda.config(state="normal")
            BValidarJuego.config(state="disabled")
            BOtroJuego.config(state="disabled")
            BReiniciarJuego.config(state="disabled")
            BTerminarJuego.config(state="disabled")
            if(MiTimer==True or MiReloj==True):
                BotonPausarTiempo.destroy()
            MiTimer = False
            MiReloj = False
            F = tk.Frame(vPrincipal,bg="#F7DC6F",width=100,height=20)
            F.place(x=660,y=50)

            if(Sonido=="ConSonido"):
                mixer.music.stop()
            JuegoFinalizado = True

def OtroJuego():
    global CuadriculaCeldas
    global PausarReloj 
    global PausarTimer
    global BotonPausarTiempo
    global MiReloj
    global MiTimer
    global JuegoActual
    global MisHoras
    global MisMinutos
    global MisSegundos
    global destructor
    global Sonido
    global TableroDeJuego
    if(MiReloj==True):
        PausarReloj = False
    if(MiTimer==True):
        PausarTimer = False
    if messagebox.askyesno("Otra partida","Seguro que desea iniciar una partida nueva?"):
        if(MiReloj==True):
            destructor = True
        MisHoras = "00"
        MisMinutos = "00"
        MisSegundos = "00"
        NuevoJuego = GeneradorJuego2(JuegoActual)
        Cuadricula(NuevoJuego)
        if(MiReloj==True):
            PausarReloj = True
        if(MiTimer==True):
            PausarTimer = True
        JuegoActual = NuevoJuego
        if(Sonido=="ConSonido"):
            mixer.music.stop()
            mixer.music.load("mario.mp3")
            mixer.music.play(-1)
    else:
        if(MiReloj==True):
            PausarReloj = True
        if(MiTimer==True):
            PausarTimer = True

def ReiniciarJuego():
    global CuadriculaCeldas
    global PausarReloj 
    global PausarTimer
    global BotonPausarTiempo
    global MiReloj
    global MiTimer
    global JuegoActual
    global MisHoras
    global MisMinutos
    global MisSegundos
    global destructor
    if(MiReloj==True):
        PausarReloj = False
    if(MiTimer==True):
        PausarTimer = False
    if messagebox.askyesno("Reiniciar","Seguro que desea reiniciar esta partida?"):
        if(MiReloj==True):
            destructor = True
        MisHoras = "00"
        MisMinutos = "00"
        MisSegundos = "00"
        CuadriculaCeldas.place_forget()
        Cuadricula(JuegoActual)
        CuadriculaCeldas.place(x=150,y=60)
        if(MiReloj==True):
            PausarReloj = True
        if(MiTimer==True):
            PausarTimer = True
        if(Sonido =="ConSonido"):
            mixer.music.stop()
            mixer.music.load("mario.mp3")
            mixer.music.play(-1)
    else:
        if(MiReloj==True):
            PausarReloj = True
        if(MiTimer==True):
            PausarTimer = True

def TerminarJuego():
    global PausarReloj 
    global PausarTimer
    global BotonPausarTiempo
    global MiReloj
    global MiTimer
    global MisHoras
    global MisMinutos
    global MisSegundos
    global destructor
    global destructorDerelojes
    global CuadriculaCeldas
    if(MiReloj==True):
        PausarReloj = False
    if(MiTimer==True):
        PausarTimer = False
    if messagebox.askyesno("Finalizar","Seguro que desea finalizar el juego actual?"):
        destructor = True
        destructorDerelojes = True
        MisHoras = "00"
        MisMinutos = "00"
        MisSegundos = "00"
        CuadriculaCeldas.place_forget()
        BIniciarJuego.config(state="normal")
        BotonIrAConfiguracion.config(state="normal")
        BotonIrAAcercaDe.config(state="normal")
        BotonAyuda.config(state="normal")
        BValidarJuego.config(state="disabled")
        BOtroJuego.config(state="disabled")
        BReiniciarJuego.config(state="disabled")
        BTerminarJuego.config(state="disabled")
        if(MiTimer==True or MiReloj==True):
            BotonPausarTiempo.destroy()
        if(Sonido=="ConSonido"):
            mixer.music.stop()
        if(MiTimer==True):
            MiReloj=False
            MiTimer=False

    else:
        if(MiReloj==True):
            PausarReloj = True
        if(MiTimer==True):
            PausarTimer = True
        
#---------------------------------------------------------TABLA MENU------------------------------------------------------------------

TablaMenuArriba = tk.Frame(vPrincipal, bg="white")
TablaMenuArriba.pack(fill="x")

BotonIrAConfiguracion = tk.Button(TablaMenuArriba, bg="white", text="Configuración del juego", width=30, bd=0, command=IrAConfiguracion, state="disabled")
BotonIrAConfiguracion.pack(side="left")

BotonAyuda = tk.Button(TablaMenuArriba,bg="white", text="Ayuda", width=30,bd=0, command=AyudaAlUsuario.IrAAcercaDe)
BotonAyuda.pack(side="left")

BotonIrAAcercaDe = tk.Button(TablaMenuArriba,bg="white", text="Acerca de", width=30,bd=0, command=AcercaDelPrograma.Acercade)
BotonIrAAcercaDe.pack(side="left")

#--------------------------------------Poner nombre--------------------------------------------------------------

EntradaNombreLabel = tk.Label(vPrincipal, text="Nombre del jugador (obligatorio)", font=("Arial",8), bg="#F7DC6F")
EntradaNombreLabel.place(x=150,y=530)

EntradaNombre = tk.Entry(vPrincipal, justify="center", width=45, relief="groove", bg="#FF5733")
EntradaNombre.place(x=100, y=550)

BValidarNombre = tk.Button(vPrincipal,text="Validar usuario", width=12, relief="groove", bg="#70E349", command=validarNombre)
BValidarNombre.place(x=190,y=575)

#-------------------------------------------------------------BOTONES-----------------------------------------------------------------------

BIniciarJuego = tk.Button(vPrincipal, state="disabled", text="Iniciar Juego",width=15, relief="groove",bg="#A1E889", command=IniciarJuego)
BIniciarJuego.place(x=60,y=470)
BIniciarJuego.bind("<Enter>", MensajeDeConfiguracion)
BIniciarJuego.bind("<Leave>",DejarMensajeConfiguracion)

BValidarJuego = tk.Button(vPrincipal, state="disabled",text="Validar juego",width=15, relief="groove",bg="#61C867", command=ValidarJuego)
BValidarJuego.place(x=190,y=470)

BOtroJuego = tk.Button(vPrincipal, state="disabled", text="Otro juego", width=15, relief="groove",bg="#FFF40F", command=OtroJuego)
BOtroJuego.place(x=320,y=470)

BReiniciarJuego = tk.Button(vPrincipal, state="disabled", text="Reiniciar juego", width=15, relief="groove",bg="#A2CEFF",command=ReiniciarJuego)
BReiniciarJuego.place(x=450,y=470)

BTerminarJuego = tk.Button(vPrincipal, state="disabled", text="Terminar juego", width=15, relief="groove",bg="#FFA2A2", command=TerminarJuego)
BTerminarJuego.place(x=580,y=470)

BTop10 = tk.Button(vPrincipal, text="TOP 10", pady=10,relief="groove", width=20, bg="#FF3333", command=AbrirTop)
BTop10.place(x=445, y=540)


vPrincipal.mainloop()
