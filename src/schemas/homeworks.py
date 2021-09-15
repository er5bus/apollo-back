from sqlalchemy.sql.sqltypes import DateTime
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class HomeworkIn(BaseModel):
    name : str
    subject : str
    deadline = datetime


class HomeworkOut(HomeworkIn):
    id: int

class HomeworkCompletedIn(BaseModel):

    timestamp : Optional[datetime]=None
    answer : str
    deposit_date : datetime
    homework_id : int
    user_id : int

class HomeworkCompletednOut(BaseModel):
    id: int
    timestamp : Optional[datetime]=None
    answer : str
    deposit_date : datetime
    

    class Config:
        orm_mode = True
