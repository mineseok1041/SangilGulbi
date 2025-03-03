-- filepath: /c:/Users/Ace/Desktop/개발/workspace/공지사항/database/notice/set_table_notice.sql
CREATE TABLE notice (
    id NUMBER PRIMARY KEY,
    title VARCHAR2(255) NOT NULL,
    content CLOB NOT NULL,
    author VARCHAR2(50) NOT NULL,
    created_date VARCHAR2(17) DEFAULT TO_CHAR(SYSDATE, 'YYYYMMDD HH24:MI:SS'),
    updated_date VARCHAR2(17)
);

CREATE SEQUENCE seq_notice_id
    START WITH 1
    INCREMENT BY 1
    NOORDER;