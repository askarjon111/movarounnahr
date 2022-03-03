-- MySQL dump 10.13  Distrib 5.7.34, for Linux (x86_64)
--
-- Host: localhost    Database: mcrm
-- ------------------------------------------------------
-- Server version	5.7.34-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_account`
--

DROP TABLE IF EXISTS `account_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_director` tinyint(1) NOT NULL,
  `token` varchar(200) DEFAULT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `is_callcenter` tinyint(1) NOT NULL,
  `filial_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `account_account_company_id_27b63eb2_fk_account_company_id` (`company_id`),
  KEY `account_account_filial_id_a0323344_fk_account_filial_id` (`filial_id`),
  CONSTRAINT `account_account_company_id_27b63eb2_fk_account_company_id` FOREIGN KEY (`company_id`) REFERENCES `account_company` (`id`),
  CONSTRAINT `account_account_filial_id_a0323344_fk_account_filial_id` FOREIGN KEY (`filial_id`) REFERENCES `account_filial` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_account`
--

LOCK TABLES `account_account` WRITE;
/*!40000 ALTER TABLE `account_account` DISABLE KEYS */;
INSERT INTO `account_account` VALUES (1,'pbkdf2_sha256$216000$D0eWo6YvWKkU$wgTgQ/bARkln+K6ok34v1yGukpxPCBB7c2vZDR0PjPk=','2021-06-16 12:01:17.991576',1,'movarounnahr','Akromjon','','',1,1,'2021-04-21 09:57:04.000000',1,NULL,NULL,1,0,NULL),(3,'pbkdf2_sha256$216000$ROhOchpN6IQ2$oVu2zUSQRnJy7BpRg/LL4beC3mwJws8UfhcvJWRJZk8=','2021-06-16 11:59:37.589111',0,'yangibozor','','','',0,1,'2021-04-24 08:44:35.000000',0,NULL,NULL,1,0,1),(4,'pbkdf2_sha256$216000$SfaZJCDDbV1O$rcBsF3kGt4T4I/+r53SBq+rYPRyqVM3X2t2ufe8eNhU=','2021-06-15 17:35:08.535327',0,'eskishahar','','','',0,1,'2021-04-24 08:44:56.000000',0,NULL,NULL,1,0,2),(7,'pbkdf2_sha256$216000$2C2kwgGFdvpG$lDCaubT0ZxaHmK8lva6tuyiFIwO//teLYSVggkct0C4=','2021-06-15 17:13:48.383519',0,'letniy','','','',0,1,'2021-06-04 11:43:48.000000',0,NULL,NULL,1,0,3),(8,'pbkdf2_sha256$216000$2bTvdXxu4xfr$10bRwVW0v2p4udtepQNf6uoiBr038Woi2dxF4ln8Z/M=','2021-06-15 16:37:31.456038',0,'nodira2000','Nodira','','',0,1,'2021-06-15 15:50:43.000000',0,NULL,NULL,1,1,NULL),(9,'pbkdf2_sha256$216000$Df48WbV17Pdw$Azujp2dNs4aUH49EXDM4H9jLUNAf4a+aSMQRqEfhgQw=','2021-06-15 17:07:33.472590',0,'shahnoza','Shahnoza','','',0,1,'2021-06-15 15:51:46.000000',0,NULL,NULL,1,1,NULL),(10,'pbkdf2_sha256$216000$cMOineahOzRv$5Cu34bXHNzRDBkRMB+46tBWLBeQpbmWPItWC5uyETsw=','2021-06-16 11:53:29.046081',0,'callcenter','','','',0,1,'2021-06-16 10:23:10.000000',0,NULL,NULL,1,1,NULL),(11,'pbkdf2_sha256$216000$N9I5UTGe2gY7$wGx/MtJQSOHJKwP3lvR0J190cZYsF6NiyThhJ9Rl+WU=','2021-06-16 11:02:19.889595',0,'manager','Qobiljon','','',0,1,'2021-06-16 11:00:55.000000',1,NULL,NULL,1,0,NULL),(12,'pbkdf2_sha256$216000$5sJWqK4kmnfP$PR1UrRKejckMpTkfmMH+PMCz25ZLZqoLY/gDWmk4NS0=',NULL,0,'marketolog','Marketolog','','',0,1,'2021-06-16 11:01:35.000000',1,NULL,NULL,1,0,NULL);
/*!40000 ALTER TABLE `account_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_account_groups`
--

DROP TABLE IF EXISTS `account_account_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_account_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_account_groups_account_id_group_id_33a11f43_uniq` (`account_id`,`group_id`),
  KEY `account_account_groups_group_id_31ca8e7b_fk_auth_group_id` (`group_id`),
  CONSTRAINT `account_account_groups_account_id_7aa27e9f_fk_account_account_id` FOREIGN KEY (`account_id`) REFERENCES `account_account` (`id`),
  CONSTRAINT `account_account_groups_group_id_31ca8e7b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_account_groups`
--

LOCK TABLES `account_account_groups` WRITE;
/*!40000 ALTER TABLE `account_account_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_account_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_account_user_permissions`
--

DROP TABLE IF EXISTS `account_account_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_account_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_account_user_per_account_id_permission_id_fa4fbca7_uniq` (`account_id`,`permission_id`),
  KEY `account_account_user_permission_id_e6a453ba_fk_auth_perm` (`permission_id`),
  CONSTRAINT `account_account_user_account_id_8c2c4a68_fk_account_a` FOREIGN KEY (`account_id`) REFERENCES `account_account` (`id`),
  CONSTRAINT `account_account_user_permission_id_e6a453ba_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_account_user_permissions`
--

LOCK TABLES `account_account_user_permissions` WRITE;
/*!40000 ALTER TABLE `account_account_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_account_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_company`
--

DROP TABLE IF EXISTS `account_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `manzil` varchar(255) NOT NULL,
  `max_worker_count` int(11) NOT NULL,
  `worker_count` int(11) NOT NULL,
  `creator` varchar(255) DEFAULT NULL,
  `about` longtext,
  `sms_token` longtext,
  `sms_balans` int(11) NOT NULL,
  `sms_from` varchar(255) DEFAULT NULL,
  `sms_callback_url` varchar(255) DEFAULT NULL,
  `sms_activated` tinyint(1) NOT NULL,
  `tg_token` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_company`
--

LOCK TABLES `account_company` WRITE;
/*!40000 ALTER TABLE `account_company` DISABLE KEYS */;
INSERT INTO `account_company` VALUES (1,'Movarounnahr','0','0',25,9,NULL,'0','0',0,'0','0',1,'0');
/*!40000 ALTER TABLE `account_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_filial`
--

DROP TABLE IF EXISTS `account_filial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_filial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_token` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `company_id` int(11) NOT NULL,
  `chat_id` longtext,
  PRIMARY KEY (`id`),
  KEY `account_filial_company_id_4ad73c3b_fk_account_company_id` (`company_id`),
  CONSTRAINT `account_filial_company_id_4ad73c3b_fk_account_company_id` FOREIGN KEY (`company_id`) REFERENCES `account_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_filial`
--

LOCK TABLES `account_filial` WRITE;
/*!40000 ALTER TABLE `account_filial` DISABLE KEYS */;
INSERT INTO `account_filial` VALUES (1,'1621178924:AAGIpk0wppaSTDkf_PpOu-JML8autb8vwtQ','Yangi bozor','Andijon viloyati',1,'538408955 1181140062 1239901764 982152007'),(2,'1744121801:AAGMgRfnEGq8lkwm37bvt5BWeMU7GyuuD-k','Eski shahar','Andijon viloyati',1,'1835446131 652107068 1658149588'),(3,'1727707630:AAFnmWUuOm5C8qThAXk43awozgMAnnNIf4Q','Letniy','Andijon viloyati',1,'598433369 1352318665');
/*!40000 ALTER TABLE `account_filial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add company',1,'add_company'),(2,'Can change company',1,'change_company'),(3,'Can delete company',1,'delete_company'),(4,'Can view company',1,'view_company'),(5,'Can add user',2,'add_account'),(6,'Can change user',2,'change_account'),(7,'Can delete user',2,'delete_account'),(8,'Can view user',2,'view_account'),(9,'Can add log entry',3,'add_logentry'),(10,'Can change log entry',3,'change_logentry'),(11,'Can delete log entry',3,'delete_logentry'),(12,'Can view log entry',3,'view_logentry'),(13,'Can add permission',4,'add_permission'),(14,'Can change permission',4,'change_permission'),(15,'Can delete permission',4,'delete_permission'),(16,'Can view permission',4,'view_permission'),(17,'Can add group',5,'add_group'),(18,'Can change group',5,'change_group'),(19,'Can delete group',5,'delete_group'),(20,'Can view group',5,'view_group'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add import template',8,'add_importtemplate'),(30,'Can change import template',8,'change_importtemplate'),(31,'Can delete import template',8,'delete_importtemplate'),(32,'Can view import template',8,'view_importtemplate'),(33,'Can add script',9,'add_script'),(34,'Can change script',9,'change_script'),(35,'Can delete script',9,'delete_script'),(36,'Can view script',9,'view_script'),(37,'Can add objection write',10,'add_objectionwrite'),(38,'Can change objection write',10,'change_objectionwrite'),(39,'Can delete objection write',10,'delete_objectionwrite'),(40,'Can view objection write',10,'view_objectionwrite'),(41,'Can add objections',11,'add_objections'),(42,'Can change objections',11,'change_objections'),(43,'Can delete objections',11,'delete_objections'),(44,'Can view objections',11,'view_objections'),(45,'Can add debtors',12,'add_debtors'),(46,'Can change debtors',12,'change_debtors'),(47,'Can delete debtors',12,'delete_debtors'),(48,'Can view debtors',12,'view_debtors'),(49,'Can add calendar',13,'add_calendar'),(50,'Can change calendar',13,'change_calendar'),(51,'Can delete calendar',13,'delete_calendar'),(52,'Can view calendar',13,'view_calendar'),(53,'Can add goal',14,'add_goal'),(54,'Can change goal',14,'change_goal'),(55,'Can delete goal',14,'delete_goal'),(56,'Can view goal',14,'view_goal'),(57,'Can add category product',15,'add_categoryproduct'),(58,'Can change category product',15,'change_categoryproduct'),(59,'Can delete category product',15,'delete_categoryproduct'),(60,'Can view category product',15,'view_categoryproduct'),(61,'Can add district',16,'add_district'),(62,'Can change district',16,'change_district'),(63,'Can delete district',16,'delete_district'),(64,'Can view district',16,'view_district'),(65,'Can add lead',17,'add_lead'),(66,'Can change lead',17,'change_lead'),(67,'Can delete lead',17,'delete_lead'),(68,'Can view lead',17,'view_lead'),(69,'Can add telegram_user',18,'add_telegram_user'),(70,'Can change telegram_user',18,'change_telegram_user'),(71,'Can delete telegram_user',18,'delete_telegram_user'),(72,'Can view telegram_user',18,'view_telegram_user'),(73,'Can add task',19,'add_task'),(74,'Can change task',19,'change_task'),(75,'Can delete task',19,'delete_task'),(76,'Can view task',19,'view_task'),(77,'Can add region',20,'add_region'),(78,'Can change region',20,'change_region'),(79,'Can delete region',20,'delete_region'),(80,'Can view region',20,'view_region'),(81,'Can add lead action',21,'add_leadaction'),(82,'Can change lead action',21,'change_leadaction'),(83,'Can delete lead action',21,'delete_leadaction'),(84,'Can view lead action',21,'view_leadaction'),(85,'Can add bot',22,'add_bot'),(86,'Can change bot',22,'change_bot'),(87,'Can delete bot',22,'delete_bot'),(88,'Can view bot',22,'view_bot'),(89,'Can add bot update',23,'add_botupdate'),(90,'Can change bot update',23,'change_botupdate'),(91,'Can delete bot update',23,'delete_botupdate'),(92,'Can view bot update',23,'view_botupdate'),(93,'Can add books',24,'add_books'),(94,'Can change books',24,'change_books'),(95,'Can delete books',24,'delete_books'),(96,'Can view books',24,'view_books'),(97,'Can add filial',25,'add_filial'),(98,'Can change filial',25,'change_filial'),(99,'Can delete filial',25,'delete_filial'),(100,'Can view filial',25,'view_filial'),(101,'Can add filial',26,'add_filial'),(102,'Can change filial',26,'change_filial'),(103,'Can delete filial',26,'delete_filial'),(104,'Can view filial',26,'view_filial'),(105,'Can add rooms',27,'add_rooms'),(106,'Can change rooms',27,'change_rooms'),(107,'Can delete rooms',27,'delete_rooms'),(108,'Can view rooms',27,'view_rooms'),(109,'Can add type room',28,'add_typeroom'),(110,'Can change type room',28,'change_typeroom'),(111,'Can delete type room',28,'delete_typeroom'),(112,'Can view type room',28,'view_typeroom');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_categoryproduct`
--

DROP TABLE IF EXISTS `board_categoryproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_categoryproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(220) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `board_categoryproduct_company_id_ff7d48ea_fk_account_company_id` (`company_id`),
  CONSTRAINT `board_categoryproduct_company_id_ff7d48ea_fk_account_company_id` FOREIGN KEY (`company_id`) REFERENCES `account_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_categoryproduct`
--

LOCK TABLES `board_categoryproduct` WRITE;
/*!40000 ALTER TABLE `board_categoryproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_categoryproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_district`
--

DROP TABLE IF EXISTS `board_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `region_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `board_district_region_id_52140812_fk_board_region_id` (`region_id`),
  KEY `board_district_company_id_e7643722_fk_account_company_id` (`company_id`),
  CONSTRAINT `board_district_company_id_e7643722_fk_account_company_id` FOREIGN KEY (`company_id`) REFERENCES `account_company` (`id`),
  CONSTRAINT `board_district_region_id_52140812_fk_board_region_id` FOREIGN KEY (`region_id`) REFERENCES `board_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_district`
--

LOCK TABLES `board_district` WRITE;
/*!40000 ALTER TABLE `board_district` DISABLE KEYS */;
INSERT INTO `board_district` VALUES (1,'Andijon tumani',1,1),(2,'Asaka tumani',1,1),(3,'Bo\'ston tumani',1,1),(4,'Baliqchi tumani',1,1),(5,'Buloqboshi tumani',1,1),(6,'Izboskan tumani',1,1),(7,'Jalaquduq tumani',1,1),(8,'Marhamat tumani',1,1),(9,'Oltinko\'l tumani',1,1),(10,'Paxtaobod tumani',1,1),(11,'Qo\'rg\'ontepa tumani',1,1),(12,'Shahrixon tumani',1,1),(13,'Ulug\'nor tumani',1,1),(14,'Xo\'jaobod tumani',1,1);
/*!40000 ALTER TABLE `board_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_lead`
--

DROP TABLE IF EXISTS `board_lead`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_lead` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `finishedPrice` int(11) NOT NULL,
  `company` varchar(255) DEFAULT NULL,
  `companyAddress` varchar(255) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `finishedDate` datetime(6) DEFAULT NULL,
  `degree` int(11) NOT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `abcxyz` varchar(255) DEFAULT NULL,
  `step1` longtext,
  `step2` longtext,
  `step3` longtext,
  `step4` longtext,
  `step5` longtext,
  `status_date` datetime(6) NOT NULL,
  `note` longtext,
  `debt` int(11) NOT NULL,
  `joinBy` int(11) NOT NULL,
  `tg_chatid` int(11) NOT NULL,
  `created_user_id` int(11) NOT NULL,
  `district_id` int(11) DEFAULT NULL,
  `where` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `board_lead_created_user_id_e68891fa_fk_account_account_id` (`created_user_id`),
  KEY `board_lead_district_id_64224efa_fk_board_district_id` (`district_id`),
  CONSTRAINT `board_lead_created_user_id_e68891fa_fk_account_account_id` FOREIGN KEY (`created_user_id`) REFERENCES `account_account` (`id`),
  CONSTRAINT `board_lead_district_id_64224efa_fk_board_district_id` FOREIGN KEY (`district_id`) REFERENCES `board_district` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_lead`
--

LOCK TABLES `board_lead` WRITE;
/*!40000 ALTER TABLE `board_lead` DISABLE KEYS */;
INSERT INTO `board_lead` VALUES (40,'рустам ака','Nuriddinov',0,0,NULL,NULL,0,'2021-06-15 16:15:51.796133',NULL,1,'998905467008',NULL,NULL,'-','-','-','-','-','2021-06-15 16:15:51.796200',NULL,0,0,0,9,NULL,NULL),(41,'','',0,0,NULL,NULL,0,'2021-06-15 16:34:30.175229',NULL,1,'',NULL,NULL,'-','-','-','-','-','2021-06-15 16:34:30.175298',NULL,0,0,0,9,NULL,NULL),(42,'123123','123213123',0,0,NULL,NULL,0,'2021-06-16 11:55:22.056228',NULL,1,'1435765324',NULL,NULL,'-','-','-','-','-','2021-06-16 11:55:22.056296',NULL,0,0,0,10,NULL,'12312 321 3123'),(43,'2342134234234','23423423',0,0,NULL,NULL,0,'2021-06-16 11:55:40.433397',NULL,1,'4234235432452',NULL,NULL,'-','-','-','-','-','2021-06-16 11:55:40.433462',NULL,0,0,0,10,NULL,'2342'),(44,'2314213423','4234213',0,0,NULL,NULL,0,'2021-06-16 11:55:59.890601',NULL,1,'45454',NULL,NULL,'-','-','-','-','-','2021-06-16 11:55:59.890666',NULL,0,0,0,10,NULL,'234234'),(45,'123123','123213123',0,0,NULL,NULL,0,'2021-06-16 11:56:34.114108',NULL,1,'14357652222','2021-06-17',NULL,'-','-','-','-','-','2021-06-16 11:56:34.114461',NULL,0,0,0,10,NULL,'12312 321 3123'),(46,'wqwqe','qwe qweq',0,0,NULL,NULL,0,'2021-06-16 11:57:57.918499',NULL,1,'21111111111','2021-06-29',NULL,'-','-','-','-','-','2021-06-16 11:57:57.918594',NULL,0,0,0,10,NULL,'tgdan');
/*!40000 ALTER TABLE `board_lead` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_lead_categoryproduct`
--

DROP TABLE IF EXISTS `board_lead_categoryproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_lead_categoryproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lead_id` int(11) NOT NULL,
  `categoryproduct_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `board_lead_categoryprodu_lead_id_categoryproduct__1f4e98df_uniq` (`lead_id`,`categoryproduct_id`),
  KEY `board_lead_categoryp_categoryproduct_id_6c4eeb5b_fk_board_cat` (`categoryproduct_id`),
  CONSTRAINT `board_lead_categoryp_categoryproduct_id_6c4eeb5b_fk_board_cat` FOREIGN KEY (`categoryproduct_id`) REFERENCES `board_categoryproduct` (`id`),
  CONSTRAINT `board_lead_categoryproduct_lead_id_111f511d_fk_board_lead_id` FOREIGN KEY (`lead_id`) REFERENCES `board_lead` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_lead_categoryproduct`
--

LOCK TABLES `board_lead_categoryproduct` WRITE;
/*!40000 ALTER TABLE `board_lead_categoryproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_lead_categoryproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_leadaction`
--

DROP TABLE IF EXISTS `board_leadaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_leadaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `oldStatus` int(11) NOT NULL,
  `newStatus` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `note` longtext NOT NULL,
  `color` varchar(255) NOT NULL,
  `changer_id` int(11) NOT NULL,
  `lead_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `board_leadaction_changer_id_d3f39e28_fk_account_account_id` (`changer_id`),
  KEY `board_leadaction_lead_id_b3804881_fk_board_lead_id` (`lead_id`),
  CONSTRAINT `board_leadaction_changer_id_d3f39e28_fk_account_account_id` FOREIGN KEY (`changer_id`) REFERENCES `account_account` (`id`),
  CONSTRAINT `board_leadaction_lead_id_b3804881_fk_board_lead_id` FOREIGN KEY (`lead_id`) REFERENCES `board_lead` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_leadaction`
--

LOCK TABLES `board_leadaction` WRITE;
/*!40000 ALTER TABLE `board_leadaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_leadaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_region`
--

DROP TABLE IF EXISTS `board_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `board_region_company_id_d3f34c12_fk_account_company_id` (`company_id`),
  CONSTRAINT `board_region_company_id_d3f34c12_fk_account_company_id` FOREIGN KEY (`company_id`) REFERENCES `account_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_region`
--

LOCK TABLES `board_region` WRITE;
/*!40000 ALTER TABLE `board_region` DISABLE KEYS */;
INSERT INTO `board_region` VALUES (1,'Andijon viloyati',1);
/*!40000 ALTER TABLE `board_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_task`
--

DROP TABLE IF EXISTS `board_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `note` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `finishedDate` datetime(6) DEFAULT NULL,
  `created_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `board_task_created_user_id_bff7fbe5_fk_account_account_id` (`created_user_id`),
  CONSTRAINT `board_task_created_user_id_bff7fbe5_fk_account_account_id` FOREIGN KEY (`created_user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_task`
--

LOCK TABLES `board_task` WRITE;
/*!40000 ALTER TABLE `board_task` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_telegram_user`
--

DROP TABLE IF EXISTS `board_telegram_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_telegram_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chat_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `companyAddress` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `step` int(11) NOT NULL,
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_telegram_user`
--

LOCK TABLES `board_telegram_user` WRITE;
/*!40000 ALTER TABLE `board_telegram_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_telegram_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_bot`
--

DROP TABLE IF EXISTS `bot_bot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bot_bot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `admin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bot_bot_admin_id_f665e11b_fk_account_account_id` (`admin_id`),
  CONSTRAINT `bot_bot_admin_id_f665e11b_fk_account_account_id` FOREIGN KEY (`admin_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_bot`
--

LOCK TABLES `bot_bot` WRITE;
/*!40000 ALTER TABLE `bot_bot` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_bot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_botupdate`
--

DROP TABLE IF EXISTS `bot_botupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bot_botupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `last_update` int(11) NOT NULL,
  `bot_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bot_botupdate_bot_id_b7581a97_fk_bot_bot_id` (`bot_id`),
  CONSTRAINT `bot_botupdate_bot_id_b7581a97_fk_bot_bot_id` FOREIGN KEY (`bot_id`) REFERENCES `bot_bot` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_botupdate`
--

LOCK TABLES `bot_botupdate` WRITE;
/*!40000 ALTER TABLE `bot_botupdate` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_botupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buyurtma_books`
--

DROP TABLE IF EXISTS `buyurtma_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buyurtma_books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ordertype` int(11) NOT NULL,
  `people` int(11) DEFAULT NULL,
  `meals` varchar(255) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  `filial_id` int(11) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `room_id` int(11) DEFAULT NULL,
  `date` datetime(6),
  `ordertime` datetime(6) DEFAULT NULL,
  `address` longtext,
  PRIMARY KEY (`id`),
  KEY `buyurtma_books_client_id_59eab01f_fk_board_lead_id` (`client_id`),
  KEY `buyurtma_books_filial_id_0207cbac_fk_account_filial_id` (`filial_id`),
  KEY `buyurtma_books_room_id_a7a260b8_fk_buyurtma_rooms_id` (`room_id`),
  CONSTRAINT `buyurtma_books_client_id_59eab01f_fk_board_lead_id` FOREIGN KEY (`client_id`) REFERENCES `board_lead` (`id`),
  CONSTRAINT `buyurtma_books_filial_id_0207cbac_fk_account_filial_id` FOREIGN KEY (`filial_id`) REFERENCES `account_filial` (`id`),
  CONSTRAINT `buyurtma_books_room_id_a7a260b8_fk_buyurtma_rooms_id` FOREIGN KEY (`room_id`) REFERENCES `buyurtma_rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=247 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyurtma_books`
--

LOCK TABLES `buyurtma_books` WRITE;
/*!40000 ALTER TABLE `buyurtma_books` DISABLE KEYS */;
INSERT INTO `buyurtma_books` VALUES (235,2,NULL,'кази 1 кг',40,1,0,NULL,'2021-06-15 16:15:51.798308','2021-06-16 19:17:00.000000',NULL),(236,2,NULL,'кази 1 кг',40,1,1,NULL,'2021-06-15 16:15:54.885239','2021-06-16 19:17:00.000000',NULL),(237,2,NULL,'Ош 1кг ',40,1,0,NULL,'2021-06-15 16:22:40.758682','2021-06-15 19:25:00.000000',NULL),(238,1,NULL,'Ош 1кг Ленинский',40,2,1,NULL,'2021-06-15 16:25:01.209141','2021-06-15 19:27:00.000000',NULL),(239,2,NULL,'Ош 1кг',40,3,0,NULL,'2021-06-15 16:32:40.222768','2021-06-15 20:36:00.000000',NULL),(240,0,14,NULL,40,1,1,139,'2021-06-15 16:33:27.461569','2021-06-17 17:34:00.000000',NULL),(241,0,14,NULL,41,1,1,139,'2021-06-15 16:34:30.178903','2021-06-16 18:36:00.000000',NULL),(242,2,NULL,'21342342 154 4235',42,1,0,NULL,'2021-06-16 11:55:22.058832','2021-06-17 11:55:00.000000',NULL),(243,1,NULL,'23423',43,3,0,NULL,'2021-06-16 11:55:40.436615','2021-06-18 11:55:00.000000','4234 345435'),(244,0,23,NULL,44,1,1,120,'2021-06-16 11:55:59.892693','2021-06-26 11:55:00.000000',NULL),(245,2,NULL,'w rf ',45,1,0,NULL,'2021-06-16 11:56:34.120604','2021-06-18 11:56:00.000000',NULL),(246,2,NULL,'123123123',46,1,0,NULL,'2021-06-16 11:57:57.920490','2021-07-09 11:57:00.000000',NULL);
/*!40000 ALTER TABLE `buyurtma_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buyurtma_rooms`
--

DROP TABLE IF EXISTS `buyurtma_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buyurtma_rooms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `filial_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `buyurtma_rooms_type_id_0406a9e3_fk_buyurtma_typeroom_id` (`type_id`),
  KEY `buyurtma_rooms_filial_id_b4647349_fk_account_filial_id` (`filial_id`),
  CONSTRAINT `buyurtma_rooms_filial_id_b4647349_fk_account_filial_id` FOREIGN KEY (`filial_id`) REFERENCES `account_filial` (`id`),
  CONSTRAINT `buyurtma_rooms_type_id_0406a9e3_fk_buyurtma_typeroom_id` FOREIGN KEY (`type_id`) REFERENCES `buyurtma_typeroom` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=206 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyurtma_rooms`
--

LOCK TABLES `buyurtma_rooms` WRITE;
/*!40000 ALTER TABLE `buyurtma_rooms` DISABLE KEYS */;
INSERT INTO `buyurtma_rooms` VALUES (106,'200 xona',0,6,2,2),(107,'201 xona',0,18,2,2),(108,'202 xona',0,10,2,3),(109,'203 xona',0,14,2,4),(110,'204 xona',0,10,2,3),(111,'205 xona',0,10,2,3),(112,'206 xona',0,14,2,3),(113,'219 xona',0,20,2,4),(114,'220 xona',0,10,2,3),(115,'221 xona',0,10,2,3),(116,'222 xona',0,10,2,3),(117,'223 xona',0,16,2,4),(118,'300 xona',0,18,2,3),(119,'301 xona',0,10,2,3),(120,'1 xona',0,15,1,1),(121,'302 xona',0,18,2,2),(122,'2 xona',0,18,1,2),(123,'303 xona',0,10,2,3),(124,'304 xona',0,14,2,4),(125,'305 xona',0,10,2,5),(126,'306 xona',0,10,2,3),(127,'3 xona',0,15,1,1),(128,'307 xona',0,16,2,3),(129,'319 xona',0,20,2,4),(130,'320 xona',0,10,2,3),(131,'321 xona',0,10,2,3),(132,'322 xona',0,10,2,3),(133,'4 xona',0,15,1,1),(134,'5 xona',0,5,1,3),(135,'6 xona',0,6,1,1),(136,'323 xona',0,10,2,3),(137,'7 xona',0,5,1,3),(138,'8 xona',0,6,1,1),(139,'9 xona',0,14,1,3),(140,'10 xona',0,15,1,1),(141,'1',0,8,3,4),(142,'11 xona',0,5,1,3),(143,'12 xona',0,6,1,1),(144,'2',0,8,3,4),(145,'3',0,12,3,4),(146,'13 xona',0,6,1,1),(147,'4',0,7,3,4),(148,'14 xona',0,5,1,3),(149,'15 xona',0,10,1,1),(150,'16 xona',0,10,1,3),(151,'5',0,7,3,4),(152,'17 xona',0,10,1,1),(153,'18 xona',0,18,1,2),(154,'6',0,7,3,4),(155,'19 xona',0,10,1,1),(156,'20 xona',0,10,1,3),(157,'21 xona',0,10,1,1),(158,'22 xona',0,10,1,3),(159,'23 xona',0,10,1,1),(160,'24 xona',0,30,1,1),(161,'7',0,7,3,4),(162,'25 Besetka',0,10,1,1),(163,'26 Besetka',0,10,1,3),(164,'27 Besetka',0,10,1,1),(165,'28 Besetka',0,10,1,4),(166,'29 Besetka',0,10,1,1),(167,'30 Besetka',0,10,1,3),(168,'31 Besetka',0,10,1,1),(169,'8',0,18,3,4),(170,'32 Besetka',0,10,1,3),(171,'9',0,7,3,4),(172,'10',0,7,3,4),(173,'11',0,7,3,4),(174,'12',0,12,3,4),(175,'13',0,7,3,4),(176,'14',0,10,3,4),(177,'15',0,7,3,4),(178,'16',0,7,3,4),(179,'17',0,10,3,4),(180,'18',0,7,3,4),(181,'19',0,7,3,4),(182,'20',0,10,3,4),(183,'21',0,7,3,4),(184,'22',0,7,3,4),(185,'23',0,10,3,4),(186,'24',0,7,3,4),(187,'25',0,7,3,4),(188,'26',0,10,3,4),(189,'27',0,7,3,4),(190,'28',0,7,3,4),(191,'29',0,10,3,4),(192,'30',0,7,3,4),(193,'31',0,7,3,4),(194,'32',0,10,3,4),(195,'33',0,7,3,4),(196,'34',0,7,3,4),(197,'35',0,10,3,4),(198,'36',0,7,3,4),(199,'37',0,7,3,4),(200,'38',0,10,3,4),(201,'39',0,7,3,4),(202,'40',0,7,3,4),(203,'41',0,10,3,4),(204,'42',0,7,3,4),(205,'43',0,16,3,4);
/*!40000 ALTER TABLE `buyurtma_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buyurtma_typeroom`
--

DROP TABLE IF EXISTS `buyurtma_typeroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buyurtma_typeroom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyurtma_typeroom`
--

LOCK TABLES `buyurtma_typeroom` WRITE;
/*!40000 ALTER TABLE `buyurtma_typeroom` DISABLE KEYS */;
INSERT INTO `buyurtma_typeroom` VALUES (1,'Supa'),(2,'Stol'),(3,'Divan'),(4,'So\'ri'),(5,'Namozxona');
/*!40000 ALTER TABLE `buyurtma_typeroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_account_account_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=551 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-04-21 09:58:37.957022','2','crm',1,'[{\"added\": {}}]',2,1),(2,'2021-04-21 09:59:28.110918','1','Movarounnahr',1,'[{\"added\": {}}]',1,1),(3,'2021-04-21 09:59:34.667611','2','crm',2,'[{\"changed\": {\"fields\": [\"Company\", \"Is director\"]}}]',2,1),(4,'2021-04-21 10:02:02.866834','2','crm',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',2,1),(5,'2021-04-24 08:45:49.428006','1','Yangi bozor',1,'[{\"added\": {}}]',26,1),(6,'2021-04-24 08:45:59.667302','2','Eski shahar',1,'[{\"added\": {}}]',26,1),(7,'2021-04-24 08:46:52.181259','1','Supa',1,'[{\"added\": {}}]',28,1),(8,'2021-04-24 08:46:55.744539','2','Stol',1,'[{\"added\": {}}]',28,1),(9,'2021-04-24 08:47:02.036235','3','Divan',1,'[{\"added\": {}}]',28,1),(10,'2021-04-24 08:47:27.311151','4','So\'ri',1,'[{\"added\": {}}]',28,1),(11,'2021-04-24 08:47:41.304721','5','Namozxona',1,'[{\"added\": {}}]',28,1),(12,'2021-04-24 08:48:18.769744','1','1-xona',1,'[{\"added\": {}}]',27,1),(13,'2021-04-24 08:48:34.069484','2','2-xona',1,'[{\"added\": {}}]',27,1),(14,'2021-04-24 08:48:50.053733','3','3-xona',1,'[{\"added\": {}}]',27,1),(15,'2021-04-24 08:52:22.109428','5','callcenter',2,'[{\"changed\": {\"fields\": [\"Is callcenter\"]}}]',2,1),(16,'2021-04-26 04:16:38.757102','1','movarounnahr',2,'[{\"changed\": {\"fields\": [\"Company\", \"Is director\"]}}]',2,1),(17,'2021-04-26 09:52:15.857644','1','Yangi bozor',2,'[{\"changed\": {\"fields\": [\"Bot token\", \"Chat id\"]}}]',26,1),(18,'2021-04-26 09:52:28.629315','2','Eski shahar',2,'[{\"changed\": {\"fields\": [\"Bot token\", \"Chat id\"]}}]',26,1),(19,'2021-05-04 13:41:17.973961','2','2-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(20,'2021-05-04 13:41:21.310324','3','3-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(21,'2021-05-04 13:44:21.439036','1','1-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(22,'2021-05-04 13:44:35.678445','3','3-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(23,'2021-05-22 12:35:21.400530','4','test',1,'[{\"added\": {}}]',27,1),(24,'2021-05-22 12:41:25.922631','5','15-hona',1,'[{\"added\": {}}]',27,1),(25,'2021-06-02 12:27:35.178377','1','Andijon viloyati',1,'[{\"added\": {}}]',20,1),(26,'2021-06-02 12:28:15.616416','1','Andijon tumani',1,'[{\"added\": {}}]',16,1),(27,'2021-06-02 12:28:29.833316','2','Asaka tumani',1,'[{\"added\": {}}]',16,1),(28,'2021-06-02 12:28:37.676120','3','Bo\'ston tumani',1,'[{\"added\": {}}]',16,1),(29,'2021-06-02 12:28:49.472585','4','Baliqchi tumani',1,'[{\"added\": {}}]',16,1),(30,'2021-06-02 12:28:58.830135','5','Buloqboshi tumani',1,'[{\"added\": {}}]',16,1),(31,'2021-06-02 12:29:05.281813','6','Izboskan tumani',1,'[{\"added\": {}}]',16,1),(32,'2021-06-02 12:29:12.881558','7','Jalaquduq tumani',1,'[{\"added\": {}}]',16,1),(33,'2021-06-02 12:29:20.032290','8','Marhamat tumani',1,'[{\"added\": {}}]',16,1),(34,'2021-06-02 12:29:27.070080','9','Oltinko\'l tumani',1,'[{\"added\": {}}]',16,1),(35,'2021-06-02 12:29:33.677153','10','Paxtaobod tumani',1,'[{\"added\": {}}]',16,1),(36,'2021-06-02 12:29:40.838991','11','Qo\'rg\'ontepa tumani',1,'[{\"added\": {}}]',16,1),(37,'2021-06-02 12:29:48.636111','12','Shahrixon tumani',1,'[{\"added\": {}}]',16,1),(38,'2021-06-02 12:29:58.070192','13','Ulug\'nor tumani',1,'[{\"added\": {}}]',16,1),(39,'2021-06-02 12:30:07.814705','14','Xo\'jaobod tumani',1,'[{\"added\": {}}]',16,1),(40,'2021-06-02 12:34:09.724764','8','11111',2,'[{\"changed\": {\"fields\": [\"Name\", \"District\", \"Abcxyz\"]}}]',17,1),(41,'2021-06-02 12:35:49.725466','15','зебо',3,'',17,1),(42,'2021-06-02 12:35:49.729435','14','зебо',3,'',17,1),(43,'2021-06-02 12:35:49.733326','13','Akmalhon ',3,'',17,1),(44,'2021-06-02 12:35:49.737509','12','vcvsdvv',3,'',17,1),(45,'2021-06-02 12:35:49.740205','11','vcvsdvv',3,'',17,1),(46,'2021-06-02 12:35:49.742693','10','963',3,'',17,1),(47,'2021-06-02 12:35:49.744653','9','test',3,'',17,1),(48,'2021-06-02 12:35:49.747115','8','11111',3,'',17,1),(49,'2021-06-02 12:35:49.748935','7','marıyam',3,'',17,1),(50,'2021-06-02 12:35:49.751317','6','vcvsdvv',3,'',17,1),(51,'2021-06-02 12:35:49.753055','5','qwe',3,'',17,1),(52,'2021-06-02 12:35:49.755241','4','qw',3,'',17,1),(53,'2021-06-02 12:35:49.756811','3','qwe',3,'',17,1),(54,'2021-06-02 12:35:49.759161','2','vcvsdvv',3,'',17,1),(55,'2021-06-02 12:35:49.760892','1','vcvsdvv',3,'',17,1),(56,'2021-06-02 12:36:08.975447','16','сева',2,'[{\"changed\": {\"fields\": [\"Surname\", \"Phone\", \"District\", \"Abcxyz\"]}}]',17,1),(57,'2021-06-04 11:32:30.120191','25','сева',3,'',17,1),(58,'2021-06-04 11:32:30.125819','24','Fazliddin',3,'',17,1),(59,'2021-06-04 11:32:30.128105','23','',3,'',17,1),(60,'2021-06-04 11:32:30.129498','22','сева',3,'',17,1),(61,'2021-06-04 11:32:30.131607','21','сева',3,'',17,1),(62,'2021-06-04 11:32:30.133036','20','сева',3,'',17,1),(63,'2021-06-04 11:32:30.134571','19','сева',3,'',17,1),(64,'2021-06-04 11:32:30.139438','18','сева',3,'',17,1),(65,'2021-06-04 11:32:30.140909','17','Fazliddin',3,'',17,1),(66,'2021-06-04 11:32:30.143233','16','сева',3,'',17,1),(67,'2021-06-04 11:43:20.154484','3','Letniy',1,'[{\"added\": {}}]',26,1),(68,'2021-06-04 11:43:48.751664','7','letniy',1,'[{\"added\": {}}]',2,1),(69,'2021-06-04 11:44:04.591592','7','letniy',2,'[{\"changed\": {\"fields\": [\"Company\", \"Filial\"]}}]',2,1),(70,'2021-06-11 08:52:32.317735','7','Test',3,'',28,1),(71,'2021-06-11 08:52:32.320150','6','Test',3,'',28,1),(72,'2021-06-11 09:56:48.765290','3','3-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(73,'2021-06-11 09:56:51.929622','4','test',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(74,'2021-06-11 10:11:12.809302','86','O\'chirilgan',3,'',24,1),(75,'2021-06-11 10:11:12.811349','85','O\'chirilgan',3,'',24,1),(76,'2021-06-11 10:11:12.812233','84','O\'chirilgan',3,'',24,1),(77,'2021-06-11 10:11:12.813036','83','O\'chirilgan',3,'',24,1),(78,'2021-06-11 10:11:12.814231','82','O\'chirilgan',3,'',24,1),(79,'2021-06-11 10:11:12.814956','81','O\'chirilgan',3,'',24,1),(80,'2021-06-11 10:20:20.827560','5','15-hona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(81,'2021-06-11 10:20:24.267195','1','1-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(82,'2021-06-11 10:20:29.598404','2','2-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(83,'2021-06-11 11:01:48.327025','134','O\'chirilgan',3,'',24,1),(84,'2021-06-11 11:01:48.329534','133','O\'chirilgan',3,'',24,1),(85,'2021-06-11 11:01:48.330993','132','O\'chirilgan',3,'',24,1),(86,'2021-06-11 11:01:48.331900','131','O\'chirilgan',3,'',24,1),(87,'2021-06-11 11:01:48.332586','130','O\'chirilgan',3,'',24,1),(88,'2021-06-11 11:01:48.333328','129','O\'chirilgan',3,'',24,1),(89,'2021-06-11 11:01:48.334351','128','Nabiyev',3,'',24,1),(90,'2021-06-11 11:01:48.335029','127','O\'chirilgan',3,'',24,1),(91,'2021-06-11 11:01:48.335696','126','O\'chirilgan',3,'',24,1),(92,'2021-06-11 11:01:48.336393','125','O\'chirilgan',3,'',24,1),(93,'2021-06-11 11:01:48.337135','124','O\'chirilgan',3,'',24,1),(94,'2021-06-11 11:01:48.339300','123','O\'chirilgan',3,'',24,1),(95,'2021-06-11 11:01:48.341029','122','O\'chirilgan',3,'',24,1),(96,'2021-06-11 11:01:48.342433','121','O\'chirilgan',3,'',24,1),(97,'2021-06-11 11:01:48.343212','120','O\'chirilgan',3,'',24,1),(98,'2021-06-11 11:01:48.343913','119','O\'chirilgan',3,'',24,1),(99,'2021-06-11 11:01:48.344582','118','O\'chirilgan',3,'',24,1),(100,'2021-06-11 11:01:48.345255','117','O\'chirilgan',3,'',24,1),(101,'2021-06-11 11:01:48.346491','116','O\'chirilgan',3,'',24,1),(102,'2021-06-11 11:01:48.347234','115','O\'chirilgan',3,'',24,1),(103,'2021-06-11 11:01:48.347965','114','O\'chirilgan',3,'',24,1),(104,'2021-06-11 11:01:48.348650','113','O\'chirilgan',3,'',24,1),(105,'2021-06-11 11:01:48.349799','112','O\'chirilgan',3,'',24,1),(106,'2021-06-11 11:01:48.350563','111','O\'chirilgan',3,'',24,1),(107,'2021-06-11 11:01:48.351278','110','O\'chirilgan',3,'',24,1),(108,'2021-06-11 11:01:48.351962','109','O\'chirilgan',3,'',24,1),(109,'2021-06-11 11:01:48.352659','108','O\'chirilgan',3,'',24,1),(110,'2021-06-11 11:01:48.353903','107','O\'chirilgan',3,'',24,1),(111,'2021-06-11 11:01:48.354639','106','O\'chirilgan',3,'',24,1),(112,'2021-06-11 11:01:48.355439','105','O\'chirilgan',3,'',24,1),(113,'2021-06-11 11:01:48.356147','104','O\'chirilgan',3,'',24,1),(114,'2021-06-11 11:01:48.356831','103','O\'chirilgan',3,'',24,1),(115,'2021-06-11 11:01:48.357944','102','O\'chirilgan',3,'',24,1),(116,'2021-06-11 11:01:48.358617','101','O\'chirilgan',3,'',24,1),(117,'2021-06-11 11:01:48.359358','100','O\'chirilgan',3,'',24,1),(118,'2021-06-11 11:01:48.360025','99','O\'chirilgan',3,'',24,1),(119,'2021-06-11 11:01:48.360701','98','O\'chirilgan',3,'',24,1),(120,'2021-06-11 11:01:48.361898','97','O\'chirilgan',3,'',24,1),(121,'2021-06-11 17:01:02.269776','197','O\'chirilgan',3,'',24,1),(122,'2021-06-11 17:01:02.272218','196','O\'chirilgan',3,'',24,1),(123,'2021-06-11 17:01:02.273293','195','Mamajonov ',3,'',24,1),(124,'2021-06-11 17:01:02.274875','194','O\'chirilgan',3,'',24,1),(125,'2021-06-11 17:01:36.000913','198','O\'chirilgan',3,'',24,1),(126,'2021-06-11 17:04:39.467509','202','O\'chirilgan',3,'',24,1),(127,'2021-06-11 17:04:39.469505','201','O\'chirilgan',3,'',24,1),(128,'2021-06-11 17:27:45.593355','4','test',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(129,'2021-06-11 17:27:48.592571','1','1-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(130,'2021-06-11 17:40:12.446751','4','test',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(131,'2021-06-11 17:40:21.599286','207','Mamajonov ',3,'',24,1),(132,'2021-06-11 17:40:21.601537','206','Nabiyev',3,'',24,1),(133,'2021-06-12 09:51:14.127413','4','test',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(134,'2021-06-12 09:51:17.879064','1','1-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(135,'2021-06-12 12:24:06.634960','4','test',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(136,'2021-06-12 12:24:09.422654','3','3-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(137,'2021-06-12 12:24:12.581241','2','2-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(138,'2021-06-12 12:24:15.468313','1','1-xona',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',27,1),(139,'2021-06-12 12:24:27.143451','213','Nabiyev',3,'',24,1),(140,'2021-06-12 12:24:27.148448','212','Nabiyev',3,'',24,1),(141,'2021-06-12 12:24:27.150137','211','Mamajonov ',3,'',24,1),(142,'2021-06-12 12:24:27.150953','210','Nabiyev',3,'',24,1),(143,'2021-06-12 12:24:27.151721','209','Mamajonov ',3,'',24,1),(144,'2021-06-12 12:24:27.152422','208','Nabiyev',3,'',24,1),(145,'2021-06-12 12:59:50.488869','3','yangibozor',2,'[{\"changed\": {\"fields\": [\"Filial\"]}}]',2,1),(146,'2021-06-12 16:23:39.765641','1','Yangi bozor',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(147,'2021-06-12 16:23:55.056313','2','Eski shahar',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(148,'2021-06-12 16:24:08.107489','3','Letniy',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(149,'2021-06-15 11:42:35.754821','224','Rozivoyhuja',3,'',24,1),(150,'2021-06-15 11:42:35.756874','223','latife',3,'',24,1),(151,'2021-06-15 11:42:35.758685','222','test',3,'',24,1),(152,'2021-06-15 11:42:35.759595','221','latife',3,'',24,1),(153,'2021-06-15 11:42:35.761214','220','Nabiyev',3,'',24,1),(154,'2021-06-15 11:42:35.762526','219','vdsfgrt',3,'',24,1),(155,'2021-06-15 11:42:35.763268','218','jfjebfebf',3,'',24,1),(156,'2021-06-15 11:42:35.763984','217','sehnoz',3,'',24,1),(157,'2021-06-15 11:42:35.764764','216','',3,'',24,1),(158,'2021-06-15 11:42:35.766180','215','test',3,'',24,1),(159,'2021-06-15 11:42:35.766928','214','latife',3,'',24,1),(160,'2021-06-15 11:42:59.178437','36','Rozivoyhuja',3,'',17,1),(161,'2021-06-15 11:42:59.180568','35','test',3,'',17,1),(162,'2021-06-15 11:42:59.182129','34','latife',3,'',17,1),(163,'2021-06-15 11:42:59.183054','33','vdsfgrt',3,'',17,1),(164,'2021-06-15 11:42:59.183981','32','jfjebfebf',3,'',17,1),(165,'2021-06-15 11:42:59.184944','31','sehnoz',3,'',17,1),(166,'2021-06-15 11:42:59.186337','30','',3,'',17,1),(167,'2021-06-15 11:42:59.187307','29','test',3,'',17,1),(168,'2021-06-15 11:42:59.188237','28','latife',3,'',17,1),(169,'2021-06-15 11:42:59.189184','27','Mamajonov ',3,'',17,1),(170,'2021-06-15 11:42:59.190577','26','Nabiyev',3,'',17,1),(171,'2021-06-15 11:43:07.903838','10','/, .m;:>',3,'',19,1),(172,'2021-06-15 11:43:07.905754','9','jv;bl,n mol',3,'',19,1),(173,'2021-06-15 11:43:07.907236','8','as das d',3,'',19,1),(174,'2021-06-15 11:43:07.908043','7','asd sad ',3,'',19,1),(175,'2021-06-15 11:43:07.908779','6','asd asd ',3,'',19,1),(176,'2021-06-15 11:43:07.910120','5','fgwerfge',3,'',19,1),(177,'2021-06-15 11:43:07.910858','4','jyhjyjtyjty',3,'',19,1),(178,'2021-06-15 11:43:07.911795','3','test3',3,'',19,1),(179,'2021-06-15 11:43:07.912574','2','test 2',3,'',19,1),(180,'2021-06-15 11:43:07.913783','1','test',3,'',19,1),(181,'2021-06-15 11:46:30.727374','5','15-hona',3,'',27,1),(182,'2021-06-15 11:46:30.729092','4','test',3,'',27,1),(183,'2021-06-15 11:46:30.731123','3','3-xona',3,'',27,1),(184,'2021-06-15 11:46:30.731963','2','2-xona',3,'',27,1),(185,'2021-06-15 11:46:30.732770','1','1-xona',3,'',27,1),(186,'2021-06-15 12:01:07.200804','6','1 xona',1,'[{\"added\": {}}]',27,1),(187,'2021-06-15 12:01:43.860594','7','2 xona',1,'[{\"added\": {}}]',27,1),(188,'2021-06-15 12:26:16.787991','8','200 xona',1,'[{\"added\": {}}]',27,1),(189,'2021-06-15 12:26:30.114011','8','200 xona',2,'[]',27,1),(190,'2021-06-15 12:26:37.736061','6','1 xona',2,'[]',27,1),(191,'2021-06-15 12:26:58.145772','9','201 xona',1,'[{\"added\": {}}]',27,1),(192,'2021-06-15 12:27:14.767881','10','201 xona',1,'[{\"added\": {}}]',27,1),(193,'2021-06-15 12:27:31.491618','11','202 xona',1,'[{\"added\": {}}]',27,1),(194,'2021-06-15 12:27:45.192274','12','203 xon',1,'[{\"added\": {}}]',27,1),(195,'2021-06-15 12:28:05.839375','13','205 xona',1,'[{\"added\": {}}]',27,1),(196,'2021-06-15 12:28:19.634068','14','206 xona',1,'[{\"added\": {}}]',27,1),(197,'2021-06-15 12:28:33.896737','15','3 xona',1,'[{\"added\": {}}]',27,1),(198,'2021-06-15 12:28:41.240005','16','219 xona',1,'[{\"added\": {}}]',27,1),(199,'2021-06-15 12:29:02.265526','17','220 xona',1,'[{\"added\": {}}]',27,1),(200,'2021-06-15 12:29:15.612641','18','221 xona',1,'[{\"added\": {}}]',27,1),(201,'2021-06-15 12:29:26.888598','19','222 xona',1,'[{\"added\": {}}]',27,1),(202,'2021-06-15 12:29:37.652255','20','4 xona',1,'[{\"added\": {}}]',27,1),(203,'2021-06-15 12:29:37.979294','21','223',1,'[{\"added\": {}}]',27,1),(204,'2021-06-15 12:29:50.744863','22','300 xona',1,'[{\"added\": {}}]',27,1),(205,'2021-06-15 12:30:08.634940','23','302 xona',1,'[{\"added\": {}}]',27,1),(206,'2021-06-15 12:30:10.650180','24','5 xona',1,'[{\"added\": {}}]',27,1),(207,'2021-06-15 12:30:27.927289','25','301 xona',1,'[{\"added\": {}}]',27,1),(208,'2021-06-15 12:30:41.023342','26','303 xona',1,'[{\"added\": {}}]',27,1),(209,'2021-06-15 12:30:45.724051','27','6 xona',1,'[{\"added\": {}}]',27,1),(210,'2021-06-15 12:30:56.736255','28','304 xona',1,'[{\"added\": {}}]',27,1),(211,'2021-06-15 12:31:12.321326','29','7 xona',1,'[{\"added\": {}}]',27,1),(212,'2021-06-15 12:31:28.919317','30','305 xona',1,'[{\"added\": {}}]',27,1),(213,'2021-06-15 12:31:39.976962','31','8 xona',1,'[{\"added\": {}}]',27,1),(214,'2021-06-15 12:31:42.724543','32','306 xona',1,'[{\"added\": {}}]',27,1),(215,'2021-06-15 12:31:54.251001','33','307 xona',1,'[{\"added\": {}}]',27,1),(216,'2021-06-15 12:32:11.887911','34','319 xona',1,'[{\"added\": {}}]',27,1),(217,'2021-06-15 12:32:26.009428','35','320 xona',1,'[{\"added\": {}}]',27,1),(218,'2021-06-15 12:32:40.558122','36','321 xona',1,'[{\"added\": {}}]',27,1),(219,'2021-06-15 12:32:46.893393','37','9 xona',1,'[{\"added\": {}}]',27,1),(220,'2021-06-15 12:32:50.934097','38','322 xona',1,'[{\"added\": {}}]',27,1),(221,'2021-06-15 12:32:51.543160','39','1',1,'[{\"added\": {}}]',27,1),(222,'2021-06-15 12:33:00.455363','40','323 xona',1,'[{\"added\": {}}]',27,1),(223,'2021-06-15 12:33:05.930821','41','10',1,'[{\"added\": {}}]',27,1),(224,'2021-06-15 12:33:15.279117','42','2',1,'[{\"added\": {}}]',27,1),(225,'2021-06-15 12:33:22.925997','43','11 xona',1,'[{\"added\": {}}]',27,1),(226,'2021-06-15 12:33:43.648572','44','12 xona',1,'[{\"added\": {}}]',27,1),(227,'2021-06-15 12:33:53.378684','21','223 xona',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',27,1),(228,'2021-06-15 12:34:02.594465','21','223 xona',2,'[]',27,1),(229,'2021-06-15 12:34:12.469152','45','13 xona',1,'[{\"added\": {}}]',27,1),(230,'2021-06-15 12:34:14.657259','12','203 xona',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',27,1),(231,'2021-06-15 12:34:26.401231','43','11 xona',2,'[]',27,1),(232,'2021-06-15 12:34:50.187473','46','14 xona',1,'[{\"added\": {}}]',27,1),(233,'2021-06-15 12:35:13.391255','47','15 xona',1,'[{\"added\": {}}]',27,1),(234,'2021-06-15 12:35:35.229694','48','16 xona',1,'[{\"added\": {}}]',27,1),(235,'2021-06-15 12:35:37.234696','49','3',1,'[{\"added\": {}}]',27,1),(236,'2021-06-15 12:35:52.263377','50','17 xona',1,'[{\"added\": {}}]',27,1),(237,'2021-06-15 12:36:00.422579','51','4',1,'[{\"added\": {}}]',27,1),(238,'2021-06-15 12:36:09.071178','52','18 xona',1,'[{\"added\": {}}]',27,1),(239,'2021-06-15 12:36:19.619289','53','5',1,'[{\"added\": {}}]',27,1),(240,'2021-06-15 12:36:21.470104','54','19 xona',1,'[{\"added\": {}}]',27,1),(241,'2021-06-15 12:36:37.205041','55','20 xona',1,'[{\"added\": {}}]',27,1),(242,'2021-06-15 12:36:46.225846','56','6',1,'[{\"added\": {}}]',27,1),(243,'2021-06-15 12:36:54.869316','57','21 xona',1,'[{\"added\": {}}]',27,1),(244,'2021-06-15 12:37:06.946495','58','7',1,'[{\"added\": {}}]',27,1),(245,'2021-06-15 12:37:14.967000','59','22 xona',1,'[{\"added\": {}}]',27,1),(246,'2021-06-15 12:37:29.089848','60','8',1,'[{\"added\": {}}]',27,1),(247,'2021-06-15 12:37:33.327190','61','23 xona',1,'[{\"added\": {}}]',27,1),(248,'2021-06-15 12:37:49.300501','62','24 xona',1,'[{\"added\": {}}]',27,1),(249,'2021-06-15 12:37:52.754706','63','9',1,'[{\"added\": {}}]',27,1),(250,'2021-06-15 12:38:27.007782','64','25 Besetka',1,'[{\"added\": {}}]',27,1),(251,'2021-06-15 12:38:28.320235','65','10',1,'[{\"added\": {}}]',27,1),(252,'2021-06-15 12:38:42.454503','66','26 Besetka',1,'[{\"added\": {}}]',27,1),(253,'2021-06-15 12:38:45.338680','67','11',1,'[{\"added\": {}}]',27,1),(254,'2021-06-15 12:38:58.437540','68','27 Besetka',1,'[{\"added\": {}}]',27,1),(255,'2021-06-15 12:39:12.547672','69','28 Besetka',1,'[{\"added\": {}}]',27,1),(256,'2021-06-15 12:39:20.195564','70','12',1,'[{\"added\": {}}]',27,1),(257,'2021-06-15 12:39:30.513176','71','29 Besetka',1,'[{\"added\": {}}]',27,1),(258,'2021-06-15 12:39:44.720446','72','30 Besetka',1,'[{\"added\": {}}]',27,1),(259,'2021-06-15 12:39:53.560819','73','13',1,'[{\"added\": {}}]',27,1),(260,'2021-06-15 12:39:59.308431','74','31 Besetka',1,'[{\"added\": {}}]',27,1),(261,'2021-06-15 12:40:10.091494','75','32 Besetka',1,'[{\"added\": {}}]',27,1),(262,'2021-06-15 12:40:16.439618','76','14',1,'[{\"added\": {}}]',27,1),(263,'2021-06-15 12:40:50.246643','77','15',1,'[{\"added\": {}}]',27,1),(264,'2021-06-15 12:41:45.991001','78','16',1,'[{\"added\": {}}]',27,1),(265,'2021-06-15 12:43:29.288065','79','17',1,'[{\"added\": {}}]',27,1),(266,'2021-06-15 12:43:45.180544','80','18',1,'[{\"added\": {}}]',27,1),(267,'2021-06-15 12:43:58.331394','81','19',1,'[{\"added\": {}}]',27,1),(268,'2021-06-15 12:44:14.352549','82','20',1,'[{\"added\": {}}]',27,1),(269,'2021-06-15 12:44:29.747885','83','21',1,'[{\"added\": {}}]',27,1),(270,'2021-06-15 12:44:41.615557','84','22',1,'[{\"added\": {}}]',27,1),(271,'2021-06-15 12:44:54.533367','85','23',1,'[{\"added\": {}}]',27,1),(272,'2021-06-15 12:45:06.605707','86','24',1,'[{\"added\": {}}]',27,1),(273,'2021-06-15 12:45:19.850361','87','25',1,'[{\"added\": {}}]',27,1),(274,'2021-06-15 12:45:40.601940','88','26',1,'[{\"added\": {}}]',27,1),(275,'2021-06-15 12:46:08.436841','89','27',1,'[{\"added\": {}}]',27,1),(276,'2021-06-15 12:46:35.421351','90','28',1,'[{\"added\": {}}]',27,1),(277,'2021-06-15 12:46:49.806393','91','29',1,'[{\"added\": {}}]',27,1),(278,'2021-06-15 12:47:05.808764','92','30',1,'[{\"added\": {}}]',27,1),(279,'2021-06-15 12:47:21.938973','93','31',1,'[{\"added\": {}}]',27,1),(280,'2021-06-15 12:47:42.450764','94','32',1,'[{\"added\": {}}]',27,1),(281,'2021-06-15 12:48:04.155336','95','33',1,'[{\"added\": {}}]',27,1),(282,'2021-06-15 12:48:17.087972','96','34',1,'[{\"added\": {}}]',27,1),(283,'2021-06-15 12:48:31.266026','97','35',1,'[{\"added\": {}}]',27,1),(284,'2021-06-15 12:48:44.208124','98','36',1,'[{\"added\": {}}]',27,1),(285,'2021-06-15 12:49:20.485911','99','37',1,'[{\"added\": {}}]',27,1),(286,'2021-06-15 12:49:42.276909','100','38',1,'[{\"added\": {}}]',27,1),(287,'2021-06-15 12:49:58.103118','101','39',1,'[{\"added\": {}}]',27,1),(288,'2021-06-15 12:50:14.861610','102','40',1,'[{\"added\": {}}]',27,1),(289,'2021-06-15 12:50:28.817878','103','41',1,'[{\"added\": {}}]',27,1),(290,'2021-06-15 12:50:42.644241','104','42',1,'[{\"added\": {}}]',27,1),(291,'2021-06-15 12:52:04.894761','105','43',1,'[{\"added\": {}}]',27,1),(292,'2021-06-15 14:26:25.251542','5','callcenter',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',2,1),(293,'2021-06-15 14:42:59.071097','37','test',3,'',17,1),(294,'2021-06-15 14:43:28.910854','228','O\'chirilgan',3,'',24,1),(295,'2021-06-15 14:43:28.912510','227','O\'chirilgan',3,'',24,1),(296,'2021-06-15 14:43:28.913322','226','O\'chirilgan',3,'',24,1),(297,'2021-06-15 14:43:28.914725','225','O\'chirilgan',3,'',24,1),(298,'2021-06-15 14:43:41.544487','105','43',3,'',27,1),(299,'2021-06-15 14:43:41.546652','104','42',3,'',27,1),(300,'2021-06-15 14:43:41.547812','103','41',3,'',27,1),(301,'2021-06-15 14:43:41.548728','102','40',3,'',27,1),(302,'2021-06-15 14:43:41.550105','101','39',3,'',27,1),(303,'2021-06-15 14:43:41.550884','100','38',3,'',27,1),(304,'2021-06-15 14:43:41.551801','99','37',3,'',27,1),(305,'2021-06-15 14:43:41.552592','98','36',3,'',27,1),(306,'2021-06-15 14:43:41.554076','97','35',3,'',27,1),(307,'2021-06-15 14:43:41.554941','96','34',3,'',27,1),(308,'2021-06-15 14:43:41.555649','95','33',3,'',27,1),(309,'2021-06-15 14:43:41.556514','94','32',3,'',27,1),(310,'2021-06-15 14:43:41.557363','93','31',3,'',27,1),(311,'2021-06-15 14:43:41.558970','92','30',3,'',27,1),(312,'2021-06-15 14:43:41.559768','91','29',3,'',27,1),(313,'2021-06-15 14:43:41.560730','90','28',3,'',27,1),(314,'2021-06-15 14:43:41.562251','89','27',3,'',27,1),(315,'2021-06-15 14:43:41.563156','88','26',3,'',27,1),(316,'2021-06-15 14:43:41.564215','87','25',3,'',27,1),(317,'2021-06-15 14:43:41.567050','86','24',3,'',27,1),(318,'2021-06-15 14:43:41.567924','85','23',3,'',27,1),(319,'2021-06-15 14:43:41.568649','84','22',3,'',27,1),(320,'2021-06-15 14:43:41.569903','83','21',3,'',27,1),(321,'2021-06-15 14:43:41.570809','82','20',3,'',27,1),(322,'2021-06-15 14:43:41.571730','81','19',3,'',27,1),(323,'2021-06-15 14:43:41.572449','80','18',3,'',27,1),(324,'2021-06-15 14:43:41.573143','79','17',3,'',27,1),(325,'2021-06-15 14:43:41.574311','78','16',3,'',27,1),(326,'2021-06-15 14:43:41.575045','77','15',3,'',27,1),(327,'2021-06-15 14:43:41.575818','76','14',3,'',27,1),(328,'2021-06-15 14:43:41.576537','75','32 Besetka',3,'',27,1),(329,'2021-06-15 14:43:41.577287','74','31 Besetka',3,'',27,1),(330,'2021-06-15 14:43:41.578691','73','13',3,'',27,1),(331,'2021-06-15 14:43:41.579470','72','30 Besetka',3,'',27,1),(332,'2021-06-15 14:43:41.580173','71','29 Besetka',3,'',27,1),(333,'2021-06-15 14:43:41.580876','70','12',3,'',27,1),(334,'2021-06-15 14:43:41.582016','69','28 Besetka',3,'',27,1),(335,'2021-06-15 14:43:41.582757','68','27 Besetka',3,'',27,1),(336,'2021-06-15 14:43:41.583427','67','11',3,'',27,1),(337,'2021-06-15 14:43:41.584096','66','26 Besetka',3,'',27,1),(338,'2021-06-15 14:43:41.584821','65','10',3,'',27,1),(339,'2021-06-15 14:43:41.586090','64','25 Besetka',3,'',27,1),(340,'2021-06-15 14:43:41.586772','63','9',3,'',27,1),(341,'2021-06-15 14:43:41.587420','62','24 xona',3,'',27,1),(342,'2021-06-15 14:43:41.588087','61','23 xona',3,'',27,1),(343,'2021-06-15 14:43:41.588777','60','8',3,'',27,1),(344,'2021-06-15 14:43:41.590056','59','22 xona',3,'',27,1),(345,'2021-06-15 14:43:41.590824','58','7',3,'',27,1),(346,'2021-06-15 14:43:41.591521','57','21 xona',3,'',27,1),(347,'2021-06-15 14:43:41.592217','56','6',3,'',27,1),(348,'2021-06-15 14:43:41.593042','55','20 xona',3,'',27,1),(349,'2021-06-15 14:43:41.594634','54','19 xona',3,'',27,1),(350,'2021-06-15 14:43:41.595674','53','5',3,'',27,1),(351,'2021-06-15 14:43:41.596771','52','18 xona',3,'',27,1),(352,'2021-06-15 14:43:41.598700','51','4',3,'',27,1),(353,'2021-06-15 14:43:41.599861','50','17 xona',3,'',27,1),(354,'2021-06-15 14:43:41.600869','49','3',3,'',27,1),(355,'2021-06-15 14:43:41.602337','48','16 xona',3,'',27,1),(356,'2021-06-15 14:43:41.603193','47','15 xona',3,'',27,1),(357,'2021-06-15 14:43:41.603932','46','14 xona',3,'',27,1),(358,'2021-06-15 14:43:41.604652','45','13 xona',3,'',27,1),(359,'2021-06-15 14:43:41.606049','44','12 xona',3,'',27,1),(360,'2021-06-15 14:43:41.606841','43','11 xona',3,'',27,1),(361,'2021-06-15 14:43:41.607659','42','2',3,'',27,1),(362,'2021-06-15 14:43:41.608519','41','10',3,'',27,1),(363,'2021-06-15 14:43:41.609287','40','323 xona',3,'',27,1),(364,'2021-06-15 14:43:41.610665','39','1',3,'',27,1),(365,'2021-06-15 14:43:41.611378','38','322 xona',3,'',27,1),(366,'2021-06-15 14:43:41.612070','37','9 xona',3,'',27,1),(367,'2021-06-15 14:43:41.612847','36','321 xona',3,'',27,1),(368,'2021-06-15 14:43:41.614524','35','320 xona',3,'',27,1),(369,'2021-06-15 14:43:41.617102','34','319 xona',3,'',27,1),(370,'2021-06-15 14:43:41.618668','33','307 xona',3,'',27,1),(371,'2021-06-15 14:43:41.619643','32','306 xona',3,'',27,1),(372,'2021-06-15 14:43:41.620577','31','8 xona',3,'',27,1),(373,'2021-06-15 14:43:41.622280','30','305 xona',3,'',27,1),(374,'2021-06-15 14:43:41.623290','29','7 xona',3,'',27,1),(375,'2021-06-15 14:43:41.624227','28','304 xona',3,'',27,1),(376,'2021-06-15 14:43:41.625198','27','6 xona',3,'',27,1),(377,'2021-06-15 14:43:41.626896','26','303 xona',3,'',27,1),(378,'2021-06-15 14:43:41.627953','25','301 xona',3,'',27,1),(379,'2021-06-15 14:43:41.629053','24','5 xona',3,'',27,1),(380,'2021-06-15 14:43:41.630623','23','302 xona',3,'',27,1),(381,'2021-06-15 14:43:41.631553','22','300 xona',3,'',27,1),(382,'2021-06-15 14:43:41.632454','21','223 xona',3,'',27,1),(383,'2021-06-15 14:43:41.633374','20','4 xona',3,'',27,1),(384,'2021-06-15 14:43:41.634836','19','222 xona',3,'',27,1),(385,'2021-06-15 14:43:41.635791','18','221 xona',3,'',27,1),(386,'2021-06-15 14:43:41.636773','17','220 xona',3,'',27,1),(387,'2021-06-15 14:43:41.638219','16','219 xona',3,'',27,1),(388,'2021-06-15 14:43:41.639240','15','3 xona',3,'',27,1),(389,'2021-06-15 14:43:41.640102','14','206 xona',3,'',27,1),(390,'2021-06-15 14:43:41.641054','13','205 xona',3,'',27,1),(391,'2021-06-15 14:43:41.642473','12','203 xona',3,'',27,1),(392,'2021-06-15 14:43:41.643390','11','202 xona',3,'',27,1),(393,'2021-06-15 14:43:41.644383','10','201 xona',3,'',27,1),(394,'2021-06-15 14:43:41.645421','9','201 xona',3,'',27,1),(395,'2021-06-15 14:43:41.646870','8','200 xona',3,'',27,1),(396,'2021-06-15 14:43:41.647800','7','2 xona',3,'',27,1),(397,'2021-06-15 14:43:41.648694','6','1 xona',3,'',27,1),(398,'2021-06-15 14:44:08.789792','15','2021-06-02 06:17:00',3,'',13,1),(399,'2021-06-15 14:44:08.792125','14','2021-05-29 11:16:00',3,'',13,1),(400,'2021-06-15 14:44:08.793613','13','2021-05-11 18:15:00',3,'',13,1),(401,'2021-06-15 14:44:08.795549','12','2021-05-09 18:58:00',3,'',13,1),(402,'2021-06-15 14:44:08.796608','11','2021-05-30 18:02:00',3,'',13,1),(403,'2021-06-15 14:44:08.797957','10','2021-05-25 17:03:00',3,'',13,1),(404,'2021-06-15 14:44:08.798801','9','2021-05-07 18:50:00',3,'',13,1),(405,'2021-06-15 14:44:08.799561','8','2021-05-22 18:30:00',3,'',13,1),(406,'2021-06-15 14:44:08.800315','7','2021-05-05 07:00:00',3,'',13,1),(407,'2021-06-15 14:44:08.801124','6','2021-05-22 07:00:00',3,'',13,1),(408,'2021-06-15 14:44:08.802272','5','2021-05-22 07:00:00',3,'',13,1),(409,'2021-06-15 14:44:08.803176','4','2021-05-03 06:11:00',3,'',13,1),(410,'2021-06-15 14:44:08.803883','3','2021-05-13 18:11:00',3,'',13,1),(411,'2021-06-15 14:44:08.804670','2','2021-05-27 18:11:00',3,'',13,1),(412,'2021-06-15 14:44:08.806054','1','2021-05-23 12:54:00',3,'',13,1),(413,'2021-06-15 14:44:22.353972','1','khfsdkmv.f',3,'',11,1),(414,'2021-06-15 14:44:31.106331','1','uytgdqyhweg',3,'',10,1),(415,'2021-06-15 14:57:08.566993','106','200 xona',1,'[{\"added\": {}}]',27,1),(416,'2021-06-15 14:57:22.537254','107','201 xona',1,'[{\"added\": {}}]',27,1),(417,'2021-06-15 14:57:39.872815','108','202 xona',1,'[{\"added\": {}}]',27,1),(418,'2021-06-15 14:57:55.513038','109','203 xona',1,'[{\"added\": {}}]',27,1),(419,'2021-06-15 14:58:16.049295','110','204 xona',1,'[{\"added\": {}}]',27,1),(420,'2021-06-15 14:58:30.605796','111','205 xona',1,'[{\"added\": {}}]',27,1),(421,'2021-06-15 14:58:40.560934','112','206 xona',1,'[{\"added\": {}}]',27,1),(422,'2021-06-15 14:58:54.019413','113','219 xona',1,'[{\"added\": {}}]',27,1),(423,'2021-06-15 14:59:03.203419','114','220 xona',1,'[{\"added\": {}}]',27,1),(424,'2021-06-15 14:59:15.083402','115','221 xona',1,'[{\"added\": {}}]',27,1),(425,'2021-06-15 14:59:27.101820','116','222 xona',1,'[{\"added\": {}}]',27,1),(426,'2021-06-15 14:59:37.392486','117','223 xona',1,'[{\"added\": {}}]',27,1),(427,'2021-06-15 14:59:50.978484','118','300 xona',1,'[{\"added\": {}}]',27,1),(428,'2021-06-15 15:00:06.923007','119','301 xona',1,'[{\"added\": {}}]',27,1),(429,'2021-06-15 15:00:40.525612','120','1 xona',1,'[{\"added\": {}}]',27,1),(430,'2021-06-15 15:00:44.163597','121','302 xona',1,'[{\"added\": {}}]',27,1),(431,'2021-06-15 15:00:54.151600','122','2 xona',1,'[{\"added\": {}}]',27,1),(432,'2021-06-15 15:00:54.553363','123','303 xona',1,'[{\"added\": {}}]',27,1),(433,'2021-06-15 15:01:03.994470','124','304 xona',1,'[{\"added\": {}}]',27,1),(434,'2021-06-15 15:01:12.714272','125','305 xona',1,'[{\"added\": {}}]',27,1),(435,'2021-06-15 15:01:25.628818','126','306 xona',1,'[{\"added\": {}}]',27,1),(436,'2021-06-15 15:01:27.907095','127','3 xona',1,'[{\"added\": {}}]',27,1),(437,'2021-06-15 15:01:36.354858','128','307 xona',1,'[{\"added\": {}}]',27,1),(438,'2021-06-15 15:01:52.776587','129','319 xona',1,'[{\"added\": {}}]',27,1),(439,'2021-06-15 15:02:06.856068','130','320 xona',1,'[{\"added\": {}}]',27,1),(440,'2021-06-15 15:02:18.443427','131','321 xona',1,'[{\"added\": {}}]',27,1),(441,'2021-06-15 15:02:27.969424','132','322 xona',1,'[{\"added\": {}}]',27,1),(442,'2021-06-15 15:02:36.897968','133','4 xona',1,'[{\"added\": {}}]',27,1),(443,'2021-06-15 15:02:55.323290','134','5 xona',1,'[{\"added\": {}}]',27,1),(444,'2021-06-15 15:03:15.442748','135','6 xona',1,'[{\"added\": {}}]',27,1),(445,'2021-06-15 15:03:21.501718','136','323 xona',1,'[{\"added\": {}}]',27,1),(446,'2021-06-15 15:03:28.169581','137','7 xona',1,'[{\"added\": {}}]',27,1),(447,'2021-06-15 15:03:40.306105','138','8 xona',1,'[{\"added\": {}}]',27,1),(448,'2021-06-15 15:04:00.231051','139','9 xona',1,'[{\"added\": {}}]',27,1),(449,'2021-06-15 15:04:24.610550','140','10 xona',1,'[{\"added\": {}}]',27,1),(450,'2021-06-15 15:04:33.767941','141','1',1,'[{\"added\": {}}]',27,1),(451,'2021-06-15 15:04:38.538467','142','11 xona',1,'[{\"added\": {}}]',27,1),(452,'2021-06-15 15:04:52.504617','143','12 xona',1,'[{\"added\": {}}]',27,1),(453,'2021-06-15 15:04:53.514661','144','2',1,'[{\"added\": {}}]',27,1),(454,'2021-06-15 15:05:23.385586','145','3',1,'[{\"added\": {}}]',27,1),(455,'2021-06-15 15:05:32.641699','146','13 xona',1,'[{\"added\": {}}]',27,1),(456,'2021-06-15 15:05:42.232556','147','4',1,'[{\"added\": {}}]',27,1),(457,'2021-06-15 15:05:44.803389','148','14 xona',1,'[{\"added\": {}}]',27,1),(458,'2021-06-15 15:05:56.960531','149','15 xona',1,'[{\"added\": {}}]',27,1),(459,'2021-06-15 15:06:09.512802','150','16 xona',1,'[{\"added\": {}}]',27,1),(460,'2021-06-15 15:06:11.109216','151','5',1,'[{\"added\": {}}]',27,1),(461,'2021-06-15 15:06:22.061558','152','17 xona',1,'[{\"added\": {}}]',27,1),(462,'2021-06-15 15:06:40.459316','153','18 xona',1,'[{\"added\": {}}]',27,1),(463,'2021-06-15 15:06:48.654928','154','6',1,'[{\"added\": {}}]',27,1),(464,'2021-06-15 15:06:52.654230','155','19 xona',1,'[{\"added\": {}}]',27,1),(465,'2021-06-15 15:07:13.104920','156','20 xona',1,'[{\"added\": {}}]',27,1),(466,'2021-06-15 15:07:39.107415','157','21 xona',1,'[{\"added\": {}}]',27,1),(467,'2021-06-15 15:07:53.009290','158','22 xona',1,'[{\"added\": {}}]',27,1),(468,'2021-06-15 15:08:05.536085','159','23 xona',1,'[{\"added\": {}}]',27,1),(469,'2021-06-15 15:08:22.047736','160','24 xona',1,'[{\"added\": {}}]',27,1),(470,'2021-06-15 15:09:25.093910','161','7',1,'[{\"added\": {}}]',27,1),(471,'2021-06-15 15:09:35.521087','160','24 xona',2,'[{\"changed\": {\"fields\": [\"Capacity\"]}}]',27,1),(472,'2021-06-15 15:09:42.752493','159','23 xona',2,'[]',27,1),(473,'2021-06-15 15:09:52.890840','160','24 xona',2,'[]',27,1),(474,'2021-06-15 15:10:14.927289','162','25 Besetka',1,'[{\"added\": {}}]',27,1),(475,'2021-06-15 15:10:27.048797','163','26 Besetka',1,'[{\"added\": {}}]',27,1),(476,'2021-06-15 15:10:44.219731','164','27 Besetka',1,'[{\"added\": {}}]',27,1),(477,'2021-06-15 15:11:01.713665','165','28 Besetka',1,'[{\"added\": {}}]',27,1),(478,'2021-06-15 15:11:17.619597','4','eskishahar',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',2,1),(479,'2021-06-15 15:11:24.517104','3','yangibozor',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',2,1),(480,'2021-06-15 15:11:27.212407','166','29 Besetka',1,'[{\"added\": {}}]',27,1),(481,'2021-06-15 15:11:50.145549','167','30 Besetka',1,'[{\"added\": {}}]',27,1),(482,'2021-06-15 15:12:03.285053','168','31 Besetka',1,'[{\"added\": {}}]',27,1),(483,'2021-06-15 15:12:05.551208','169','8',1,'[{\"added\": {}}]',27,1),(484,'2021-06-15 15:12:21.445805','170','32 Besetka',1,'[{\"added\": {}}]',27,1),(485,'2021-06-15 15:12:24.883407','171','9',1,'[{\"added\": {}}]',27,1),(486,'2021-06-15 15:12:47.060070','172','10',1,'[{\"added\": {}}]',27,1),(487,'2021-06-15 15:13:01.263460','173','11',1,'[{\"added\": {}}]',27,1),(488,'2021-06-15 15:13:12.060098','1','Yangi bozor',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(489,'2021-06-15 15:13:20.186466','174','12',1,'[{\"added\": {}}]',27,1),(490,'2021-06-15 15:13:24.761288','2','Eski shahar',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(491,'2021-06-15 15:13:34.108917','175','13',1,'[{\"added\": {}}]',27,1),(492,'2021-06-15 15:13:50.879677','176','14',1,'[{\"added\": {}}]',27,1),(493,'2021-06-15 15:14:04.549789','177','15',1,'[{\"added\": {}}]',27,1),(494,'2021-06-15 15:14:06.123499','1','Yangi bozor',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(495,'2021-06-15 15:14:22.860251','178','16',1,'[{\"added\": {}}]',27,1),(496,'2021-06-15 15:14:45.855335','179','17',1,'[{\"added\": {}}]',27,1),(497,'2021-06-15 15:15:07.364070','180','18',1,'[{\"added\": {}}]',27,1),(498,'2021-06-15 15:15:37.726104','181','19',1,'[{\"added\": {}}]',27,1),(499,'2021-06-15 15:15:52.894458','182','20',1,'[{\"added\": {}}]',27,1),(500,'2021-06-15 15:16:06.646673','183','21',1,'[{\"added\": {}}]',27,1),(501,'2021-06-15 15:16:21.834361','184','22',1,'[{\"added\": {}}]',27,1),(502,'2021-06-15 15:16:54.932654','185','23',1,'[{\"added\": {}}]',27,1),(503,'2021-06-15 15:17:13.054334','186','24',1,'[{\"added\": {}}]',27,1),(504,'2021-06-15 15:17:27.235891','187','25',1,'[{\"added\": {}}]',27,1),(505,'2021-06-15 15:17:47.095376','188','26',1,'[{\"added\": {}}]',27,1),(506,'2021-06-15 15:18:03.663255','189','27',1,'[{\"added\": {}}]',27,1),(507,'2021-06-15 15:18:23.199306','190','28',1,'[{\"added\": {}}]',27,1),(508,'2021-06-15 15:18:37.653169','191','29',1,'[{\"added\": {}}]',27,1),(509,'2021-06-15 15:18:54.410946','192','30',1,'[{\"added\": {}}]',27,1),(510,'2021-06-15 15:19:11.878349','193','31',1,'[{\"added\": {}}]',27,1),(511,'2021-06-15 15:19:28.546983','194','32',1,'[{\"added\": {}}]',27,1),(512,'2021-06-15 15:19:39.570354','195','33',1,'[{\"added\": {}}]',27,1),(513,'2021-06-15 15:20:06.279838','196','34',1,'[{\"added\": {}}]',27,1),(514,'2021-06-15 15:20:21.437613','197','35',1,'[{\"added\": {}}]',27,1),(515,'2021-06-15 15:20:42.414585','3','Letniy',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(516,'2021-06-15 15:20:50.438062','198','36',1,'[{\"added\": {}}]',27,1),(517,'2021-06-15 15:21:02.711136','199','37',1,'[{\"added\": {}}]',27,1),(518,'2021-06-15 15:21:19.105393','200','38',1,'[{\"added\": {}}]',27,1),(519,'2021-06-15 15:21:23.923491','1','Yangi bozor',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(520,'2021-06-15 15:21:33.792186','201','39',1,'[{\"added\": {}}]',27,1),(521,'2021-06-15 15:21:54.032076','202','40',1,'[{\"added\": {}}]',27,1),(522,'2021-06-15 15:22:11.332521','203','41',1,'[{\"added\": {}}]',27,1),(523,'2021-06-15 15:22:28.635125','204','42',1,'[{\"added\": {}}]',27,1),(524,'2021-06-15 15:22:45.705335','205','43',1,'[{\"added\": {}}]',27,1),(525,'2021-06-15 15:30:57.718849','3','Letniy',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(526,'2021-06-15 15:37:55.873650','2','Eski shahar',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(527,'2021-06-15 15:47:16.451378','2','Eski shahar',2,'[{\"changed\": {\"fields\": [\"Chat id\"]}}]',26,1),(528,'2021-06-15 15:48:22.046101','5','callcenter',3,'',2,1),(529,'2021-06-15 15:48:22.047897','2','crm',3,'',2,1),(530,'2021-06-15 15:48:22.048699','6','muhabbat',3,'',2,1),(531,'2021-06-15 15:50:43.675395','8','nodira2000',1,'[{\"added\": {}}]',2,1),(532,'2021-06-15 15:51:16.009783','8','nodira2000',2,'[{\"changed\": {\"fields\": [\"First name\", \"Company\", \"Is callcenter\"]}}]',2,1),(533,'2021-06-15 15:51:46.143306','9','shahnoza',1,'[{\"added\": {}}]',2,1),(534,'2021-06-15 15:52:07.390269','9','shahnoza',2,'[{\"changed\": {\"fields\": [\"First name\", \"Company\", \"Is callcenter\"]}}]',2,1),(535,'2021-06-15 15:53:01.162474','8','nodira2000',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',2,1),(536,'2021-06-15 15:54:02.861850','234','O\'chirilgan',3,'',24,1),(537,'2021-06-15 15:54:02.864344','233','O\'chirilgan',3,'',24,1),(538,'2021-06-15 15:54:02.865462','232','O\'chirilgan',3,'',24,1),(539,'2021-06-15 15:54:02.867158','231','O\'chirilgan',3,'',24,1),(540,'2021-06-15 15:54:02.868354','230','O\'chirilgan',3,'',24,1),(541,'2021-06-15 15:54:02.869315','229','O\'chirilgan',3,'',24,1),(542,'2021-06-15 16:37:18.318736','4','eskishahar',2,'[{\"changed\": {\"fields\": [\"Filial\"]}}]',2,1),(543,'2021-06-16 10:23:10.173191','10','callcenter',1,'[{\"added\": {}}]',2,1),(544,'2021-06-16 10:23:18.409274','10','callcenter',2,'[{\"changed\": {\"fields\": [\"Company\", \"Is callcenter\"]}}]',2,1),(545,'2021-06-16 10:52:05.440564','1','movarounnahr',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',2,1),(546,'2021-06-16 11:00:40.687430','1','movarounnahr',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',2,1),(547,'2021-06-16 11:00:55.745123','11','manager',1,'[{\"added\": {}}]',2,1),(548,'2021-06-16 11:01:07.246665','11','manager',2,'[{\"changed\": {\"fields\": [\"First name\", \"Company\", \"Is director\"]}}]',2,1),(549,'2021-06-16 11:01:36.051903','12','marketolog',1,'[{\"added\": {}}]',2,1),(550,'2021-06-16 11:01:48.015918','12','marketolog',2,'[{\"changed\": {\"fields\": [\"First name\", \"Company\", \"Is director\"]}}]',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'account','account'),(1,'account','company'),(26,'account','filial'),(3,'admin','logentry'),(5,'auth','group'),(4,'auth','permission'),(15,'board','categoryproduct'),(16,'board','district'),(17,'board','lead'),(21,'board','leadaction'),(20,'board','region'),(19,'board','task'),(18,'board','telegram_user'),(22,'bot','bot'),(23,'bot','botupdate'),(24,'buyurtma','books'),(25,'buyurtma','filial'),(27,'buyurtma','rooms'),(28,'buyurtma','typeroom'),(6,'contenttypes','contenttype'),(14,'goal','goal'),(13,'main','calendar'),(12,'main','debtors'),(8,'main','importtemplate'),(11,'main','objections'),(10,'main','objectionwrite'),(9,'main','script'),(7,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-21 09:56:19.244846'),(2,'contenttypes','0002_remove_content_type_name','2021-04-21 09:56:19.276036'),(3,'auth','0001_initial','2021-04-21 09:56:19.316373'),(4,'auth','0002_alter_permission_name_max_length','2021-04-21 09:56:19.377924'),(5,'auth','0003_alter_user_email_max_length','2021-04-21 09:56:19.385237'),(6,'auth','0004_alter_user_username_opts','2021-04-21 09:56:19.391249'),(7,'auth','0005_alter_user_last_login_null','2021-04-21 09:56:19.397612'),(8,'auth','0006_require_contenttypes_0002','2021-04-21 09:56:19.399633'),(9,'auth','0007_alter_validators_add_error_messages','2021-04-21 09:56:19.405114'),(10,'auth','0008_alter_user_username_max_length','2021-04-21 09:56:19.411475'),(11,'auth','0009_alter_user_last_name_max_length','2021-04-21 09:56:19.417797'),(12,'auth','0010_alter_group_name_max_length','2021-04-21 09:56:19.426194'),(13,'auth','0011_update_proxy_permissions','2021-04-21 09:56:19.432707'),(14,'auth','0012_alter_user_first_name_max_length','2021-04-21 09:56:19.438703'),(15,'account','0001_initial','2021-04-21 09:56:19.493744'),(16,'admin','0001_initial','2021-04-21 09:56:19.614469'),(17,'admin','0002_logentry_remove_auto_add','2021-04-21 09:56:19.644354'),(18,'admin','0003_logentry_add_action_flag_choices','2021-04-21 09:56:19.653468'),(19,'board','0001_initial','2021-04-21 09:56:19.833743'),(20,'bot','0001_initial','2021-04-21 09:56:20.071528'),(21,'goal','0001_initial','2021-04-21 09:56:20.131538'),(22,'main','0001_initial','2021-04-21 09:56:20.296679'),(23,'sessions','0001_initial','2021-04-21 09:56:20.395089'),(24,'buyurtma','0001_initial','2021-04-21 12:06:01.053788'),(25,'account','0002_auto_20210424_1341','2021-04-24 08:41:39.858306'),(26,'buyurtma','0002_auto_20210424_1341','2021-04-24 08:41:40.106556'),(27,'account','0003_filial_chat_id','2021-04-26 09:41:05.077094'),(28,'buyurtma','0003_remove_books_ordertime','2021-06-11 10:08:44.836554'),(29,'buyurtma','0004_remove_books_date','2021-06-11 10:10:54.250829'),(30,'buyurtma','0005_auto_20210611_1514','2021-06-11 10:14:15.219156'),(31,'buyurtma','0006_auto_20210611_1601','2021-06-11 11:01:22.224777'),(32,'buyurtma','0007_auto_20210611_1602','2021-06-11 11:03:03.431295'),(33,'main','0002_debtors_comment','2021-06-12 17:21:03.003455'),(34,'buyurtma','0008_auto_20210615_1401','2021-06-15 14:01:44.714584'),(35,'buyurtma','0009_books_address','2021-06-16 09:20:20.480049'),(36,'main','0003_auto_20210616_1050','2021-06-16 10:51:05.500516'),(37,'board','0002_lead_where','2021-06-16 11:54:48.761603');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0kcimvxvujwjgwxv6llmy4heb04lrx8y','.eJxVjDsOwjAQBe_iGln-fyjpcwZr7V3hALKlOKkQdyeRUkA7M--9WYJtrWkbtKQZ2ZV5dvllGcqT2iHwAe3eeeltXebMj4SfdvCpI71uZ_t3UGHUfR3RoMNcpA4mOgNSAEYoirI0hF4SKS00Fhs87UBpFEA2B-vA6KiAfb77aThZ:1lt2UA:DXtA9H5YDVODmOl6xTxXEcRucGnEgwoM6tMqctAUWYE','2021-06-29 11:23:42.813734'),('36gzhs4l0ezhqe3hgmz88nzr9tvqa7pi','.eJxVjE0OwiAYRO_C2hChBYpL956BfH9I1dCktCvj3W2TLnQ3mfdm3irBupS0NpnTyOqiojr9dgj0lLoDfkC9T5qmuswj6l3RB236NrG8rof7d1CglW1tnKcg2cZgsiWUoefssumZQkYnHXs8GxEx1BFtEaLj4Afw3jJSBvX5Ag83OVc:1lt7qv:21TFYfSNEn7PisSPFiTXM3Qdf6wtb3Ly9cqWNqW3EQ4','2021-06-29 17:07:33.478436'),('57ic60srh6yhqwjdys84f3xb35wmynpe','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1lt3U4:Ap4v-jqtmDKqDzjvOO0smV7Wew60XgDinnR9HXxvuKY','2021-06-29 12:27:40.923493'),('5xrq4e2tqntyu76hcan7q5f0jw53k465','.eJxVjDsOwjAQBe_iGln-fyjpcwZr7V3hALKlOKkQdyeRUkA7M--9WYJtrWkbtKQZ2ZV5dvllGcqT2iHwAe3eeeltXebMj4SfdvCpI71uZ_t3UGHUfR3RoMNcpA4mOgNSAEYoirI0hF4SKS00Fhs87UBpFEA2B-vA6KiAfb77aThZ:1lt7wy:473iBoWqWy7ZtDJcaID0RqgtoyGFNRWNCcmx8sYjun4','2021-06-29 17:13:48.389456'),('7vd49xeivtb2dbefbmf3gvdps6t2fcny','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1lncms:iJMiaXYCxUCgcXJMq2M6F3xq-8QokOs9Ejw6eIMEcKY','2021-06-14 07:56:38.671597'),('8thuw07sfxtkgcgwru2momuzvjc4klwn','.eJxVjMsKwyAQAP_FcxHWZ-yx936DrO5a0xYDMTmF_nsRcmivM8McIuK-1bh3XuNM4iqMuPyyhPnFbQh6YnssMi9tW-ckRyJP2-V9IX7fzvZvULHXsc1K58BOY0KjOThTPFKgiYOywA5d0N6WlAFSQTBWIymPRsHkFUIRny_xojgC:1lt7mn:E9tNwS_yeYSS7qGPN59dJfgVPsOmfVYafqtBL3BGpgw','2021-06-29 17:03:17.475902'),('8y861yemyedtu9lvlxebkgvpw3txd305','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1lt30u:LVP05mI8vwhdRsOt995w9CWH_TmX2eI1hXO36kKfTE0','2021-06-29 11:57:32.262062'),('94ngaz9iivnodfi4rs744wms07zrm9dx','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1ls2F4:DyaHHHmxaGrIL_8IuMN3Z4VupRyfUYGNxfyaLEcPTHw','2021-06-26 16:55:58.957721'),('aqqr1gx35tfulh8to1pxe97fdgz9xw16','.eJxVjMEOwiAQRP-FsyGwdgU8evcbCMuuUjWQlPZk_HfbpAe9zGHem3mrmJa5xKXLFEdWZ2WNOvyWlPJT6kb4keq96dzqPI2kN0XvtOtrY3lddvfvoKRe1jUcwRlgwmyCCwnXGLINDj0nIJGAQie-oUUw5MNAliQT20AC3hivPl_wMzfa:1ltPQX:v51fK3Z98_gPydQhvsMXHqXZQwgn4L_tjpowuSSnX9o','2021-06-30 11:53:29.053246'),('dtcoecuifak1wz0shitzl11brnhygk00','.eJxVjEEOwiAQRe_C2hAoZSa4dO8ZyAxDpWogKe3KeHdt0oVu_3vvv1SkbS1x63mJs6izcur0uzGlR647kDvVW9Op1XWZWe-KPmjX1yb5eTncv4NCvXxry0wIBoNLwD5ACt57SkFATAB0jCnb0bBM3hgeCJAmwEEcZMshj-r9Ad4qN9k:1lt6Uh:WnK2OW2KisJu-R9ZZ68fu14dWOhitXKZub2GIlA0agA','2021-06-29 15:40:31.513557'),('g7qn6nqoi5e35g8wq5gbsoandp8eahbp','.eJxVjMsKwyAQAP_FcxHWZ-yx936DrO5a0xYDMTmF_nsRcmivM8McIuK-1bh3XuNM4iqMuPyyhPnFbQh6YnssMi9tW-ckRyJP2-V9IX7fzvZvULHXsc1K58BOY0KjOThTPFKgiYOywA5d0N6WlAFSQTBWIymPRsHkFUIRny_xojgC:1lt6TU:Pmkw3uM5lvKJB18Rr1t9jZynTmuG8nr3Ccv7x3L4Yks','2021-06-29 15:39:16.455010'),('gw488k8lqpbtzqfxpmroo7hqc5h3xlfc','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1lmvGk:eDPUfZz4W6NjQNMKXfm-jCTIgJeiT9Dp1pSuqU_CW5U','2021-06-12 09:28:34.064531'),('h7am9g8qqlz8y007fqw49i4mvef3vq9g','.eJxVjEEOwiAQRe_C2hAoZSa4dO8ZyAxDpWogKe3KeHdt0oVu_3vvv1SkbS1x63mJs6izcur0uzGlR647kDvVW9Op1XWZWe-KPmjX1yb5eTncv4NCvXxry0wIBoNLwD5ACt57SkFATAB0jCnb0bBM3hgeCJAmwEEcZMshj-r9Ad4qN9k:1lrvgy:aLRVSboIA9KexlSTU3EXY4b_heFEpfm04-mxQsP_3iE','2021-06-26 09:56:20.753763'),('hb0sr0p5278ry0q4razro6i37hv2jef2','.eJxVjDsOwjAQBe_iGln-fyjpcwZr7V3hALKlOKkQdyeRUkA7M--9WYJtrWkbtKQZ2ZV5dvllGcqT2iHwAe3eeeltXebMj4SfdvCpI71uZ_t3UGHUfR3RoMNcpA4mOgNSAEYoirI0hF4SKS00Fhs87UBpFEA2B-vA6KiAfb77aThZ:1lt7Ln:BssdSTAjZXMY1xIF31s0J9K9yjrYgTEcmRUxIzj2lwk','2021-06-29 16:35:23.001594'),('kz1qx0wb9r5ckjh9r7axslpcty1f3kk7','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1lt3Rc:WZZCbPkCtDcvXovjORuA5PylbzbNk1uPCYjInG_K_So','2021-06-29 12:25:08.685790'),('msp5ui0zeu0saaeg1oiyoo5wt9a8tzw3','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1ltPY5:-ejMpUOw9RIq1UdoTELrfBnVVwkBqVkS7VJpppyd6J8','2021-06-30 12:01:17.997669'),('nl3lgdfu1snw8pmf7jk802yx6d90d4tm','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1lncrG:s5Xvya-bqP86qzZ9T1i7xfrkdTLPwB3ZZunBYp3wjI0','2021-06-14 08:01:10.472107'),('nujbmp4u6xlnhi4jd202kfseoacc7uld','.eJxVjEEOwiAQRe_C2hAoZSa4dO8ZyAxDpWogKe3KeHdt0oVu_3vvv1SkbS1x63mJs6izcur0uzGlR647kDvVW9Op1XWZWe-KPmjX1yb5eTncv4NCvXxry0wIBoNLwD5ACt57SkFATAB0jCnb0bBM3hgeCJAmwEEcZMshj-r9Ad4qN9k:1lt7Kw:Vl7hCHI6wY-R33t8JLHlMDWJmiFDJhXfgMHz4uPfjRM','2021-06-29 16:34:30.278500'),('ouf41n6gs3ozifk8otzs2zvkaqw2mopq','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1ldvIP:lYI4yH33aMguwGrINE-HOrIzLusGzBeHqXgkLH4Tp5M','2021-05-18 13:41:05.726906'),('pu3kai3z44xtq3jfm7eumgnj09v0kdct','.eJxVjMsKwyAQAP_FcxHWZ-yx936DrO5a0xYDMTmF_nsRcmivM8McIuK-1bh3XuNM4iqMuPyyhPnFbQh6YnssMi9tW-ckRyJP2-V9IX7fzvZvULHXsc1K58BOY0KjOThTPFKgiYOywA5d0N6WlAFSQTBWIymPRsHkFUIRny_xojgC:1lt7AW:eIM6U1F00-IHtp46AYt0zYpBPzWVENtqaMX5d4VM7U0','2021-06-29 16:23:44.475284'),('qdhrgqfu0dcfl1b2uzu7d8xidecv78a5','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1lm8Xa:cjvgaMOlt5uhMakNrNHOYbT8-S9LRvDyE-CYm7uD6PE','2021-06-10 05:26:42.556623'),('rlqtcvr9fp6yenaybt6mtvrwb31iegof','.eJxVjEEOwiAQRe_C2hAoZSa4dO8ZyAxDpWogKe3KeHdt0oVu_3vvv1SkbS1x63mJs6izcur0uzGlR647kDvVW9Op1XWZWe-KPmjX1yb5eTncv4NCvXxry0wIBoNLwD5ACt57SkFATAB0jCnb0bBM3hgeCJAmwEEcZMshj-r9Ad4qN9k:1lrywh:lQlFipFf10UTPH9PeF4_GidW1BXi6MhbgCEub_B1QCE','2021-06-26 13:24:47.907825'),('s4m2yuqrxfglnycyibon6xbyyz2t4ryl','.eJxVjMsKwyAQAP_FcxHWZ-yx936DrO5a0xYDMTmF_nsRcmivM8McIuK-1bh3XuNM4iqMuPyyhPnFbQh6YnssMi9tW-ckRyJP2-V9IX7fzvZvULHXsc1K58BOY0KjOThTPFKgiYOywA5d0N6WlAFSQTBWIymPRsHkFUIRny_xojgC:1lt7Jb:UnI8AyeROtHtFev07GfjGGZsPrRlttd19GO07CG_oq4','2021-06-29 16:33:07.539203'),('xqy88huxtgdnb1ek5sgjg3ac468xngiq','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1laWpp:uSjjyahXgdGIRTwUIfKgIIJGhUhthPzwPZVJ7h15WoU','2021-05-09 04:57:33.567881'),('xuq2ntlbb3vfjit3nbja6qeqg24ygijs','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1laE27:iKaxkHsoJJdrE4QGHLTrA5OhK2UO_RfYLq38tqTOeQM','2021-05-08 08:52:59.853856'),('ygodqaavaosi54dyburjam939jij5fpg','.eJxVjEEOwiAQRe_C2hCgAlOX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERVpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eOZ2e0Gw277C1ZxhFIAYElHrIxJimlNTEoQMwZoxusdp6iSs54DSTeH944N8o:1layNP:LXjD7S14SHV239OKsONGjsTJsNaPUfm6l_jnJHlzziI','2021-05-10 10:22:03.958021'),('yj7hd4q6n4zrt7pc1lirstn7zk1bipvz','.eJxVjEEOwiAQRe_C2hCgtMO4dO8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnEWWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLa-P0vBzu30GhXr51Jm14AHbOZZrsmCAkm9EBWedw0oyIzGwSDKQVgxmjUtECI6DV2oj3B-bTN2c:1lt3WC:Fj7NwIfmqrzUONa2x-pW5k1UySeoH5VGbXDjz8PpIZc','2021-06-29 12:29:52.951974');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goal_goal`
--

DROP TABLE IF EXISTS `goal_goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goal_goal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(25) NOT NULL,
  `savdo` int(11) NOT NULL,
  `mijoz_soni` int(11) NOT NULL,
  `date` date NOT NULL,
  `oy` int(11) NOT NULL,
  `yil` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goal_goal_user_id_617d3bd4_fk_account_account_id` (`user_id`),
  CONSTRAINT `goal_goal_user_id_617d3bd4_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goal_goal`
--

LOCK TABLES `goal_goal` WRITE;
/*!40000 ALTER TABLE `goal_goal` DISABLE KEYS */;
/*!40000 ALTER TABLE `goal_goal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_calendar`
--

DROP TABLE IF EXISTS `main_calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_calendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `color` varchar(255) NOT NULL,
  `event` varchar(255) NOT NULL,
  `date` datetime(6) NOT NULL,
  `created_user_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_calendar_created_user_id_2771823f_fk_account_account_id` (`created_user_id`),
  KEY `main_calendar_user_id_d284e2f0_fk_account_account_id` (`user_id`),
  CONSTRAINT `main_calendar_created_user_id_2771823f_fk_account_account_id` FOREIGN KEY (`created_user_id`) REFERENCES `account_account` (`id`),
  CONSTRAINT `main_calendar_user_id_d284e2f0_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_calendar`
--

LOCK TABLES `main_calendar` WRITE;
/*!40000 ALTER TABLE `main_calendar` DISABLE KEYS */;
INSERT INTO `main_calendar` VALUES (17,'bg-primary','Organization Organization Organization ','2021-06-17 10:52:00.000000',10,1);
/*!40000 ALTER TABLE `main_calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_debtors`
--

DROP TABLE IF EXISTS `main_debtors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_debtors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `summa` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `debt` tinyint(1) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `comment` longtext,
  PRIMARY KEY (`id`),
  KEY `main_debtors_create_user_id_431468f1_fk_account_account_id` (`create_user_id`),
  KEY `main_debtors_user_id_091dbaa7_fk_board_lead_id` (`user_id`),
  CONSTRAINT `main_debtors_create_user_id_431468f1_fk_account_account_id` FOREIGN KEY (`create_user_id`) REFERENCES `account_account` (`id`),
  CONSTRAINT `main_debtors_user_id_091dbaa7_fk_board_lead_id` FOREIGN KEY (`user_id`) REFERENCES `board_lead` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_debtors`
--

LOCK TABLES `main_debtors` WRITE;
/*!40000 ALTER TABLE `main_debtors` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_debtors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_importtemplate`
--

DROP TABLE IF EXISTS `main_importtemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_importtemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `xlsx` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_importtemplate`
--

LOCK TABLES `main_importtemplate` WRITE;
/*!40000 ALTER TABLE `main_importtemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_importtemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_objections`
--

DROP TABLE IF EXISTS `main_objections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_objections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objection` longtext NOT NULL,
  `solution` longtext NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_objections_create_user_id_94853825_fk_account_account_id` (`create_user_id`),
  CONSTRAINT `main_objections_create_user_id_94853825_fk_account_account_id` FOREIGN KEY (`create_user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_objections`
--

LOCK TABLES `main_objections` WRITE;
/*!40000 ALTER TABLE `main_objections` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_objections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_objectionwrite`
--

DROP TABLE IF EXISTS `main_objectionwrite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_objectionwrite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objection` longtext NOT NULL,
  `solution` longtext NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_objectionwrite_create_user_id_dec85800_fk_account_a` (`create_user_id`),
  CONSTRAINT `main_objectionwrite_create_user_id_dec85800_fk_account_a` FOREIGN KEY (`create_user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_objectionwrite`
--

LOCK TABLES `main_objectionwrite` WRITE;
/*!40000 ALTER TABLE `main_objectionwrite` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_objectionwrite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_script`
--

DROP TABLE IF EXISTS `main_script`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_script` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_script_create_user_id_f31c0e9c_fk_account_account_id` (`create_user_id`),
  CONSTRAINT `main_script_create_user_id_f31c0e9c_fk_account_account_id` FOREIGN KEY (`create_user_id`) REFERENCES `account_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_script`
--

LOCK TABLES `main_script` WRITE;
/*!40000 ALTER TABLE `main_script` DISABLE KEYS */;
INSERT INTO `main_script` VALUES (1,'<h1>&nbsp;ассаломуалекум &quot;Моворауннахр&quot; мененджери Зебо лаббай эшитаман!!</h1>\r\n\r\n<p>&nbsp;</p>\r\n',NULL);
/*!40000 ALTER TABLE `main_script` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-16 10:43:50
