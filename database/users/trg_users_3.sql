CREATE OR REPLACE TRIGGER trg_calc_point
BEFORE INSERT OR UPDATE ON users
FOR EACH ROW
BEGIN
    :NEW.point := NVL(:NEW.addPoint, 0) + NVL(:NEW.delPoint, 0);
END;