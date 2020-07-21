cities = {'Loser' : 100, 'winner' : 1000 }
#dictonary with {}
del cities['winner']
cities['Nerd'] = 500    #add
cities['Loser'] = 1000  #update 

print(cities)

for k, v in cities.items():
    print("Ranks: {}, Boosters : {} ".format(k,v))