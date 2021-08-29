from fastapi import Depends, Response, Request
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from ..config import settings
from ..models.users import user_db, User
from ..schemas.users import UserOut, UserInCreate, UserInUpdate


jwt_authentication = JWTAuthentication(secret=settings.jwt_secret, lifetime_seconds=3600, tokenUrl="/auth/login")

accounts = FastAPIUsers(
    db=user_db,
    auth_backends=[jwt_authentication],
    user_model=UserOut,
    user_create_model=UserInCreate,
    user_update_model=UserInUpdate,
    user_db_model=User,
)

authrouter = accounts.get_auth_router(jwt_authentication)
authresetpasswordrouter = accounts.get_reset_password_router(reset_password_token_secret=settings.reset_password_secret)
registerrouter = accounts.get_register_router()
usersrouter = accounts.get_users_router()


@authrouter.post("/refresh-token")
async def refresh_token(response: Response, user=Depends(accounts.get_current_active_user)):
    return await jwt_authentication.get_login_response(user, response)
