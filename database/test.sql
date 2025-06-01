select * from users;
select * from pointLog;
select * from notice;
select * from pointReason;

drop table users;
drop table pointLog;
drop table notice;
drop SEQUENCE seq_users_no;
drop SEQUENCE seq_pointLog_no;
drop SEQUENCE seq_notice_id;

--다 승인시키는거
update users set verified=1 where verified=0;