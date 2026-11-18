from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/", summary="Afficher la version de l'API")
async def home():
    return {"version": "0.1a"}

@router.post("/register", summary="Créer un compte utilisateur (mot de passe aléatoire)")
async def register(username: str):
    return {"id": 1, "username": username, "generated_password": "aB9x#kL2pQ", "role": "user"}

@router.post("/login", summary="Connexion utilisateur")
async def login(username: str, password: str):
    return {"id": 1, "username": username, "role": "user", "is_blocked": False}

@router.patch("/users/password", summary="Modifier son mot de passe")
async def change_password():
    return {"message": "Mot de passe mis à jour"}

@router.patch("/admin/users/{uid}/block", summary="Bloquer un compte utilisateur")
async def block_user(uid: int):
    return {"id": uid, "is_blocked": True}

@router.post("/admin/products", summary="Créer un produit")
async def create_product():
    return {"id": 3, "message": "Produit créé (mock)"}

@router.patch("/admin/products/{pid}", summary="Modifier un produit ou son stock")
async def update_product(pid: int):
    return {"id": pid, "message": "Produit mis à jour (mock)"}

@router.delete("/admin/products/{pid}", summary="Désactiver un produit")
async def delete_product(pid: int):
    return {"id": pid, "is_active": False}

app.include_router(router, prefix="/api")