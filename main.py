from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/", summary="Afficher la version de l'API")
async def home():
    return {"version": "0.1a"}

@router.post("/register", summary="Créer un compte utilisateur (mot de passe aléatoire)")
async def register(username: str):
    return {"id": 1, "username": username, "generated_password": "aB9x#kL2pQ", "role": "user"}



app.include_router(router, prefix="/api")