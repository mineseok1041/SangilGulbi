from dataclasses import dataclass

@dataclass
class usersDTO:
    no: int = None
    id: str = None
    password: str = None
    name: str = None
    grade: int = None
    classNo: int = None
    num: int = None
    stdNum: int = None
    addPoint: int = None
    delPoint: int = None
    point: int = None
    signeddate: str = None
    lastlogin: str = None
    identity: int = None
    verified: int = None