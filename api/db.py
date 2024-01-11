from fastapi import FastAPI, HTTPException
from supabase import create_client, Client

SUPABASE_URL = "https://zrzfhfoxyhsdetttpehr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpyemZoZm94eWhzZGV0dHRwZWhyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNDk3Nzg4MSwiZXhwIjoyMDIwNTUzODgxfQ.9bFc9RS1C2u9mKWHjKTLKwsnygP4wYiVkuqBnpaTL0k"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
    try:
        plates = supabase.table("plates").select("*").eq("number_plate", number_plate).execute()
        if not plates["data"]:
            raise HTTPException(status_code=404, detail="Plate not found")
        return plates
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")