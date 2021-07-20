-- 회원가입 테이블 

CREATE TABLE user (u_id INT not null auto_increment primary key,
     id varchar(20) not null unique,
     pw varchar(20) not null,
	 name varchar(20) not null,
     email varchar(50) not null unique);
     
     
-- 회원데이터 넣을 때 써야하는 쿼리
INSERT INTO user(id, pw, name, email) VALUES ('tjsdud594', '1234@', '룬선영', 'fbtjsdud594@gmail.com');
INSERT INTO user(id, pw, name, email) VALUES ('Ryu594', '1234@', '류선영', 'dud594@gmail.com');

-- 회원탈퇴 티이블 형성alter

delete from user where name='룬선영';
delete from user where name='류선영';
select * from user;
 