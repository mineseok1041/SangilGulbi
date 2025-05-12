from dataclasses import dataclass

@dataclass
class pointLogDTO:
    no: int = None
    type: str = None
    studentId: str = None
    writeTeacherId: str = None
    giveTeacherId: str = None
    point: int = None
    reason: str = None
    opinion: str = None
    addDate: str = None