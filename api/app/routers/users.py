from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from typing import List

from ..models.user import User, UserCreateDTO, UserModel, UserSignInDTO

from ..db import get_db

router = APIRouter()


@router.get("/users", response_model=List[User], status_code=200)
def get_users(db: Session = Depends(get_db)):
    """
    Récupère la liste des users
    """
    return db.query(UserModel).all()


@router.get("/users/{user_id}", response_model=User, status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Récupère un user par son id
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    """
    Créé un nouveau user
    """
    # TODO: chiffrer le mot de passe avec bcrypt
    existing_user = db.query(UserModel).filter(
        UserModel.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/users/sign-up", response_model=User, status_code=201)
def sign_up_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    """
    Inscrire un nouveau user
    """
    # TODO: chiffrer le mot de passe avec bcrypt
    existing_user = db.query(UserModel).filter(
        UserModel.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/users/sign-in", response_model=str, status_code=200)
def sign_in_user(user: UserSignInDTO, db: Session = Depends(get_db)):
    """
    Connecter un nouveau user
    """
    existing_user = db.query(UserModel).filter(
        UserModel.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User does not exist")

    # TODO: chiffrer le mot de passe fourni et le comparer avec le mot de passe chiffré et stocké en BDD
    # TODO: si mot de passe incorrect retourner erreur HTTP 401
    # TODO: si mot de passe correct générer un token JWT et le retourner à l'utilisateur
    return "token"


@router.put("/users/{user_id}", response_model=User, status_code=200)
def update_user(user_id: int, updated_user: User, db: Session = Depends(get_db)):
    """
    Met à jour un user sélectionné selon son id
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in updated_user.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Supprime un user sélectionné selon son id
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
