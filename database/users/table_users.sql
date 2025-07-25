create table users (
    no number,
    id varchar2(12) primary key,
    password varchar2(24) not null,
    name varchar2(50) not null,
    grade number(1),
    classNo number(2),
    num number(2),
    stdnum number(10),
    addPoint number default 0,
    delPoint number default 0,
    point number default 0,
    signeddate varchar2(17) default to_char(sysdate, 'YYYY/MM/DD'),
    signedtime varchar2(17) default to_char(sysdate, 'HH24:MI:SS'),
    lastlogindate varchar2(17),
    lastlogintime varchar2(17),
    identity number(1),
    verified number(1),
    checkCode varchar2(20)
);
-- 0 : 최고 관리자(1명)
-- 1 : 선생님
-- 2 : 학생