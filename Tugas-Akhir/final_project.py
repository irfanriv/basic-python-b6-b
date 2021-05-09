from tkinter import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def sent():
    global almt_email, password, subject, pesan
    almt_email = str(e1.get())
    password = str(e2.get())
    subject = str(e3.get())
    pesan = str(T.get("1.0",END))
    #print(almt_email)
    #print(password)
    #print(subject)
    #print(pesan)
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email import encoders

    alamat_emailnya = []
    listalamatemail = []
    file = open("receiver_list.txt", "r")
    for nama in file:
        alamat_emailnya.append(nama)
    
    for nama in alamat_emailnya:
        list_kata_hapus = nama.replace("\n","")
        listalamatemail.append(list_kata_hapus)
    sender = almt_email
    receiver = listalamatemail
    body_of_email = pesan

    #buat message, subject line, from and to
    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    
    #memperhubung ke gmail
    s = smtplib.SMTP_SSL(host = 'smpt.gmail.com', port = 465)
    s.login(user = sender, password = password)
    s.sendmail(sender, receivers, msg.as_string())
    s.quit

def keluar():
    exit()

ui=Tk()
ui.title('Email Messanger Indonesian.ai Batch 6')
ui.geometry("400x400")

l1 = Label(ui, text='Enter Your Email :').grid(row=0, pady=5) 
l2 = Label(ui, text='Enter Your Password :').grid(row=1, pady=5)
l3 = Label(ui, text='Enter Your Subject :').grid(row=2, pady=5) 

e1 = Entry(ui, width=40) 
e1.grid(row=0, column=1, pady=5)
e2 = Entry(ui, width=40) 
e2.grid(row=1, column=1, pady=5) 
e3 = Entry(ui, width=40) 
e3.grid(row=2, column=1, pady=5) 

l4 = Label(ui, text="Your Message :").grid(row=3)
T = Text(ui, height=10, width=30) 
T.insert(END,"") 
T.grid(row=3, column=1, pady=5)

b1 = Button(ui, text='Sent', width=10, command=sent, bg='white') 
b1.grid(row=4, column=0, pady=10)
b2 = Button(ui, text='Exit', width=10, command=keluar, bg='white') 
b2.grid(row=5, column=0, pady=10)
ui.mainloop() 