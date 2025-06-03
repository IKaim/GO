from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import math as m
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.title("Punkt względem wielokąta")
root.geometry("850x550")

root.configure(bg='#dfdcd8')

t_pasek = Text(root, height=10, width=37)
t_pasek.place(x=10, y=190)

fig = Figure(figsize = (5,5), dpi = 100)
plt = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master = root)
canvas.draw()
canvas.get_tk_widget().place(x=340,y=10)

labelW = Label(root, text='Punkt do sprawdzenia').place(x = 10, y = 45)
labelX = Label(root, text='X = ').place(x = 10, y = 70)
x_e = Entry(root, width = 20, borderwidth = 2)
x_e.place(x = 40, y = 70)
labelY = Label(root, text='Y = ').place(x = 10, y = 95)
y_e = Entry(root, width = 20, borderwidth = 2)
y_e.place(x = 40, y = 95)

clicked_pkt = StringVar()
clicked_pkt.set('red')
drop_pkt = OptionMenu(root, clicked_pkt, 'red', 'blue', 'black', 'green', 'yellow')
drop_pkt.place(x=75, y=370)
label_color_pkt = Label(root, text="kolor pkt:")
label_color_pkt.place(x=10, y=375)

label_color_l = Label(root, text="kolor linii:")
label_color_l.place(x=10, y=405)
clicked_l = StringVar()
clicked_l.set('black')
drop_l = OptionMenu(root, clicked_l, 'red', 'blue', 'black', 'green', 'yellow')
drop_l.place(x=75, y=400)


styl = ['________________', '. . . . . . . . . . . . . . . . . . . ', '-----------------', '_ . _ . _ . _ . _ . _ . _']
Combo = ttk.Combobox(root, values = styl, width = 10)
Combo.set('Styl linii')
Combo.place(x = 10, y = 450)

gr = Scale(root, from_=1, to=5, length = 100,
               tickinterval = 1, orient=HORIZONTAL, sliderlength = 15)
gr.place(x = 100, y = 450)

global p
p = []

def wyczysc_wykres():
    fig = Figure(figsize = (5,5), dpi = 100)
    plt = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().place(x=340,y=10)        
    
def wczytaj_wielokat():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/izuni/Documents/studia/geoinf pw/GO", title="Select A File", filetypes=(("txt files", "*.txt"),("all files","*.*")))
    sciezka = root.filename
    list_x = []
    list_y = []
    with open(sciezka, 'r') as plik:
        for l in plik:
            linia = l.strip().split()
            p.append([float(linia[0]), float(linia[1])])
            list_x.append(float(linia[0]))
            list_y.append(float(linia[1]))
            global mini
            global maks
            mini = [min(list_x), min(list_y)]
            maks = [max(list_x), max(list_y)]
    rysuj_wielokat()

def getstyle():
    s = Combo.get()
    if s == 'Styl linii' or s == '________________':
        w = '-'
    elif s == '. . . . . . . . . . . . . . . . . . . ':
        w = ':'
    elif s == '-----------------':
        w = '--'
    elif s == '_ . _ . _ . _ . _ . _ . _':
        w = '-.'
    return w
        
def rysuj_wielokat():
    plt.cla()
    kolor_pkt = clicked_pkt.get()
    kolor_linii = clicked_l.get()
    s = getstyle()
    try:
        for i in range(len(p)):
            if i == 0:
                continue
            else:
                x1 = p[i-1][0]
                y1 = p[i-1][1]
                x2 = p[i][0]
                y2 = p[i][1]
                plt.scatter(x1, y1, c=kolor_pkt)
                #plt.text(x1, y1, s=i)

                odcx = [x1, x2]
                odcy = [y1, y2]

                plt.plot(odcx, odcy, zorder=0, c=kolor_linii, linestyle = s, linewidth = gr.get())

            canvas = FigureCanvasTkAgg(fig, master = root)
            canvas.draw()
            canvas.get_tk_widget().place(x=340,y=10)
    except ValueError:
            pass

def getDistance(a, b):
    return m.sqrt((a[0]-b[0])**2+ (a[1]-b[1])**2)  

def isInside(wielokat, punkt, mini, maks):
    suma_katow = 0
    if punkt[0] > mini[0] or punkt[0] < maks[0] or punkt[1] > mini[1] or punkt[1] < maks[1]:
        for i in range(len(wielokat) - 1):
            a = wielokat[i]
            b = wielokat[i + 1]
            
            #odleglosci
            A = getDistance(a, b);
            B = getDistance(punkt, a)
            C = getDistance(punkt, b)

            #kierunek wektora
            ta_x = a[0] - punkt[0]
            ta_y = a[1] - punkt[1]
            tb_x = b[0] - punkt[0]
            tb_y = b[1] - punkt[1]
            cross = tb_y * ta_x - tb_x * ta_y
            clockwise = cross < 0
            
            try:
                # calculate sum of angles
                if(clockwise):
                    suma_katow = suma_katow + m.degrees(m.acos((B * B + C * C - A * A) / (2.0 * B * C)))
                else:
                    suma_katow = suma_katow - m.degrees(m.acos((B * B + C * C - A * A) / (2.0 * B * C)))
            except ZeroDivisionError:
                return True
        if(abs(round(suma_katow)) == 360):
            return True
    return False


def sprawdz():
    try:
        pp = [float(x_e.get()), float(y_e.get())]
        plt.cla()
        rysuj_wielokat()
        plt.scatter(pp[0], pp[1], c='blue')
        #plt.text(pp[0],pp[1], s='P')
        canvas = FigureCanvasTkAgg(fig, master = root)
        canvas.draw()
        canvas.get_tk_widget().place(x=340,y=10)            
        
        if isInside(p, pp, mini, maks):
            t_pasek.insert(1.0, 'Punkt (' + str(pp[0]) + ',' + str(pp[1]) + ') znajduje się wewnątrz wielokąta.\n\n')
            #punkt wenatrz
        else:
            #punkt poza
            t_pasek.insert(1.0, 'Punkt (' + str(pp[0]) + ',' + str(pp[1]) + ') znajduje się na zewnątrz wielokąta.\n\n')
            
    except ValueError:
            pass

def wczytaj_punkty():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/izuni/Documents/studia/geoinf pw/GO", title="Select A File", filetypes=(("txt files", "*.txt"),("all files","*.*")))
    sciezka = root.filename
    ile = 0
    pkt_ok = []

    with open(sciezka, 'r') as plik:
        for l in plik:
            linia = l.strip().split()
            x = float(linia[0])
            y = float(linia[1])
            if isInside(p, [x,y], mini, maks):
                pkt_ok.append([x,y])
                ile += 1

    t_pasek.insert(1.0, 'Wewnątrz wielokąta znajduje się: ' + str(ile) + '\n\n')
    for pkt in pkt_ok:
        plt.scatter(pkt[0], pkt[1], c='green')

    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().place(x=340,y=10)


    

ButtonGraph = Button(root, text='Odśwież', padx=20, command=rysuj_wielokat)
ButtonGraph.place(x=340, y=520)
    
ButtonEnd = Button(root, text="Zamknij program", padx=20, command=root.destroy)
ButtonEnd.place(x=700, y=520)

ButtonPlik = Button(root, text='Wczytaj wielokąt', padx=25, command=wczytaj_wielokat)
ButtonPlik.place(x=10, y=10)

ButtonSprawdz = Button(root, text="Sprawdź", padx=20, command=sprawdz)
ButtonSprawdz.place(x=180, y=80)

ButtonPunkty = Button(root, text="Wczytaj punkty i sprawdź", padx=20, command=wczytaj_punkty)
ButtonPunkty.place(x=10, y=140)

ButtonWyczyscWykres = Button(root, text="Wyczyść", command=wyczysc_wykres)
ButtonWyczyscWykres.place(x=640, y=520)

root.mainloop()
