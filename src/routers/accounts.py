from src.config import settings
from src.utils.auth import jwt_authentication, user_manager


authrouter = user_manager.get_auth_router(jwt_authentication)
authresetpasswordrouter = user_manager.get_reset_password_router(
    reset_password_token_secret=settings.reset_password_secret)
registerrouter = user_manager.get_register_router()
usersrouter = user_manager.get_users_router()
