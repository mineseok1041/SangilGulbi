create table pointLog (
    no number,
    type VARCHAR2(10) CHECK (type IN ('bonus', 'penalty')),
    studentId varchar2(12),
    studentNum varchar2(12),
    studentName varchar2(50),
    writeTeacherId varchar2(12),
    writeTeacherName varchar2(50),
    giveTeacherId varchar2(12),
    giveTeacherName varchar2(50),
    point number,
    reason varchar2(255),
    opinion varchar2(255),
    addDate varchar2(17) default to_char(sysdate, 'YYYY/MM/DD'),
    addTime varchar2(17) default to_char(sysdate, 'HH24:MI:SS')
);