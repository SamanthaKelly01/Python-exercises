import csv

rows = []

with open("advertising.csv", 'r') as file:
    fileReader = csv.reader(file)
    fields = next(fileReader) # fields vira uma lista com o cabeçalho do csv
    firstRow = next(fileReader)

    for line in fileReader:
        rows.append(line)
    
    for line in rows[:5]:
        print(line)

    print("Cabeçalho: " + ", ".join(fields)) #transforma a lista em uma string com os itens separados por ", " 

    print(type(firstRow))
    print("primeira linha " + str(firstRow)) # transforma em string para exibir mas mantém a forma de lista 

# retorno:
# ['44.5', '39.3', '45.1', '10.4']
# ['17.2', '45.9', '69.3', '12']
# ['151.5', '41.3', '58.5', '16.5']
# ['180.8', '10.8', '58.4', '17.9']
# ['8.7', '48.9', '75', '7.2']
# Cabeçalho: TV, Radio, Jornal, Vendas
# <class 'list'>
# primeira linha ['230.1', '37.8', '69.2', '22.1']