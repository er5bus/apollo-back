from src.utils.auth import user_manager

current_active_user = user_manager.current_user(active=True)
current_active_superuser = user_manager.current_user(active=True, superuser=True)
