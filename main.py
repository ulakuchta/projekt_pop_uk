from tkinter import *

import tkintermapview


carefacility:list=[]
boarders:list=[]
workers:list=[]

class carefacility:
    def __init__(self,carefacility_name,carefacility_location):
        self.carefacility_name=carefacility_name
        self.carefacility_location=carefacility_location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.carefacility_location}"
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
    user= carefacility(name=zmienna_imie, location=zmienna_miejscowosc)
    boarders.append(user)

    entry_name.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_carefacility()



def show_users():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(carefacility):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name} {user.surname}')


def remove_user():
    i=listbox_lista_obiketow.index(ACTIVE)
    carefacility[i].marker.delete()
    carefacility.pop(i)
    show_users()

def edit_user():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=carefacility[i].name
    location=carefacility[i].location

    entry_name.insert(0,name)
    entry_location.insert(0,location)

    button_dodaj_obiekt.config(text='zapisz',command=lambda: update_user(i))

def update_user(i):
    new_name=entry_name.get()
    new_location=entry_location.get()

    carefacility[i].name=new_name
    carefacility[i].location=new_location

    carefacility[i].marker.delete()
    carefacility[i].coordinates=carefacility[i].get_coordinates()
    carefacility[i].marker=map_widget.set_marker(carefacility[i].coordinates[0],carefacility[i].coordinates[1])



    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_location.delete(0,END)
    entry_posts.delete(0,END)
    entry_name.focus()


    button_dodaj_obiekt.config(text='Dodaj obiekt',command=add_carefacility)
    show_users()


def show_user_details():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=carefacility[i].name
    location=carefacility[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)

    map_widget.set_position(carefacility[i].coordinates[0],carefacility[i].coordinates[1])
    map_widget.set_zoom(17)



class boarders():
    def __init__(self, boarders_name, boarders_location):
        self.boarders_name = boarders_name
        self.boarders_location = boarders_location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.boarders_location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

class workers():
    def __init__(self, workers_name, workers_location):
        self.boarders_name = workers_name
        self.boarders_location = workers_location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
         import requests
         from bs4 import BeautifulSoup
         url = f"https://pl.wikipedia.org/wiki/{self.workers_location}"
         response = requests.get(url).text
         response_html = BeautifulSoup(response, "html.parser")
         longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
         latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
         print(longitude)
         print(latitude)
         return [latitude, longitude]







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
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista domó opieki")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt.grid(row=2, column=2)


label_lista_obiektow_klient=Label(ramka_lista_obiektow, text="Lista pensjonariuszy")
label_lista_obiektow_klient.grid(row=0, column=3,columnspan=2)
listbox_lista_obiektow_klient=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_klient.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu_klient=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu_klient.grid(row=2, column=3)
button_usun_obiekt_klient=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt_klient.grid(row=2, column=4)
button_edytuj_obiekt_klient=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt_klient.grid(row=2, column=5)

label_lista_obiektow_klient=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_klient.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_klient=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_klient.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_klient=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu_klient.grid(row=2, column=6)
button_usun_obiekt_klient=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt_klient.grid(row=2, column=7)
button_edytuj_obiekt_klient=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt_klient.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Imię:")
label_name.grid(row=1, column=0, sticky=W)
label_surname=Label(ramka_formularz, text="Nazwisko:")
label_surname.grid(row=2, column=0,sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=3, column=0,sticky=W)
label_posts=Label(ramka_formularz, text="Postów:")
label_posts.grid(row=4, column=0,sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname=Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=3, column=1)
entry_posts=Entry(ramka_formularz)
entry_posts.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj obiekt')
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegoly obiektu:")
label_szczegoly_obiektow.grid(row=3, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Imię:")
label_szczegoly_name.grid(row=1, column=0)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=1)
label_szczegoly_surname=Label(ramka_szczegoly_obiektow, text="Nazwisko:")
label_szczegoly_surname.grid(row=1, column=2)
label_szczegoly_surname_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_surname_wartosc.grid(row=1, column=3)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=4)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=5)
label_szczegoly_posts=Label(ramka_szczegoly_obiektow, text="Posty:")
label_szczegoly_posts.grid(row=1, column=6)
label_szczegoly_posts_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_posts_wartosc.grid(row=1, column=7)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()



root.mainloop()