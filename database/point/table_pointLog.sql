create table pointLog (
    no number,
    type VARCHAR2(10) CHECK (type IN ('bonus', 'penalty')),
    studentId varchar2(12),
    writeTeacherId varchar2(12),
    giveteacherId varchar2(12),
    point number,
    reason varchar2(255),
    opinion varchar2(255),
    addDate varchar2(17) default to_char(sysdate, 'YYYYMMDD HH24:MI:SS')
);


