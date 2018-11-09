CREATE DATABASE IF NOT EXISTS RAWLS;

Use RAWLS;

CREATE USER IF NOT EXISTS 'test_user'@'localhost' IDENTIFIED BY 'test_123456';
GRANT ALL PRIVILEGES ON RAWLS.* TO 'test_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'test_user'@'localhost';

/*CREATE TABLE User (
    user_ID INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    user_email VARCHAR(50) NOT NULL,
    user_password VARCHAR(20) NOT NULL,
    PRIMARY KEY (user_ID)
)ENGINE=INNODB;

CREATE TABLE Devices (
    user_ID INT,
    device_SN VARCHAR(100) NOT NULL PRIMARY KEY,
    device_brand VARCHAR(100),
    FOREIGN KEY (user_ID)
        REFERENCES user (user_ID)
        ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE Permissions (
    device_SN VARCHAR(100),
    gender BOOLEAN,
    age BOOLEAN,
    height BOOLEAN,
    weight BOOLEAN,
    heart_rate BOOLEAN,
    sleeping_cycle BOOLEAN,
    activity_frequency BOOLEAN,
    FOREIGN KEY (device_SN)
        REFERENCES devices (device_SN)
        ON DELETE CASCADE ON UPDATE CASCADE
)  ENGINE=INNODB;*/
