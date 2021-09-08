from fastapi_users import models

class UserOut(models.BaseUser):
    pass

class UserInCreate(models.BaseUserCreate):
    pass

class UserInUpdate(UserOut, models.BaseUserUpdate):
    pass

<<<<<<< HEAD
=======

>>>>>>> 512606cf3862edfb72701c57401e2db4237bb502
class BaseUser(UserOut, models.BaseUserDB):
    pass
