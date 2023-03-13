import sqlite3

#Databasen
con = sqlite3.connect("movies.db")

#Cursor
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS imdb_movies (
        movie_id integer PRIMARY KEY,
        movie_name text,
        genre text,
        release_year integer,
        director text,
        starring text,
        cover text,
        rating float
        )""")

"""
#Insert

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
         {
             #The Batman
             "movie_id": 1,
             "movie_name": "The Batman",
             "genre":"Action",
             "director":"Matt Reeves",
             "release_year":2022,
             "starring":"Robert Pattinson",
             "cover":"the_batman.png",
            
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #IT
             "movie_id": 2,
             "movie_name": "IT",
             "genre":"Horror",
             "director":"Andy Muschietti",
             "release_year":2017,
             "starring":"Bill Skarsgård",
             "cover":"it.png",
         })


c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #The Shawshank Redemption
             "movie_id": 3,
             "movie_name": "The Shawshank Redemption",
             "genre":"Drama",
             "director":"Frank Darabont",
             "release_year":1994,
             "starring":"Morgan Freeman",
             "cover":"the_shawshank_redemption.png",
         })


c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #The Mummy
             "movie_id": 4,
             "movie_name": "The Mummy",
             "genre":"Action",
             "director":"Stephen Sommers",
             "release_year":1999,
             "starring":"Brendan Fraser",
             "cover":"the_mummy.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Home Alone
             "movie_id": 5,
             "movie_name": "Home Alone",
             "genre":"Comedy",
             "director":"Chris Columbus",
             "release_year":1990,
             "starring":"Macaulay Culkin",
             "cover":"home_alone.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Me Before You
             "movie_id": 6,
             "movie_name": "Me Before You",
             "genre":"Romance",
             "director":"Thea Sharrock",
             "release_year":2016,
             "starring":"Emilia Clarke",
             "cover":"me_before_you.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #American Pie
             "movie_id": 7,
             "movie_name": "American Pie",
             "genre":"Comedy",
             "director":"Paul Weitz, Chris Weitz",
             "release_year":1999,
             "starring":"Jason Biggs",
             "cover":"american_pie.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Top Gun: Maverick
             "movie_id": 8,
             "movie_name": "Top Gun: Maverick",
             "genre":"Action",
             "director":"Joseph Kosinki",
             "release_year":2022,
             "starring":"Tom Cruise",
             "cover":"top_gun_maverick.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #American Psycho
             "movie_id": 9,
             "movie_name": "American Psycho",
             "genre":"Drama, Horror",
             "director":"Mary Harron",
             "release_year":2000,
             "starring":"Christian Bale",
             "cover":"american_psycho.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Avatar
             "movie_id": 10,
             "movie_name": "Avatar",
             "genre":"Action",
             "director":"James Cameron",
             "release_year":2009,
             "starring":"Sam Worthington",
             "cover":"avatar.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #The Notebook
             "movie_id": 11,
             "movie_name": "The Notebook",
             "genre":"Drama, Romance",
             "director":"Nick Cassavetes",
             "release_year":2004,
             "starring":"Ryan Gosling",
             "cover":"the_notebook.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Smile
             "movie_id": 12,
             "movie_name": "Smile",
             "genre":"Horror",
             "director":"Parker Finn",
             "release_year":2022,
             "starring":"Sosie Bacon",
             "cover":"smile.png",
         })


c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Titanic
             "movie_id": 13,
             "movie_name": "Titanic",
             "genre":"Drama, Romance",
             "director":"James Cameron",
             "release_year":1997,
             "starring":"Leonardo DiCaprio",
             "cover":"titanic.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Halloween
             "movie_id": 14,
             "movie_name": "Halloween",
             "genre":"Horror",
             "director":"John Carpenter",
             "release_year":1978,
             "starring":"Donald Pleasence",
             "cover":"halloween.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Clueless
             "movie_id": 15,
             "movie_name": "Clueless",
             "genre":"Comedy, Romance",
             "director":"Amy Heckerling",
             "release_year":1995,
             "starring":"Alicia Silverstone",
             "cover":"clueless.png",
         })

c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Zootopia
             "movie_id": 16,
             "movie_name": "Zootopia",
             "genre":"Comedy",
             "director":"Byron Howard",
             "release_year":2016,
             "starring":"Ginnifer Goodwin",
             "cover":"zootopia.png",
         })


c.execute("INSERT OR REPLACE INTO movies VALUES (:movie_id, :movie_name, :genre, :director, :release_year, :starring, :cover)",
        {
            #Black Panther
             "movie_id": 17,
             "movie_name": "Black Panther",
             "genre":"Action",
             "director":"Ryan Coogler",
             "release_year":2018,
             "starring":"Chadwick Boseman",
             "cover":"black_panther.png",
         })
         """