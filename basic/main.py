from fastapi import FastAPI,Path,HTTPException
import json
app=FastAPI()
def load_data():
    with open("patients.json","r") as file:
        data=json.load(file)
    return data

@app.get("/")
def hello():
    return {"message":"Patient Management System API"}

@app.get("/about")
def about():
    return {"message":"This API manages patient information."}

@app.get("/patients")
def get_patients():
    data=load_data()
    return data

@app.get("/patients/{patient_id}")
def get_patient(patient_id:str=Path(..., description="The ID of the patient to retrieve like P001, P002")):
    data=load_data()
    if patient_id in data:
        return data[patient_id] 
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/patients/age/{age}")
def get_patients_by_age(age:int=Path(..., description="The age of the patients to retrieve")):
    data=load_data()
    result={pid:info for pid,info in data.items() if info["age"]==age}
    if result:
        return result
    raise HTTPException(status_code=404, detail="No patients found with the specified age")

@app.get("/patients/gender/{gender}")
def get_patients_by_gender(gender:str=Path(..., description="The gender of the patients to retrieve")):
    data=load_data()
    result={pid:info for pid,info in data.items() if info["gender"].lower()==gender.lower()}
    if result:
        return result
    raise HTTPException(status_code=404, detail="No patients found with the specified gender")
