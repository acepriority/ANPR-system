"""
This module provides CRUD (Create, Read, Update, Delete) operations for managing plates.

def get_plate(number_plate: str):
    Retrieve all plates.

    Returns:
        List[dict]: List of plates.

def get_plate(number_plate: str):
    Retrieve a specific plate by its number plate.

    Args:
        number_plate (str): The number plate to retrieve.

    Returns:
        dict: The plate information.

def insert_plate(plate: PlatesSchema):
    Insert a new plate.

    Args:
        plate (PlatesSchema): The plate information to insert.

    Returns:
        dict: The inserted plate information.

def delete_plate(number_plate: str):
    Delete a plate by its number plate.

    Args:
        number_plate (str): The number plate to delete.

    Returns:
        dict: A message indicating the deletion status.
"""





from fastapi import FastAPI, HTTPException, status
from supabase import create_client, Client
from pydantic import BaseModel

SUPABASE_URL = "https://zrzfhfoxyhsdetttpehr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpyemZoZm94eWhzZGV0dHRwZWhyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNDk3Nzg4MSwiZXhwIjoyMDIwNTUzODgxfQ.9bFc9RS1C2u9mKWHjKTLKwsnygP4wYiVkuqBnpaTL0k"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class PlatesSchema(BaseModel):
    permit_number: str
    name: str
    number_plate: str

app = FastAPI()

@app.get("/plates/")
def get_all_plates():
    try:
        plates = supabase.table("plates").select("*").execute()
        return plates
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/plates/{number_plate}")
def get_plate(number_plate: str):
    plate = supabase.table("plates").select("*").eq("number_plate", number_plate).execute()
    return plate

@app.post("/plates/", status_code=status.HTTP_201_CREATED)
def insert_plate(plate: PlatesSchema):
    plate = supabase.table("plates").insert({
        "permit_number": plate.permit_number,
        "name": plate.name,
        "number_plate": plate.number_plate 
    }).execute()

@app.delete("/plates/{number_plate}", status_code=status.HTTP_204_NO_CONTENT)
def delete_plate(number_plate: str):
    plate = supabase.table("plates").delete().eq("number_plate", number_plate).execute()
    return {"msg": "Deleted"}
