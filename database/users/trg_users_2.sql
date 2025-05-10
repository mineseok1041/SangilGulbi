CREATE TRIGGER trg_users_set_no
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    IF :NEW.no IS NULL THEN
        :NEW.no := SEQ_users_NO.nextval;
    END IF;
END;