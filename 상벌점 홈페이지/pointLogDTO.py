from dataclasses import dataclass

@dataclass
class pointLogDTO:
    no: int = None
    type: str = None
    studentId: str = None
    studentNum: str = None
    studentName: str = None
    writeTeacherId: str = None
    writeTeacherName: str = None
    giveTeacherId: str = None
    giveTeacherName: str = None
    point: int = None
    reason: str = None
    opinion: str = None
    addDate: str = None