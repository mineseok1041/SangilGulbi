from dataclasses import dataclass

@dataclass
class usersDTO:
    no: int = None
    id: str = None
    password: str = None
    name: str = None
    currentgrade: int = None
    currentclass: int = None
    currentnum: int = None
    currentstdnum: int = None
    point: int = None
    signeddate: str = None
    lastlogin: str = None
    identity: int = None
    profile_pic: str = None