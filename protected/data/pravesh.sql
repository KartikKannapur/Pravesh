DROP DATABASE IF EXISTS `pravesh_web`;

CREATE DATABASE IF NOT EXISTS pravesh_web;
USE pravesh_web;

DROP TABLE IF EXISTS `tbl_technology`;

CREATE TABLE IF NOT EXISTS `tbl_technology` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `technology` VARCHAR(255) NULL,
  PRIMARY KEY(`id`));


DROP TABLE IF EXISTS `tbl_event`;

CREATE TABLE IF NOT EXISTS `tbl_event` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `event_date` VARCHAR(255) NOT NULL,
  `venue` VARCHAR(255) NOT NULL,
  `type` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `technology_id` VARCHAR(2048) NOT NULL,
  `googlePlusLink` VARCHAR(255) NULL,
  `event_points` INT NULL,
  `dev_registered` VARCHAR(2048) NULL,
  `dev_attended` VARCHAR(2048) NULL,
  PRIMARY KEY (`id`));

DROP TABLE IF EXISTS `tbl_developer`;

CREATE TABLE IF NOT EXISTS `tbl_developer` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(45) NOT NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `phone` INT NOT NULL,
  `sex` VARCHAR(45) NOT NULL,
  `technology_id` VARCHAR(2048) NULL,
  `event_id` VARCHAR(2048) NULL,  
  `total_points` INT NULL,
  PRIMARY KEY (`id`));

DROP TABLE IF EXISTS `tbl_developerPoints`;

CREATE TABLE IF NOT EXISTS `tbl_developerPoints` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `developer_id` INT NOT NULL,
  `android` INT NULL,
  `chrome` INT NULL,
  `polymer` INT NULL,
  `cloud` INT NULL,
  `uxui` INT NULL,
  PRIMARY KEY (`id`), 
  CONSTRAINT `fk_tbl_developer_id`
    FOREIGN KEY (`id`)
    REFERENCES `tbl_developer` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);
