CREATE TABLE DEPT
 (DEPTNO NUMBER(2) CONSTRAINT PK_DEPT PRIMARY KEY,
  DNAME VARCHAR2(14) ,
  LOC VARCHAR2(13));

SELECT * FROM DEPT;

CREATE OR REPLACE PROCEDURE INSERT_DEPT
( VDEPTNO IN 	DEPT.DEPTNO%TYPE,
  VDNAME IN DEPT.DNAME%TYPE,
  VLOC IN DEPT.LOC%TYPE
)
IS
BEGIN
  INSERT INTO DEPT
  VALUES(VDEPTNO, VDNAME, VLOC);
END;
/

BEGIN
	INSERT_DEPT(99, '영업','목포');
END;

SELECT * FROM DEPT;


CREATE TABLE BLOBTABLE(
	USERID CHAR(15) NOT NULL PRIMARY KEY,
	FILENAME VARCHAR2(1000),
	FILECONTENT BLOB);

SELECT * FROM BLOBTABLE;

