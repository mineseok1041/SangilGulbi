CREATE TRIGGER trg_users_set_studentid
BEFORE INSERT OR UPDATE ON users
FOR EACH ROW
BEGIN
    IF :NEW.currentgrade IS NOT NULL 
    AND :NEW.currentclass IS NOT NULL 
    AND :NEW.currentnum IS NOT NULL THEN
        IF :NEW.currentgrade = 1 THEN
            :NEW.firststdnum := :NEW.currentgrade * 10000 + 
                                :NEW.currentclass * 100 + 
                                :NEW.currentnum;
        ELSIF :NEW.currentgrade = 2 THEN
            :NEW.secondstdnum := :NEW.currentgrade * 10000 + 
                                :NEW.currentclass * 100 + 
                                :NEW.currentnum;
        ELSIF :NEW.currentgrade = 3 THEN
            :NEW.thirdstdnum := :NEW.currentgrade * 10000 + 
                                :NEW.currentclass * 100 + 
                                :NEW.currentnum;
        END IF;
    END IF;
END;