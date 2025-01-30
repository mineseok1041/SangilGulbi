from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    profile_pic = db.Column(db.String(120))  # 프로필 사진 파일명 저장

    # Point 테이블과 관계 설정
    points = db.relationship('Point', backref='user', lazy=True)

    def total_points(self):
        return sum(point.points for point in self.points)  # 모든 상벌점 합산


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Point {self.points}>'
