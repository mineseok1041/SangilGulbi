import pointDAO
import usersDTO
import pointLogDTO
import pointReasonDTO
from typing import Literal

class pointSVC:
    def __init__(self):
        self.pointDAO = pointDAO.pointDAO()

    def givePoint(self, stdDTO:usersDTO, writerDTO:usersDTO, giverDTO:usersDTO, point:int, reason: int, opinion: str):
        try:
            if point > 0:
                self.pointDAO.addPoint(stdDTO, point)
                self.pointDAO.recordPointLog('bonus', stdDTO, writerDTO, giverDTO, point, reason, opinion)
            elif point < 0:
                self.pointDAO.delPoint(stdDTO, point)
                self.pointDAO.recordPointLog('penalty', stdDTO, writerDTO, giverDTO, point, reason, opinion)
            else:
                raise Exception("0점은 부여할 수 없습니다.")
            
        except Exception as e:
            raise Exception(f"givePoint Error: {e}")
        
    def getPointReason(self, type: Literal['bonus', 'penalty']) -> list[pointReasonDTO]: # type: ignore
        try:
            return self.pointDAO.getPointReason(type)
        except Exception as e:
            raise Exception(f"getPointReason Error: {e}")
        
    def getPointLog(self, page: int) -> list[pointLogDTO]: # type: ignore
        try:
            return self.pointDAO.getPointLog(page)
        except Exception as e:
            raise Exception(f"getPointLog Error: {e}")
        
    def getPointLogByStdID(self, reqDTO: usersDTO):
        try:
            return self.pointDAO.getPointLogByStdID(reqDTO)
        except Exception as e:
            raise Exception(f"getPointLogByStdID Error: {e}")