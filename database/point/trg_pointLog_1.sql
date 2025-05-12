CREATE TRIGGER trg_pointLog_set_no
BEFORE INSERT ON pointLog
FOR EACH ROW
BEGIN
    IF :NEW.no IS NULL THEN
        :NEW.no := SEQ_pointLog_NO.nextval;
    END IF;
END;