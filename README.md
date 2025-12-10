🔐 Password Manager (Python + Tkinter + JSON Storage)

A simple yet powerful Password Manager built using Python Tkinter, featuring password generation, secure local storage, and an intuitive UI.
This application allows users to easily generate strong passwords, save credentials, and search stored data with ease.

🚀 Features
✔ Strong Password Generator

Randomly generates secure passwords using:
  Uppercase & lowercase letters
  Numbers
  Symbols

Automatically copied to clipboard using pyperclip.

✔ Save Login Credentials

Stores:
  Website
  Email/Username
  Password

All saved securely inside a passwords.json file using a structured dictionary format.

✔ Search Function

Quickly find saved credentials by entering a website name and retrieving:
  Email
  Password
  Instantly displayed using popup messages.

✔ Clean, Modern Tkinter UI

Includes:

  Custom color theme
  Styled labels & buttons
  Embedded logo
  Smooth form layout

🛠 Technologies Used

Python 3

Tkinter – GUI framework
json – local database storage
pyperclip – clipboard copy
random – password generation

▶️ How to Run
1. Install dependency:
  pip install pyperclip

2. Make sure main.py and logo.png are in the same folder.
3. Run the application:
  python main.py
