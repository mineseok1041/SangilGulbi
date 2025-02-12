from dataclasses import dataclass

@dataclass
class studentDTO():
    no: int = None
    id: str = None
    password: str = None
    name: str = None
    currentgrade: int = None
    currentclass: int = None
    currentnum: int = None
    firststdnum: int = None
    secondstdnum: int = None
    thirdstdnum: int = None
    point: int = None
    signeddate: str = None
    lastlogin: str = None
    phone: str = None
    parentphone: str = None
    email: str = None
    birth: str = None