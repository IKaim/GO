from tkinter import *
from tkinter import filedialog
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.title("Projekt")
root.geometry("850x500")
labelblank3 = Label(root, text='               ')
labelblank3.grid(row=2, column=5, columnspan=10)

fig = Figure(figsize = (4,4), dpi = 100)
plt = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master = root)
canvas.draw()
canvas.get_tk_widget().place(x=400,y=10)
#plt.get_xaxis().set_visible(False)
#plt.get_yaxis().set_visible(False)
#plt.axis('off')

labelXA = Label(root, text='Xa = ').grid(row=0, column=0)
xa_e = Entry(root, width = 20, borderwidth = 2)
xa_e.grid(row=0, column=1)
labelYA = Label(root, text='Ya = ').grid(row=1, column=0)
ya_e = Entry(root, width = 20, borderwidth = 2)
ya_e.grid(row=1, column=1)

xa_e.insert(0,'0')
ya_e.insert(0,'0')

labelXB = Label(root, text='Xb = ').grid(row=0, column=2)
xb_e = Entry(root, width = 20, borderwidth = 2)
xb_e.grid(row=0, column=3)
labelYB = Label(root, text='Yb = ').grid(row=1, column=2)
yb_e = Entry(root, width = 20, borderwidth = 2)
yb_e.grid(row=1, column=3)

xb_e.insert(0,'0')
yb_e.insert(0,'0')

labelXC = Label(root, text='Xc = ').grid(row=3, column=0)
xc_e = Entry(root, width = 20, borderwidth = 2)
xc_e.grid(row=3, column=1)
labelYC = Label(root, text='Yc = ').grid(row=4, column=0)
yc_e = Entry(root, width = 20, borderwidth = 2)
yc_e.grid(row=4, column=1)

xc_e.insert(0,'0')
yc_e.insert(0,'0')

labelXD = Label(root, text='Xd = ').grid(row=3, column=2)
xd_e = Entry(root, width = 20, borderwidth = 2)
xd_e.grid(row=3, column=3)
labelYD = Label(root, text='Yd = ').grid(row=4, column=2)
yd_e = Entry(root, width = 20, borderwidth = 2)
yd_e.grid(row=4, column=3)

xd_e.insert(0,'0')
yd_e.insert(0,'0')


labelblank = Label(root, text='   ').grid(row=5, column=0)
labelblank2 = Label(root, text='   ').grid(row=7, column=0)

labelXP = Label(root, text='Xp = ').grid(row=8, column=0)
labelYP = Label(root, text='Yp = ').grid(row=9, column=0)

xp_e = Entry(root, width = 20, borderwidth = 2)
xp_e.grid(row=8, column=1)
yp_e = Entry(root, width = 20, borderwidth = 2)
yp_e.grid(row=9, column=1)

xp_e.insert(0, '-')
yp_e.insert(0, '-')

labelblank = Label(root, text='   ').grid(row=10, column=0)
t_pasek = Text(root, height=9.5, width=45)
t_pasek.place(x=20, y=247)

clicked_CD = StringVar()
clicked_CD.set('red')
drop_CD = OptionMenu(root, clicked_CD, 'red', 'blue', 'black', 'green', 'yellow')
drop_CD.place(x=670, y=425)
label_color_cd = Label(root, text="CD:")
label_color_cd.place(x=650, y=430)

label_color_ab = Label(root, text="AB:")
label_color_ab.place(x=550, y=430)
clicked_AB = StringVar()
clicked_AB.set('blue')
drop_AB = OptionMenu(root, clicked_AB, 'red', 'blue', 'black', 'green', 'yellow')
drop_AB.place(x=571, y=425)

def dane_do_pliku():
    #nazwa_w = 'wynik.txt'
    with open('wynik.txt', 'w') as nazwa_w:
         print('A', xa_e.get(), ya_e.get(), file=nazwa_w)
         print('B', xb_e.get(), yb_e.get(), file=nazwa_w)
         print('C', xc_e.get(), yc_e.get(), file=nazwa_w)
         print('D', xd_e.get(), yd_e.get(), file=nazwa_w)
         print('P', xp_e.get(), yp_e.get(), file=nazwa_w)
    t_pasek.insert(1.0, 'Zapisano dane do pliku: wynik.txt\n\n')

def dane_z_pliku():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/izuni/Documents/studia/geoinf pw/GO", title="Select A File", filetypes=(("txt files", "*.txt"),("all files","*.*")))
    sciezka = root.filename
    with open(sciezka, 'r') as plik:
        punkty = []
        for l in plik:
            linia = l.strip().split()
            punkty.append(linia)
        xa_e.insert(0, punkty[0][1])
        ya_e.insert(0, punkty[0][2])

        xb_e.insert(0, punkty[1][1])
        yb_e.insert(0, punkty[1][2])

        xc_e.insert(0, punkty[2][1])
        yc_e.insert(0, punkty[2][2])

        xd_e.insert(0, punkty[3][1])
        yd_e.insert(0, punkty[3][2])
        t_pasek.insert(1.0, 'Wczytano dane z pliku: ' + sciezka)
        
def oblicz():
    xp_e.delete(0, END)
    yp_e.delete(0, END)
    xa = float(xa_e.get())
    ya = float(ya_e.get())

    xb = float(xb_e.get())
    yb = float(yb_e.get())

    xc = float(xc_e.get())
    yc = float(yc_e.get())
    
    xd = float(xd_e.get())
    yd = float(yd_e.get())

    #t_pasek.insert(1.0, str(xa) + ' ' + str(ya) + '\n' + str(xb) + ' ' + str(yb) + '\n' + str(xc) + ' ' + str(yc)+ '\n' + str(xd) + ' ' + str(yd)+ '\n')

    try :
        t1 = ( (xc-xa)*(yd-yc) - (yc-ya)*(xd-xc) ) / ( (xb-xa)*(yd-yc) - (yb-ya)*(xd-xc) )
        t2 = ( (xc-xa)*(yb-ya) - (yc-ya)*(xb-xa) ) / ( (xb-xa)*(yd-yc) - (yb-ya)*(xd-xc) )
        if 0<=t1<=1 and 0<=t2<=1:
            #punkt nalezy do odcinkow
            xp = xa + t1*(xb-xa)
            yp = ya + t1*(yb-ya)
            xp = str("{:.3f}".format(xp))
            yp = str("{:.3f}".format(yp))
            t_pasek.insert(1.0, 'Poprawnie obliczone współrzędne Punktu P:\n' + str(xp) + ' ' + str(yp) + '\n\n')
    except ZeroDivisionError:
        if (xb-xa)*(yd-yc) - (yb-ya)*(xd-xc) == 0:
            if (xc-xa)*(yd-yc) - (yc-ya)*(xd-xc) == 0:
                #nakladaja
                xp = '--'
                yp = '--'
                t_pasek.insert(1.0, 'Odcinki AB i CD się nakładają.\n\n')
                
            else:
                #rownolegle, nie przecinaja sie
                xp = '--'
                yp = '--'
                t_pasek.insert(1.0, 'Odcinki AB i CD są równoległe.\n\n')
    
    xp_e.insert(0, xp)
    yp_e.insert(0, yp)


def graph():
    c_AB = clicked_AB.get()
    c_CD = clicked_CD.get()
    plt.cla()
    try:
        xa = float(xa_e.get())
        ya = float(ya_e.get())
    
        xb = float(xb_e.get())
        yb = float(yb_e.get())

        xc = float(xc_e.get())
        yc = float(yc_e.get())
    
        xd = float(xd_e.get())
        yd = float(yd_e.get())


        plt.scatter(xa, ya, c=c_AB)
        plt.text(xa,ya, s='A')
        
        plt.scatter(xb, yb, c=c_AB)
        plt.text(xb,yb, s='B')
        
        plt.scatter(xc, yc, c=c_CD)
        plt.text(xc,yc, s='C')
        
        plt.scatter(xd, yd, c=c_CD)
        plt.text(xd,yd, s='D')
        
        try:
            xp = float(xp_e.get())
            yp = float(yp_e.get())

            plt.scatter(xp, yp, c='k', zorder=10)
            plt.text(xp,yp, s='P')
              
        except ValueError:
            pass

        odc_ab_x = [xa, xb]
        odc_ab_y = [ya, yb]
        odc_cd_x = [xc, xd]
        odc_cd_y = [yc, yd]
        
        plt.plot(odc_ab_x, odc_ab_y, c=c_AB, zorder=0)
        plt.plot(odc_cd_x, odc_cd_y, c=c_CD, zorder=0)
        
        canvas = FigureCanvasTkAgg(fig, master = root)
        canvas.draw()
        canvas.get_tk_widget().place(x=400,y=10)
        #NavigationToolbar2Tk(canvas, root).place(x=400,y=200)
##        toolbar.update()
##        canvas.get_tk_widget().place(x=400,y=100)#grid(row=0, column=20)
        #plt.show()
        t_pasek.insert(1.0, 'Narysowano punkty i odcinki.\n\n')
    except ValueError:
        pass

def wyczysc_pasek():
    t_pasek.delete(1.0, END)

def wyczysc_wykres():
    fig = Figure(figsize = (4,4), dpi = 100)
    plt = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().place(x=400,y=10)

ButtonOblicz = Button(root, text='Oblicz', padx=20, command=oblicz).grid(row=6, column=0, columnspan=3) #pady
ButtonGraph = Button(root, text='Rysuj/Odswiez', padx=20, command=graph) #.grid(row=11, column=3, columnspan=3)
ButtonGraph.place(x=400, y=430)
ButtonPlik = Button(root, text='Wczytaj dane z pliku', padx=25, command=dane_z_pliku)
ButtonPlik.place(x=180, y=125)
ButtonPlik_w = Button(root, text='Zapisz dane do pliku', padx=25, command=dane_do_pliku)
ButtonPlik_w.place(x=180, y=160)
#ButtonPNG = Button(root, text='Zapisz wykres', padx=20, command=zapisz_wykres)
#ButtonPNG.place(x=400, y=460)
ButtonEnd = Button(root, text="Zamknij program", padx=20, command=root.destroy)
ButtonEnd.place(x=700, y=465)
ButtonWyczyscWykres = Button(root, text="Wyczyść", command=wyczysc_wykres)
ButtonWyczyscWykres.place(x=400, y=465)
ButtonWyczyscPasek = Button(root, text="Wyczyść pasek poleceń", command=wyczysc_pasek)
ButtonWyczyscPasek.place(x=20, y=430)
root.mainloop()
