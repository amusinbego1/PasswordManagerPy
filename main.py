from tkinter import *
from tkinter import messagebox
from gen_pas import gen_pas
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.configure(padx = 20, pady=20)
FONT = ("Courier", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)
    password = gen_pas()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------------#
def search():
    if not website_entry.get():
        messagebox.showerror("Error", "Blank search field")
    else:
        try:
            with open("passwords.json") as file:
                all_data = json.load(file)
                semail = all_data[website_entry.get().lower()]["email"]
                spass = all_data[website_entry.get().lower()]["password"]
                messagebox.showinfo(website_entry.get(), f"Email/Username: {semail}\nPassword: {spass}")
        except:
            messagebox.showerror("Name error", f"Could not find website with name: '{website_entry.get()}'")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    website_entry.delete(0, END)
    email = email_entry.get()
    email_entry.delete(0, END)
    password = password_entry.get()
    password_entry.delete(0, END)
    website_entry.focus()
    if password and website and email:
        new_data = {
            website.lower(): {
                "email": email,
                "password": password,
            }
        }
        try:
            with open("passwords.json", mode="r") as file:
                data = json.load(file)
        except:
            with open("passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)
        messagebox.showinfo("Added", "Password added successfully")
    else:
        messagebox.showerror("Empty fields", "Please fill all fields")
# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(height=200, width=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = img)
canvas.grid(row = 0, column = 1, pady=(0,20))

website_label = Label(text="Website: ", font=FONT, height=2)
website_label.grid(row = 1, column = 0, padx=(100, 10), sticky="e")

email_label = Label(text="Email/Username: ", font=FONT, height=2)
email_label.grid(row = 2, column = 0, padx=(100,10), sticky="e")

password_label = Label(text="Password: ", font=FONT, height=2)
password_label.grid(row=3, column = 0, padx=(100, 10), sticky="e")

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

email_entry = Entry(width = 60)
email_entry.grid(row=2, column=1, columnspan=2, padx=(0, 100), sticky="w")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="w")

gen_button = Button(text="Generate Password", font=FONT, command=generate)
gen_button.grid(row=3, column=2, sticky="e", padx=(0, 100))

add_button = Button(text="Add", width=20, font=FONT, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=(0,100), pady=(10, 50))

search_button = Button(text="Search",width=17, font=FONT, command=search)
search_button.grid(row=1, column = 2, padx=(0, 100), sticky="e")



window.mainloop()