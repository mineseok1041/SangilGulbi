select * from student;

insert into student (id, password, name) values ('test1', 'test1', 'testname1');

insert into student (id, password, name) values ('test2', 'test2', 'testname2');

update student 
set currentgrade = 1, currentclass = 3, currentnum = 6 
where id = 'test1';

delete from student where id = 'test1';

SELECT SEQ_STUDENT_ID.CURRVAL FROM DUAL; 

commit;
