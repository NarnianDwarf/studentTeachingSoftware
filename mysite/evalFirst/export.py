import sqlite3, os, openpyxl #make sure to install openpyxl in command prompt, it is what allows the export to excel.
from sqlite3 import Error

DBFILE = "db.sqlite3" 

# (B) OPEN DATABASE & CREATE EXCEL
conn = sqlite3.connect(DBFILE) 
cursor = conn.cursor()
book = openpyxl.Workbook()
sheet = book.active
 
# (C) EXPORT DATA TO EXCEL
cursor.execute("SELECT FROM `evalFirst.models`") 
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
book.save("demo.xlsx") # Change name to the name of the excel file we want to save it to
conn.close()
