from pydantic import AnyUrl, BaseModel, EmailStr
from typing import List,Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    linked_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contacts: Dict[str, str]

def insert_patient_to_db(patient: Patient):
    print(patient)
    print(patient.name)
    print(patient.email)
    print(patient.linked_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)    
    print(patient.contacts)
    print("Data inserted successfully")

patient_info={
    "name":"John",
    "email":"astik@gmail.com",
    "linked_url":"https://www.linkedin.com/in/johndoe",
    "age":30, 
    "weight":70.5, 
    "married":True,
    "allergies":["pollen","nuts"],
    "contacts":{"home":"123-456-7890","work":"987-654-3210"}
}
patient=Patient(**patient_info)
insert_patient_to_db(patient)
