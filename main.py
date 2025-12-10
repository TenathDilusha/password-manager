from tkinter import *
from tkinter import messagebox
import pyperclip
import json

def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save_data():
    web = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web : {
            "email": email,
            "password": password
        }
    }
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Dont leave any box empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message="Do you want to save?\n")
        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.insert(0, "@gmail.com")

def search_data():
    web_name = website_entry.get().capitalize()
    try:
        with open("passwords.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.askokcancel(title=web_name, message="No data")
    else:
        try:
            email = data[web_name]["email"]
            password = data[web_name]["password"]
        except KeyError:
            messagebox.askokcancel(title=web_name, message="No data")
        else:
            messagebox.askokcancel(title=web_name, message=f"email: {email}\n password: {password}")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#2C3E50")
window.focus()

canvas = Canvas(width=200, height=200, bg="#2C3E50", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 20))

label_1 = Label(text="Website:", font=("Arial", 11, "bold"), bg="#2C3E50", fg="#ECF0F1")
label_1.grid(column=0, row=1, sticky="w", pady=8, padx=(0, 10))

label_2 = Label(text="Email/Username:", font=("Arial", 11, "bold"), bg="#2C3E50", fg="#ECF0F1")
label_2.grid(column=0, row=2, sticky="w", pady=8, padx=(0, 10))

label_3 = Label(text="Password:", font=("Arial", 11, "bold"), bg="#2C3E50", fg="#ECF0F1")
label_3.grid(column=0, row=3, sticky="w", pady=8, padx=(0, 10))

website_entry = Entry(width=35, font=("Arial", 10), bg="#ECF0F1", fg="#2C3E50", relief="flat", 
                      borderwidth=2, highlightthickness=1, highlightbackground="#34495E", highlightcolor="#3498DB")
website_entry.grid(column=1, row=1, sticky="ew", padx=(5, 2))
website_entry.focus()

search_btn = Button(text="Search", font=("Arial", 9, "bold"),
                    bg="#3498DB", fg="white", activebackground="#2980B9", activeforeground="white",
                    relief="flat", cursor="hand2", command=search_data)
search_btn.grid(column=2, row=1, padx=(2, 0), sticky="ew")

email_entry = Entry(width=35, font=("Arial", 10), bg="#ECF0F1", fg="#2C3E50", relief="flat",
                    borderwidth=2, highlightthickness=1, highlightbackground="#34495E", highlightcolor="#3498DB")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5)
email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=35, font=("Arial", 10), bg="#ECF0F1", fg="#2C3E50", relief="flat",
                       borderwidth=2, highlightthickness=1, highlightbackground="#34495E", highlightcolor="#3498DB")
password_entry.grid(column=1, row=3, sticky="ew", padx=(5, 2))

password_btn = Button(text="Generate Password", font=("Arial", 9, "bold"), 
                      bg="#9B59B6", fg="white", activebackground="#8E44AD", activeforeground="white",
                      relief="flat", cursor="hand2", command=password_generator)
password_btn.grid(column=2, row=3, padx=(2, 0), sticky="ew")

add_btn = Button(text="Add", font=("Arial", 10, "bold"), 
                 bg="#27AE60", fg="white", activebackground="#229954", activeforeground="white",
                 relief="flat", cursor="hand2", command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, pady=(15, 0), padx=5, sticky="ew")

window.mainloop()
