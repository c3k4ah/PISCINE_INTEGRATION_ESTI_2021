import cv2
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import image_resize
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
print("okay1")
#PAGE D'ACCEUILLE
page = Tk()
style = ttk.Style(page)
style.configure('lefttab.TNotebook', background='#ff706e',tabposition='ws')
nb = ttk.Notebook(page, style='lefttab.TNotebook')
nb.pack(expand=1, fill="both")
page.geometry("1366x768")
page.title("PHOTOBOOTH")
# page.iconbitmap("./images/photoBooth.ico")

page1 = ttk.Frame(nb)
nb.add(page1, text='1')
# page.resizable(0,0)
label1 = Label(page1)
label1.place(relx=0, rely=0, width=1366, height=768)
img1 = PhotoImage(file="./images/acceuille.png")
label1.configure(image=img1)

def ouvrirMain():
    nb.select(page2)
print("okay2")
mainButton = Button(page1, text="GO!!", command=ouvrirMain)
mainButton.place(x=645, y=340, width=140, height=100)
mainButton.configure(overrelief="flat")
mainButton.configure(relief="flat")
mainButton.configure(activebackground="white")
mainButton.configure(background="#fe8062")
mainButton.configure(foreground="white")
mainButton.configure(cursor="hand2")
mainButton.configure(font="-family {Poppins SemiBold} -size 30")
mainButton.configure(borderwidth=50)
page3 = ttk.Frame(nb)
nb.add(page3, text='3')
def send_message():
    address_info = address.get()

    email_body_info = email_body.get()

    print(address_info, email_body_info)

    sender_email = "*******************"

    sender_password = "*******"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = address_info
    msg['Subject'] = 'PHOTOBOOTH'

    body = email_body_info
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = './img/save.jpg'
    attachment = open('./img/save.jpg', "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload(attachment.read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    # Converts the Multipart msg into a string
    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, sender_password)
    print("Login successful")

    server.sendmail(sender_email, address_info, text)
    messagebox.showinfo("BRAVO", "Votre mail a bien été envoyer!")
    print("Message sent")

    address_entry.delete(0, END)
    email_body_entry.delete(0, END)

    server.quit()
    print("Done")
# #PAGE MAIL SEND
# win = Tk()
# win.geometry("1366x768")
# #win.iconbitmap(r"photoBooth.ico")
# #win.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='photoBooth.ico'))
# #win.iconphoto(False, tk.PhotoImage(file='photoBooth.ico'))
# win.resizable(0, 0)
# win.title("ALEFA MAILAKA ZARAINA AMIN'NY BANDY AKAMA!")

label3 = Label(page3)
label3.place(relx=0, rely=0, width=1366, height=768)
img3 = PhotoImage(file="./images/send.png")
label3.configure(image=img3)
print("okay3")
def fotona2():
    time_string = time.strftime('%H:%M:%S-%p')
    lera2.config(text=time_string)
    lera2.after(1000, fotona2)
lera2=Label(page3, text = fotona2,fg='black')
lera2.place(relx=0.81, rely=0.060, width=150, height=36)
lera2.configure(background="#D2463E")
lera2.configure(font="-family {Poppins SemiBold} -size 15")
fotona2()

address = StringVar()
email_body = StringVar()

email_body_entry = Entry(page3, textvariable=email_body)
email_body_entry.place(x=480, y=285, width=411, height=37)

address_entry = Entry(page3, textvariable=address)
address_entry.place(x=480, y=199, width=411, height=37)

def retourMain():
    nb.select(page2)

saveButton = Button(page3, text="ENVOYER", command=send_message)
saveButton.place(relx=0.376, rely=0.730, width=356, height=43)
saveButton.configure(overrelief="flat")
saveButton.configure(relief="flat")
saveButton.configure(activebackground="#D2463E")
saveButton.configure(background="#D2463E")
saveButton.configure(foreground="#ffffff")
saveButton.configure(cursor="hand2")
saveButton.configure(font="-family {Poppins SemiBold} -size 15")
saveButton.configure(borderwidth="0")

print("okay4")
retourButton = Button(page3, text="RETOUR", command=retourMain)
retourButton.place(relx=0.376, rely=0.840, width=356, height=43)
retourButton.configure(overrelief="flat")
retourButton.configure(relief="flat")
retourButton.configure(activebackground="#D2463E")
retourButton.configure(background="#D2463E")
retourButton.configure(foreground="#ffffff")
retourButton.configure(cursor="hand2")
retourButton.configure(font="-family {Poppins SemiBold} -size 15")
retourButton.configure(borderwidth="0")

# def Exit():
#     sure = messagebox.askyesno("Quiter", "Etes-vous sur de vouloir quitter?", parent=win)
#     if sure == True:
#         win.destroy()
# win.protocol("WM_DELETE_WINDOW", Exit)
#PAGE APPLI
#def mainWin():
page2 = ttk.Frame(nb)
nb.add(page2, text='2')

cap = cv2.VideoCapture(0)
face_cascade        = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
eyes_cascade        = cv2.CascadeClassifier('cascades/third-party/frontalEyes35x16.xml')
nose_cascade        = cv2.CascadeClassifier('cascades/third-party/Nose18x15.xml')
glasses             = cv2.imread("images/fun/glasses2.png", -1)
glasses1             = cv2.imread("images/fun/glasses1.png", -1)
mustache            = cv2.imread('images/fun/mustache.png',-1)
mustache1                = cv2.imread('images/fun/mustache1.png',-1)
print("okay5")
lunette1 = 0
lunette = 0
moustache1 = 0
moustache = 0
#nomFichier= " "


def writeString(frame):
    cv2.putText(frame,nom.get(),(20,450),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),cv2.LINE_AA)

def lunetteFUnction():
    global lunette

    if lunette == 0:
        lunette = 1
    elif lunette ==1:
        lunette = 0


def lunette1Function():
    global lunette1

    if lunette1 == 0:
        lunette1 = 1
    elif lunette1 == 1:
        lunette1 = 0

def moustacheFunction():
    global moustache

    if moustache == 0:
        moustache = 1
    elif moustache == 1:
        moustache = 0

def moustache1Function():
    global moustache1

    if moustache1 == 0:
        moustache1 = 1
    elif moustache1 == 1:
        moustache1 = 0

def glass(roi_gray):
    eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
    for (ex, ey, ew, eh) in eyes:
        # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
        roi_eyes = roi_gray[ey: ey + eh, ex: ex+ int(ex/-1.0) + ew]
        glasses2 = image_resize(glasses.copy(), width=int(ew*1.2))

        gw, gh, gc = glasses2.shape
        for i in range(0, gw):
            for j in range(0, gh):
                # print(glasses[i, j]) #RGBA
                if glasses2[i, j][3] != 0:  # alpha 0
                    roi_color[ey + i, ex + j] = glasses2[i, j]
print("okay6")
def lunetteB(roi_gray):
    eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
    for (ex, ey, ew, eh) in eyes:
        # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
        roi_eyes = roi_gray[ey: ey + eh, ex: ex + int(ex / -1.0) + ew]
        glasses2 = image_resize(glasses1.copy(), width=int(ew * 1.2))

        gw, gh, gc = glasses2.shape
        for i in range(0, gw):
            for j in range(0, gh):
                # print(glasses[i, j]) #RGBA
                if glasses2[i, j][3] != 0:  # alpha 0
                    roi_color[ey + i, ex + j] = glasses2[i, j]

def nose(roi_gray):
    nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
    for (nx, ny, nw, nh) in nose:
        # cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
        roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]
        mustache2 = image_resize(mustache.copy(), width=int(nw*1.2))

        mw, mh, mc = mustache2.shape
        for i in range(0, mw):
            for j in range(0, mh):
                # print(glasses[i, j]) #RGBA
                if mustache2[i, j][3] != 0:  # alpha 0
                    roi_color[ny + int(nh / 2.0) + i, nx + j] = mustache2[i, j]

def mustacheB(roi_gray):
    mustacheB = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
    for (nx, ny, nw, nh) in mustacheB:
        # cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
        roi_tete = roi_gray[ny: ny + nh, nx: nx + nw]
        mustache2 = image_resize(mustache1.copy(), width=nw)

        mw, mh, mc = mustache2.shape
        for i in range(0, mw):
            for j in range(0, mh):
                # print(glasses[i, j]) #RGBA
                if mustache2[i, j][3] != 0:  # alpha 0
                    roi_color[ny + int(nh / 3.0)+ i, nx + j] = mustache2[i, j]


def SaveTimePic():
    #global nomFichier
    #nomFichier = nom.get()+".jpg"
    image = Image.fromarray(imgPrise)
    messagebox.showinfo("BIEN!", "BOGOSY ANNN ...l'image a été enregistré!")
    image.save("img/save.jpg")
print("okay7")
# root = Tk()
# root.geometry("1366x768")
# #root.iconbitmap(r"photoBooth.ico")
# #root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='photoBooth.ico'))
# #root.iconphoto(False, tk.PhotoImage(file='photoBooth.ico'))
# root.resizable(0,0)
label2 = Label(page2)
label2.place(relx=0, rely=0, width=1366, height=768)
img2 = PhotoImage(file="./images/frame.png")
label2.configure(image=img2)

def fotona():
    time_string = time.strftime('%H:%M:%S-%p')
    lera.config(text=time_string)
    lera.after(1000, fotona)

lera=Label(page2, text = fotona,fg='black')
lera.place(relx=0.81, rely=0.060, width=150, height=36)
lera.configure(background="#ffa970")
lera.configure(font="-family {Poppins SemiBold} -size 15")
fotona()
#
# def Exit():
#     sure = messagebox.askyesno("Quiter", "Etes-vous sur de vouloir quitter?", parent=root)
#     if sure == True:
#         root.destroy()
# root.protocol("WM_DELETE_WINDOW", Exit)
#Boutton lunette
lunneteButton = Button(page2, text="Lunette1", command=lunetteFUnction)
lunneteButton.place(x=163,y=145,width=117, height=33)
lunneteButton.configure(overrelief="flat")
lunneteButton.configure(relief="flat")
lunneteButton.configure(activebackground="#ffa970")
lunneteButton.configure(background="#ff706e")
lunneteButton.configure(foreground="#ffc071")
lunneteButton.configure(cursor="hand2")
lunneteButton.configure(font="-family {Poppins SemiBold} -size 13")
lunneteButton.configure(borderwidth="0")

MoustacheButton =Button(page2, text="Lunette2", command=lunette1Function)
MoustacheButton.place(x=163,y=295,width=117, height=33)
MoustacheButton.configure(overrelief="flat")
MoustacheButton.configure(relief="flat")
MoustacheButton.configure(activebackground="#ffa970")
MoustacheButton.configure(background="#ff706e")
MoustacheButton.configure(foreground="#ffc071")
MoustacheButton.configure(cursor="hand2")
MoustacheButton.configure(font="-family {Poppins SemiBold} -size 13")
MoustacheButton.configure(borderwidth="0")
print("okay8")
#Boutton mustache
hateButton =Button(page2, text="Moustache1", command=moustacheFunction)
hateButton.place(x=163,y=449,width=117, height=33)
hateButton.configure(overrelief="flat")
hateButton.configure(relief="flat")
hateButton.configure(activebackground="#ffa970")
hateButton.configure(background="#ff706e")
hateButton.configure(foreground="#ffc071")
hateButton.configure(cursor="hand2")
hateButton.configure(font="-family {Poppins SemiBold} -size 13")
hateButton.configure(borderwidth="0")

mustache1Button =Button(page2, text="Moustache2", command=moustache1Function)
mustache1Button.place(x=163,y=600,width=117, height=33)
mustache1Button.configure(overrelief="flat")
mustache1Button.configure(relief="flat")
mustache1Button.configure(activebackground="#ffa970")
mustache1Button.configure(background="#ff706e")
mustache1Button.configure(foreground="#ffc071")
mustache1Button.configure(cursor="hand2")
mustache1Button.configure(font="-family {Poppins SemiBold} -size 13")
mustache1Button.configure(borderwidth="0")

saveButton =Button(page2, text="SHOOT", command=SaveTimePic)
saveButton.place(x=850,y=634,width=117, height=33)
saveButton.configure(overrelief="flat")
saveButton.configure(relief="flat")
saveButton.configure(activebackground="#ffa970")
saveButton.configure(background="#ffa970")
saveButton.configure(foreground="#ff6b6d")
saveButton.configure(cursor="hand2")
saveButton.configure(font="-family {Poppins SemiBold} -size 15")
saveButton.configure(borderwidth="0")

def ouvrirSend():
    #ttk.Notebook.select(page3)
    nb.select(page3)
print("okay9")
mailButton =Button(page2, text="SEND", command=ouvrirSend)
mailButton.place(x=1025,y=634,width=70, height=33)
mailButton.configure(overrelief="flat")
mailButton.configure(relief="flat")
mailButton.configure(activebackground="#ffa970")
mailButton.configure(background="#ffa970")
mailButton.configure(foreground="#ff6b6d")
mailButton.configure(cursor="hand2")
mailButton.configure(font="-family {Poppins SemiBold} -size 15")
mailButton.configure(borderwidth="0")

# root.title("PHOTOBOOTH")


fi = LabelFrame(page2,bg="#ffa970")
fi.place(x=490, y=100)
Li = Label(fi, bg="black")
Li.pack()

nom = tk.StringVar()
nomTaper = ttk.Entry(page2, textvariable=nom)
nomTaper.place(x=475,y=630, width=280, height=40)
print("okay10")
#tous ce qui est detection et filtre
while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    writeString(frame)

    for (x, y, tw, h) in faces:
        roi_gray    = gray[y:y+h, x:x+h] # rec
        roi_color   = frame[y:y+h, x:x+h]


        if lunette == 1:
            glass(roi_gray)
        if lunette1 == 1:
            lunetteB(roi_gray)
        if moustache == 1:
            nose(roi_gray)
        if moustache1 == 1:
            mustacheB(roi_gray)

    imgPrise = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(Image.fromarray(frame))
    Li['image'] = frame
    page.update()#ne jamais supprimer ce truc ..JAMAIS!!!
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
# root.mainloop()
print("okay11")
#FONCTION SEND MAIL
# def sendWin():


page.mainloop()