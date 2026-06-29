from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'shobhit'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5)

new_student = {'age' : 25, 'email': 'shobhit.1453@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)
print(type(student_dict))