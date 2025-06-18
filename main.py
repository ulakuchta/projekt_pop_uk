from tkinter import *

import tkintermapview


carefacility:list=[]
boarder:list=[]
worker:list=[]

class carefacilitys:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

def add_carefacility():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    user= carefacilitys(name=zmienna_imie, location=zmienna_miejscowosc)
    carefacility.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_carefacility()



def show_carefacility():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(carefacility):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name}')


def remove_carefacility():
    i=listbox_lista_obiketow.index(ACTIVE)
    carefacility[i].marker.delete()
    carefacility.pop(i)
    show_carefacility()

def edit_carefacility():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=carefacility[i].name
    location=carefacility[i].location

    entry_name.insert(0,name)
    entry_location.insert(0,location)

    button_dodaj_placowke.config(text='zapisz',command=lambda: update_carefacility(i))

def update_carefacility(i):
    new_name=entry_name.get()
    new_location=entry_location.get()

    carefacility[i].name=new_name
    carefacility[i].location=new_location

    carefacility[i].marker.delete()
    carefacility[i].coordinates=carefacility[i].get_coordinates()
    carefacility[i].marker=map_widget.set_marker(carefacility[i].coordinates[0],carefacility[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_placowke.config(text='Dodaj obiekt',command=add_carefacility)
    show_carefacility()


def show_carefacility_details():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=carefacility[i].name
    location=carefacility[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)

    map_widget.set_position(carefacility[i].coordinates[0],carefacility[i].coordinates[1])
    map_widget.set_zoom(17)



class boarders():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]


def add_boarder():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= boarders(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    boarder.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_boarder()



def show_boarder():
    listbox_lista_boarder.delete(0,END)
    for idx,user in enumerate(boarder):
        listbox_lista_boarder.insert(idx,f'{idx+1}. {user.name}')

def remove_boarder():
    i=listbox_lista_boarder.index(ACTIVE)
    boarder[i].marker.delete()
    boarder.pop(i)
    show_boarder()

def edit_boarder():
    i=listbox_lista_boarder.index(ACTIVE)
    name=boarder[i].name
    location=boarder[i].location
    location2=boarder[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_boarder.config(text='Zapisz',command=lambda: update_boarder(i))

def update_boarder(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    boarder[i].name=new_name
    boarder[i].location=new_location
    boarder[i].location2=new_location2

    boarder[i].marker.delete()
    boarder[i].coordinates=boarder[i].get_coordinates()
    boarder[i].marker=map_widget.set_marker(boarder[i].coordinates[0],boarder[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_boarder.config(text='Dodaj obiekt',command=add_boarder)
    show_boarder()


def show_boarder_details():
    i=listbox_lista_boarder.index(ACTIVE)
    name=boarder[i].name
    location=boarder[i].location
    location2=boarder[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(boarder[i].coordinates[0],boarder[i].coordinates[1])
    map_widget.set_zoom(17)



class workers():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
         import requests
         from bs4 import BeautifulSoup
         url = f"https://pl.wikipedia.org/wiki/{self.location}"
         response = requests.get(url).text
         response_html = BeautifulSoup(response, "html.parser")
         longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
         latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
         print(longitude)
         print(latitude)
         return [latitude, longitude]

def add_worker():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= workers(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    worker.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_worker()



def show_worker():
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,user in enumerate(worker):
        listbox_lista_obiektow_worker.insert(idx,f'{idx+1}. {user.name}')


def remove_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    worker[i].marker.delete()
    worker.pop(i)
    show_worker()

def edit_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_worker.config(text='zapisz',command=lambda: update_worker(i))

def update_worker(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    worker[i].name=new_name
    worker[i].location=new_location
    worker[i].location2=new_location2

    worker[i].marker.delete()
    worker[i].coordinates=worker[i].get_coordinates()
    worker[i].marker=map_widget.set_marker(worker[i].coordinates[0],worker[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_worker.config(text='Dodaj obiekt',command=add_carefacility)
    show_carefacility()


def show_worker_details():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(worker[i].coordinates[0],worker[i].coordinates[1])
    map_widget.set_zoom(17)









root = Tk()
root.geometry("1200x760")
root.title("Map Book MJ")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista domów opieki")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_carefacility_details)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_carefacility)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_carefacility)
button_edytuj_obiekt.grid(row=2, column=2)


label_lista_obiektow_boarder=Label(ramka_lista_obiektow, text="Lista pensjonariuszy")
label_lista_obiektow_boarder.grid(row=0, column=3,columnspan=2)
listbox_lista_boarder=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_boarder.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu_boarder=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_boarder_details)
button_pokaz_szczegoly_obiektu_boarder.grid(row=2, column=3)
button_usun_obiekt_boarder=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_boarder)
button_usun_obiekt_boarder.grid(row=2, column=4)
button_edytuj_obiekt_boarder=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_boarder)
button_edytuj_obiekt_boarder.grid(row=2, column=5)

label_lista_obiektow_worker=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_worker.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_worker=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_worker.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_worker=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_worker_details)
button_pokaz_szczegoly_obiektu_worker.grid(row=2, column=6)
button_usun_obiekt_worker=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_worker)
button_usun_obiekt_worker.grid(row=2, column=7)
button_edytuj_obiekt_worker=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_worker)
button_edytuj_obiekt_worker.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Name:")
label_name.grid(row=1, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=2, column=0,sticky=W)
label_location2=Label(ramka_formularz, text="Placówka:")
label_location2.grid(row=3, column=0,sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=2, column=1)
entry_location2=Entry(ramka_formularz)
entry_location2.grid(row=3, column=1)

button_dodaj_placowke=Button(ramka_formularz, text='Dodaj placówkę',command=add_carefacility)
button_dodaj_placowke.grid(row=5, column=0, columnspan=2)

button_dodaj_boarder=Button(ramka_formularz, text='Dodaj pensjonariusza',command=add_boarder)
button_dodaj_boarder.grid(row=6, column=0, columnspan=2)

button_dodaj_worker=Button(ramka_formularz, text='Dodaj pracownika',command=add_worker)
button_dodaj_worker.grid(row=7, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegoly obiektu:")
label_szczegoly_obiektow.grid(row=1, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Imię:")
label_szczegoly_name.grid(row=1, column=1)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=2)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=3)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=4)
label_szczegoly_location2=Label(ramka_szczegoly_obiektow, text="Placówka:")
label_szczegoly_location2.grid(row=1, column=5)
label_szczegoly_location2_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location2_wartosc.grid(row=1, column=6)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()



root.mainloop()