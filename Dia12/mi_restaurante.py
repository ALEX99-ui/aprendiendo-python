from tkinter import *


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximixar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Mi restaurante - Sistema de Facturacion')

# color de fondo de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior,
                        text='Sistema de Facturacion',
                        fg='azure4',
                        font=('Dosis', 58),
                        bg='burlywood',
                        width=22)
etiqueta_titulo.grid(row=0,
                     column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)


# panel comidas
panel_comidas = LabelFrame(panel_izquierdo,
                           text='Comidas',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                           text='Bebidas',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo,
                           text='Postres',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='azure4')
panel_postres.pack(side=LEFT)


# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha,
                          bd=1,
                          relief=FLAT,
                          bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha,
                     bd=1,
                     relief=FLAT,
                     bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha,
                      bd=1,
                      relief=FLAT,
                      bg='burlywood')
panel_botones.pack()


# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmo', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)


    contador += 1

# generar items postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador])
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)

    contador += 1

# evitar que la pantalla se cierre
aplicacion.mainloop()