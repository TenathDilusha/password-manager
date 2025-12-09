from tkinter import *
from tkinter import messagebox
import pyperclip

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
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Dont leave any box empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message="Do you want to save?\n")
        if is_ok:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{web} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(0, "tenathdilusha@gmail.com")

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="black")
window.focus()

canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_1 = Label(text="Website:", font=("Arial", 12, "bold"), bg="black", fg="white")
label_1.grid(column=0, row=1, sticky="e", pady=5)

label_2 = Label(text="Email/Username:", font=("Arial", 12, "bold"), bg="black", fg="white")
label_2.grid(column=0, row=2, sticky="e", pady=5)

label_3 = Label(text="Password:", font=("Arial", 12, "bold"), bg="black", fg="white")
label_3.grid(column=0, row=3, sticky="e", pady=5)

website_entry = Entry(width=49)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=49)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "tenathdilusha@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

password_btn = Button(text="Generate Password", width=15, command=password_generator)
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=42, bg="#4CAF50", fg="white", command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, pady=10)
















window.mainloop()
