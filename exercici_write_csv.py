import csv

with open("D:\Coding\Py\basket_players.csv", 'r', newline='') as f_in, open("jugadors_basket.csv", 'w', newline='') as f_out:
    csv_reader = csv.reader(f_in, delimiter=';')
    csv_writer = csv.writer(f_out, delimiter='^')
    for fila in csv_reader:
        csv_writer.writerow(fila)