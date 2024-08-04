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
  `dob` date DEFAULT NULL,
  `gender` char(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acc_statement`
--

LOCK TABLES `acc_statement` WRITE;
/*!40000 ALTER TABLE `acc_statement` DISABLE KEYS */;
INSERT INTO `acc_statement` VALUES ('V Sanjith','vsanjith2007@okjstbnk',3182007,'JSTBNK01','9445141655','2007-08-31 00:00:00','VSANJITH678','tn','2007-08-31',NULL),('balajisanjay','balajisanjay753@okjstbnk',5074131,'JSTBNK01','9887631087','2024-08-03 00:00:00','BALAJISA123','tn','2007-06-21',NULL),('AMAN VERMA','amanver123@okjstbnk',1234567,'JSTBNK027','9123456780','2015-01-01 00:00:00','amanver123','mh','1990-01-01','M'),('RIA SHAH','riashah456@okjstbnk',2345678,'JSTBNK013','9123456781','2016-02-02 00:00:00','riashah456','gj','1991-02-02','F'),('VIJAY PATEL','vijapat789@okjstbnk',3456789,'JSTBNK051','9123456782','2017-03-03 00:00:00','vijapat789','up','1992-03-03','M'),('NITA SINGH','nitasing012@okjstbnk',4567890,'JSTBNK027','9123456783','2018-04-04 00:00:00','nitasing012','dl','1993-04-04','F'),('RAJ MEHTA','rajmeht345@okjstbnk',5678901,'JSTBNK021','9123456784','2019-05-05 00:00:00','rajmeht345','ka','1994-05-05','M'),('KAVYA AGARWAL','kavyaga678@okjstbnk',6789012,'JSTBNK045','9123456785','2020-06-06 00:00:00','kavyaga678','tn','1995-06-06','F'),('ARJUN DESAI','arjdesa901@okjstbnk',7890123,'JSTBNK055','9123456786','2021-07-07 00:00:00','arjdesa901','wb','1996-07-07','M'),('LINA KHAN','linakha234@okjstbnk',8901234,'JSTBNK039','9123456787','2022-08-08 00:00:00','linakha234','pb','1997-08-08','F'),('ROHIT MALHOTRA','rohmala567@okjstbnk',9012345,'JSTBNK015','9123456788','2023-09-09 00:00:00','rohmala567','hr','1998-09-09','M'),('ISHA ROY','isharoy890@okjstbnk',123456,'JSTBNK025','9123456789','2024-10-10 00:00:00','isharoy890','mp','1999-10-10','F'),('RAHUL CHOPRA','rahchop123@okjstbnk',1234568,'JSTBNK041','9123456790','2015-11-11 00:00:00','rahchop123','rj','1980-11-11','M'),('TARA JAIN','tarjain456@okjstbnk',2345679,'JSTBNK002','9123456791','2016-12-12 00:00:00','tarjain456','ap','1981-12-12','F'),('VIHAN GUPTA','vihgupt789@okjstbnk',3456790,'JSTBNK023','9123456792','2017-01-13 00:00:00','vihgupt789','kl','1982-01-13','M'),('MEERA YADAV','meeraya012@okjstbnk',4567901,'JSTBNK037','9123456793','2018-02-14 00:00:00','meeraya012','or','1983-02-14','F'),('SAMAR NAIR','samnair345@okjstbnk',5679012,'JSTBNK047','9123456794','2019-03-15 00:00:00','samnair345','ts','1984-03-15','M'),('PIYA RAO','piyarao678@okjstbnk',6780123,'JSTBNK031','9123456795','2020-04-16 00:00:00','piyarao678','jk','1985-04-16','F'),('KABIR SHARMA','kabshar901@okjstbnk',7891234,'JSTBNK007','9123456796','2021-05-17 00:00:00','kabshar901','br','1986-05-17','M'),('ANVI KAPOOR','anvikap234@okjstbnk',8902345,'JSTBNK005','9123456797','2022-06-18 00:00:00','anvikap234','as','1987-06-18','F'),('RISHI SAXENA','rishsax567@okjstbnk',9013456,'JSTBNK009','9123456798','2023-07-19 00:00:00','rishsax567','ct','1988-07-19','M'),('AVNI BHATT','avnibha890@okjstbnk',124567,'JSTBNK011','9123456799','2024-08-20 00:00:00','avnibha890','go','1989-08-20','F'),('AARAV TRIPATHI','aartrip123@okjstbnk',1235678,'JSTBNK049','9123456700','2015-09-21 00:00:00','aartrip123','tr','1990-09-21','M'),('SHIVANI MITTAL','shivmit456@okjstbnk',2346789,'JSTBNK053','9123456701','2016-10-22 00:00:00','shivmit456','ut','1991-10-22','F'),('RAHUL SRIVASTAVA','rahsriv789@okjstbnk',3457890,'JSTBNK051','9123456702','2017-11-23 00:00:00','rahsriv789','up','1992-11-23','M'),('ANIKA GARG','anikgarg012@okjstbnk',4568901,'JSTBNK027','9123456703','2018-12-24 00:00:00','anikgarg012','mh','1993-12-24','F'),('RAJESH PRASAD','rajpras345@okjstbnk',5679013,'JSTBNK021','9123456704','2019-01-25 00:00:00','rajpras345','ka','1994-01-25','M'),('PRIYA MISHRA','priyamis678@okjstbnk',6780124,'JSTBNK013','9123456705','2020-02-26 00:00:00','priyamis678','gj','1995-02-26','F'),('AMIT RATHORE','amirat901@okjstbnk',7891235,'JSTBNK027','9123456706','2021-03-27 00:00:00','amirat901','dl','1996-03-27','M'),('SANJANA DUBEY','sandube234@okjstbnk',8902346,'JSTBNK055','9123456707','2022-04-28 00:00:00','sandube234','wb','1997-04-28','F'),('MANISH TIWARI','mantiwa567@okjstbnk',9013457,'JSTBNK039','9123456708','2023-05-29 00:00:00','mantiwa567','pb','1998-05-29','M'),('REENA BANSAL','reebans890@okjstbnk',124568,'JSTBNK045','9123456709','2024-06-30 00:00:00','reebans890','tn','1999-06-30','F'),('SURESH KAUR','surkaur123@okjstbnk',1235679,'JSTBNK025','9123456710','2015-07-31 00:00:00','surkaur123','mp','1980-07-31','M'),('NIDHI AHUJA','nidiahu456@okjstbnk',2346780,'JSTBNK041','9123456711','2016-08-01 00:00:00','nidiahu456','rj','1981-08-01','F');
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
INSERT INTO `login_details` VALUES ('AARAV','TRIPATHI','tr','9123456700','1990-09-21','Pas$word9','M','aartrip123'),('AMAN','SHAH','go','9123456720','1990-05-10','Pas$word9','M','amansha123'),('AMAN','VERMA','mh','9123456780','1990-01-01','Password1!','M','amanver123'),('AMIT','RATHORE','dl','9123456706','1996-03-27','P@ssW0rd5','M','amirat901'),('ANIKA','GARG','mh','9123456703','1993-12-24','P@$$word3','F','anikgarg012'),('ANU','SEN','kl','9123456713','1983-10-03','P@$$word2','F','anusen012'),('ANVI','KAPOOR','as','9123456797','1987-06-18','Pa$$word6','F','anvikap234'),('ARJUN','DESAI','wb','9123456786','1996-07-07','Pas$word6','M','arjdesa901'),('ARJUN','KHAN','dl','9123456726','1996-11-16','Pas$word4','M','arjkhan901'),('AVNI','BHATT','go','9123456799','1989-08-20','P@ssword8','F','avnibha890'),('BALAJI','SANJAY','tn','6380809232','2007-06-21','Balaji123.','M','BALAJISA123'),('BENJAMIN','GRAHAM','tn','8765432136','1932-07-17','Benjamin123.','M','benjami483'),('D','VALARMATHY','tn','9444514164','2001-08-31','Va1.','F','dvalarm105'),('ISHA','ROY','mp','9123456789','1999-10-10','P@ssword8','F','isharoy890'),('JOSEPH','VIJAY','tn','9775162922','1972-05-14','Joseph123.','M','josephv221'),('KABIR','SHARMA','br','9123456796','1986-05-17','P@ssW0rd5','M','kabshar901'),('KAVYA','DESAI','gj','9123456725','1995-10-15','P@$$word3','F','kavdes678'),('KAVYA','AGARWAL','tn','9123456785','1995-06-06','P@$$word5','F','kavyaga678'),('LINA','KHAN','pb','9123456787','1997-08-08','Passw0rd!','F','linakha234'),('LINA','MALHOTRA','wb','9123456727','1997-12-17','Passw0rd!','F','linamalhotra111'),('MANISH','TIWARI','pb','9123456708','1998-05-29','P@ssword7','M','mantiwa567'),('MEERA','YADAV','or','9123456793','1983-02-14','P@$$word2','F','meeraya012'),('NEHA','VERMA','ct','9123456719','1989-04-09','P@ssword8','F','nehverm890'),('NIDHI','AHUJA','rj','9123456711','1981-08-01','Passw0rd!','F','nidiahu456'),('NITA','SINGH','dl','9123456783','1993-04-04','Passw0rd!','F','nitasing012'),('NITA','MEHTA','mh','9123456723','1993-08-13','Passw0rd!','F','nitmeht012'),('N','VIJAYAKUMAR','tn','9556514514','1992-02-26','Vijayakumar123.','M','nvijaya301'),('PIYA','RAO','jk','9123456795','1985-04-16','P@ssword4','F','piyarao678'),('PRIYA','MISHRA','gj','9123456705','1995-02-26','Passw0rd!','F','priyamis678'),('PRIYA','JHA','ts','9123456715','1985-12-05','Passw0rd!','F','priyjha678'),('RAHUL','CHOPRA','rj','9123456790','1980-11-11','Pa$$word9','M','rahchop123'),('RAHUL','NAIK','as','9123456718','1988-03-08','P@ssword7','M','rahnaik567'),('RAHUL','SRIVASTAVA','up','9123456702','1992-11-23','P@ssW0rd2','M','rahsriv789'),('RAJ','AGARWAL','ka','9123456724','1994-09-14','P@ssW0rd2','M','rajagar345'),('RAJEEV','BAJAJ','ap','9123456712','1982-09-02','P@ssW0rd1','M','rajbaja789'),('RAJ','MEHTA','ka','9123456784','1994-05-05','P@ssW0rd4','M','rajmeht345'),('RAJESH','PRASAD','ka','9123456704','1994-01-25','Pas$word4','M','rajpras345'),('RAMESH','ROY','or','9123456714','1984-11-04','Pas$word3','M','ramroy345'),('REENA','BANSAL','tn','9123456709','1999-06-30','P@ssword8','F','reebans890'),('RIA','PATEL','tr','9123456721','1991-06-11','P@ssW0rd0','F','riapata456'),('RIA','SHAH','gj','9123456781','1991-02-02','P@ssword2','F','riashah456'),('RISHI','SAXENA','ct','9123456798','1988-07-19','P@ssword7','M','rishsax567'),('ROHIT','MALHOTRA','hr','9123456788','1998-09-09','P@ssW0rd7','M','rohmala567'),('SAMAR','NAIR','ts','9123456794','1984-03-15','Pas$word3','M','samnair345'),('SANJANA','DUBEY','wb','9123456707','1997-04-28','Pa$$word6','F','sandube234'),('SANJAY','RATHOD','jk','9123456716','1986-01-06','P@ssW0rd5','M','sanrath901'),('SHIVANI','MITTAL','ut','9123456701','1991-10-22','Passw0rd!','F','shivmit456'),('SONA','SHETTY','br','9123456717','1987-02-07','Pa$$word6','F','sonshe234'),('SURESH','KAUR','mp','9123456710','1980-07-31','Pas$word9','M','surkaur123'),('TARA','JAIN','ap','9123456791','1981-12-12','P@ssword0','F','tarjain456'),('VIHAN','GUPTA','kl','9123456792','1982-01-13','P@ssW0rd1','M','vihgupt789'),('VIJAY','PATEL','up','9123456782','1992-03-03','Pa$$word3','M','vijapat789'),('VIJAY','SINGH','ut','9123456722','1992-07-12','Pa$$word1','M','vijasing789'),('V','SANJITH','tn','9444149729','2008-08-31','Sanjith123.','M','vsanjit926'),('V','SANJITH','tn','9445141604','2007-08-31','Sanjith123.','M','VSANJITH678');
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

-- Dump completed on 2024-08-04 10:54:16
