from dataclasses import dataclass

@dataclass
class NoticeDTO:
    id: int = None
    title: str = None
    content: str = None
    author: str = None
    created_date: str = None
    updated_date: str = None