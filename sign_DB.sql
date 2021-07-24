
DROP TABLE user;
-- 회원가입 테이블 
CREATE TABLE user (u_id INT not null auto_increment primary key,
     id varchar(20) not null unique,
     pw varchar(20) not null,
	 name varchar(20) not null,
     email varchar(50) not null unique);
     
     
-- 회원데이터 넣을 때 써야하는 쿼리
INSERT INTO user(id, pw, name, email) VALUES ('tjsdud594', '1234@', '룬선영', 'fbtjsdud594@gmail.com');
INSERT INTO user(id, pw, name, email) VALUES ('Ryu594', '1234@', '류선영', 'dud594@gmail.com');


DROP TABLE deleteuser;
-- 회원탈퇴 테이블 형성
CREATE TABLE deleteuser (u_id INT not null auto_increment primary key,
     id varchar(20) not null unique,
     pw varchar(20) not null,
	 name varchar(20) not null,
     email varchar(50) not null unique,
     deldate DATE);
     
     
delete from user where name='룬선영';

-- 서브쿼리써서 삭제나 업데이트를 할 경우 mysql/maria는 자기자신의 테이블 데이터를 바로 사용하지 못하게 되어있으므로
-- sub_user라는 임시 테이블을 만들어 해결
delete from user where email=(
			select sub_user.email
            from (
				select email from user where id='손유진'
                ) sub_user
			);
            
            
-- 테이블 데이터확인 
select * from user;
select * from deleteuser;


DROP TRIGGER trg_deleteuser;
-- 회원탈퇴 트리거
-- 회원탈퇴할 경우 자동으로 탈퇴테이블로 추가된 후 회원테이블에서 삭제
DELIMITER //
CREATE TRIGGER trg_deleteuser
	AFTER DELETE
    ON user
    FOR EACH ROW
BEGIN
	INSERT INTO deleteuser
		VALUES (OLD.u_id, OLD.id, OLD.pw, OLD.name, OLD.email, CURDATE());
END //
DELIMITER ;


-- 구매제품 테이블 생성
CREATE TABLE product (p_id INT not null auto_increment primary key,
     p_name varchar(50) not null unique,
     p_price INT not null
     );


-- 구매 제품 정보 추가
INSERT INTO product(p_name, p_price) VALUES ('smile gru', 3000);
INSERT INTO product(p_name, p_price) VALUES ('freeze', 2000);
INSERT INTO product(p_name, p_price) VALUES ('in snow', 3500);
INSERT INTO product(p_name, p_price) VALUES ('sleepy', 1500);
INSERT INTO product(p_name, p_price) VALUES ('cherryblossom', 2500);
INSERT INTO product(p_name, p_price) VALUES ('best friend', 4000);
INSERT INTO product(p_name, p_price) VALUES ('bye', 500);


-- 주문 테이블 생성
CREATE TABLE p_order (p_no INT not null auto_increment primary key,
     p_name varchar(50) not null unique,
     p_price INT not null,
     id varchar(20) not null,
);


-- 스케줄러 사용하기
-- 이벤트 스케줄러 활성화
SET GLOBAL event_scheduler = ON;
SET @@global.event_scheduler = ON;
SET GLOBAL event_scheduler = 1;
SET @@global.event_scheduler = 1; 


-- 이벤트 등록 30초 test
CREATE Event IF NOT EXISTS del_event
ON SCHEDULE
	EVERY 30 second
    STARTS current_timestamp()
DO
	DELETE FROM deleteuser where deleteuser.deldate < now();


-- 이벤트 삭제
drop event del_event;


 
