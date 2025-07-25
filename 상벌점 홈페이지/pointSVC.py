import pointDAO
import usersDAO
import usersDTO
import pointLogDTO
import pointReasonDTO
from typing import Literal

class pointSVC:
    def __init__(self):
        self.pointDAO = pointDAO.pointDAO()
        self.usersDAO = usersDAO.usersDAO()

    def givePoint(self, stdDTO:usersDTO, writerDTO:usersDTO, giverDTO:usersDTO, point:int, reason: int, opinion: str):
        try:
            stdDTO = self.usersDAO.getUsersInfo(stdDTO)
            writerDTO = self.usersDAO.getUsersInfo(writerDTO)
            giverDTO = self.usersDAO.getUsersInfo(giverDTO)

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
        
    def getPointLogByTeacherID(self, reqDTO: usersDTO, type: Literal['all', 'bonus', 'penalty']):
        try:
            return self.pointDAO.getPointLogByTeacherID(reqDTO, type)
        except Exception as e:
            raise Exception(f"getPointLogByTeacherID Error: {e}")
        
    def cancelPointLog(self, logNo: int):
        try:
            pointLogDTO = self.pointDAO.getPointLogByNo(logNo)
            returnPoint = pointLogDTO.point
            studentDTO = self.usersDAO.getUsersInfo(usersDTO.usersDTO(id=pointLogDTO.studentId))

            if returnPoint > 0:
                self.pointDAO.addPoint(studentDTO, (returnPoint * -1))
            elif returnPoint < 0:
                self.pointDAO.delPoint(studentDTO, (returnPoint * -1))
            self.pointDAO.deletePointLog(logNo)
        except Exception as e:
            raise Exception(f"deletePointLog Error: {e}")