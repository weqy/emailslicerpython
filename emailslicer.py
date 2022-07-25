import tkinter as tk
from email_validator import validate_email, EmailNotValidError

root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=600)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(400, 280, window=entry1)


def slice():
    email = entry1.get()
    username = email[:email.index("@")]
    domain_name = email[email.index("@") + 1:]
    format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")

    label1 = tk.Label(root, text=format_)
    canvas1.create_window(400, 460, window=label1)

    try:
      email = validate_email(email).email
    except EmailNotValidError as e:
        error = (str(e))

    label2 = tk.Label(root, text=error)
    canvas1.create_window(400,460, window=label2)

label3 = tk.Label(text='Email Slicer and Validator')
canvas1.create_window(400, 100, window=label3)
button1 = tk.Button(text='Slice!', command=slice)
canvas1.create_window(400, 360, window=button1)

root.mainloop()
