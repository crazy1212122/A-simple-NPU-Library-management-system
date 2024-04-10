-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: npulib
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `book_manager`
--

DROP TABLE IF EXISTS `book_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_manager` (
  `ID` char(10) NOT NULL,
  `姓名` varchar(20) DEFAULT NULL,
  `password` char(10) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_manager`
--

LOCK TABLES `book_manager` WRITE;
/*!40000 ALTER TABLE `book_manager` DISABLE KEYS */;
INSERT INTO `book_manager` VALUES ('5001','王五','123456');
/*!40000 ALTER TABLE `book_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `ISBN号` char(15) NOT NULL,
  `书名` varchar(20) DEFAULT NULL,
  `作者` varchar(20) DEFAULT NULL,
  `书籍类别` varchar(15) DEFAULT NULL,
  `出版社` varchar(30) DEFAULT NULL,
  `被借次数` int DEFAULT NULL,
  `馆藏册数` int DEFAULT NULL,
  `在馆册数` int DEFAULT NULL,
  `书架号` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`ISBN号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('987654321','数据库系统概论','王珊 杜小勇 陈红','计算机技术','高等教育出版社',12,20,15,'C01'),('987654322','计算机网络原理','谢希仁','计算机技术','电子工业出版社',2,15,15,'C01'),('987654323','巴黎圣母院','雨果','经典文学','译林出版社',5,10,15,'W01'),('987654324','数字信号处理','高西平','电子信息','西安电子科技大学出版社',15,20,15,'E01'),('987654325','马克思主义基本原理','编写组','思想政治','高等教育出版社',15,20,15,'Z01');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookshelf`
--

DROP TABLE IF EXISTS `bookshelf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookshelf` (
  `书架号` char(5) NOT NULL,
  `图书类别` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`书架号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookshelf`
--

LOCK TABLES `bookshelf` WRITE;
/*!40000 ALTER TABLE `bookshelf` DISABLE KEYS */;
INSERT INTO `bookshelf` VALUES ('C01','计算机技术'),('E01','电子信息'),('W01','经典文学'),('Z01','思想政治');
/*!40000 ALTER TABLE `bookshelf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrow_record`
--

DROP TABLE IF EXISTS `borrow_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow_record` (
  `ISBN` char(15) NOT NULL,
  `读者ID` varchar(10) NOT NULL,
  `借书时间` date NOT NULL,
  `归还日期` date NOT NULL,
  PRIMARY KEY (`ISBN`,`读者ID`,`借书时间`,`归还日期`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_record`
--

LOCK TABLES `borrow_record` WRITE;
/*!40000 ALTER TABLE `borrow_record` DISABLE KEYS */;
INSERT INTO `borrow_record` VALUES ('987654321','0001','2023-11-11','2023-11-11');
/*!40000 ALTER TABLE `borrow_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `ISBN` varchar(10) NOT NULL,
  `ID` varchar(10) NOT NULL,
  `借书时间` date NOT NULL,
  `还书时间` date NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`ISBN`,`ID`,`借书时间`,`还书时间`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES ('987654321','0001','2023-01-01','2023-12-12','borrow'),('987654321','0001','2023-11-11','2023-11-11','borrow'),('987654321','1','2023-12-02','2023-12-02','return'),('987654322','0001','2023-01-01','2023-12-12','borrow'),('987654325','0001','2023-10-10','2023-11-11','borrow');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_record`
--

DROP TABLE IF EXISTS `login_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_record` (
  `ID号` char(10) NOT NULL,
  `日期` date NOT NULL,
  `单日登录次数` int NOT NULL,
  PRIMARY KEY (`ID号`,`日期`,`单日登录次数`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_record`
--

LOCK TABLES `login_record` WRITE;
/*!40000 ALTER TABLE `login_record` DISABLE KEYS */;
INSERT INTO `login_record` VALUES ('1','2023-12-02',1),('1','2023-12-03',1),('1','2023-12-03',2),('1001','2023-12-02',2),('1001','2023-12-02',3),('1001','2023-12-02',4),('1001','2023-12-02',5),('1001','2023-12-02',6),('1001','2023-12-02',7),('1001','2023-12-02',8),('1001','2023-12-02',9),('1001','2023-12-02',10),('1001','2023-12-02',11);
/*!40000 ALTER TABLE `login_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reader`
--

DROP TABLE IF EXISTS `reader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reader` (
  `ID号` varchar(10) NOT NULL,
  `姓名` varchar(20) DEFAULT NULL,
  `学院` varchar(20) DEFAULT NULL,
  `性别` varchar(5) DEFAULT NULL,
  `读者类型` varchar(20) DEFAULT NULL,
  `电话` char(10) DEFAULT NULL,
  `可借册数` int DEFAULT NULL,
  `信用级别` int DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reader`
--

LOCK TABLES `reader` WRITE;
/*!40000 ALTER TABLE `reader` DISABLE KEYS */;
INSERT INTO `reader` VALUES ('0001','小沈','教育实验学院','男','本科生','1815647',20,2,'123456'),('0002','小张','教育实验学院','男','本科生','1815648',20,2,'123456'),('0003','小赵','教育实验学院','男','本科生','1815678',20,2,'123456'),('0101','小薛','计算机学院','男','研究生','18147678',25,2,'123456'),('1001','李老师','计算机学院','女','教授','18147678',30,2,'123456');
/*!40000 ALTER TABLE `reader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `return_record`
--

DROP TABLE IF EXISTS `return_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `return_record` (
  `ISBN` char(10) NOT NULL,
  `读者ID` varchar(15) NOT NULL,
  `借书时间` date NOT NULL,
  `归还时间` date NOT NULL,
  PRIMARY KEY (`ISBN`,`读者ID`,`借书时间`,`归还时间`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `return_record`
--

LOCK TABLES `return_record` WRITE;
/*!40000 ALTER TABLE `return_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `return_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03  0:09:54
