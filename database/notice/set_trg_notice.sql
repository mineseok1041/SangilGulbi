-- filepath: /c:/Users/Ace/Desktop/개발/workspace/공지사항/database/notice/set_trg_notice.sql
CREATE OR REPLACE TRIGGER trg_notice_set_dates
BEFORE INSERT OR UPDATE ON notice
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        :NEW.created_date := TO_CHAR(SYSDATE, 'YYYYMMDD HH24:MI:SS');
    ELSIF UPDATING THEN
        :NEW.updated_date := TO_CHAR(SYSDATE, 'YYYYMMDD HH24:MI:SS');
    END IF;
END;