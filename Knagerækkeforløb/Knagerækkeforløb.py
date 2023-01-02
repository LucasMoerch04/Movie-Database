import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as CTk


#connect to database
con = sqlite3.connect("movies.db")
#Cursor
c = con.cursor()

#GUI Colors

rootcolor = "tan4"
framecolor = "khaki"
frametextcolor = "white"
dropdowncolor = "lightgoldenrod2"
activedropdowncolor = "lightgoldenrod3"
buttoncolor = "chartreuse2"
activebuttoncolor = "dark green"
timesfont =("Times New Roman",18)
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("dark-blue")
textcolor = "black"


#GUI
root = CTk.CTk()
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))
root.title("Movie Database")
root.resizable(1,1)
#root.configure(background=rootcolor)
root.columnconfigure(5, weight=1)
root.rowconfigure(5, weight=1)
#Frame
content = CTk.CTkFrame(root, fg_color=framecolor,width=800)
frame = CTk.CTkFrame(content, border_width=2, width=1100, height=450,fg_color=framecolor)
content.grid(column=4, row=2,columnspan=2, rowspan=4,)
frame.grid(column=4, row=2, columnspan=2, rowspan=4,padx=10)


titlelogolabelimage = CTk.CTkImage(light_image = Image.open("movielogo2black.png"), dark_image = Image.open("movielogo2.png"),size=(600,150))
titlelogolabel = CTk.CTkLabel(master=root,image=titlelogolabelimage,text="")
titlelogolabel.grid(row=1, column=4,columnspan=2,pady=10)



def switch_event():
    if switch_var.get() == "on":
        CTk.set_appearance_mode("dark")
       
    else:
        CTk.set_appearance_mode("light")
        
    
#TITLE IMAGE


#source
data_from = CTk.CTkLabel(master=root, text = "Data from imdb.com", font=("helvetica neu", 8))
data_from.grid(row=6,column=5,sticky=N)

#Show movies function
def Show():
    
    error =" "
    #resets frame
    for item in frame.winfo_children():
        item.destroy()
    
    #chosen genre
    genre_chosen = dropdown.get()

    #if genre is not 12 (if genre been chosen)
    if len(genre_chosen)!= 12:
        error =" "
        #CHOOSES 4 RANDOM MOVIES DEPENDING ON GENRE CHOSEN
        c.execute("SELECT * FROM movies WHERE genre LIKE ? ORDER BY RANDOM() LIMIT 4", ('%'+genre_chosen+'%',))
        records = c.fetchone()
        records2 = c.fetchone()
        records3 = c.fetchone()
        records4 = c.fetchone()
            
            
        #seperates movie_id and cover name
        records = list(records)
        records.pop(0)
        cover = records.pop(5)
        records2 = list(records2)
        records2.pop(0)
        cover2 = records2.pop(5)
        records3 = list(records3)
        records3.pop(0)
        cover3 = records3.pop(5)
        records4 = list(records4)
        records4.pop(0)
        cover4 = records4.pop(5)
            
            
        #path variable
        path=r'Moviecovers\\'
        #IMAGE1
        image1 = CTk.CTkImage(Image.open(str(path+cover)),size=(235,349))  
        image1 = CTk.CTkLabel(master=frame,image=image1,text="")
        image1.grid(row=4, column=1, padx=20)
        #IMAGE2
        image2 = CTk.CTkImage(Image.open(str(path+cover2)),size=(235,349))  
        image2 = CTk.CTkLabel(master=frame,image=image2,text="")
        image2.grid(row=4, column=2, padx=20)
        #IMAGE3
        image3 = CTk.CTkImage(Image.open(str(path+cover3)),size=(235,349))  
        image3 = CTk.CTkLabel(master=frame,image=image3,text="")
        image3.grid(row=4, column=3, padx=20)
            
        #IMAGE4
        image4 = CTk.CTkImage(Image.open(str(path+cover4)),size=(235,349))  
        image4 = CTk.CTkLabel(master=frame,image=image4,text="")
        image4.grid(row=4, column=4, padx=20)
                
                
        print_records = ""
        for record in records:
            print_records +=str(record) + "\n"
        
            
        label = CTk.CTkLabel(frame, text=print_records,font=timesfont,text_color=textcolor)
        label.grid(row=3,column=1,sticky=CTk.N,padx=20,pady=5)
            
        
        print_records2 = ""
        for record in records2:
            print_records2 +=str(record) + "\n"    
            
            
            
        label = CTk.CTkLabel(frame, text=print_records2,font=timesfont,text_color=textcolor)
        label.grid(row=3, column=2,sticky=CTk.N,padx=20,pady=5)
            
            
        print_records3 = ""
        for record in records3:
            print_records3 +=str(record) + "\n"    
            
            
            
        label = CTk.CTkLabel(frame, text=print_records3,font=timesfont,text_color=textcolor)
        label.grid(row=3, column=3,sticky=CTk.N,padx=20,pady=5)
        
        print_records4 = ""
        for record in records4:
            print_records4 +=str(record) + "\n"    
            
            
            
        label = CTk.CTkLabel(frame, text=print_records4,font=timesfont,text_color=textcolor)
        label.grid(row=3, column=4,sticky=CTk.N,padx=20,pady=5)
        
    
    
        
    else:
        #ERRORLABEL THAT DISAPPEARS AFTER 1500ms 
        
        error = "*Please choose a genre"
       
        errorlabel = CTk.CTkLabel(root, text=error,fg=frametextcolor,bg=rootcolor,font=("Times New Roman bold",12) )
        errorlabel.grid(row=3,column=7,sticky=CTk.E,padx=30)
        errorlabel.after(1500,errorlabel.destroy)
        
        
        con.commit()    
    
        
#SORTED GENRELIST    
""""   
genrelist = ["Horror","Action","Comedy","Romance","Drama","Sci-fi","Thriller","Mystery","Crime","Adventure","Fantasy","Animation"]
genrelist.sort()
print(genrelist)
"""
#KNAPPER

options = StringVar()

dropdown = CTk.CTkOptionMenu(root,values=[ 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family','Fantasy', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-fi', 'Thriller'])
dropdown.set("Choose Genre")
dropdown.configure(height=25)

#dropdown["menu"].config(bg=dropdowncolor)
dropdown.grid(row=2,column=7,padx=50,sticky=S)


showimage = CTk.CTkImage(dark_image=Image.open("showicon3.png"),size=(20,20))

button = CTk.CTkButton(root, command=Show, image=showimage,text="Show Movies",width=140).grid(row=1,column=7,pady=20,padx=50,sticky=S)  


switch_var = CTk.StringVar(value="on")



switch = CTk.CTkSwitch(master=root,text="Light/Dark", command=switch_event,variable=switch_var, onvalue="on", offvalue="off")
switch.grid(row=1,column=7)

#FIXED FRAME SIZE
frame.grid_propagate(True)



root.mainloop()