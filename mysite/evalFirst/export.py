# (A) INIT
# (A1) LOAD MODULES
import sqlite3, os, openpyxl #install openpyxl in command prompt
from sqlite3 import Error

# (A2) SETTINGS
DBFILE = "users.db" #change name to the name of our database

# (B) OPEN DATABASE & CREATE EXCEL
conn = sqlite3.connect(DBFILE) 
cursor = conn.cursor()
book = openpyxl.Workbook()
sheet = book.active
 
# (C) EXPORT DATA TO EXCEL
cursor.execute("SELECT * FROM `users`") #again, change where it says user
results = cursor.fetchall()
i = 0
for row in results:
  i += 1
  j = 1
  for col in row:
    cell = sheet.cell(row = i, column = j)
    cell.value = col
    j += 1
 
# (D) SAVE EXCEL FILE & CLOSE DB
book.save("demo.xlsx") #change name of what we save it to
conn.close()

#     https://code-boxx.com/python-export-database-excel/#sec-download
