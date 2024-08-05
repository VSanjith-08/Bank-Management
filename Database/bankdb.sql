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
  `mobileno` char(10) NOT NULL,
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
INSERT INTO `login_details` VALUES ('AARAV','TRIPATHI','9123456700','Pas$word9','M','aartrip123'),('AMAN','SHAH','9123456720','Pas$word9','M','amansha123'),('AMAN','VERMA','9123456780','Password1!','M','amanver123'),('AMIT','RATHORE','9123456706','P@ssW0rd5','M','amirat901'),('ANIKA','GARG','9123456703','P@$$word3','F','anikgarg012'),('ANU','SEN','9123456713','P@$$word2','F','anusen012'),('ANVI','KAPOOR','9123456797','Pa$$word6','F','anvikap234'),('ARJUN','DESAI','9123456786','Pas$word6','M','arjdesa901'),('ARJUN','KHAN','9123456726','Pas$word4','M','arjkhan901'),('AVNI','BHATT','9123456799','P@ssword8','F','avnibha890'),('BALAJI','SANJAY','9218332345','Balaji123.','M','balajis345'),('BALAJI','SANJAY','6380809232','Balaji123.','M','BALAJISA123'),('BENJAMIN','GRAHAM','8765432136','Benjamin123.','M','benjami483'),('DHAS','','9885141644','Dhas123.','M','dhas988'),('D','VALARMATHY','9444514164','Va1.','F','dvalarm105'),('HRUSHIKESH','SENAPATY','9665112020','Senapathy123.','M','hrushik682'),('ISHA','ROY','9123456789','P@ssword8','F','isharoy890'),('JOSEPH','VIJAY','9775162922','Joseph123.','M','josephv221'),('KABIR','SHARMA','9123456796','P@ssW0rd5','M','kabshar901'),('KAVYA','DESAI','9123456725','P@$$word3','F','kavdes678'),('KAVYA','AGARWAL','9123456785','P@$$word5','F','kavyaga678'),('LINA','KHAN','9123456787','Passw0rd!','F','linakha234'),('LINA','MALHOTRA','9123456727','Passw0rd!','F','linamalhotra111'),('MANISH','TIWARI','9123456708','P@ssword7','M','mantiwa567'),('MEERA','YADAV','9123456793','P@$$word2','F','meeraya012'),('M','LAKSHITH','9263331087','Lakshit123.','M','mlakshi657'),('NEHA','VERMA','9123456719','P@ssword8','F','nehverm890'),('NIDHI','AHUJA','9123456711','Passw0rd!','F','nidiahu456'),('NITA','SINGH','9123456783','Passw0rd!','F','nitasing012'),('NITA','MEHTA','9123456723','Passw0rd!','F','nitmeht012'),('N','VIJAYAKUMAR','9556514514','Vijayakumar123.','M','nvijaya301'),('PIYA','RAO','9123456795','P@ssword4','F','piyarao678'),('PRIYA','MISHRA','9123456705','Passw0rd!','F','priyamis678'),('PRIYA','JHA','9123456715','Passw0rd!','F','priyjha678'),('RAHUL','CHOPRA','9123456790','Pa$$word9','M','rahchop123'),('RAHUL','NAIK','9123456718','P@ssword7','M','rahnaik567'),('RAHUL','SRIVASTAVA','9123456702','P@ssW0rd2','M','rahsriv789'),('RAJ','AGARWAL','9123456724','P@ssW0rd2','M','rajagar345'),('RAJEEV','BAJAJ','9123456712','P@ssW0rd1','M','rajbaja789'),('RAJ','MEHTA','9123456784','P@ssW0rd4','M','rajmeht345'),('RAJESH','PRASAD','9123456704','Pas$word4','M','rajpras345'),('RAMESH','ROY','9123456714','Pas$word3','M','ramroy345'),('REENA','BANSAL','9123456709','P@ssword8','F','reebans890'),('RIA','PATEL','9123456721','P@ssW0rd0','F','riapata456'),('RIA','SHAH','9123456781','P@ssword2','F','riashah456'),('RISHI','SAXENA','9123456798','P@ssword7','M','rishsax567'),('ROHIT','MALHOTRA','9123456788','P@ssW0rd7','M','rohmala567'),('SAMAR','NAIR','9123456794','Pas$word3','M','samnair345'),('SANJANA','DUBEY','9123456707','Pa$$word6','F','sandube234'),('SANJAY','RATHOD','9123456716','P@ssW0rd5','M','sanrath901'),('SHIVANI','MITTAL','9123456701','Passw0rd!','F','shivmit456'),('SONA','SHETTY','9123456717','Pa$$word6','F','sonshe234'),('SURESH','KAUR','9123456710','Pas$word9','M','surkaur123'),('TARA','JAIN','9123456791','P@ssword0','F','tarjain456'),('VIHAN','GUPTA','9123456792','P@ssW0rd1','M','vihgupt789'),('VIJAY','PATEL','9123456782','Pa$$word3','M','vijapat789'),('VIJAY','SINGH','9123456722','Pa$$word1','M','vijasing789'),('V','SANJITH','9444149729','Sanjith123.','M','vsanjit926'),('V','SANJITH','9445141604','Sanjith123.','M','VSANJITH678');
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

-- Dump completed on 2024-08-05 19:55:00
