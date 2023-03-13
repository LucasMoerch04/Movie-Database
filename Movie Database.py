import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as CTk
import imdb
import urllib.request 
import random



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


searchbar = CTk.CTkEntry(root, width=200, height=30,corner_radius=20,fg_color="white",text_color="black",font=("Times New Roman",14))
searchbar.grid(column=5,row=4,columnspan=1,sticky=E,padx=70)


def switch_event():
    if switch_var.get() == "on":
        CTk.set_appearance_mode("dark")
       
    else:
        CTk.set_appearance_mode("light")
        
    
#TITLE IMAGE

#source
data_from = CTk.CTkLabel(master=root, text = "Data from imdb.com", font=("helvetica neu", 10))
data_from.grid(row=6,column=5,sticky=N)

ia = imdb.Cinemagoer()


dict ={} 



def Show_by_search():
    search = searchbar.get()
    movies = ia.search_movie(search)
    movie_nr = 1
    
    random.shuffle(movies)
    
    count = 0

    for movie in movies[movie_nr:15]:
            if movie['kind'] == 'movie':
                try:
                    count += 1
                    id = movies[movie_nr].movieID
                    movie = ia.get_movie(id)
                    title = movie['title']
                    year = movie['year']
                    rating = movie['rating']
                    genres = movie['genres'][0:2]
                    genres = '/'.join(genres)    
                    for person in movie['directors']:
                        director = person['name']
                    url = movie['full-size cover url']
                    starring = str(movie['cast'][0])+ " & " + str(movie['cast'][1])
                    
                    records = [str(title),str(genres), str(year),str(director),str(starring), "IMDB Rating: " + str(rating)]
        
                    print_records = ""
                    for record in records:
                        print_records +=str(record) + "\n"
        
                    dict['movie{0}'.format(count)] = print_records
        
                    dict['url{0}'.format(count)] = url
                    movie_nr +=1
                    
                except KeyError: 
                    pass
                    
                   
            else:
                pass
        
        
        

    
    if 'movie1' in dict:
        label = CTk.CTkLabel(frame, text=dict["movie1"],font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=1,sticky=CTk.N,padx=20,pady=5)
    else: 
        label = CTk.CTkLabel(frame, text="empty",font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=1,sticky=CTk.N,padx=20,pady=5)
    if 'movie2' in dict:
        label = CTk.CTkLabel(frame, text=dict["movie2"],font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=2,sticky=CTk.N,padx=20,pady=5)
    else: 
        label = CTk.CTkLabel(frame, text="empty",font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=2,sticky=CTk.N,padx=20,pady=5)
    
    if 'movie3' in dict:
        label = CTk.CTkLabel(frame, text=dict["movie3"],font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=3,sticky=CTk.N,padx=20,pady=5)
    else: 
        label = CTk.CTkLabel(frame, text="empty",font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=3,sticky=CTk.N,padx=20,pady=5)
    
    if 'movie4' in dict:
        label = CTk.CTkLabel(frame, text=dict["movie4"],font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=4,sticky=CTk.N,padx=20,pady=5)
    else: 
        label = CTk.CTkLabel(frame, text="empty",font=timesfont,text_color=textcolor)
        label = label.grid(row=3,column=4,sticky=CTk.N,padx=20,pady=5)
    
    # IMAGE 1
    
    urllib.request.urlretrieve(dict["url1"],"cover1.jpeg")
    im = Image.open("cover1.jpeg")
    im.save("cover1.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
    
    image1 = CTk.CTkImage(Image.open("cover1.jpeg"),size=(235,349))  
    image1 = CTk.CTkLabel(master=frame,image=image1,text="")
    image1.grid(row=4, column=1, padx=20)

    
    #IMAGE 2
    urllib.request.urlretrieve(dict["url2"],"cover2.jpeg")
    im = Image.open("cover2.jpeg")
    im.save("cover2.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
    
    image2 = CTk.CTkImage(Image.open("cover2.jpeg"),size=(235,349))  
    image2 = CTk.CTkLabel(master=frame,image=image2,text="")
    image2.grid(row=4, column=2, padx=20)
    
    #IMAGE 3
    urllib.request.urlretrieve(dict["url3"],"cover3.jpeg")
    im = Image.open("cover3.jpeg")
    im.save("cover3.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
    
    image3 = CTk.CTkImage(Image.open("cover3.jpeg"),size=(235,349))  
    image3 = CTk.CTkLabel(master=frame,image=image3,text="")
    image3.grid(row=4, column=3, padx=20)


    #IMAGE 4
    urllib.request.urlretrieve(dict["url4"],"cover4.jpeg")
    im = Image.open("cover4.jpeg")
    im.save("cover4.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
    
    image4 = CTk.CTkImage(Image.open("cover4.jpeg"),size=(235,349))  
    image4 = CTk.CTkLabel(master=frame,image=image4,text="")
    image4.grid(row=4, column=4, padx=20)
    


#Show movies function   
def Show():
    search = searchbar.get()
    print(search)
    #chosen genre
    genre_chosen = dropdown.get()
    print(genre_chosen)
    error =" "
    #resets frame
    for item in frame.winfo_children():
        item.destroy()
    
    #If searchbar is not empty
    if search != "":
        Show_by_search()
    

    #if genre is not 12 (if genre been chosen)
    elif len(genre_chosen) != 12:
        error =" "
        #CHOOSES 4 RANDOM MOVIES DEPENDING ON GENRE CHOSEN
        c.execute("SELECT * FROM imdb_movies WHERE genre LIKE ? ORDER BY RANDOM() LIMIT 4", ('%'+genre_chosen+'%',))
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
            
        #IMAGE1    
        urllib.request.urlretrieve(cover,"cover1.jpeg")
        im = Image.open("cover1.jpeg")
        im.save("cover1.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
        image1 = CTk.CTkImage(Image.open("cover1.jpeg"),size=(235,349))
        image1 = CTk.CTkLabel(master=frame,image=image1,text="")
        image1.grid(row=4, column=1, padx=20)
        #IMAGE2
        urllib.request.urlretrieve(cover2,"cover2.jpeg")
        im = Image.open("cover2.jpeg")
        im.save("cover2.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
        image2 = CTk.CTkImage(Image.open("cover2.jpeg"),size=(235,349))
        image2 = CTk.CTkLabel(master=frame,image=image2,text="")
        image2.grid(row=4, column=2, padx=20)
        #IMAGE3
        urllib.request.urlretrieve(cover3,"cover3.jpeg")
        im = Image.open("cover3.jpeg")
        im.save("cover3.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
        image3 = CTk.CTkImage(Image.open("cover3.jpeg"),size=(235,349))
        image3 = CTk.CTkLabel(master=frame,image=image3,text="")
        image3.grid(row=4, column=3, padx=20)
            
        #IMAGE4
        urllib.request.urlretrieve(cover4,"cover4.jpeg")
        im = Image.open("cover4.jpeg")
        im.save("cover4.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
        image4 = CTk.CTkImage(Image.open("cover4.jpeg"),size=(235,349))
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
       
        errorlabel = CTk.CTkLabel(root, text=error,font=("Times New Roman bold",12) )
        errorlabel.grid(row=4,column=7,columnspan=1,padx=30)
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

#FIXED FRAME SIZE (true)
frame.grid_propagate(True)


root.mainloop()