create table pointLog (
    stdId varchar2(12),
    managerId varchar2(12),
    point number,
    reason varchar2(255),
    addDate varchar2(17) default to_char(sysdate, 'YYYYMMDD HH24:MI:SS'),
    foreign key (stdId) references users(id),
    foreign key (managerId) references users(id)
);