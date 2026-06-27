from typing import TypedDict

class person(TypedDict):
    name : str
    age : int

new_Person : person = {'name':'Shobhit','age':21}

print(new_Person)