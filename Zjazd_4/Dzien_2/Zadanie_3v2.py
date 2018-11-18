import tkinter
root = tkinter.Tk()

def koszt():
    a = float(cena_paliwa_entry.get())
    b = float(spalanie_entry.get())
    dystans = int(dystans_entry.get())
    wynik_label.configure(text=int(((b*a)/100)*dystans))

dystans_label = tkinter.Label(master = root, text = "Dystans")
dystans_label.grid(row = 0, column = 0)
dystans_entry = tkinter.Entry(master = root)
dystans_entry.grid(row = 0, column = 1)

spalanie_label = tkinter.Label(master = root, text = "Spalanie na 100km")
spalanie_label.grid(row = 1, column = 0)
spalanie_entry = tkinter.Entry(master = root)
spalanie_entry.grid(row = 1, column = 1)

cena_paliwa_label = tkinter.Label(master = root, text = "Cena paliwa")
cena_paliwa_label.grid(row = 2, column = 0)
cena_paliwa_entry = tkinter.Entry(master = root)
cena_paliwa_entry.grid(row = 2, column = 1)

wynik = tkinter.Label(master = root, text = "Wynik")
wynik.grid(row = 4, column = 1)
wynik_label = tkinter.Label(master = root, text = " - ")
wynik_label.grid(row = 5, column = 1)

policz_button = tkinter.Button(master = root, text = "Oblicz", command = koszt)

policz_button.grid(row = 3, column = 1)

root.title("Kalkulator spalania")
root.mainloop()