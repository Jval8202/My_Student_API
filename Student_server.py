from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Root
@app.get("/")
async def root():
    return {"message": "Videogames API running"}

# ✅ GET (Read all)
@app.get("/videogames")
async def get_videogames():
    response = supabase.table("videogames").select("*").execute()
    return response.data

# ✅ POST (Create)
@app.post("/videogames")
async def create_videogame(videogame: dict):
    response = supabase.table("videogames").insert(videogame).execute()
    return response.data

# ✅ PUT (Update)
@app.put("/videogames/{game_id}")
async def update_videogame(game_id: int, videogame: dict):
    response = supabase.table("videogames").update(videogame).eq("id", game_id).execute()
    return response.data

# ✅ DELETE (Delete)
@app.delete("/videogames/{game_id}")
async def delete_videogame(game_id: int):
    response = supabase.table("videogames").delete().eq("id", game_id).execute()
    return {"deleted": response.data}
