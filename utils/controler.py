    zmienna_imie=entry_name.get()
    zmienna_nazwisko=entry_surname.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_post=entry_posts.get()
    user= boarders(name=zmienna_imie, surname=zmienna_nazwisko, location=zmienna_miejscowosc, post=zmienna_post)
    boarders.append(user)

    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_location.delete(0,END)
    entry_posts.delete(0,END)

    entry_name.focus()

    show_users()



def show_users():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(users):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name} {user.surname}')


def remove_user():
    i=listbox_lista_obiketow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    show_users()

def edit_user():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    location=users[i].location
    post=users[i].post

    entry_name.insert(0,name)
    entry_surname.insert(0,surname)
    entry_location.insert(0,location)
    entry_posts.insert(0,post)

    button_dodaj_obiekt.config(text='zapisz',command=lambda: update_user(i))

def update_user(i):
    new_name=entry_name.get()
    new_surname=entry_surname.get()
    new_location=entry_location.get()
    new_post=entry_posts.get()

    users[i].name=new_name
    users[i].surname=new_surname
    users[i].location=new_location
    users[i].post=new_post

    users[i].marker.delete()
    users[i].coordinates=users[i].get_coordinates()
    users[i].marker=map_widget.set_marker(users[i].coordinates[0],users[i].coordinates[1])



    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_location.delete(0,END)
    entry_posts.delete(0,END)
    entry_name.focus()


    button_dodaj_obiekt.config(text='Dodaj obiekt',command=add_user)
    show_users()


def show_user_details():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    location=users[i].location
    post=users[i].post
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_surname_wartosc.config(text=surname)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_posts_wartosc.config(text=post)

    map_widget.set_position(users[i].coordinates[0],users[i].coordinates[1])
    map_widget.set_zoom(17)