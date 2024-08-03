-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: localhost    Database: Bank_Management
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.22.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acc_statement`
--

DROP TABLE IF EXISTS `acc_statement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acc_statement` (
  `cu_name` varchar(30) NOT NULL,
  `upi_id` varchar(30) DEFAULT NULL,
  `acc_no` int NOT NULL,
  `Ifsc` varchar(10) NOT NULL,
  `mobile_no` varchar(11) DEFAULT NULL,
  `Date_of_opening` datetime NOT NULL,
  `uid` varchar(20) DEFAULT NULL,
  `state` varchar(3) DEFAULT NULL,
  `dob` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acc_statement`
--

LOCK TABLES `acc_statement` WRITE;
/*!40000 ALTER TABLE `acc_statement` DISABLE KEYS */;
INSERT INTO `acc_statement` VALUES ('V Sanjith','vsanjith2007@okjstbnk',3182007,'JSTBNK01','9445141655','2007-08-31 00:00:00','VSANJITH678','tn','2007-08-31'),('balajisanjay','balajisanjay753@okjstbnk',5074131,'JSTBNK01','9887631087','2024-08-03 00:00:00','BALAJISA123','tn','2007-06-21'),('V SANJITH','sanjith.ind971@okjstbnk',5431392,'JSTBNK02','9444149729','2024-08-03 00:00:00','vsanjit926','tn','2008-08-31');
/*!40000 ALTER TABLE `acc_statement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_details`
--

DROP TABLE IF EXISTS `login_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_details` (
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `mobileno` char(10) NOT NULL,
  `dob` date DEFAULT NULL,
  `passwd` varchar(100) NOT NULL,
  `gender` char(2) NOT NULL,
  `uid` varchar(20) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_details`
--

LOCK TABLES `login_details` WRITE;
/*!40000 ALTER TABLE `login_details` DISABLE KEYS */;
INSERT INTO `login_details` VALUES ('BALAJI','SANJAY','tn','6380809232','2007-06-21','Balaji123.','M','BALAJISA123'),('D','VALARMATHY','tn','9444514164','2001-08-31','Va1.','F','dvalarm105'),('JOSEPH','VIJAY','tn','9775162922','1972-05-14','Joseph123.','M','josephv221'),('N','VIJAYAKUMAR','tn','9556514514','1992-02-26','Vijayakumar123.','M','nvijaya301'),('V','SANJITH','tn','9444149729','2008-08-31','Sanjith123.','M','vsanjit926'),('V','SANJITH','tn','9445141604','2007-08-31','Sanjith123.','M','VSANJITH678');
/*!40000 ALTER TABLE `login_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-03 23:36:36
