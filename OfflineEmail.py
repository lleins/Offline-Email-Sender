import smtplib
import ssl
from email.message import EmailMessage
from tkinter import *
import os.path
from os.path import exists
import socket
import platform
from datetime import datetime
from tkinter import scrolledtext  # For Beta Version the password is always "Pass"
import os
import time
import datetime
import requests


#Last worked on:
#October 26, 2022


#Email to use: na2012176@gmail.com
#Password: fdsfsfsd12312

#Python Access Password: trylxxqyzqnwowiy


dir = os.path.join("C:\\","Offline Email")

if os.path.exists(dir):
    ""
else:
    os.mkdir(dir)
    path = "C:\\Offline Email\\Saved Emails.txt"
    path2 = "C:\\Offline Email\\AutoFill.txt"
    create2 = open(path2,"w")
    create = open(path, "w")
    create2.close()
    create.close()



def Remove_File(File_Name):
    path = "D:\\Offline Email\\" + File_Name +".txt"
    os.remove(path)


def Remove_File_Line_Content(Draft_Name):
    path = "D:\\Offline Email\\Saved Emails.txt"
    file = open(path, "r")
    replacement = ""
    for line in file:
        line = line.strip()
        changes = line.replace(Draft_Name, "")
        replacement = changes + "\n"
    file.close()
    fout = open(path, "w")
    fout.write(replacement)
    fout.close()

def close2():
    root1.destroy()

def Email_Valid(Email):
    email_address = Email
    response = requests.get("https://isitarealemail.com/api/email/validate", params={'email': email_address})
    status = response.json()['status']
    if status == "valid":
        return ("Valid")
    elif status == "invalid":
        return ("Not Valid")
    else:
        return("Does Not Exist")

def Login_Btn():

    def close():
        root.destroy()
        root1.wm_attributes('-alpha', 0.9)
    def Save_Draft():
        if (Subjectfld.get() == ""):
            lbl_Subject = Label(root, text="Subject Required.....", font=("Terminal", 8), bg="black", fg="red")  # Will be Gmailfl.get()
            lbl_Subject.place(x=550, y=226)
            lbl_Subject.after(2500, lambda: lbl_Subject.destroy())

        elif(Gmailfld.get() == ""):
            lbl_Subject2 = Label(root, text="Gmail Required......", font=("Terminal", 8), bg="black",fg="red")  # Will be Gmailfl.get()
            lbl_Subject2.place(x=550, y=226)
            lbl_Subject2.after(2500, lambda: lbl_Subject2.destroy())

        else:
            root1.wm_attributes('-alpha', 0.0)
            lbl_Subject = Label(root, text="                    ", font=("Terminal", 8), bg="black", fg="red")  # Will be Gmailfl.get()
            lbl_Subject.place(x=550, y=226)

            def close3():
                root3.destroy()

            def Save_Draft_Official():
                if (Draft_Namefld.get() == ""):
                    bl_Success = Label(root3, text="Name Required..", fg='red', font=("Terminal", 8), bg="black")
                    bl_Success.place(x=255, y=95)
                    bl_Success.after(2500, lambda: bl_Success.destroy())

                else:
                    bl_Success = Label(root3, text="Draft Saved....", fg='green', font=("Terminal", 8), bg="black")
                    bl_Success.place(x=255, y=95)
                    bl_Success.after(2500, lambda: bl_Success.destroy())

                    Draft_Name_Path = "D:\\Offline Email\\Saved Emails.txt"
                    Email_File_Creation = "D:\\Offline Email\\" + Draft_Namefld.get() + " Gmail.txt"
                    Subject_File_Creation = "D:\\Offline Email\\" + Draft_Namefld.get() + " Subject.txt"
                    Body_File_Creation = "D:\\Offline Email\\" + Draft_Namefld.get() + " Body.txt"
                    Open_Draft_File = open(Draft_Name_Path, "a")
                    Open_Gmail_File = open(Email_File_Creation, "w")
                    Open_Subject_File = open(Subject_File_Creation, "w")
                    Open_Body_File = open(Body_File_Creation, "w")
                    Open_Draft_File.write(Draft_Namefld.get() + "\n")
                    Open_Gmail_File.write(Recipientfld.get())
                    Open_Subject_File.write(Subjectfld.get())
                    Open_Body_File.write(bodyfld.get(1.0, "end-1c"))

                    Recipientfld.delete(0, END)
                    bodyfld.delete(1.0, END)
                    Subjectfld.delete(0, END)



            root3 = Tk()

            root3_app_width = 450
            root3_app_height = 250

            root3_screen_width = root3.winfo_screenwidth()
            root3_screen_height = root3.winfo_screenheight()

            root3_x = int((root3_screen_width / 2) - (root3_app_width / 2))
            root3_y = int((root3_screen_height / 2) - (root3_app_height / 2))


            lbl_Draft_Name = Label(root3, text="Name Draft: ", fg='white', font=("Terminal", 11), bg="black")
            lbl_Draft_Name.place(x=135, y=35)

            Draft_Namefld = Entry(root3, text="This is Password Widget", bd=1, fg='grey', font=("Terminal", 11),
                               bg="black", width=21)  # Passcode feild
            Draft_Namefld.place(x=135, y=55)
            Draft_Namefld.config(insertbackground="white")  # Changes test cursor color

            lbl_Accent12 = Label(root3, text=".\n.\n.\n.", fg='white', font=("System", 18), bg="black")
            lbl_Accent12.place(x=60, y=30)

            lbl_Accent22 = Label(root3, text=".\n.\n.\n.", fg='white', font=("System", 18), bg="black")
            lbl_Accent22.place(x=370, y=30)

            btn_Save = Button(root3, text="Save", padx=55, font=("Terminal", 11), fg='white', bg="green", command=Save_Draft_Official)
            btn_Save.place(x=145, y=140)

            btn_Close = Button(root3, text="Close", font=("Terminal", 11), fg='white', bg="red", command=close3)
            btn_Close.place(x=370, y=210)


            root3.wm_attributes('-alpha', 0.9)  # Transparency
            root3.protocol("WM_DELETE_WINDOW",
                           close3)  # controling the function of the close window icon (top right of window)
            root3.resizable(False, False)  # Cannot change size of the Window(It is locked)
            root3.title('Save Draft')  # Add Username to top of WebPage
            root3.geometry(f'{root3_app_width}x{root3_app_height}+{root3_x}+{root3_y}')
            root3.configure(bg='black')
            root3.mainloop()










    if (Email_Valid(Gmailfld.get()) == "Valid"):



        lbl_error = Label(root1, text="Login succesful.......", fg='light green', bg="black", font=("Terminal", 8))
        lbl_error.place(x=100, y=140)
        lbl_error.after(2500, lambda: lbl_error.destroy())
        root1.wm_attributes('-alpha', 0.0)  # Transparency
        def Send_Email():
            if (Email_Valid(Recipientfld.get()) == "Valid"):

                def Send_Another():
                    Recipientfld.delete(0, END)
                    bodyfld.delete(1.0, END)
                    Subjectfld.delete(0, END)
                    lbl_EmailSender.place_forget()
                    btn_Another.place_forget()

                now = datetime.datetime.now()
                year = '{:02d}'.format(now.year)
                month = '{:02d}'.format(now.month)
                day = '{:02d}'.format(now.day)
                day_month_year = '{}-{}-{}'.format(year, month, day)

                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)

                uname = platform.uname()

                hostname = socket.gethostname()
                IPAddr = socket.gethostbyname(hostname)
                email_sender = Gmailfld.get()
                email_password = Passfld.get()
                email_receiver = Recipientfld.get()

                subject = Subjectfld.get()

                body = (bodyfld.get(1.0, "end-1c"))

                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())



                lbl_EmailSender = Label(root, text="Email Sent.......", font=("Terminal", 8), bg="black", fg="light green")  # Will be Gmailfl.get()
                lbl_EmailSender.place(x=550, y=226)
                lbl_EmailSender.after(2500, lambda: lbl_EmailSender.destroy())

                btn_Another = Button(root, text="Send Another", font=("Terminal", 11), fg='white', bg="blue", command=Send_Another)
                btn_Another.place(x=767, y=425)

            elif(Email_Valid(Recipientfld.get()) == "Not Valid"):
                lbl_EmailSender2 = Label(root, text="Recipient Invalid", font=("Terminal", 8), bg="black", fg="red")  # Will be Gmailfl.get()
                lbl_EmailSender2.place(x=550, y=226)
                lbl_EmailSender2.after(2500, lambda: lbl_EmailSender2.destroy())

        def View_Drafts():
            root.wm_attributes('-alpha', 0.0)

            def File_Exists(File_Name):
                exists = os.path.isfile("D:\\Offline Email\\" + File_Name + " Body.txt")
                return exists

            def ReadFileLine(Line_Number):
                file = open("D:\\Offline Email\\Saved Emails.txt", "r")
                Line = file.readlines()
                return (Line[Line_Number])

            def Replace(Name):
                path = "D:\\Offline Email\\Saved Emails.txt"
                Number_of_Lines = sum(1 for line in open(path))
                list = []
                i = 0
                while i < Number_of_Lines:
                    if (ReadFileLine(i) == Name + "\n"):
                        i = i + 1
                    else:
                        list.append(ReadFileLine(i))
                        i = i + 1
                file_open = open(path, "w")
                for i in range(len(list)):
                    file_open.write(list[i])

            def Open_Draft():

                if (File_Exists(Openfld.get()) == False):
                    lbl_Error4 = Label(root4, text="Draft does not exist...", font=("Terminal", 8), bg="black",
                                       fg="red")
                    lbl_Error4.place(x=500, y=430)
                    lbl_Error4.after(2500, lambda: lbl_Error4.destroy())

                elif (File_Exists(Openfld.get()) == True):
                    lbl_Error4 = Label(root4, text="                       ", font=("Terminal", 8), bg="black",
                                       fg="black")
                    lbl_Error4.place(x=500, y=430)
                    Recipientfld.delete(0, END)
                    bodyfld.delete(1.0, END)
                    Subjectfld.delete(0, END)
                    Recipientfld.insert(0, Read_File("D:\\Offline Email\\" + Openfld.get() + " Gmail.txt"))
                    Subjectfld.insert(0, Read_File("D:\\Offline Email\\" + Openfld.get() + " Subject.txt"))
                    bodyfld.insert(1.0, Read_File("D:\\Offline Email\\" + Openfld.get() + " Body.txt"))
                    Remove_File(Openfld.get() + " Body")
                    Remove_File(Openfld.get() + " Subject")
                    Remove_File(Openfld.get() + " Gmail")
                    Replace(Openfld.get())
                    root4.destroy()
                    root.wm_attributes('-alpha', 0.9)

            def close4():
                root4.destroy()
                root.wm_attributes('-alpha', 0.9)
            def Read_File(File_Path):
                file_content = open(File_Path, "r")
                if (exists(File_Path)):  # opens/reads a file with a given file path....
                    return (file_content.read())
                else:
                    raise Exception("Error, File not present or empty....")

            now = datetime.datetime.now()
            year = '{:02d}'.format(now.year)
            month = '{:02d}'.format(now.month)
            day = '{:02d}'.format(now.day)
            day_month_year = '{}-{}-{}'.format(year, month, day)

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)




            root4 = Toplevel()

            root4_app_width = 900
            root4_app_height = 500

            root4_screen_width = root4.winfo_screenwidth()
            root4_screen_height = root4.winfo_screenheight()

            root4_x = int((root4_screen_width / 2) - (root4_app_width / 2))
            root4_y = int((root4_screen_height / 2) - (root4_app_height / 2))


            path = "D:\\Offline Email\\Saved Emails.txt"

            lbl_Header = Label(root4, text="Saved Drafts", font=("Terminal", 12), bg="black", fg="white")
            lbl_Header.place(x=380, y=25)

            lbl_Accent1 = Label(root4, text=". .", fg='white', bg='black', font=("Terminal", 13),
                                relief="flat")  # Accents
            lbl_Accent1.place(x=320, y=20)

            lbl_Accent2 = Label(root4, text=". .", fg='white', bg='black', font=("Terminal", 13),
                                relief="flat")  # Accents
            lbl_Accent2.place(x=550, y=20)

            lbl_Number_Saved_Drafts = Label(root4, text="Number of\nSaved Drafts:", font=("Terminal", 11), bg="black",
                                            fg="white")
            lbl_Number_Saved_Drafts.place(x=30, y=100)

            lbl_Number_Saved_Drafts_Actual = Label(root4, text=(sum(1 for line in open(path))) - 1, font=("Terminal", 11),
                                                   bg="black", fg="white", relief="sunken", width=4, height=2)
            lbl_Number_Saved_Drafts_Actual.place(x=60, y=150)

            lbl_Date = Label(root4, text="Day/Time:", font=("Terminal", 11), bg="black", fg="white")
            lbl_Date.place(x=803, y=100)

            lbl_Date_Actual = Label(root4, text=day_month_year + "\n" + current_time, font=("Terminal", 11), bg="black",
                                    fg="white", relief="sunken", width=12, height=4)
            lbl_Date_Actual.place(x=790, y=140)

            lbl_Header = Label(root4, text="Saved Drafts", font=("Terminal", 12), bg="black", fg="white")
            lbl_Header.place(x=380, y=25)

            Drafts_Viewfld = scrolledtext.ScrolledText(root4, bd=1, fg='grey', font=("Terminal", 12), bg="black",
                                                       width=50,
                                                       height=20)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
            Drafts_Viewfld.place(x=150, y=100)
            Drafts_Viewfld.insert(1.0, Read_File(path))
            Drafts_Viewfld.config(state=DISABLED)
            Drafts_Viewfld.config(insertbackground="white")  # Changes test cursor color

            Openfld = Entry(root4, bd=1, fg='grey', font=("Terminal", 12), bg="black", width=42)
            Openfld.place(x=150, y=450)
            Openfld.config(insertbackground="white")  # Changes text cursor color

            btn_Open = Button(root4, text="Open", padx=30, font=("Terminal", 11), fg='white', bg="green",
                              command=Open_Draft)
            btn_Open.place(x=669, y=450)

            btn_Close4 = Button(root4, text="Close", font=("Terminal", 11), fg='white', bg="red", command=close4)
            btn_Close4.place(x=820, y=450)

            lbl_Header = Label(root4, text="*Note*\nDrafts are deleted\nonce they are opened.\nYou would need to\nre-save after opening.", font=("Terminal", 8), bg="black", fg="red")
            lbl_Header.place(x=771, y=270)

            root4.wm_attributes('-alpha', 0.9)  # Transparency
            root4.protocol("WM_DELETE_WINDOW",
                           close4)  # controling the function of the close window icon (top right of window)
            root4.resizable(False, False)  # Cannot change size of the Window(It is locked)
            root4.title('View Drafts')  # Add Username to top of WebPage
            root4.geometry(f'{root4_app_width}x{root4_app_height}+{root4_x}+{root4_y}')#900x500
            root4.configure(bg='black')
            root4.mainloop()

        def Clear():
            Recipientfld.delete(0, END)
            bodyfld.delete(1.0, END)
            Subjectfld.delete(0, END)

        #Main Email GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        root = Toplevel()

        root_app_width = 900
        root_app_height = 500

        root_screen_width = root.winfo_screenwidth()
        root_screen_height = root.winfo_screenheight()

        root_x = int((root_screen_width / 2) - (root_app_width / 2))
        root_y = int((root_screen_height / 2) - (root_app_height / 2))

        lbl_EmailSender = Label(root, text=Gmailfld.get(), font=("Terminal", 12), bg="black", fg="white")  # Will be Gmailfl.get()
        lbl_EmailSender.place(x=325, y=20)

        lbl_Accent = Label(root, text=". .", font=("Terminal", 13), fg="white", bg="black")
        lbl_Accent.place(x=267, y=16)

        lbl_Accent2 = Label(root, text=". .", font=("Terminal", 13), fg="white", bg="black")
        lbl_Accent2.place(x=594, y=16)

        lbl_EmailSender = Label(root, text="Recipient Gmail Address: ", font=("Terminal", 12), bg="black",
                                fg="white")  # Will be Gmailfl.get()
        lbl_EmailSender.place(x=50, y=65)

        Recipientfld = Entry(root, bd=1, fg='grey', font=("Terminal", 12), bg="black", width=50)
        Recipientfld.place(x=52, y=100)
        Recipientfld.config(insertbackground="white")  # Changes test cursor color

        lbl_Subject = Label(root, text="Subject: ", font=("Terminal", 12), bg="black", fg="white")
        lbl_Subject.place(x=50, y=146)

        Subjectfld = Entry(root, bd=1, fg='grey', font=("Terminal", 12), bg="black", width=50)
        Subjectfld.place(x=52, y=180)
        Subjectfld.config(insertbackground="white")  # Changes test cursor color

        lbl_body = Label(root, text="Body: ", font=("Terminal", 12), bg="black", fg="white")
        lbl_body.place(x=50, y=235)

        bodyfld = scrolledtext.ScrolledText(root, bd=1, fg='grey', font=("Terminal", 12), bg="black", width=50, height=13)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
        bodyfld.place(x=52, y=265)
        bodyfld.config(insertbackground="white")  # Changes test cursor color

        btn = Button(root, text="Send ➤", font=("Terminal", 11), fg='white', bg="green", command=Send_Email)
        btn.place(x=820, y=460)

        btn = Button(root, text="Clear", font=("Terminal", 11), fg='white', bg="red", command=Clear)
        btn.place(x=758, y=460)

        btn = Button(root, text="Logout", font=("Terminal", 11), fg='white', bg="red", command=close)
        btn.place(x=820, y=20)

        btn = Button(root, text="Save as Draft", font=("Terminal", 11), fg='white', bg="blue", command=Save_Draft)
        btn.place(x=740, y=55)

        btn_ViewDrafts = Button(root, text="View Drafts", font=("Terminal", 11), fg='white', bg="green", command=View_Drafts)
        btn_ViewDrafts.place(x=710, y=20)



        root.wm_attributes('-alpha', 0.9)  # Transparency
        root.protocol("WM_DELETE_WINDOW",
                      close)  # controling the function of the close window icon (top right of window)
        root.resizable(False, False)  # Cannot change size of the Window(It is locked)
        root.title('Email Sender')  # Add Username to top of WebPage
        root.geometry(f'{root_app_width}x{root_app_height}+{root_x}+{root_y}') #900x500
        root.configure(bg='black')
        root.mainloop()
    # Main Email GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif(Email_Valid(Gmailfld.get()) == "Not Valid"):
        lbl_error = Label(root1, text="Email is not valid....", fg='red', bg="black", font=("Terminal", 8))
        lbl_error.place(x=100, y=140)
        lbl_error.after(2500, lambda: lbl_error.destroy())

    else:
        lbl_error = Label(root1, text="Email does not exist..", fg='red', bg="black", font=("Terminal", 8))
        lbl_error.place(x=100, y=140)
        lbl_error.after(2500, lambda: lbl_error.destroy())

#Login GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Write_to_File(Path, Text):
    fout = open(Path, "a")
    fout.write(Text + "\n")
    fout.close()



def Save_btn():
    def File_Exists(File_Name):
        exists = os.path.isfile("C:\\Offline Email\\" + File_Name + ".txt")
        return exists
    def Email_Valid(Email):
        email_address = Email
        response = requests.get("https://isitarealemail.com/api/email/validate", params={'email': email_address})
        status = response.json()['status']
        if status == "valid":
            return ("Valid")
        elif status == "invalid":
            return ("Not Valid")
        else:
            return ("Does Not Exist")


    if (Gmailfld.get() == "") and (Passfld.get() == ""):
        lbl_Number = Label(root1, text="Error", fg='red', font=("Terminal", 6), bg="black")
        lbl_Number.place(x=280, y=135)
        lbl_Number.after(2500, lambda: lbl_Number.destroy())

    elif(Gmailfld.get() == ""):
        lbl_Number = Label(root1, text="Error", fg='red', font=("Terminal", 6), bg="black")
        lbl_Number.place(x=280, y=135)
        lbl_Number.after(2500, lambda: lbl_Number.destroy())

    elif (Passfld.get() == ""):
        lbl_Number = Label(root1, text="Error", fg='red', font=("Terminal", 6), bg="black")
        lbl_Number.place(x=280, y=135)
        lbl_Number.after(2500, lambda: lbl_Number.destroy())

    else:
        if (Email_Valid(Gmailfld.get()) == "Valid") and (Passfld.get() != "") and (File_Exists(Gmailfld.get()) == False):
            Gmail = Gmailfld.get()
            Access = Passfld.get()

            Write_to_File("C:\\Offline Email\\AutoFill.txt", Gmail)
            Write_to_File("C:\\Offline Email\\" + Gmail + ".txt", Gmail)
            Write_to_File("C:\\Offline Email\\" + Gmail + " Pass.txt:Secret.txt", Access)

            lbl_Number = Label(root1, text="Saved", fg='green', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=280, y=135)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())
        else:
            lbl_Number = Label(root1, text="Error", fg='red', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=280, y=135)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())

def Saved_Emails():
    root1.wm_attributes('-alpha', 0.0)
    def Remove_File_Line_Content2(Draft_Name):
        path = "C:\\Offline Email\\AutoFill.txt"
        file = open(path, "r")
        replacement = ""
        for line in file:
            line = line.strip()
            changes = line.replace(Draft_Name, "")
            replacement = changes + "\n"
        file.close()
        fout = open(path, "w")
        fout.write(replacement)
        fout.close()

    def Remove_FileEmail(File_Name):
        path = "C:\\Offline Email\\" + File_Name + ".txt"
        os.remove(path)

    def Remove_FilePass(File_Name):
        path = "C:\\Offline Email\\" + File_Name + " Pass.txt"
        os.remove(path)

    def File_Exists(File_Name):
        exists = os.path.isfile("C:\\Offline Email\\" + File_Name + ".txt")
        return exists

    def Remove_Email():
        if (OpenfldEmail.get() == ""):
            lbl_Number = Label(SavedEmailsWindow, text="Error", fg='red', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=300, y=185)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())

        elif (File_Exists(OpenfldEmail.get()) == True):
            Remove_FileEmail(OpenfldEmail.get())
            Remove_FilePass(OpenfldEmail.get())
            Remove_File_Line_Content2(OpenfldEmail.get())
            OpenfldEmail.delete(0, END)

            lbl_Number = Label(SavedEmailsWindow, text="Removed", fg='green', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=300, y=185)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())

            lbl_NumberActual = Label(SavedEmailsWindow, text=Read_Line(), fg='white', font=("System", 12), bg="black",
                                     relief="sunken", width=4, height=2)
            lbl_NumberActual.place(x=350, y=80)

            Saved_Viewfld = scrolledtext.ScrolledText(SavedEmailsWindow, bd=1, fg='green', font=("Terminal", 11),
                                                      bg="black",
                                                      width=30,
                                                      height=13)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
            Saved_Viewfld.place(x=30, y=30)
            Saved_Viewfld.insert(1.0, Read_File("C:\\Offline Email\\AutoFill.txt"))
            Saved_Viewfld.config(state=DISABLED)
            Saved_Viewfld.config(insertbackground="white")

        else:
            lbl_Number = Label(SavedEmailsWindow, text="Error", fg='red', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=300, y=185)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())

    def Open_Saved_Email():
        OpenfldEmail.get()
        if (OpenfldEmail.get() == ""):
            lbl_Number = Label(SavedEmailsWindow, text="Error", fg='red', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=300, y=185)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())

        elif(File_Exists(OpenfldEmail.get()) == True):
            Gmailfld.insert(0, (Read_File("C:\\Offline Email\\" + OpenfldEmail.get() + ".txt")).strip("\n"))
            Passfld.insert(0, (Read_File("C:\\Offline Email\\" + OpenfldEmail.get() + " Pass.txt:Secret.txt")).strip("\n"))
            SavedEmailsWindow.destroy()
            root1.wm_attributes('-alpha', 0.9)

        else:
            lbl_Number = Label(SavedEmailsWindow, text="Error", fg='red', font=("Terminal", 6), bg="black")
            lbl_Number.place(x=300, y=185)
            lbl_Number.after(2500, lambda: lbl_Number.destroy())

    def Read_Line():
        with open("C:\Offline Email\AutoFill.txt", 'r') as fp:
            x = len(fp.readlines())
            return(x)

    def Close_SavedEmails_Window():
        SavedEmailsWindow.destroy()
        root1.wm_attributes('-alpha', 0.9)
    def Read_File(File_Path):
        file_content = open(File_Path, "r")
        if (exists(File_Path)):  # opens/reads a file with a given file path....
            return (file_content.read())
        else:
            raise Exception("Error, File not present or empty....")

    SavedEmailsWindow = Tk()

    SavedEmailsWindow_app_width = 450
    SavedEmailsWindow_app_height = 250

    SavedEmailsWindow_screen_width = SavedEmailsWindow.winfo_screenwidth()
    SavedEmailsWindow_screen_height = SavedEmailsWindow.winfo_screenheight()

    SavedEmailsWindow_x = int((SavedEmailsWindow_screen_width / 2) - (SavedEmailsWindow_app_width / 2))
    SavedEmailsWindow_y = int((SavedEmailsWindow_screen_height / 2) - (SavedEmailsWindow_app_height / 2))

    Saved_Viewfld = scrolledtext.ScrolledText(SavedEmailsWindow, bd=1, fg='grey', font=("Terminal", 11), bg="black",
                                              width=30,
                                              height=13)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
    Saved_Viewfld.place(x=30, y=30)
    Saved_Viewfld.insert(1.0, Read_File("C:\\Offline Email\\AutoFill.txt"))
    Saved_Viewfld.config(state=DISABLED)
    Saved_Viewfld.config(insertbackground="white")

    lbl_Number = Label(SavedEmailsWindow, text="Number of\nSaved Emails:", fg='white', font=("System", 12), bg="black",
                       relief="sunken")
    lbl_Number.place(x=320, y=30)

    lbl_NumberActual = Label(SavedEmailsWindow, text=Read_Line(), fg='white', font=("System", 12), bg="black", relief="sunken", width=4, height=2)
    lbl_NumberActual.place(x=350, y=80)

    OpenfldEmail = Entry(SavedEmailsWindow, text="This is Open Widget", bd=1, fg='grey', bg="black",
                         font=("Terminal", 10), width=22)  # Gmail feild
    OpenfldEmail.place(x=30, y=206)
    OpenfldEmail.config(insertbackground="white")

    btn_open = Button(SavedEmailsWindow, text="Open", font=("Terminal", 9), fg='white', bg="green", padx=10, command = Open_Saved_Email)
    btn_open.place(x=230, y=204)

    btn_open = Button(SavedEmailsWindow, text="Remove", font=("Terminal", 9), fg='white', bg="red", padx=1, command=Remove_Email)
    btn_open.place(x=340, y=204)

    SavedEmailsWindow.wm_attributes('-alpha', 0.9)  # Transparency
    SavedEmailsWindow.protocol("WM_DELETE_WINDOW",
                               Close_SavedEmails_Window)  # controling the function of the close window icon (top right of window)
    SavedEmailsWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
    SavedEmailsWindow.title('Saved Emails')  # Add Username to top of WebPage
    SavedEmailsWindow.geometry(f'{SavedEmailsWindow_app_width}x{SavedEmailsWindow_app_height}+{SavedEmailsWindow_x}+{SavedEmailsWindow_y}') #450x250
    SavedEmailsWindow.configure(bg='black')
    SavedEmailsWindow.mainloop()



root1 = Tk()

root1_app_width = 450
root1_app_height = 250


root1_screen_width = root1.winfo_screenwidth()
root1_screen_height = root1.winfo_screenheight()


root1_x = int((root1_screen_width / 2) - (root1_app_width / 2))
root1_y = int((root1_screen_height / 2) - (root1_app_height / 2))


lbl_Gmail=Label(root1, text="Gmail:", fg='white', font=("Terminal", 11), bg="black" )
lbl_Gmail.place(x=135, y=25)


Gmailfld=Entry(root1, text="This is UserName Widget", bd=1, fg='grey',  bg="black" , font=("Terminal", 11), width=21)   #Gmail feild
Gmailfld.place(x=135, y=45)
Gmailfld.config(show="x")
Gmailfld.config(insertbackground="white")


lbl_Access=Label(root1, text="Access Password:", fg='white', font=("Terminal", 11), bg="black")
lbl_Access.place(x=135, y=85)

Passfld=Entry(root1, text="This is Password Widget", bd=1, fg='grey', font=("Terminal", 11), bg="black", width=21)    #Passcode feild
Passfld.place(x=135, y=105)
Passfld.config(show="*")
Passfld.config(insertbackground="white")#Changes test cursor color

btn_Login = Button(root1, text="Login", padx = 55 , font=("Terminal", 11), fg='white', bg="black", command=Login_Btn)
btn_Login.place(x=140, y=165)

btn_Create=Button(root1, text="Saved Emails", fg='white', font=("Terminal", 11), bg="black", command=Saved_Emails)
btn_Create.place(x=165, y=205)

lbl_Accent1=Label(root1, text=".\n.\n.\n.", fg='white', font=("System", 18), bg="black")
lbl_Accent1.place(x=60, y=30)

lbl_Accent2=Label(root1, text=".\n.\n.\n.", fg='white', font=("System", 18), bg="black")
lbl_Accent2.place(x=370, y=30)

btn_Close = Button(root1, text="Close" , font=("Terminal", 11), fg='white', bg="red", command=close2)
btn_Close.place(x=370, y=210)

btn_Close = Button(root1, text="Save" , font=("Terminal", 11), fg='white', bg="green", command=Save_btn)
btn_Close.place(x=374, y=185)



root1.wm_attributes('-alpha', 0.9) #Transparency
root1.protocol("WM_DELETE_WINDOW", close2) #controling the function of the close window icon (top right of window)
root1.resizable(False,False) #Cannot change size of the Window(It is locked)
root1.title('Login') #Add Username to top of WebPage
root1.geometry(f'{root1_app_width}x{root1_app_height}+{root1_x}+{root1_y}')#450x200
root1.configure(bg='black')
root1.mainloop()



#Login GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
