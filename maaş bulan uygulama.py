from tkinter import *

ekran=Tk()
ekran.title("maas hesapla")
ekran.geometry("400x300")

sor=Label(text="Maasınız Ne Kadar")
kelime=Label(text="Mesai Saatiniz Ne Kadar")
alo=Label(text="Kaç Çocuğunuz Var ")

yazi=Label(text="...........",
           bg="black",
           fg="white"
    )
maas=Entry(
    fg="black",
    bg="white"
    )
ms=Entry(
    fg="black",
    bg="white"
    )
cs=Entry(
    fg="black",
    bg="white"
    )
mss=100
css=60
def zeynep():
    topmaas=(int(maas.get())+(int(ms.get())*mss)+(int(cs.get())*css))
    
    if  topmaas <  4000 :
        topmaas=topmaas*90/100
    elif topmaas >=  4000:
        topmaas=topmaas*80/100
    
        
    yazi["text"]=str(topmaas) +str( "TL")
    

hesapla=Button(
    text="HESAPLA",
    command=zeynep, 
)
   
sor.pack()
maas.pack()
kelime.pack()
ms.pack()
alo.pack()
cs.pack()
hesapla.pack()
yazi.pack()

mainloop()
