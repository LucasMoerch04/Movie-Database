import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as CTk
import imdb
from imdb import Cinemagoer
ia = imdb.Cinemagoer()
import random

#connect to database
con = sqlite3.connect("movies.db")
#Cursor
c = con.cursor()

#ADMIN GUI
admin = CTk.CTk()
admin.geometry("1000x300")
admin.title("Administer Movies")
admin.resizable(0,0)
#admin.configure(background="grey85")
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("dark-blue")
#pre-written movie_id
c.execute("SELECT movie_id FROM movies")
#automatic movie_id
movie_id_count = c.fetchall()
movie_id_count = len(movie_id_count)
movie_id_count += 1


searchbar = CTk.CTkEntry(admin, width=200, height=30,corner_radius=20,fg_color="white",text_color="black",font=("Times New Roman",14))
searchbar.grid(column=8,row=4,columnspan=1,sticky=E,padx=70)




def imdb_add():
    search = searchbar.get()
    movies = ia.search_movie(search)
    
    #random.shuffle(movies)
    movie_nr = 0
    
    for movie in movies[movie_nr:7]:
        if movie['kind'] == 'movie':
            try:
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
            
                
                records = (str(id),str(title),str(genres), str(year), str(director),str(starring),str(url), "IMDB Rating: " + str(rating))
                print(records)
                
                
                c.execute("INSERT OR REPLACE INTO imdb_movies VALUES (?,?,?,?,?,?,?,?)",(records))
        
                print("**SUBMISSION SUCCESSFULL**")
                movie_nr += 1
            except KeyError: 
                    print("Movie is missing data")
                    
                    pass
            else:
                pass

    
    con.commit()
#SUBMIT MOVIE
def submitvals():
    
    submitted_movie_id = movie_id_entry.get()
    submitted_movie_name = movie_name_entry.get()
    submitted_genre = genre_entry.get()
    submitted_director = director_entry.get()
    submitted_release_year = release_year_entry.get()
    submitted_starring = starring_entry.get()
    submitted_cover = cover_entry.get()

     
    c.execute("INSERT OR REPLACE INTO movies VALUES (?,?,?,?,?,?,?)", (submitted_movie_id,submitted_movie_name,submitted_genre,submitted_director,submitted_release_year,submitted_starring,submitted_cover))
        
    print("**SUBMISSION SUCCESSFULL**")

    success = CTk.CTkLabel(admin, text="**MOVIE SUCCESSFULLY SUBMITTED**",font=("Helvetica neu", 8))
    success.grid(row=8,column=1,columnspan=3,sticky=W)
    success.after(1500,success.destroy)
   
    
    
    con.commit()

#Remove movie based on movie_id
def removevals():
    
    remove_movie_id = remove_entry.get()
    
    c.execute("DELETE FROM movies WHERE movie_id = ?",(remove_movie_id,))
    
    print("**MOVIE SUCCESSFULLY REMOVED**")
    removed = CTk.CTkLabel(admin, text="**MOVIE SUCCESSFULLY REMOVED**",font=("Helvetica neu", 8))
    removed.grid(row=8,column=5,columnspan=2)
    removed.after(1500,removed.destroy)
    
    con.commit()

#clears entries after submitting
def cleartext():
    
    movie_id_entry.delete(0, END)
    movie_name_entry.delete(0, END)
    genre_entry.delete(0, END)
    director_entry.delete(0, END)
    release_year_entry.delete(0, END)
    starring_entry.delete(0, END)
    cover_entry.delete(0, END)
    
def cleartext2():
    movie_id_entry.delete(0, END)
    remove_entry.delete(0, END)

#updates movie_id_count 
def movie_id_count_func():
    c.execute("SELECT movie_id FROM movies")

    movie_id_count = c.fetchall()
    movie_id_count = len(movie_id_count)
    movie_id_count += 1
    movie_id_entry.insert(0,movie_id_count)

#Textlabels
movie_id = CTk.CTkLabel(admin, text="movie_id",font=("Helvetica neu", 12))
movie_name = CTk.CTkLabel(admin, text="movie_name",font=("Helvetica neu", 12))
genre = CTk.CTkLabel(admin, text="genre",font=("Helvetica neu", 12))
director = CTk.CTkLabel(admin, text="director",font=("Helvetica neu", 12))
release_year = CTk.CTkLabel(admin, text="release_year",font=("Helvetica neu", 12))
starring = CTk.CTkLabel(admin, text="starring",font=("Helvetica neu", 12))
cover = CTk.CTkLabel(admin, text="cover",font=("Helvetica neu", 12))
remove = CTk.CTkLabel(admin,text="remove movie_id",font=("Helvetica neu", 12))

#Textlabels positioning
movie_id.grid(row=1,padx=3,pady=3)
movie_name.grid(row=2,padx=3,pady=3)
genre.grid(row=3,padx=3,pady=3)
director.grid(row=4,padx=3,pady=3)
release_year.grid(row=5,padx=3,pady=3)
starring.grid(row=6,padx=3,pady=3)
cover.grid(row=7,padx=3,pady=3)
remove.grid(row=6, column=5,padx=5,stick=SE)

#INSTRUCTIONS FOR ADMINS
instructionstext = """INSTRUCTIONS:
*movie_id is automatically updated*
Remember correct Uppercase/Lowerscase
Seperate genres and names with commas
Do NOT put too many characters in one section 
(Preferably max 2 people in 'starring') 
'remove movie_id' removes all of a movies data based on the movie_id
Cover-filename has to end in .png
Download and place cover into folder 'Moviecovers'"""

instructions = CTk.CTkLabel(admin,text=instructionstext,font=("Helvetica neu", 10))
instructions.grid(row=2,column=4,rowspan=4,columnspan=4,sticky=W)


#input values
movie_id_input = StringVar()
movie_name_input = StringVar()
genre_input = StringVar()
director_input = StringVar()
release_year_input = StringVar()
starring_input = StringVar()
cover_input = StringVar()
remove_input = StringVar()

#entry text
movie_id_entry = CTk.CTkEntry(admin, textvariable = movie_id_input)
movie_name_entry = CTk.CTkEntry(admin, textvariable = movie_name_input,)
genre_entry = CTk.CTkEntry(admin, textvariable = genre_input)
director_entry = CTk.CTkEntry(admin, textvariable = director_input)
release_year_entry = CTk.CTkEntry(admin, textvariable = release_year_input)
starring_entry = CTk.CTkEntry(admin, textvariable = starring_input)
cover_entry = CTk.CTkEntry(admin, textvariable = cover_input)
remove_entry = CTk.CTkEntry(admin, textvariable = remove_input,width=50)

#Entry positioning
movie_id_entry.grid(row=1, column=1)
movie_name_entry.grid(row=2, column=1)
genre_entry.grid(row=3, column=1)
director_entry.grid(row=4, column=1)
release_year_entry.grid(row=5, column=1)
starring_entry.grid(row=6, column=1)
cover_entry.grid(row=7, column=1)
remove_entry.grid(row=7,column=5, padx=50)

#clears pre-written text and makes text black
def temp_text1(e):
    entry1.delete(0,"end")
    movie_name_entry.config(fg_color="black")
def temp_text2(e):
    entry2.delete(0,"end")
    genre_entry.config(fg_color="black")
def temp_text3(e):
    entry3.delete(0,"end")
    director_entry.config(fg_color="black")
def temp_text4(e):
    entry4.delete(0,"end")
    release_year_entry.config(fg_color="black")
def temp_text5(e):
    entry5.delete(0,"end")
    starring_entry.config(fg_color="black")
def temp_text6(e):
    entry6.delete(0,"end")
    cover_entry.config(fg_color="black")

    
#pre-written movie_id
#fixes 0 added back of number
movie_id_entry.delete(0, END) 
movie_id_entry.insert(0,movie_id_count)


#pre-written movie_name
entry1=movie_name_entry
movie_name_entry.insert(0,"e.g. The Batman")
movie_name_entry.configure(text_color="grey")
movie_name_entry.bind("<FocusIn>", temp_text1)

#pre-written genre
entry2=genre_entry
genre_entry.insert(0,"e.g. Action")
genre_entry.configure(text_color="grey")
genre_entry.bind("<FocusIn>", temp_text2)

#pre-written director
entry3=director_entry
director_entry.insert(0,"e.g. Matt Reeves")
director_entry.configure(text_color="grey")
director_entry.bind("<FocusIn>", temp_text3)

#pre-written release_year
#fixes 0 added back of number
release_year_entry.delete(0, END) 
entry4=release_year_entry
release_year_entry.insert(0,str("e.g. 2022"))
release_year_entry.configure(text_color="grey")
release_year_entry.bind("<FocusIn>", temp_text4)

#pre-written starring
entry5=starring_entry
starring_entry.insert(0,"e.g. Robert Pattinson")
starring_entry.configure(text_color="grey")
starring_entry.bind("<FocusIn>", temp_text5)

#pre-written cover
entry6=cover_entry
cover_entry.insert(0,"e.g. file_name.png")
cover_entry.configure(text_color="grey")
cover_entry.bind("<FocusIn>", temp_text6)






imdb_button = CTk.CTkButton(admin,text="Submit", command = imdb_add)
imdb_button.grid(column=8, row = 5)

#Submitbutton
CTk.CTkButton(admin, width=20, text="Submit", command=lambda:[submitvals(),cleartext(),movie_id_count_func()]).grid(row=7, column=3,padx=6)
#Removebutton
CTk.CTkButton(admin,width=10, text="Remove", command=lambda:[removevals(),cleartext2(),movie_id_count_func()]).grid(row=7, column=5,padx=6,sticky=E)
admin.mainloop()