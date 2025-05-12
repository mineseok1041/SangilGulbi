CREATE TABLE pointReason (
    no NUMBER(3) PRIMARY KEY,
    reason VARCHAR2(255),
    value NUMBER(3),
    type VARCHAR2(10) CHECK (type IN ('bonus', 'penalty'))
);
