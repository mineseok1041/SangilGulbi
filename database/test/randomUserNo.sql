-- 교차 배치를 위한 목표 no 순서:
-- 12: 학생, 13: 선생님, 14: 학생, 15: 선생님, ...
UPDATE users SET no = 1001 WHERE no = 12;
UPDATE users SET no = 12 WHERE no = 32;

UPDATE users SET no = 1002 WHERE no = 14;
UPDATE users SET no = 14 WHERE no = 34;

UPDATE users SET no = 1003 WHERE no = 16;
UPDATE users SET no = 16 WHERE no = 36;

UPDATE users SET no = 1004 WHERE no = 18;
UPDATE users SET no = 18 WHERE no = 38;

UPDATE users SET no = 1005 WHERE no = 20;
UPDATE users SET no = 20 WHERE no = 40;

UPDATE users SET no = 1006 WHERE no = 22;
UPDATE users SET no = 22 WHERE no = 42;

UPDATE users SET no = 1007 WHERE no = 24;
UPDATE users SET no = 24 WHERE no = 44;

UPDATE users SET no = 1008 WHERE no = 26;
UPDATE users SET no = 26 WHERE no = 46;

UPDATE users SET no = 1009 WHERE no = 28;
UPDATE users SET no = 28 WHERE no = 48;

UPDATE users SET no = 1010 WHERE no = 30;
UPDATE users SET no = 30 WHERE no = 50;

UPDATE users SET no = 32 WHERE no = 1001;
UPDATE users SET no = 34 WHERE no = 1002;
UPDATE users SET no = 36 WHERE no = 1003;
UPDATE users SET no = 38 WHERE no = 1004;
UPDATE users SET no = 40 WHERE no = 1005;
UPDATE users SET no = 42 WHERE no = 1006;
UPDATE users SET no = 44 WHERE no = 1007;
UPDATE users SET no = 46 WHERE no = 1008;
UPDATE users SET no = 48 WHERE no = 1009;
UPDATE users SET no = 50 WHERE no = 1010;

commit;