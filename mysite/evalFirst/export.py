# import sqlite3, os, openpyxl #make sure to install openpyxl in command prompt, it is what allows the export to excel.
# from sqlite3 import Error

# DBFILE = "db.sqlite3" 

# # (B) OPEN DATABASE & CREATE EXCEL
# conn = sqlite3.connect(DBFILE) 
# cursor = conn.cursor()
# book = openpyxl.Workbook()
# sheet = book.active
 
# # (C) EXPORT DATA TO EXCEL
# cursor.execute("SELECT FROM `evalFirst.models`") 
# results = cursor.fetchall()
# i = 0
# for row in results:
#   i += 1
#   j = 1
#   for col in row:
#     cell = sheet.cell(row = i, column = j)
#     cell.value = col
#     j += 1
 
# # (D) SAVE EXCEL FILE & CLOSE DB
# book.save("demo.xlsx") # Change name to the name of the excel file we want to save it to
# conn.close()

# from django.core.exceptions import PermissionDenied
# from django.http import HttpResponse
# # from pyExcelerator import *


# def export_as_xls(modeladmin, request, queryset):
#     """
#     Generic xls export admin action.
#     """
#     if not request.user.is_staff:
#         raise PermissionDenied
#     opts = modeladmin.model._meta
    
#     wb = Workbook()
#     ws0 = wb.add_sheet('0')
#     col = 0
#     field_names = []
#     # write header row
#     for field in opts.fields:
#         ws0.write(0, col, field.name)
#         field_names.append(field.name)
#         col = col + 1
    
#     row = 1
#     # Write data rows
#     for obj in queryset:
#         col = 0
#         for field in field_names:
#             val = unicode(getattr(obj, field)).strip()
#             ws0.write(row, col, val)
#             col = col + 1
#         row = row + 1
    
#     wb.save('/tmp/output.xls')
#     response = HttpResponse(open('/tmp/output.xls','r').read(),
#                   mimetype='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
#     return response
    
# export_as_csv.short_description = "Export selected objects to XLS"