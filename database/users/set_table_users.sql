create table users (
    no number,
    id varchar2(12) primary key,
    password varchar2(24) not null,
    name varchar2(50) not null,
    currentgrade number,
    currentclass number,
    currentnum number,
    currentstdnum number(10),
    point number default 0,
    signeddate varchar2(17) default to_char(sysdate, 'YYYYMMDD HH24:MI:SS'),
    lastlogin varchar2(17),
    identity number default 2,
    profile_pic varchar2(255)
);
-- 0 : 최고 관리자(1명)
-- 1 : 관리자
-- 2 : 학생