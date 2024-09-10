import tkinter as tk
from tkinter import messagebox
import random as rand
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from array import array
from threading import Timer
import winsound 
ikkuna=tk.Tk()

ikkuna.title(" Plot Window ")
ikkuna.geometry("2000x1000")
names = [
"Diksha Premysl",
"Angelika Johanna",
"Bébinn Karolina",
"Mahmoud Iphigenia",
"Maja Nazeer",
"Wealdmær Kumari",
"Joaquina Lilja",
"Latona Elvire",
"Łucja Alkinoe",
"Andoni Aharon",
"Hrodulf Clitus",
"Conrad Josepha",
"Seo-Yeon Küllike",
"Seòsaidh Hauwa",
"Sujatha Hananiah",
"Jørg Magda",
"Fionnbarra Iustin",
"Gabrielle Kəmal",
"Achaikos Ana Isabel",
"Alec Jarek",
"Patroclus Gernot",
"Dipika Mohini",
"Fien Lesleigh",
"Kristi Vello",
"Anders Abiah"
]

Runners_years = {
}


speeds=[]
years=[]
figs, axs = plt.subplots()
for val in range(1900,2050):
    randomspeed = rand.uniform(9.58,14.23)
    randomspeed = round(randomspeed,3)
    speeds.append(randomspeed)
speeds.sort()

for i, val in enumerate(range(1900,2050)):
    randomvalue = rand.randint(0,len(names)-1)
    randomspeed = rand.uniform(9.58,10.23)
    Runners_years[i] = {"year": val,"name": names[randomvalue], "speed": speeds[i]}
    years.append(val)
axs.plot(speeds,years)
axs.grid()
print(Runners_years)
figs.show()

Kernestipos = [0,2]
Kernestiperformace = {
    "loops" : 0,
    "lastloop" : None,
    "finalspeed": None
}
Eernestipos = [0,2]
Eernestiperformance = {
    "loops" : 0,
    "lastloop" : None,
    "finalspeed": None
}
averagerunningspeed = 5.0


fig, ax = plt.subplots()    
ax.figure.set_figwidth(20)
ax.figure.set_dpi(100)
ax.set_xlim(0,100)
ax.set_ylim(0,5)
ax.axis('scaled')
ax.set_yticklabels([])
tempoint = ax.plot(Eernestipos[0],2,'go')
tempointtext = ax.text(Eernestipos[0]-1,3,"Eernesti")
kuvaaja = FigureCanvasTkAgg(fig,master=ikkuna)
kuvaaja.get_tk_widget().place(x=0,y=500)
kuvaaja.draw()

fig2, ax2 = plt.subplots()
ax2.figure.set_figwidth(20)
ax2.figure.set_dpi(100)
ax2.set_xlim(0,100)
ax2.set_ylim(0,5)
ax2.axis('scaled')
ax2.set_yticklabels([])
tempoint2 = ax2.plot(Kernestipos[0],2,'go')
tempointtext2 = ax2.text(Kernestipos[0]-1,3,"Kernesti")
kuvaaja2 = FigureCanvasTkAgg(fig2,master=ikkuna)
kuvaaja2.get_tk_widget().place(x=0,y=0)
kuvaaja2.draw()

def juoksuK():
    global tempoint
    global tempointtext
    tempointtext.remove()
    tempoint[0].remove()
    tempoint.clear()
    runnningspeed = rand.uniform(averagerunningspeed-2,averagerunningspeed+1)
    Kernestipos[0] = Kernestipos[0] + runnningspeed
    if(Kernestipos[0]>100):
        Kernestiperformace["lastloop"] = Kernestipos[0]
        Kernestiperformace["finalspeed"] = runnningspeed
        Kernestipos[0] = 100
    tempoint = ax2.plot(Kernestipos[0],2,'go')
    tempointtext = ax2.text(Kernestipos[0]-1,3,"Kernesti")
    kuvaaja2 = FigureCanvasTkAgg(fig2,master=ikkuna)
    kuvaaja2.get_tk_widget().place(x=0,y=0)
    kuvaaja2.draw()
    winsound.Beep(400, 20)
    juoksunaloitusK()

def juoksuE():
    global tempoint2
    global tempointtext2
    tempointtext2.remove()
    tempoint2[0].remove()
    tempoint2.clear()
    runnningspeed = rand.uniform(averagerunningspeed-2,averagerunningspeed+1)
    Eernestipos[0] = Eernestipos[0] + runnningspeed
    if(Eernestipos[0]>100):
        Eernestiperformance["lastloop"] = Eernestipos[0]
        Eernestiperformance["finalspeed"] = runnningspeed
        Eernestipos[0] = 100
    tempoint2 = ax.plot(Eernestipos[0],2,'go')
    tempointtext2 = ax.text(Eernestipos[0]-1,3,"Eernesti")
    kuvaaja = FigureCanvasTkAgg(fig,master=ikkuna)
    kuvaaja.get_tk_widget().place(x=0,y=500)
    kuvaaja.draw()
    winsound.Beep(1000, 20)
    juoksunaloitusE()
    
def winner():   
    if(Kernestipos[0]==100 and Eernestipos[0]==100):
        if(Kernestiperformace["loops"]<Eernestiperformance["loops"]):
            print("Kernesti won!")
            lastseconds = Kernestiperformace["lastloop"]-100
            lastseconds = round(lastseconds/Kernestiperformace["finalspeed"],3)
            seconds = Kernestiperformace["loops"]-1
            seconds = seconds+1*round(lastseconds,2)
            messagebox.showinfo(title="Winner!",message="Keernesti won! " + "Seconds: " + str(seconds))
        else:
            print("Eernesti won!")
            lastseconds = Eernestiperformance["lastloop"]-100
            lastseconds = round(lastseconds/Eernestiperformance["finalspeed"],3)
            seconds = Eernestiperformance["loops"]-1
            seconds = seconds+1*round(lastseconds,2)
            messagebox.showinfo(title="Winner!",message="Eernersti won! " + "Seconds: " + str(seconds))
    
def juoksunaloitusE():
    Eernestiperformance["loops"] = Eernestiperformance["loops"]+1
    if(Eernestipos[0]<100):
        r = Timer(1.0,juoksuE)
        r.start()
    else:
        Eernestiperformance["loops"] = Eernestiperformance["loops"]-1
        winner()
        print(Eernestiperformance["loops"])

def juoksunaloitusK():
    Kernestiperformace["loops"] = Kernestiperformace["loops"]+1
    if(Kernestipos[0]<100):
        r = Timer(1.0,juoksuK)
        r.start()
    else: 
        Kernestiperformace["loops"] = Kernestiperformace["loops"]-1
        winner()
        print(Kernestiperformace["loops"])

def yleislähtö():
    winsound.Beep(2000, 100)
    juoksunaloitusK()
    juoksunaloitusE()

def exit():
    for items in kuvaaja.get_tk_widget().find_all():
        kuvaaja.get_tk_widget().delete(items)
        kuvaaja2.get_tk_widget().delete(items)
    ikkuna.destroy()

for i in range(1,11): 
    randomvalue = rand.randint(69,79)
    lionspeed = round(randomvalue*0.27777777777778,3)
    randomvalue = rand.randint(0,len(names)-1)
    lionname = names[randomvalue].split(" ")
    Runners_years[len(Runners_years)] = {"name": "lion " + lionname[0] , "speed": lionspeed}

print(Runners_years)

def reset():
    Kernestipos[0] = 0
    Eernestipos[0] = 0

EernestiJuoksu=tk.Button(ikkuna,text="Juokse E",command=juoksunaloitusE)
EernestiJuoksu.place(x=600,y=475)
KeernestiJuoksu=tk.Button(ikkuna,text="Juokse K",command=juoksunaloitusK)
KeernestiJuoksu.place(x=800,y=475)
Yhetislahtöjuoksu=tk.Button(ikkuna,text="Yhteislähtö",command=yleislähtö)
Yhetislahtöjuoksu.place(x=1000,y=475)
Statistiikat=tk.Button(ikkuna,text="show winner",command=winner)
Statistiikat.place(x=1200,y=475)
resetointi=tk.Button(ikkuna,text="reset",command=reset)
resetointi.place(x=1400,y=475)
sulkemis=tk.Button(ikkuna,text="Exit",command=exit)
sulkemis.place(x=1600,y=475)
 
ikkuna.mainloop()
