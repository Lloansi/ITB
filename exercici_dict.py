import csv

with open("/home/sjo/Escriptori/DADES/DavidGomez/Python/basket_players.csv", 'r') as f:
    #writer = csv.writer(f, delimiter =";",quoting=csv.QUOTE_MINIMAL)
    lines = f.readlines()
    
#Variables
real_dict = {}
age_player = {}
string = "Jugador"
iterator = 0
aux = 0
size_players = 0
size_list = size_players
pes_playermax = 0
altura_playermin = 10000
count_base = 0
count_escorta = 0
count_aler = 0
count_alapivot = 0
count_pivot = 0
auxi = 0
pastteam_player = "BAL"   
count_player= 0   
number_of_teams = 0    
men20_29 = 0
men30_39 = 0
men40_49 = 0   

#Lists
list = ["Nom", "Equip", "Posició", "Altura", "Pes", "Edad"]
list_keys = []
list_teams = ["BAL"]
num_players_team = []
list_teams_result = []
dictionary_team_results_players = {}
list_aux_results = []
keysTeams = []

def inch_to_cm(inch):
    result = inch * 2.54
    return result

def pound_to_kg(pound):
    result = pound * 0.45
    return result

def print_results(pes_playermax,altura_playermin,count_base,count_escorta,count_aler,count_alapivot,count_pivot,men20_29,men30_39,men40_49):
    print("\n\nEl pes màxim és de: " + str(pes_playermax))
    print("La altura mínima és de: " + str(altura_playermin))
    print("Hi han " + str(count_base) + " bases")
    print("Hi han " + str(count_escorta) + " escortas")
    print("Hi han " + str(count_aler) + " alers")
    print("Hi han " + str(count_alapivot) + " ala-pivots")
    print("Hi han " + str(count_pivot) + " pivots")
    print("Hi han " + str(men20_29) + " de 20 a 29 anys")
    print("Hi han " + str(men30_39-men20_29) + " de 30 a 39 anys")
    print("Hi han " + str(men40_49-men30_39) + " de 40 a 49 anys")
    print("\n\n")
    
def print_dict(real_dict):
    #Printejem el diccionari creat amb els nous valors
    for k, v in real_dict.items():
        print(k, v)

def main():
    #Exercici 1
    print_dict(real_dict)
    #Exercici 2
    print_results(pes_playermax,altura_playermin,count_base,count_escorta,count_aler,count_alapivot,count_pivot,men20_29,men30_39,men40_49)

#Exercici 1
#Llegim linea per linea el csv i separem la informació per tractarla posteriorment
#Itarem aquesta informació per traduir les keys al català i modificar els valors de [pound i polzades --> kg i cm ], tot això afegint-ho a un nou diccionari anometa "real_dict"
for line in lines:
    size_players += 1
    dictionary_line = {}
    words = line.split(";")
    size = len(words)
    key = string + str(iterator)
    if aux != 0:
        for i in range(size):
                
                match list[i]:
                    case "Altura":
                        words[i] = inch_to_cm(float(words[i]))
                        words[i] = round(words[i],2)
                    case "Pes":
                        words[i] = pound_to_kg(float(words[i]))    
                        words[i] = round(words[i],2) 
                    case "Posició":
                        if words[i] == "Point Guard":
                            words[i] = "Base"  
                        elif words[i] == "Shooting Guard":
                            words[i] = "Escorta" 
                        elif words[i] == "Small Forward":
                            words[i] = "Aler" 
                        elif words[i] == "Power Forward":
                            words[i] = "Ala-pivot" 
                        elif words[i] == "Center":
                            words[i] = "Pivot"     
                    case "Edad":
                        words[i] = round(float(words[i]))                    
                dictionary_line[list[i]] = words[i]
    list_keys.append(key)
    real_dict.setdefault(key, [])
    real_dict[key].append(dictionary_line)
    iterator += 1
    aux += 1
    
#Printejem el diccionari creat
for k, v in real_dict.items():
    print(k, v)  

#Exercici 2
#Després de tractar les dades i afegirles al diccionari "real_dict"
#Iterem els valors i anem treient estadístiques, pes màxim, altura minima, jugadors per posició i franges d'edad
for key in real_dict.keys():
    if auxi != 0:
        for values in real_dict.get(key):
            
            age_player = values[list[5]]
            pes_player = values[list[4]]
            altura_player = values[list[3]]
            pos_player = values[list[2]]
            team_player = values[list[1]]

            if pes_player > pes_playermax:
                pes_playermax = pes_player

            if altura_player < altura_playermin:
                altura_playermin = altura_player
                
            if age_player < 30:
                men20_29 += 1
            if age_player < 40:
                men30_39 += 1
            if age_player < 50: 
                men40_49 += 1  
           

            match pos_player:
                case "Base":
                    count_base += 1
                case "Escorta":    
                    count_escorta += 1
                case "Aler":
                    count_aler += 1
                case "Ala-pivot":
                    count_alapivot += 1
                case "Pivot":
                    count_pivot += 1

            if team_player != pastteam_player:
                list_teams.append(team_player)
                pastteam_player = team_player
                num_players_team.append(count_player)
                count_player = 0
                number_of_teams += 1
            if team_player == pastteam_player:
                list_teams_result.append(str(altura_player) + "," + str(pes_player))
                count_player += 1
    auxi += 1                


#Finalment ara crearem un nou diccionari, per tenir les dades de altura i pes, per equips.
#Creem totes les keys  per guardar els resultats
for i in range(number_of_teams):
    dictionary_team_results_players.setdefault(list_teams[i], [])


#Separem les dades per jugador en dos: pes_altura[0] = Altura i pes_altura[1] = Pes
for i in range(size_players-1):
    pes_altura = list_teams_result[i].split(",")
    list_aux_results.append(pes_altura)
    

#Creem un diccionari amb les keys sent els noms dels equips guardats en una llista previa
for dictKey in dictionary_team_results_players.keys():
   keysTeams.append(dictKey)


num_done = 0
name_team = 0

#Afegim a cada equip (key) el pes i altura de cada jugador (value)
for i in range(len(num_players_team)):
    a = num_players_team[i]
    for i in range(a):
        dictionary_team_results_players[keysTeams[name_team]].append(list_aux_results[num_done + i])
    num_done += a    
    name_team += 1

main()

#Printeja el diccionari nou diccionari, amb les dades de altura i pes per equip
auxz=0
for key in dictionary_team_results_players.keys():
    for values in dictionary_team_results_players.get(key):
        name = string + str(auxz)
        print(name + " del Equip: {} Té un pes i altura de: {}".format(key,values))
        auxz += 1
        
            
'''
Prints per veure totes les llistes

1- Número de jugadors per equip
print(num_players_team)

2- Llista dels equips
print(list_teams)

3- Resultats de guardar altura i pes de cada jugador
print(list_teams_result)

4- Llista amb tots els resultats de cada jugador, sense estar a cap diccionari
print(list_aux_results)

5- Diccionari amb els resultats per equip
print(dictionary_team_results_players)
'''