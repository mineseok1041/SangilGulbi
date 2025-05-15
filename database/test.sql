select * from users;
select * from pointReason;
select * from pointLog;

drop table users;
drop SEQUENCE seq_users_no;

ALTER TABLE pointLog MODIFY (
    studentName VARCHAR2(50),
    writeTeacherName VARCHAR2(50),
    giveTeacherName VARCHAR2(50)
);