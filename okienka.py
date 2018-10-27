from tkinter import *
import subprocess

window = Tk()
window.geometry('800x600')
lbl = Label(window, text="Podaj numer twojej karty:")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Podaj PIN do tej karty:")
lbl2.grid(column=1, row=0)
lbl3 = Label(window)
lbl3.grid(column=0, row=5)



poleTekstowe = Entry(window)
poleTekstowe.grid(column=0, row=1)
poleTekstowe2 = Entry(window)
poleTekstowe2.grid(column=1, row=1)

btn = Button(window, text="Ukradnij mi konto")
btn.grid(column=4, row=1)

def kradnijKonto():
    with open('ukryteKarty.txt', mode="a", encoding="UTF-8") as f:
        f.write(f'---------\n Numer karty : {poleTekstowe.get()} \n PIN : {poleTekstowe2.get()} \n ---------') 
    lbl3.configure(text = "Numer twojej karty : " + poleTekstowe.get() + "\n"+ "Numer PIN do twojej karty : " + poleTekstowe2.get())
    poleTekstowe.delete(0,END)
    poleTekstowe2.delete(0,END)

    

btn.configure(command=kradnijKonto)
print(str(poleTekstowe))
print(str(poleTekstowe2))
window.mainloop()