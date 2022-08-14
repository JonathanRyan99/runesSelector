import os
from tkinter import *
from pathlib import Path
from crawler import get_mobafire_build
from Inteface_controller import RuneBuilder
import webbrowser
import sys


class GUI:

    def __init__(self, master):
        self.master = master
        master.title("Rune Selector")
        
        #initialize save folder
        #sys.executable is true path when program is an executable
        if getattr(sys,'frozen',False):
            print("freeze = false")
            basedir = os.path.dirname(sys.executable) # this points to the directory that the executable was launched from
            baseDirPath = Path(basedir)
            self.save_folder_path =  baseDirPath/"saves"

        else:
            print("freeze = true")
            self.save_folder_path = Path('./saves')

        self.save_files_list = self.update_save_folder()
       
        #top frame
        self.topFrame  = Frame(master, height=300,width=150,padx=5,pady=5)
        self.topFrame.grid(row=0,column=0,)
       
        #search term vars
        self.search_var = StringVar()
        self.selected_build = StringVar()
        #watchs for change in search term and recalls listbox generation
        self.search_var.trace("w", lambda name, index, mode: self.update_list())
        
        #save list widgets
        self.entry = Entry(self.topFrame, textvariable=self.search_var, width=13)
        self.lbox = Listbox(self.topFrame, width=35, height=15)
        
        #load link widget
        self.load_link = Button(self.topFrame,text="Open Link",command=self.open_link)
        
        #descriptor widget
        self.selector_descriptor = Label(self.topFrame,text="double click or press enter on the above to build page")
        
        #binds listbox selection to mouse click // enter
        self.lbox.bind('<<ListboxSelect>>',self.update_selection)
        self.lbox.bind('<Double-1>',self.selector_build_page) 
        self.lbox.bind('<Return>',self.selector_build_page)

        #position topframe objects
        self.entry.grid(row=0, column=0, padx=5, pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3)
        self.selector_descriptor.grid(row=2,column=0, padx=10, pady=3)
        self.load_link.grid(row=3,column=0)
        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

        #bottom frame
        self.bottomFrame = Frame(master, height=300,width=150)
        self.bottomFrame.grid(row=1,column=0)
        

        #descriptor widget
        self.save_descriptor = Label(self.bottomFrame, text="new saved builds will appear on restart")

        #quick search widgets
        self.quick_build_var = StringVar()
        self.quick_build_var.set("")
        self.quick_build_entry = Entry(self.bottomFrame, textvariable= self.quick_build_var, width=30)
        self.quick_build_button = Button(self.bottomFrame, text="MOBAFIRE Quick Build", command=self.quick_build_page)

        #quick save widgets
        self.quick_save_var = StringVar()
        self.quick_save_var.set("")
        self.quick_save_entry = Entry(self.bottomFrame, textvariable=self.quick_save_var, width=13)
        self.quick_save_button = Button(self.bottomFrame,text="Save",command=self.save_build)

        #position bottom frame widgets
        self.quick_build_entry.grid(row=1,column=0 ,padx=10, pady=3)
        self.quick_build_button.grid(row=2,column=0, padx=10, pady=3)


        self.quick_save_entry.grid(row=3,column=0 ,padx=10, pady=3)
        self.quick_save_button.grid(row=4,column=0 ,padx=10, pady=3)
        self.save_descriptor.grid(row=5,column=0,padx=10, pady=3, )

    def update_save_folder(self):
    #initialise save folder    
        if(self.save_folder_path.exists() == False):
            Path(self.save_folder_path).mkdir()
        
        temp = list(self.save_folder_path.glob('*.txt'))
        file_names = []
        for item in temp:
            file_names.append(item.stem)

        return file_names
     
    #this refreshes the search bar
    def update_list(self):
        
        search_term = self.search_var.get()
        lbox_list = self.save_files_list 
        
        #clear all items in listbox
        self.lbox.delete(0, END)
        #if search term is in listItem add it to listbox
        for item in lbox_list:
            if search_term.lower() in item.lower():
                self.lbox.insert(END, item)

    #build button
    def quick_build_page(self):
        url = self.quick_build_var.get()
        if url != "" and  ("mobafire" in url):
            print("quick build: "+ url)
            build = get_mobafire_build(url)
            RuneBuilder(build)

    #updates selector, tracks cursor in lbox
    def update_selection(self,event):
        selection = event.widget.curselection()
        index = selection[0]
        self.selected_build = event.widget.get(index)
        print("selection updated: " + self.selected_build)
    
    #takes the double/enter clicked option and builds page
    def selector_build_page(self,event):
        selection = event.widget.curselection()
        index = selection[0]
        self.selected_build = event.widget.get(index)
        print("selector build: " + self.selected_build)
        
        #open and read file
        file_path = self.save_folder_path / (self.selected_build + ".txt")
        if (file_path).exists():
            build_params = []
            file = open( file_path ,"r")
            for line in file:
                #build_params.append(line[:-1]) #removes \n at end (dont strip cuz urls are used)
                build_params.append(line.strip()) #urls dont use \ should just target whitespace
            RuneBuilder(build_params)

    #save build from quick build link
    def save_build(self):
        file_name = self.quick_save_var.get()
        file_name = file_name.replace(" ","_")
        file_path = self.save_folder_path / (file_name + ".txt")
        url = self.quick_build_var.get()
        if (file_name != "") and (url != "") and ("mobafire" in url):
            print("saving: "+ file_name)
            temp = get_mobafire_build(url)
            file =open( file_path , "w" )
            for item in temp: 
                file.write(item + "\n")
            file.close()
            

    def open_link(self):
        if self.selected_build !="":
            file_path = self.save_folder_path / (self.selected_build + ".txt")
            if (file_path).exists():
                build_params = []
                file = open( file_path ,"r")
                for line in file:
                    #build_params.append(line[:-1]) #removes \n at end (dont strip cuz urls are used)
                    build_params.append(line.strip()) #urls dont use \ should just target whitespace
                if (len(build_params) != 0) and ("mobafire" in build_params[len(build_params)-1]):
                    url = build_params[len(build_params)-1]
                    print("opening link: " + url)
                    webbrowser.open(url)
                    #open webpage




root = Tk()
my_gui = GUI(root)
root.mainloop()