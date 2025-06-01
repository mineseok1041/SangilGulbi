CREATE OR REPLACE TRIGGER trg_notice_set_dates
BEFORE INSERT OR UPDATE ON notice
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        :NEW.created_date := TO_CHAR(SYSDATE, 'YYYY/MM/DD');
        :NEW.created_time := TO_CHAR(SYSDATE, 'HH24:MI:SS');
    ELSIF UPDATING THEN
        :NEW.updated_date := TO_CHAR(SYSDATE, 'YYYY/MM/DD');
        :NEW.updated_time := TO_CHAR(SYSDATE, 'HH24:MI:SS');
    END IF;
END;