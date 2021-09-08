from fastapi_users import models

class UserOut(models.BaseUser):
    pass

class UserInCreate(models.BaseUserCreate):
    pass

class UserInUpdate(UserOut, models.BaseUserUpdate):
    pass

class BaseUser(UserOut, models.BaseUserDB):
    pass
