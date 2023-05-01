#This is a movie recommender/database. It uses IMDB' database to find movies from searching wished titles. As of March 2022, 
#the database contained some 10.1 million titles (including television episodes) and 11.5 million person records.
#This means that searching the database to find movies takes a bit of time, and occasionally crashes the program.
#For this reason, we have created an SQLite database with movies from IMDB's database, which is used when the user 
#searches for movies based on genres, and not title. To make SQLite database easier to configure, a seperate program 
#has been made (admin.py). 
#To make the GUI, we used the modern and customizable Python UI-library based on Tkinter, CustomTkinter)



#Imports (custom)tkinter, sqlite, PIL, IMDB database, URLlib.req, and Random.
import sqlite3
from tkinter import *
from PIL import Image
import customtkinter as CTk
import imdb
import urllib.request 
import random


#Connects to limited movie databse
con = sqlite3.connect("movies.db")
#Database cursor - Class used to invoke and fetch data from database
c = con.cursor()

#GUI
#GUI theme
#CTk.set_appearance_mode("dark")
#CTk.set_default_color_theme("dark-blue")

#GUI Colors and font, to easily configure the design of the program
rootcolor = "black"
framecolor = "khaki"
frametextcolor = "white"
dropdowncolor = "RoyalBlue3"
dropdownbuttonhovercolor = "RoyalBlue4"
activedropdowncolor = "RoyalBlue4"
buttoncolor = "RoyalBlue3"
activebuttoncolor = "RoyalBlue4"
timesfont =("Calibri Light",18)
textcolor = "white"

#Creates GUI window
root = CTk.CTk()
#Width and height of screen used to size window
width = root.winfo_screenwidth()               
height = root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))
#Title of window
root.title("Movie Database")
#Window is resizable
root.resizable(1,1)
root.configure(background=rootcolor)
#Creates window grid
root.columnconfigure(5, weight=1)
root.rowconfigure(5, weight=1)
#Creates and positions frame
frame = CTk.CTkScrollableFrame(root, border_width=2, width=1200, height=480,fg_color="transparent",orientation=HORIZONTAL,scrollbar_button_color="white",)
frame.grid(column=4, row=2, columnspan=3, rowspan=4,padx=10)

#Creates, sizes and positions titlelogo image depending on light- or darkmode
titlelogolabelimage = CTk.CTkImage(light_image = Image.open("movielogo2black.png"), dark_image = Image.open("movielogo2.png"),size=(600,150))
titlelogolabel = CTk.CTkLabel(master=root,image=titlelogolabelimage,text="")
titlelogolabel.grid(row=1, column=4,columnspan=2,pady=10)

#Creates and positions searchbar
searchbar = CTk.CTkEntry(root, width=200, height=26,corner_radius=6,fg_color="white",text_color="black",font=("Times New Roman",14),placeholder_text="Movie Title")
searchbar.grid(column=5,row=3,columnspan=1,sticky=NE,padx=75)

#Fetches data from imdb's web server
ia = imdb.Cinemagoer()

#Declares global empty dictionary
dict ={} 

#Light- and darkmode function
def switch_event():
    if switch_var.get() == "on":
        CTk.set_appearance_mode("dark")
    else:
        CTk.set_appearance_mode("light")
        

#Creates and positions label text with source reference
data_from = CTk.CTkLabel(master=root, text = "Data from imdb.com", font=("helvetica neu", 10))
data_from.grid(row=6,column=5,sticky=N)



#Function to clear all labels in frame
def clear_all():
    for label in frame.children.values():label.destroy
    


    

#Funtion to request, open and save cover image from url and places it to match movie information
def movie_image(nr):
    urllib.request.urlretrieve(dict['url{0}'.format(nr)],f"cover{nr}.jpeg")
    im = Image.open(f"cover{nr}.jpeg")
    im.save(f"cover{nr}.jpeg",format='jpeg',quality = 95, subsampling= 0,optimize=True)
    
    image = CTk.CTkImage(Image.open(f"cover{nr}.jpeg"),size=(235,349))  
    image = CTk.CTkLabel(master=frame,image=image,text="")
    image.grid(row=4, column=int(nr), padx=20,pady=0)
    
#Function to create and position label with movie information
def movie_information(nr):
    label = CTk.CTkLabel(frame, text=dict['movie{0}'.format(nr)],font=timesfont,text_color=textcolor)
    label = label.grid(row=3,column=int(nr),sticky=CTk.N,padx=20,pady=0)

#Function to to create and position labels on found movies
def create_labels():
    x = 1
    while x <= 4:
        try:
            #Runs movie_information() and movie_image() function to display the movie images and information that was found 
            movie_information(x)
            movie_image(x)
            x+=1
        except:
            print('movie{0} error'.format(x))
            x+=1

#Function to set-up data and adds information and url to seperate keys
def print_records(records, url, x = 1):
    print_records = ""
    for record in records:
        print_records +=str(record) + "\n"
    
    
    dict['movie{0}'.format(x)] = print_records
    dict['url{0}'.format(x)] = url
    print(print_records) 

def show_by_genre(genre_chosen):
    #Fetches data on 4 random movies with matching genre in limited database    
    c.execute("SELECT * FROM imdb_movies WHERE genre LIKE ? ORDER BY RANDOM() LIMIT 4", ('%'+genre_chosen+'%',))
    #seperates movie_id and cover url for each movie
    x = 1
    while x <= 4:
        
        records = c.fetchone()
        
        records = list(records)
        records.pop(0)
        url = records.pop(5)
        
        print_records(records, url, x)
        x+=1
        
    #Runs create_labels() to create and position the movies
    create_labels()

#Function to show movies by search
def show_by_search():
    #Gets and searches imdb's database from searchbar
    search = searchbar.get()
    movies = ia.search_movie(search)
    
    #Movies found counter
    x = 0
    #Randomly shuffles movies found from search
    random.shuffle(movies)
    
    #For-loop to find movies
    for i in movies:
        #Breaks loop when 4 movies has been found
        if x >= 4:
            break
        #Elif-statement to only find movies (some items are labeled incorrectly)
        elif i['kind'] == 'movie':
            #If no error, adds movie data to dict.
            try:
                id = i.movieID
                movie = ia.get_movie(id)
                title = movie['title']
                year = movie['year']
                rating = movie['rating']
                genres = movie['genres'][0:2]
                genres = '/'.join(genres)    
                for person in movie['directors']:
                    director = person['name']
                url = movie['full-size cover url']
                #If movie cast is only 1 person
                try:
                    starring = str(movie['cast'][0])+ " & " + str(movie['cast'][1])
                except IndexError:
                    starring = str(movie['cast'][0])
                
                #adds all information to records
                records = [str(title),str(genres), str(year),str(director),str(starring), "IMDB Rating: " + str(rating)]
                
                #adds 1 to movies found counter
                x+=1
                
                #Runs print_records with found movies
                print_records(records, url, x)
                
            #When movie misses any kind of data, it will raise a KeyError    
            except KeyError: 
                print("Movie is missing data")
                
        #Tells if item is not a movie        
        else:
            print("Item is not a movie")
            
    #Sometimes, a specific search will only find few amounts of matching movies. 
    #Therefore, the program will show up to 4 movies.
    
    #Runs create_labels() to create and position the movies
    create_labels()
    

#Show movies function 
def show():
    #Clears all labels in frame
    clear_all()
    #Gets input in searchbar
    search = searchbar.get()
    print(search)
    #Gets genre chosen in dropdown
    genre_chosen = dropdown.get()
    print(genre_chosen)
    error =" "
    #Resets frame every time button is clicked
    for item in frame.winfo_children():
        item.destroy()
    
    #If searchbar is not empty, runs show_by_search function
    if search != "":
        show_by_search()
    
    #if length of genre is not 12 (if genre been chosen)
    elif len(genre_chosen) != 12:
        
        #Runs show_by_genre() function to show movies from limited database
        show_by_genre(genre_chosen)
        
        
    else:
        #ERRORLABEL THAT DISAPPEARS AFTER 1500ms 
        error = "*Please choose a genre"
        errorlabel = CTk.CTkLabel(root, text=error,font=("Times New Roman bold",12) )
        errorlabel.grid(row=4,column=7,columnspan=1,padx=30)
        errorlabel.after(1500,errorlabel.destroy)
           
    
        
#SORTED GENRELIST    
""""   
genrelist = ["Horror","Action","Comedy","Romance","Drama","Sci-fi","Thriller","Mystery","Crime","Adventure","Fantasy","Animation"]
genrelist.sort()
print(genrelist)
"""

#Buttons
#Dropdown menu to choose genre
dropdown = CTk.CTkOptionMenu(root,values=[ 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family','Fantasy', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-fi', 'Thriller'],
                             fg_color=dropdowncolor,button_color=dropdowncolor,button_hover_color=dropdownbuttonhovercolor)
#Sets default value
dropdown.set("Choose Genre")
dropdown.configure(height=25)

#dropdown["menu"].config(bg=dropdowncolor)
dropdown.grid(row=2,column=7,padx=50,sticky=S)

#"Show Movies" button that runs show() function
#"Eye" Image on button
showimage = CTk.CTkImage(dark_image=Image.open("showicon3.png"),size=(20,20))
button = CTk.CTkButton(root, command=show, image=showimage,fg_color=buttoncolor,hover_color=activebuttoncolor ,text="Show Movies",width=140).grid(row=1,column=7,pady=20,padx=50,sticky=S)  

#Light/Dark mode switch
switch_var = CTk.StringVar(value="on")
switch = CTk.CTkSwitch(master=root,text="Light/Dark", command=switch_event,variable=switch_var, onvalue="on", offvalue="off",button_color=buttoncolor,fg_color=buttoncolor)
switch.grid(row=1,column=7)

#Method that runs program in infinite loop
root.mainloop()
