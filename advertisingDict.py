import csv
 
# Open the CSV file for reading
with open('advertising.csv', mode='r') as file:
    # Create a CSV reader with DictReader
    csv_reader = csv.DictReader(file)
 
    # Initialize an empty list to store the dictionaries
    data_list = []
 
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each row (as a dictionary) to the list
        data_list.append(row)
 
# Print the list of dictionaries
for data in data_list[:5]:
    print(data)

# retorno:
# {'TV': '230.1', 'Radio': '37.8', 'Jornal': '69.2', 'Vendas': '22.1'}
# {'TV': '44.5', 'Radio': '39.3', 'Jornal': '45.1', 'Vendas': '10.4'} 
# {'TV': '17.2', 'Radio': '45.9', 'Jornal': '69.3', 'Vendas': '12'}   
# {'TV': '151.5', 'Radio': '41.3', 'Jornal': '58.5', 'Vendas': '16.5'}
# {'TV': '180.8', 'Radio': '10.8', 'Jornal': '58.4', 'Vendas': '17.9'}