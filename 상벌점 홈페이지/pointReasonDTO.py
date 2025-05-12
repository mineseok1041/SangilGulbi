from dataclasses import dataclass

@dataclass
class pointReasonDTO:
    no: int = None
    reason: str = None
    value: int = None
    type: str = None