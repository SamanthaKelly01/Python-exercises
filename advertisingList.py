# importing csv module
import csv
 
# csv file name
filename = "advertising.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
 
    # extracting field names through first row
    fields = next(csvreader)
    print(type(fields))
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
        number = (csvreader.line_num)
    print("Total no. of rows: {}".format(number) )
 
# printing the field names
print('Field names are: ' + ', '.join(field for field in fields))
 
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')

# retorno:
# <class 'list'>
# Total no. of rows: 201
# Field names are: TV, Radio, Jornal, Vendas

# First 5 rows are:

#      230.1       37.8       69.2       22.1

#       44.5       39.3       45.1       10.4

#       17.2       45.9       69.3         12

#      151.5       41.3       58.5       16.5

#      180.8       10.8       58.4       17.9
