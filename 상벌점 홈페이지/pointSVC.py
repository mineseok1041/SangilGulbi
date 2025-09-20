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
        
    def getFavPointReason(self, type: Literal['bonus', 'penalty'], usersDTO: usersDTO) -> list[pointReasonDTO]: # type: ignore
        try:
            pointReason = self.pointDAO.getPointReason(type)
            favoritePointNo = self.pointDAO.getFavoritePointReasonNo(usersDTO)

            favoriteItems = [pr for pr in pointReason if pr.no in favoritePointNo]
            otherItems = [pr for pr in pointReason if pr.no not in favoritePointNo]

            sortedPointReason = favoriteItems + otherItems

            return sortedPointReason
        except Exception as e:
            raise Exception(f"getFavPointReason Error: {e}")
        
    def getPointLog(self, page: int, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]: # type: ignore
        try:
            return self.pointDAO.getPointLog(page, type)
        except Exception as e:
            raise Exception(f"getPointLog Error: {e}")
        
    def getPointLogByStdID(self, reqDTO: usersDTO, page: int, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]: # type: ignore
        try:
            return self.pointDAO.getPointLogByStdID(reqDTO, page, type)
        except Exception as e:
            raise Exception(f"getPointLogByStdID Error: {e}")
        
    def getPointLogByTeacherID(self, reqDTO: usersDTO, page: int, type: Literal['all', 'bonus', 'penalty']) -> list[pointLogDTO]: # type: ignore
        try:
            return self.pointDAO.getPointLogByTeacherID(reqDTO, page, type)
        except Exception as e:
            raise Exception(f"getPointLogByTeacherID Error: {e}")
        
    def getTeacherPointLogMaxPage(self, teacherDTO) -> int:
        try:
            return self.pointDAO.getTeacherPointLogMaxPage(teacherDTO)
        except Exception as e:
            raise Exception(f"getTeacherPointLogMaxPage Error: {e}")
        
    def getStudentPointLogMaxPage(self, studentDTO) -> int:
        try:
            return self.pointDAO.getStudentPointLogMaxPage(studentDTO)
        except Exception as e:
            raise Exception(f"getStudentPointLogMaxPage Error: {e}")
        
    def getPointLogMaxPage(self) -> int:
        try:
            return self.pointDAO.getPointLogMaxPage()
        except Exception as e:
            raise Exception(f"getPointLogMaxPage Error: {e}")
        
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
        

    def searchPointLogs(self, keyword: str, teacher_id: str = None) -> list[pointLogDTO]:
        return self.pointDAO.searchPointLogs(keyword, teacher_id)

    def addFavoritePointReason(self, usersDTO: usersDTO, pointReasonDTO: pointReasonDTO):
        try:
            self.pointDAO.addFavoritePointReason(usersDTO, pointReasonDTO)
        except Exception as e:
            raise Exception(f"addFavoritePointReason Error: {e}")
        
    def removeFavoritePointReason(self, usersDTO: usersDTO, pointReasonDTO: pointReasonDTO):
        try:
            self.pointDAO.removeFavoritePointReason(usersDTO, pointReasonDTO)
        except Exception as e:
            raise Exception(f"removeFavoritePointReason Error: {e}")
        
    def getFavoritePointReasonNo(self, usersDTO: usersDTO) -> list[int]:
        try:
            return self.pointDAO.getFavoritePointReasonNo(usersDTO)
        except Exception as e:
            raise Exception(f"getFavoritePointReasonNo Error: {e}")
