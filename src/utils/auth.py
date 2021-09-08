from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import JWTAuthentication

from src.config import settings
from src.config.database import database
from src.models.users import User
from src.schemas.users import UserOut, BaseUser, UserInCreate, UserInUpdate


user_db = SQLAlchemyUserDatabase(BaseUser, database, User.__table__)


jwt_authentication = JWTAuthentication(secret=settings.jwt_secret,
                                       lifetime_seconds=3600, tokenUrl="/auth/login")


user_manager = FastAPIUsers(
    db=user_db,
    auth_backends=[jwt_authentication],
    user_model=UserOut,
    user_create_model=UserInCreate,
    user_update_model=UserInUpdate,
    user_db_model=BaseUser,
)
