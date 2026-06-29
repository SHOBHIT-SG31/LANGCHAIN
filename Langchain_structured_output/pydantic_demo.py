from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name : str = 'shobhit'
    age : Optional[int] = None
    email : EmailStr
new_student = {'age' : 25, 'email': 'shobhit.1453@gmail.com'}

student = Student(**new_student)

print(student)