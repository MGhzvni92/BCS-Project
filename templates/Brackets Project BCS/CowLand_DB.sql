CREATE DATABASE  IF NOT EXISTS `cowLand` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cowLand`;
-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: cowLand
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

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
-- Table structure for table `GroupUser`
--

DROP TABLE IF EXISTS `GroupUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GroupUser` (
  `id` int NOT NULL,
  `groupId` int NOT NULL,
  `userId` int NOT NULL,
  `relation` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GroupUser`
--

LOCK TABLES `GroupUser` WRITE;
/*!40000 ALTER TABLE `GroupUser` DISABLE KEYS */;
/*!40000 ALTER TABLE `GroupUser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cow`
--

DROP TABLE IF EXISTS `cow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cow` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cawName` varchar(45) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `groupId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cow`
--

LOCK TABLES `cow` WRITE;
/*!40000 ALTER TABLE `cow` DISABLE KEYS */;
/*!40000 ALTER TABLE `cow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cowGroup`
--

DROP TABLE IF EXISTS `cowGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cowGroup` (
  `id` int NOT NULL,
  `type` int DEFAULT NULL,
  `cowLandId` int DEFAULT NULL,
  `cowGroupName` varchar(45) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cowGroup`
--

LOCK TABLES `cowGroup` WRITE;
/*!40000 ALTER TABLE `cowGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `cowGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cowLand`
--

DROP TABLE IF EXISTS `cowLand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cowLand` (
  `id` int NOT NULL,
  `cowLandName` varchar(45) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cowLandName_UNIQUE` (`cowLandName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cowLand`
--

LOCK TABLES `cowLand` WRITE;
/*!40000 ALTER TABLE `cowLand` DISABLE KEYS */;
/*!40000 ALTER TABLE `cowLand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cowLandUser`
--

DROP TABLE IF EXISTS `cowLandUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cowLandUser` (
  `id` int NOT NULL,
  `cowLandId` int NOT NULL,
  `userId` int NOT NULL,
  `relation` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cowLandUser`
--

LOCK TABLES `cowLandUser` WRITE;
/*!40000 ALTER TABLE `cowLandUser` DISABLE KEYS */;
/*!40000 ALTER TABLE `cowLandUser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cowState`
--

DROP TABLE IF EXISTS `cowState`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cowState` (
  `id` int NOT NULL,
  `cowId` int NOT NULL,
  `dateTime` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  `cowState` int NOT NULL,
  `description` varchar(5000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cowState`
--

LOCK TABLES `cowState` WRITE;
/*!40000 ALTER TABLE `cowState` DISABLE KEYS */;
/*!40000 ALTER TABLE `cowState` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groupState`
--

DROP TABLE IF EXISTS `groupState`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groupState` (
  `id` int NOT NULL,
  `groupId` int NOT NULL,
  `dateTime` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  `groupState` int NOT NULL,
  `description` varchar(5000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupState`
--

LOCK TABLES `groupState` WRITE;
/*!40000 ALTER TABLE `groupState` DISABLE KEYS */;
/*!40000 ALTER TABLE `groupState` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inputData`
--

DROP TABLE IF EXISTS `inputData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inputData` (
  `id` int NOT NULL,
  `dateTime` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  `type` int DEFAULT NULL,
  `sourceAddress` varchar(300) COLLATE utf8mb3_persian_ci NOT NULL,
  `cowId` int NOT NULL,
  `userId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inputData`
--

LOCK TABLES `inputData` WRITE;
/*!40000 ALTER TABLE `inputData` DISABLE KEYS */;
/*!40000 ALTER TABLE `inputData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `id` int NOT NULL,
  `dateTime` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  `content` varchar(500) COLLATE utf8mb3_persian_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userNotification`
--

DROP TABLE IF EXISTS `userNotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userNotification` (
  `id` int NOT NULL,
  `userId` int NOT NULL,
  `notificationId` int NOT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userNotification`
--

LOCK TABLES `userNotification` WRITE;
/*!40000 ALTER TABLE `userNotification` DISABLE KEYS */;
/*!40000 ALTER TABLE `userNotification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  `password` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  `access` varchar(45) COLLATE utf8mb3_persian_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-07 23:15:27
