use cardb;

DROP TABLE IF EXISTS car_data;
DROP TABLE IF EXISTS car_total;
DROP TABLE IF EXISTS car_region;
DROP TABLE IF EXISTS car_type;
DROP TABLE IF EXISTS race_type;
DROP TABLE IF EXISTS car_monthly;
DROP TABLE IF EXISTS faq_kia;

CREATE TABLE car_region (
    region_id INT NOT NULL AUTO_INCREMENT,
    sido_name VARCHAR(50) NOT NULL,
    sigungu_name VARCHAR(50) NULL,
    PRIMARY KEY (region_id)
) ENGINE = INNODB;


CREATE TABLE car_type (
    type_id INT NOT NULL AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (type_id)
) ENGINE = INNODB;


CREATE TABLE race_type (
    race_id INT NOT NULL AUTO_INCREMENT,
    race_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (race_id)
) ENGINE = INNODB;


CREATE TABLE car_monthly (
    monthly_id INT NOT NULL AUTO_INCREMENT,
    month_year VARCHAR(7) NOT NULL,
    PRIMARY KEY (monthly_id)
) ENGINE = INNODB;


CREATE TABLE car_data (
    data_id INT NOT NULL AUTO_INCREMENT,
    region_id INT NOT NULL,
    type_id INT NOT NULL,
    race_id INT NOT NULL,
    monthly_id INT NOT NULL,
    vehicle_count INT NOT NULL,
    PRIMARY KEY (data_id),
    FOREIGN KEY (region_id) REFERENCES car_region(region_id),
    FOREIGN KEY (type_id) REFERENCES car_type(type_id),
    FOREIGN KEY (race_id) REFERENCES race_type(race_id),
    FOREIGN KEY (monthly_id) REFERENCES car_monthly(monthly_id)
) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS faq_kia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    answer TEXT
) ENGINE = INNODB;

insert into car_type(type_name) values 
	('승용'),
    ('승합'),
    ('화물'),
    ('특수');
    
insert into race_type(race_name) values 
	('관용'),
    ('자가용'),
    ('영업용');
commit;

select * from car_monthly;
select * from car_region;
select * from car_data;
select * from race_type;

SELECT m.month_year AS 월, r.sido_name AS 시도명, r.sigungu_name AS 시군구, 
       t.type_name AS 차량유형, rc.race_name AS 사용유형, d.vehicle_count AS 차량수
FROM car_data d
left JOIN car_monthly m ON d.monthly_id = m.monthly_id
left JOIN car_region r ON d.region_id = r.region_id
left JOIN car_type t ON d.type_id = t.type_id
left JOIN race_type rc ON d.race_id = rc.race_id
WHERE 1 = 1 
  AND m.month_year = '2024-12' 
  AND r.sido_name IN ('서울', '부산')
  AND t.type_name IN ('승용');