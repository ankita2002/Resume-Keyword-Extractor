from tkinter import *
from tkinter import ttk, filedialog
import os
from tkinter import messagebox
import textract
import re
import PyPDF2
from pdf_to_txt import convert_pdf_to_txt

def show():
    for i in range(enterNoField):
        enterKeyField.append(input().lower())

    dirname = os.path.dirname(__file__)
    directory = os.path.join(dirname, 'Resumes')
    directory = str(input('Directory'))
    for filename in os.listdir(directory):
        pathToFile = os.path.join(directory, filename)
        text = ""
        if filename.endswith(".doc") or filename.endswith(".docx"):
            text = str(textract.process(pathToFile)).lower()
        elif filename.endswith(".pdf"):
            text = str(convert_pdf_to_txt(pathToFile)).lower()
        else:
            continue
     
    keywordsFound = []
    for keyword in enterKeyField:
        if (re.search(re.escape(keyword), text)):
            keywordsFound.append(keyword)
        if (len(keywordsFound) > 0):
            print("Found keywords in " + filename + " :")



if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="hot pink1") #background color
    gui.title("Resume Analyzer") #title of GUI window
    gui.geometry("250x300") #window size
    enterNo = Label(gui, text="Enter no of keywords", bg="hot pink1") #label
    enterNoField = Entry(gui,bg="lemon chiffon",) #text
    enterkey = Label(gui, text="Enter no of keywords", bg="hot pink1") #label
    enterKeyField = Entry(gui,bg="lemon chiffon",) #text
    submit = Button(gui,text="Submit",fg="Black",bg="cyan", command= show)
    textArea = Text(gui,height=5,width=25, font="lucida 13",bg="lemon chiffon")
    #grid
    enterNo.grid(row=0, column =3)
    enterNoField.grid(row=1, column =3,ipadx=50)
    enterkey.grid(row=2, column =3)
    enterKeyField.grid(row=3, column =3,ipadx=50)
    submit.grid(row=4, column =3) 
    textArea.grid(row=5, column =3,padx=10 , sticky= W)    
    gui.mainloop() #start gui