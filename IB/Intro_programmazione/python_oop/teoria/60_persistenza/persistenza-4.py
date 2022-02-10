import json
relative_path = 'IB/Intro_programmazione/python_oop/teoria/60_persistenza/demo_file.json'

class Foo(object):
    def __init__(self, data = None):
        self.x = 1
        self.y = 2

foo = Foo()
s = json.dumps(foo.__dict__) # s set to: {"x":1, "y":2}
print(s)

with open(relative_path, 'w') as f:
    json.dump(foo.__dict__, f, indent=4) # Salvo su file


f = open(relative_path)
data = json.load(f)
print(data)
new_foo = Foo(data)