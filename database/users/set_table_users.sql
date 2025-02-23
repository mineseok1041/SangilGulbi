create table users (
    no number,
    id varchar2(12) primary key,
    password varchar2(24) not null,
    name varchar2(50) not null,
    currentgrade number,
    currentclass number,
    currentnum number,
    firststdnum number(10),
    secondstdnum number(10),
    thirdstdnum number(10),
    point number default 0,
    signeddate varchar2(17) default to_char(sysdate, 'YYYYMMDD HH24:MI:SS'),
    lastlogin varchar2(17),
    phone varchar2(12),
    parentphone varchar2(12),
    email varchar2(50),
    birth varchar2(8),
    identity number default 2,
    profile_pic varchar2(255)
);
-- 0 : 최고 관리자(1명)
-- 1 : 관리자
-- 2 : 학생