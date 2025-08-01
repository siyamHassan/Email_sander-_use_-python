import smtplib
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x500")
root.title("this is a email sander")
root.config(bg="#6495ed")

def Email_sander(sender,resever,sub,pass_key,body):
    To = sender
    From = resever
    subject = sub
    passkey = pass_key
    main_body = body
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(To, passkey)
    server.sendmail(To, From, main_body)
    messagebox.showinfo("Email has been sand")
def submit():
    To = to_email.get()
    resever_email = from_email.get()
    subject = suject.get()
    passkey = pass_key.get()
    main_body = body.get()
    final = [To,resever_email,subject,passkey,main_body]
    print(final)
    Email_sander(To,resever_email,subject,passkey,main_body)

to_labal = tk.Label(root,text="TO:", font=("Arial", 12))
to_labal.pack(pady=10)
to_email = tk.Entry(root,width=30)
to_email.pack(pady=5)

from_lable = tk.Label(root, text="Form:", font=("Arial", 12))
from_lable.pack(pady=5)
from_email = tk.Entry(root, width=30)
from_email.pack(pady =5)

subject_lable = tk.Label(root, text="Subject:", font=("Arial", 12))
subject_lable.pack(pady=5)
suject = tk.Entry(root, width=30)
suject.pack(pady=5)

pass_labal = tk.Label(root,text="passkey:",font=("Arial",12))
pass_labal.pack(pady=5)
pass_key = tk.Entry(root,width=40,highlightthickness=8)
pass_key.pack(pady=5)

body_labal = tk.Label(root,text="Body write here:",font=("Arial",12))
body_labal.pack(pady=5)
body = tk.Entry(root,width=50,highlightthickness=12)
body.pack(pady=5)

tk.Button(root, text="Submit", command=submit, font=("Arial", 12), bg="lightblue").pack(pady=20)
root.mainloop()

# vwtd ushf mzro xjzv