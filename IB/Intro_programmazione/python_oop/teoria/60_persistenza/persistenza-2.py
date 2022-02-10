import json
relative_path = 'IB/Intro_programmazione/python_oop/teoria/60_persistenza/demo_file.json'

dictionary_list = [
    {
        'id': "0",
        'nome': "Davide"
    },
    {
        'id': "1",
        'nome': "Anna",
    },
    {
        'id': "2",
        'email': "email@email.it"
    },
]
 

'''
1) json.dump()

- Is used when the Python objects have to be stored in a file.	
- Needs the json file name in which the output has to be stored as an argument.	
- This method writes in the memory and then command for writing to disk is executed separately.
- Faster method	

Syntax: json.dump(d, skipkeys=False, ensure_ascii=True, check_circular=True, 
                  allow_nan=True, cls=None, indent=None, separators=None)


+ indent: It improves the readability of the json file. 
The possible values that can be passed to this parameter are simply double 
quotes(""), any integer values. 
Simple double quotes makes every key-value pair appear in new line.

'''

with open(relative_path, 'w') as f:
    json.dump(dictionary_list, f, indent=4) # Salvo su file
    

'''
2) json.dumps()

- json.dumps() is a function that converts a Python object into a json string.
- used when the objects are required to be in string format and is used for 
  parsing, printing, etc, .
- This method writes in the memory and then command for writing to disk 
  is executed separately
'''

json_string = json.dumps(dictionary_list)
print(json_string)

# NOTA: una volta che abbiamo il json in stringa, per salvare su file:
''' f = open(relative_path, "a")
f.write(json_string)
f.close() '''


'''
3) Leggere da file json 

- json.load() takes a file object and returns the json object. 
- A JSON object contains data in the form of key/value pair. The keys are strings and the values are the JSON types. 
Keys and values are separated by a colon. Each entry (key/value pair) is separated by a comma.

Syntax: json.load(file_object)



'''

f = open(relative_path)
data = json.load(f)
print(data)
