CREATE TABLESPACE forSangil
        DATAFILE 'database\SANGILDB.DBF'
        SIZE 100M
        AUTOEXTEND ON NEXT 10M
        MAXSIZE UNLIMITED;

alter user sangil default tablespace forSangil;