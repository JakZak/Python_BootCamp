import tkinter

def koszt():
    a = float(cena_paliwa_entry.get())
    b = float(spalanie_entry.get())
    dystans = int(dystans_entry.get())
    wynik.configure(text=int(((b*a)/100)*dystans))

root = tkinter.Tk()

a_label = tkinter.Label(master=root, text = "Mijesce początkowe")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text = "Mijesce docelowe")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

cena_paliwa_label = tkinter.Label(master=root, text = "Cena paliwa")
cena_paliwa_label.pack()
cena_paliwa_entry = tkinter.Entry(master=root)
cena_paliwa_entry.pack()

spalanie_label = tkinter.Label(master = root, text = "Spalanie na 100km")
spalanie_label.pack()
spalanie_entry = tkinter.Entry(master = root)
spalanie_entry.pack()

dystans_label = tkinter.Label(master = root, text = "Dystans")
dystans_label.pack()
dystans_entry = tkinter.Entry (master = root)
dystans_entry.pack()

wynik_label = tkinter.Label(master=root, text = "Koszt")
wynik_label.pack()

wynik = tkinter.Label(master=root, text = " - ")
wynik.pack()

policz_button = tkinter.Button(master = root, text = "Oblicz", command = koszt)

policz_button.pack()

root.title("Koszt przejazdu")
root.mainloop()

