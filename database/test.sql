select * from users;
select * from notice;
select * from pointLog;

drop table users;
drop SEQUENCE seq_users_no;

SELECT COUNT(*) FROM users WHERE id = 'test1' AND verified = 1;

commit;