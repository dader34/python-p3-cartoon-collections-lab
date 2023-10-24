def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf)+1}. {dwarf}')

def summon_captain_planet(planeteer_calls):
    return [word.capitalize() + "!" for word in planeteer_calls]

def long_planeteer_calls(words):
        return True in [len(word)>4 for word in words]

def find_the_cheese(arr):
    found = None
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
         if(cheese in arr):
              found = cheese
              break
    return found
