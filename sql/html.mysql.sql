CREATE DATABASE IF NOT EXISTS `hstestdb`;
USE `hstestdb`;

CREATE USER `hsdb`@`%` IDENTIFIED BY 'hsdbpass';
GRANT ALL ON `hstestdb`.* TO `hsdb`@`%`;
FLUSH PRIVILEGES;

DROP TABLE IF EXISTS HTML;

CREATE TABLE `hstestdb`.`HTML` (
    `uuid` CHAR(36) NOT NULL,
    `content` TEXT NULL,
    PRIMARY KEY (`uuid`)
);

INSERT INTO HTML (uuid, content) VALUES
  ('550e8400-e29b-41d4-a716-446655440000', 'Sample content 1'),
  ('550e8400-e29b-41d4-a716-446655440001', 'Sample content 2');
