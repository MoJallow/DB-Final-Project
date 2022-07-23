from codecs import getencoder
import csv
from cs50 import SQL
open("bookdatabase.db","w").close()

db = SQL("sqlite:///bookdatabase.db")

db.execute("CREATE TABLE books(book_id INTEGER, title TEXT , genre TEXT, ISBN TEXT, year_of_publication INTEGER, PRIMARY KEY(book_id))")
db.execute("CREATE TABLE mid_table(mid_id INTEGER, inter_id INTEGER , PRIMARY KEY(mid_id), FOREIGN KEY(inter_id) REFERENCES books(book_id))")
db.execute("CREATE TABLE author_table(author_id INTEGER , name TEXT , gender TEXT, nationality TEXT, telephone INTEGER, PRIMARY KEY(author_id) , FOREIGN KEY(author_id) REFERENCES mid_table(mid_id)) ")

with open("books.csv" , "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        title = row["Title of Book"]
        genre = row["Genre"]
        ISBN = row["ISBN No."]
        year_of_publication = row["Year of Publication"]
        
        book_id = db.execute("INSERT INTO books(title, genre, ISBN, year_of_publication) VALUES(?,?,?,?)" , title, genre, ISBN, year_of_publication)
        
        for name in row["Author"].split(" , "):
            
            name = name.strip()
            gender = row["Gender"]
            nationality = row["Nationality"]
            telephone = row["Telephone"]
            
            magic_id = db.execute("INSERT INTO mid_table(inter_id) VALUES((SELECT book_id FROM books WHERE title = ?))",title)
            db.execute("INSERT INTO author_table(author_id , name, gender, nationality, telephone) VALUES((SELECT inter_id FROM mid_table WHERE inter_id = ?),?,?,?,?)",magic_id , name, gender, nationality, telephone) 
            
        
    
    

