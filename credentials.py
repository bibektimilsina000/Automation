from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def get_credentials():
    email = ""
    password = ""
    def submit():
        nonlocal email, password
        email = email_field.get()
        password = password_field.get()

    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("350x500")

    # Facebook Logo
    img = Image.open("facebook-logo.png")
    img = img.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    # Login Screen
    login_frame = ttk.Frame(login_screen, padding=20)
    login_frame.pack(expand=True, fill=BOTH)

    # Facebook Logo
    img_label = ttk.Label(login_frame, image=img)
    img_label.pack(pady=(30,0))

    # Email Entry
    email_field = ttk.Entry(login_frame, width=30,)
    email_field.pack(pady=(30,5))
    email_field.insert(0, "Email or Phone number")

    # Password Entry
    password_field = ttk.Entry(login_frame, show="*", width=30)
    password_field.pack()
    password_field.insert(0, "Password")

    # Submit Button
    submit_btn = ttk.Button(login_frame, text="Log In", command=submit)
    submit_btn.pack(pady=(20,0))

    # Separator Line
    separator = ttk.Separator(login_frame, orient=HORIZONTAL)
    separator.pack(fill=X, pady=20)

    # Footer Text
    footer_text = ttk.Label(login_frame, text="Forgot Password?  |  Sign Up for Facebook")
    footer_text.pack()

    login_screen.mainloop()
    return email, password

