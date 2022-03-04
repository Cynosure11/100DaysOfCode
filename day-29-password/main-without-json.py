from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        # If user leave message box empty:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty."
                                                  "\n Pay attention peach!")
    else:
        # messagebox.showinfo(title="title", message="message")
        is_ok = messagebox.askokcancel(title="website",
                                       message=f"These are details entered of {website}: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it correct to save?")
        if is_ok:
            # with command automatically closing file, and you don't need close() function
            with open("data.txt", "a") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                # my version hot save email/password
                data_file.write(f"Website: {website}\n     Email: {email}\n     Password: {password}\n\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Creating window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# padx and pady is space between frame and picture

# Canvas (picture) settings
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
# canvas.pack()

# ---------------------------- Labels ------------------------------- #
# Website
website_label = Label(text="Website", font=("Arial", 18, "bold"))
website_label.config(text="Website: ")
website_label.grid(column=0, row=1)

# Email
email_label = Label(text="Email/Username", font=("Arial", 18, "bold"))
email_label.config(text="Email/Username: ")
email_label.grid(column=0, row=2)

# Password
password_label = Label(text="password", font=("Arial", 18, "bold"))
password_label.config(text="Password: ")
password_label.grid(column=0, row=3)


# ---------------------------- Buttons ------------------------------- #
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button # command=button_clicked
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=3)

# ---------------------------- Entries ------------------------------- #
# Entry Website input
website_entry = Entry(width=40)
print(website_entry.get())
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Entry Email/Username
email_entry = Entry(width=40)
print(email_entry.get())
email_entry.grid(column=1, row=2, columnspan=2)
# You ca use your email to automatically enter own email
# email_entry.insert(0, "atlasaial@gmail.com")

# Entry Password
password_entry = Entry(width=23)
print(password_entry.get())
password_entry.grid(column=1, row=3)

window.mainloop()
