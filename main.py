from tkinter import *
import os
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from matcher import matcher
from tkinter import ttk
from converter import converter

def fing():
    global search
    search_text = str(search_word.get())
    if not os.path.isdir(str(folder_name.get())):
        var=messagebox.showerror(message="Invalid directory.")
        folder_name.delete(0,END)
    elif search_text.isspace() or len(search_text) == 0:
        var=messagebox.showwarning(message="Please enter a search word")
    else:
        keywords = search_text.split(' ')
        path = folder_name.get()
        iid = 0
        for filename in os.listdir(path):
            pathToFile = os.path.join(path, filename)
            # get text content for each file in directory
            content = converter(pathToFile)
            # get matching keywords from content
            keywordsFound = matcher(content, keywords)
            if (len(keywordsFound) > 0):
                results.insert('', END, text=filename, iid=iid, open=False)
                curr_file_iid = iid
                iid+=1
                for i in range(len(keywordsFound)):
                    results.insert('', END, text=keywordsFound[i],iid=iid,open=False,)
                    results.move(iid, curr_file_iid, i)
                    iid+=1

def save_list():
    with open("saved_result.txt","w") as sfile:
        sfile.write('\n'.join(d.get(0,END)))
    var=messagebox.showwarning(message="File names are saved as {}".format("saved_result.txt"))
    
def chose_folder():
    global path
    foldername = askdirectory() 
    path=foldername
    folder_name.delete(0,END)
    folder_name.update()
    folder_name.insert(END, path)    
    
if __name__=="__main__":
    parent=Tk()
    parent.title('File Finder')
    print("Hello")
    Label(parent,text="Folder name: ").grid(row=0,column=0,sticky='e')

    folder_name=Entry(parent,width=20)
    folder_name.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)

    Label(parent,text="Search word: ").grid(row=1,column=0,sticky='e')
    search_word=Entry(parent,width=20)
    search_word.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=9)

    # Label(parent,text="Search Results: ").grid(row=3,column=0,sticky='e')

    # d=Listbox(parent,width=125,height=20)
    # d.grid(row=4,column=3,padx=2,pady=2,sticky='we',columnspan=9)

    results = ttk.Treeview(parent)    
    results.heading('#0', text="Search results", anchor="w")
    results.grid(row=4,column=1, sticky='nsew')

    Button(parent,text="Folder",command=lambda:chose_folder()).grid(row=0,column=10,sticky='e'+'w',padx=2,pady=2,)
    start=Button(parent,text="Start",command=lambda:fing()).grid(row=1,column=10,sticky='e'+'w',padx=2,pady=2,)
    #save=Button(parent,text="Save",command=lambda:save_list())
    #save.grid(row=2,column=10,sticky='e'+'w',padx=2,pady=2)

    Button(parent,text="Exit",command=parent.destroy).grid(row=3,column=10,sticky='e'+'w',padx=2,pady=2)

    parent.mainloop()

    
