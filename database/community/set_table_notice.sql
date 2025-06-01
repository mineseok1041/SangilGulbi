CREATE TABLE notice (
    id NUMBER PRIMARY KEY,
    title VARCHAR2(255) NOT NULL,
    content CLOB NOT NULL,
    author VARCHAR2(50) NOT NULL,
    created_date VARCHAR2(17) DEFAULT TO_CHAR(SYSDATE, 'YYYY/MM/DD'),
    created_time VARCHAR2(17) DEFAULT TO_CHAR(SYSDATE, 'HH24:MI:SS'),
    updated_date VARCHAR2(17),
    updated_time VARCHAR2(17)
);