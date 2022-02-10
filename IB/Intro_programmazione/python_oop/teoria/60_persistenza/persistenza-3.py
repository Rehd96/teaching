import json
relative_path = 'IB/Intro_programmazione/python_oop/teoria/60_persistenza/demo_file.json'

dictionary_list = ['a', 'a', 'c']
 

with open(relative_path, 'w') as f:
    json.dump(dictionary_list, f, indent=4) # Salvo su file
    

f = open(relative_path)
data = json.load(f)
print(data)
