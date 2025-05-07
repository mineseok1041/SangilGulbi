from dataclasses import dataclass

@dataclass
class pointLogDTO:
    stdID: str = None
    managerID: str = None
    point: int = None
    reason: str = None
    addDate: str = None