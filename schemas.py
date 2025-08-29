# schemas.py

from pydantic import BaseModel,StrictStr, validator,root_validator
from typing import List, Optional
from datetime import date,time

# ======================================
#       Database Schema
# ======================================

class Department(BaseModel):
    Did: Optional[int] = None
    dep: StrictStr
    role: StrictStr

    @validator('dep')
    def dep_must_be_alpha(cls, v):
        if not v.isalpha():
            raise ValueError('Department must contain only alphabetic characters')
        return v

    @validator('role')
    def role_must_be_alpha(cls, v):
        if not v.isalpha():
            raise ValueError('Role must contain only alphabetic characters')
        return v

    class Config:
        orm_mode = True

class Teacher(BaseModel):
    Tid: Optional[int]
    Did : Optional[int]
    name: str
    name_code : str
    email: str
    pw: Optional[str] = None
    role: Optional[str]   

    class Config:
        orm_mode = True

class Student(BaseModel):
    Sid: Optional[int] 
    Did: Optional[int]
    dep: Optional[str] = None   
    name: str
    email: str
    pw: Optional[str] = None
    u_roll: str
    c_roll: Optional[str] = None
    year: int
    sem: int
    role :str

    class Config:
        orm_mode = True
      
class Subject(BaseModel):
    Sub_id: Optional[int]
    Did: Optional[int] = None       # <-- keep Did for POST
    dep: Optional[str] = None       # <-- dep optional for GET/display only
    sub_name: str
    sub_code: str
    year: int
    sem: int

    class Config:
        orm_mode = True

class SubjectTeacher(BaseModel):
    STid : Optional[int]
    Sub_id :Optional[int]
    Tid : Optional[int]
    
    sub_name :Optional[str]
    sub_code :Optional[str]
    dep :Optional[str]
    year :Optional[int]
    sem :Optional[int]
    name_code :Optional[str]
    name :Optional[str]
    subject: Optional[str] 
    teacher: Optional[str] 

    class Config :
        orm_mode =True
        
class Slot(BaseModel):
    Sl_id: Optional[int]
    start: time
    end: time
    # day: str
    sl_name: str

    class Config:
        orm_mode = True


    #  


class Routine (BaseModel):
    STid: int
    Sl_id: int
    Did: Optional[int]
    dep :str
    day :str



class Notice(BaseModel):
    N_id: Optional[int]
    Tid: Optional[int]
    Did : Optional[int]
    content: Optional[str]=None
    file : Optional[str]=None
    file_type : Optional[str]=None
    email: str
    # dep :str

    class Config:
        orm_mode = True
        
    @root_validator
    def check_content_or_file(cls, values):
        content, file = values.get("content"), values.get("file")
        if not content and not file:
            raise ValueError("Either content or file must be provided")
        return values



# class NoticeOut(BaseModel):
#     N_id: int
#     Tid: int
#     Did: int
#     content: Optional[str]
#     file: Optional[str]

#     class Config:
#         orm_mode = True

# class EditNotice(BaseModel)
# ===============..... Done .....====================

class Attendance(BaseModel):
    Aid: Optional[int] = None
    Sub_id: Optional[int] = None
    Sid: Optional[int] = None
    Tid :int
    date: date
    status: str

    class Config:
        orm_mode = True
        

# class Routine(BaseModel):
#     r_id: Optional[int] = None
#     sl_id: int
#     d_id: int
#     t_id: int
#     item3: Optional[str] = None

#     class Config:
#         orm_mode = True

class AttendanceUpdate(BaseModel):
    new_status: str

# ==============================================
#    Authentication
# ==============================================
        
class Login(BaseModel):
    username: str
    password: str

        
class TokenData(BaseModel):
    email: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
    
class ResetPwRequest(BaseModel):
    old_pw: str
    new_pw: str
    
# ===============..... Done .....====================



        










