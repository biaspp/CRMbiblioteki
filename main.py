from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import colorchooser
import csv
import tkinter as tk

root = Tk()
root.title('Biblioteka')
root.iconbitmap('bib.ico')
root.geometry("1000x500")

root['bg'] = "white"

# combobox do szukania w menu


def save_csv():
    odpowiedz = messagebox.askyesno(
        "UUUUUWAGA!!!", "Po kliknięciu tak, dane zostaną zapisane w pliku o nazwie zapis.csv \n Jesteś pewien????")
    if odpowiedz == 1:
        with open("zapis.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')

            for row_id in my_tree.get_children():
                row = my_tree.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)


def query_database():
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect('ksiazki.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM ksiazki")
    records = c.fetchall()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
        count += 1

    conn.commit()
    conn.close()


def search_records():

    selected = search_entry.get()
    lookup_record = search_entry2.get()
    if selected == "Autor":
        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE autor like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()

    if selected == "Tytuł":
        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE tytul like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()

    if selected == "ID":

        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE oid like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()
#"Autor", "Tytuł", "ID", "Gatunek", "Rok wydania", "Język", "Wydawnictwo"
    if selected == "Gatunek":
        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE gatunek like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()

    if selected == "Rok wydania":
        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE rok_wydania like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()
    if selected == "Język":
        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE jezyk like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()

    if selected == "Wydawnictwo":
        search.destroy()

        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM ksiazki WHERE wydawnictwo like ?",
                  (lookup_record,))
        records = c.fetchall()

        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        conn.commit()
        conn.close()


def lookup_records():
    global search_entry, search, search_entry2

    search = Toplevel(root)
    search.title("Wyszukaj rekordy")
    search.geometry("400x300")
    search.iconbitmap('bib.ico')
    search['bg'] = "#fbd2d7"

    search_frame = LabelFrame(search, text="Po której kolumnie wyszukać?")
    search_frame.pack(padx=10, pady=10)
    search_frame['bg'] = "#fbd2d7"

    search_entry = ttk.Combobox(search_frame, value=[
                                "Autor", "Tytuł", "ID", "Gatunek", "Rok wydania", "Język", "Wydawnictwo"], font=("Helvetica", 18))
    search_entry.current(0)

    search_entry.pack(pady=20, padx=20)

    search_frame2 = LabelFrame(search, text="Co wyszukać?")
    search_frame2.pack(padx=10, pady=10)
    search_frame2['bg'] = "#fbd2d7"

    search_entry2 = Entry(search_frame2, font=("Helvetica", 18))
    search_entry2.pack(pady=20, padx=20)

    search_button = Button(
        search,  text="Wyszukaj rekordy", command=search_records, background="#e4a199", foreground="white")
    search_button.pack(padx=20, pady=20)


def primary_color():
    primary_color = colorchooser.askcolor()[1]

    if primary_color:

        my_tree.tag_configure('evenrow', background=primary_color)


def secondary_color():
    secondary_color = colorchooser.askcolor()[1]
    if secondary_color:

        my_tree.tag_configure('oddrow', background=secondary_color)


def highlight_color():
    highlight_color = colorchooser.askcolor()[1]
    if highlight_color:
        style.map("Treeview",
                  background=[('selected', highlight_color)])


my_menu = Menu(root)
root.config(menu=my_menu)

option_menu = Menu(my_menu, tearoff=0)
option_menu['bg'] = "#fbd2d7"
my_menu.add_cascade(label="Opcje", menu=option_menu)

option_menu.add_command(label="Pierwszy kolor", command=primary_color)
option_menu.add_command(label="Drugi kolor", command=secondary_color)
option_menu.add_command(label="Kolor zaznaczenia", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Wyjdź z aplikacji", command=root.quit)

search_menu = Menu(my_menu, tearoff=0)
search_menu['bg'] = "#fbd2d7"
my_menu.add_cascade(label="Wyszukaj", menu=search_menu)

search_menu.add_command(label="Wyszukaj", command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Resetuj", command=query_database)

conn = sqlite3.connect('ksiazki.db')

c = conn.cursor()

c.execute(""" CREATE TABLE if not exists ksiazki(
    autor text,
    tytul text,
    id integer,
    gatunek text,
    rok_wydania text,
    jezyk text,
    wydawnictwo text)
    """)

conn.commit()

conn.close()

# styl
style = ttk.Style()
# tematstylu
style.theme_use('default')
# kolorki
style.configure("Treeview",
                background="#fbd2d7",
                foreground="black",
                rowheight=25,
                fieldbackground="#fbd2d7")
style.configure("Treeview.Heading", background="#e4a199", foreground="white")
style.map("Treeview",
          background=[('selected', "#e4a199")])
tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview, bg="#ce897b")

my_tree['columns'] = ("Autor", "Tytuł", "ID",
                      "Gatunek", "Rok wydania", "Język", "Wydawnictwo")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=40)
my_tree.column("Autor", anchor=W, width=140)
my_tree.column("Tytuł", anchor=CENTER, width=140)
my_tree.column("Gatunek", anchor=W, width=200)
my_tree.column("Rok wydania", anchor=W, width=140)
my_tree.column("Język", anchor=CENTER, width=140)
my_tree.column("Wydawnictwo", anchor=CENTER, width=140)

my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Autor", text="Autor", anchor=CENTER)
my_tree.heading("Tytuł", text="Tytuł", anchor=CENTER)
my_tree.heading("Gatunek", text="Gatunek", anchor=CENTER)
my_tree.heading("Rok wydania", text="Rok wydania", anchor=CENTER)
my_tree.heading("Język", text="Język", anchor=CENTER)
my_tree.heading("Wydawnictwo", text="Wydawnictwo", anchor=CENTER)

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="#fbd2d7")

# dotaddziala
data_frame = LabelFrame(root, text="Rekord")
data_frame.pack(fill="x", expand="yes", padx=20)
data_frame['bg'] = "#fbd2d7"

fn_label = Label(data_frame, text="Autor")
fn_label['bg'] = "#fbd2d7"
fn_label.grid(row=0, column=0, padx=10, pady=10)
autor_entry = Entry(data_frame)
autor_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Tytuł")
ln_label['bg'] = "#fbd2d7"
ln_label.grid(row=0, column=2, padx=10, pady=10)
tyt_entry = Entry(data_frame)
tyt_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")

id_entry = Entry(data_frame)

# kasiajestzajebista
gatunek_label = Label(data_frame, text="Gatunek")
gatunek_label['bg'] = "#fbd2d7"
gatunek_label.grid(row=1, column=0, padx=10, pady=10)
gat_entry = Entry(data_frame)
gat_entry.grid(row=1, column=1, padx=10, pady=10)

rok_wydania_label = Label(data_frame, text="Rok wydania")
rok_wydania_label['bg'] = "#fbd2d7"
rok_wydania_label.grid(row=1, column=2, padx=10, pady=10)
rok_entry = Entry(data_frame)
rok_entry.grid(row=1, column=3, padx=10, pady=10)

jezyk_label = Label(data_frame, text="Język")
jezyk_label['bg'] = "#fbd2d7"
jezyk_label.grid(row=1, column=4, padx=10, pady=10)
jez_entry = Entry(data_frame)
jez_entry.grid(row=1, column=5, padx=10, pady=10)

wydawnictwo_label = Label(data_frame, text="Wydawnictwo")
wydawnictwo_label['bg'] = "#fbd2d7"
wydawnictwo_label.grid(row=1, column=6, padx=10, pady=10)
wyd_entry = Entry(data_frame)
wyd_entry.grid(row=1, column=7, padx=10, pady=10)


# dogory
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
# dodolu


def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
    conn = sqlite3.connect('ksiazki.db')
    c = conn.cursor()
    c.execute("DELETE from ksiazki WHERE oid=" + id_entry.get())
    conn.commit()
    conn.close()
    clear_entries()
    messagebox.showinfo("Usunięto! ", "Rekord został usunięty!! :333")


def remove_many():
    response = messagebox.askyesno(
        "HOOOOOOOOOLA!!!", "To usunie WSZYSTKIE zaznaczone przez Ciebie rekordy\n Jesteś pewien????")

    if response == 1:
        x = my_tree.selection()

        ids_to_delete = []

        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[2])

        for record in x:
            my_tree.delete(record)

        conn = sqlite3.connect('ksiazki.db')

        c = conn.cursor()

        c.executemany("DELETE FROM ksiazki WHERE id = ?",
                      [(a,) for a in ids_to_delete])

        conn.commit()
        conn.close()
        clear_entries()


def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


def clear_entries():
    autor_entry.delete(0, END)
    tyt_entry.delete(0, END)
    id_entry.delete(0, END)
    gat_entry.delete(0, END)
    rok_entry.delete(0, END)
    jez_entry.delete(0, END)
    wyd_entry.delete(0, END)


def select_record(e):
    autor_entry.delete(0, END)
    tyt_entry.delete(0, END)
    id_entry.delete(0, END)
    gat_entry.delete(0, END)
    rok_entry.delete(0, END)
    jez_entry.delete(0, END)
    wyd_entry.delete(0, END)

    selected = my_tree.focus()

    values = my_tree.item(selected, 'values')

    autor_entry.insert(0, values[0])
    tyt_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    gat_entry.insert(0, values[3])
    rok_entry.insert(0, values[4])
    jez_entry.insert(0, values[5])
    wyd_entry.insert(0, values[6])


def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(autor_entry.get(), tyt_entry.get(), id_entry.get(
    ), gat_entry.get(), rok_entry.get(), jez_entry.get(), wyd_entry.get(),))

    conn = sqlite3.connect('ksiazki.db')

    c = conn.cursor()

    c.execute("""UPDATE ksiazki SET
        autor = :autor,
        tytul = :tytul,
        gatunek = :gatunek,
        rok_wydania = :rok_wydania,
        jezyk = :jezyk,
        wydawnictwo = :wydawnictwo

        WHERE oid = :oid""",
              {
                  'autor': autor_entry.get(),
                  'tytul': tyt_entry.get(),
                  'gatunek': gat_entry.get(),
                  'rok_wydania': rok_entry.get(),
                  'jezyk': jez_entry.get(),
                  'wydawnictwo': wyd_entry.get(),
                  'oid': id_entry.get(),
              })
    conn.commit()

    conn.close()

    autor_entry.delete(0, END)
    tyt_entry.delete(0, END)
    id_entry.delete(0, END)
    gat_entry.delete(0, END)
    rok_entry.delete(0, END)
    jez_entry.delete(0, END)
    wyd_entry.delete(0, END)


def add_record():
    conn = sqlite3.connect('ksiazki.db')
    c = conn.cursor()

    c.execute("INSERT INTO ksiazki VALUES (:autor, :tytul, :id, :gatunek, :rok_wydania, :jezyk, :wydawnictwo)",
              {
                  'autor': autor_entry.get(),
                  'tytul': tyt_entry.get(),
                  'id': id_entry.get(),
                  'gatunek': gat_entry.get(),
                  'rok_wydania': rok_entry.get(),
                  'jezyk': jez_entry.get(),
                  'wydawnictwo': wyd_entry.get(),
              })

    conn.commit()
    conn.close()

    autor_entry.delete(0, END)
    tyt_entry.delete(0, END)
    id_entry.delete(0, END)
    gat_entry.delete(0, END)
    rok_entry.delete(0, END)
    jez_entry.delete(0, END)
    wyd_entry.delete(0, END)

    # czysc treeview
    my_tree.delete(*my_tree.get_children())
    query_database()


# przyciski
button_frame = LabelFrame(root, text="Działania")
button_frame.pack(fill="x", expand="yes", padx=20)
button_frame['bg'] = "#fbd2d7"

update_button = Button(
    button_frame, text="Zaktualizuj wybrany rekord", bg='#e4a199', fg='White', command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Dodaj rekord",
                    bg='#e4a199', fg='White', command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)


remove_one_button = Button(
    button_frame, text="Usuń zaznaczony", bg='#e4a199', fg='White', command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(
    button_frame, text="Usuń wiele zaznaczonych", bg='#e4a199', fg='White', command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(
    button_frame, text="Przenieś w górę", bg='#e4a199', fg='White', command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(
    button_frame, text="Przenieś w dół", bg='#e4a199', fg='White', command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

button_save = tk.Button(button_frame, text='Zapisz w csv',
                        bg='#e4a199', fg='White', command=save_csv)
button_save.grid(row=0, column=7, padx=10, pady=10)

select_record_button = Button(
    button_frame, text="Wyczyść", bg='#e4a199', fg='White', command=clear_entries)
select_record_button.grid(row=0, column=8, padx=10, pady=10)


# bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

query_database()

root.mainloop()
