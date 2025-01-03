-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: Bank_Management
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

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
-- Table structure for table `acc_details`
--

DROP TABLE IF EXISTS `acc_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acc_details` (
  `cu_name` varchar(30) NOT NULL,
  `upi_id` varchar(30) DEFAULT NULL,
  `acc_no` int NOT NULL,
  `Ifsc` varchar(10) NOT NULL,
  `Date_of_opening` datetime NOT NULL,
  `uid` varchar(20) DEFAULT NULL,
  `state` varchar(3) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` char(2) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acc_details`
--

LOCK TABLES `acc_details` WRITE;
/*!40000 ALTER TABLE `acc_details` DISABLE KEYS */;
INSERT INTO `acc_details` VALUES ('D VALARMATHY','valarmathy764@okjstbnk',1854993,'JSTBNK02','2024-08-14 00:00:00','DVALARM243','tn','2007-08-31','F','Valarmathy123.'),('sanjith','sanjith@ok',31082007,'JSTBNK01','2007-08-31 00:00:00','sanjith','tn','2007-08-31','M','sanjith'),('VIJAYAKUMAR','vijayakumar442@okjstbnk',1312930,'JSTBNK58','2024-08-15 00:00:00','VIJAYAK199','tn','2007-08-31','M','Vijayakumar123.'),('RAM SWAMY','sda319@okjstbnk',2323576,'JSTBNK01','2024-08-15 00:00:00','RAMSWAM216','tn','2021-09-21','M','Ra1.'),('VSANJITH','vsanjith.ind667@okjstbnk',8904783,'JSTBNK23','2024-09-06 00:00:00','VSANJIT913','kl','2007-08-31','M','Sanjith123.'),('VSANJITH','san@san',1000000,'JSTBNK02','2007-08-31 00:00:00','san','tn','2007-08-31','F','sanjith123.'),('V SANJITH','sanjith603@okjstbnk',4498453,'JSTBNK58','2024-09-08 00:00:00','VSANJIT602','tn','2007-08-31','M','Sanjith123.');
/*!40000 ALTER TABLE `acc_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-27 19:46:16

