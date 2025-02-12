create table student (
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
    profile_pic varchar2(255)
);

create sequence seq_student_id
    start with 1
    increment by 1
    NOORDER;

CREATE TRIGGER trg_student_set_studentid
BEFORE INSERT OR UPDATE ON student
FOR EACH ROW
BEGIN
    IF :NEW.currentgrade IS NOT NULL 
    AND :NEW.currentclass IS NOT NULL 
    AND :NEW.currentnum IS NOT NULL THEN
        IF :NEW.currentgrade = 1 THEN
            :NEW.firstID := :NEW.currentgrade * 10000 + 
                                :NEW.currentclass * 100 + 
                                :NEW.currentnum;
        ELSIF :NEW.currentgrade = 2 THEN
            :NEW.secondID := :NEW.currentgrade * 10000 + 
                                :NEW.currentclass * 100 + 
                                :NEW.currentnum;
        ELSIF :NEW.currentgrade = 3 THEN
            :NEW.thirdID := :NEW.currentgrade * 10000 + 
                                :NEW.currentclass * 100 + 
                                :NEW.currentnum;
        END IF;
    END IF;
END;

CREATE TRIGGER trg_student_set_no
BEFORE INSERT ON student
FOR EACH ROW
BEGIN
    IF :NEW.no IS NULL THEN
        :NEW.no := SEQ_STUDENT_ID.nextval;
    END IF;
END;

commit;