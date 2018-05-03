-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: py08
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu2-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add home_user',7,'add_home_user'),(20,'Can change home_user',7,'change_home_user'),(21,'Can delete home_user',7,'delete_home_user'),(22,'Can add users',8,'add_users'),(23,'Can change users',8,'change_users'),(24,'Can delete users',8,'delete_users'),(25,'Can add goods',9,'add_goods'),(26,'Can change goods',9,'change_goods'),(27,'Can delete goods',9,'delete_goods'),(28,'Can add type',10,'add_type'),(29,'Can change type',10,'change_type'),(30,'Can delete type',10,'delete_type'),(31,'Can add orders',11,'add_orders'),(32,'Can change orders',11,'change_orders'),(33,'Can delete orders',11,'delete_orders'),(34,'Can add detail',12,'add_detail'),(35,'Can change detail',12,'change_detail'),(36,'Can delete detail',12,'delete_detail'),(37,'Can add types',10,'add_types'),(38,'Can change types',10,'change_types'),(39,'Can delete types',10,'delete_types'),(40,'Can add turnimg',13,'add_turnimg'),(41,'Can change turnimg',13,'change_turnimg'),(42,'Can delete turnimg',13,'delete_turnimg');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'home','home_user'),(12,'myadmin','detail'),(9,'myadmin','goods'),(11,'myadmin','orders'),(13,'myadmin','turnimg'),(10,'myadmin','types'),(8,'myadmin','users'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-04-11 12:42:35.797237'),(2,'auth','0001_initial','2018-04-11 12:42:38.444131'),(3,'admin','0001_initial','2018-04-11 12:42:38.917405'),(4,'admin','0002_logentry_remove_auto_add','2018-04-11 12:42:39.003876'),(5,'contenttypes','0002_remove_content_type_name','2018-04-11 12:42:39.251899'),(6,'auth','0002_alter_permission_name_max_length','2018-04-11 12:42:39.375072'),(7,'auth','0003_alter_user_email_max_length','2018-04-11 12:42:39.577744'),(8,'auth','0004_alter_user_username_opts','2018-04-11 12:42:39.624291'),(9,'auth','0005_alter_user_last_login_null','2018-04-11 12:42:39.719829'),(10,'auth','0006_require_contenttypes_0002','2018-04-11 12:42:39.729394'),(11,'auth','0007_alter_validators_add_error_messages','2018-04-11 12:42:39.761471'),(12,'auth','0008_alter_user_username_max_length','2018-04-11 12:42:40.068886'),(13,'home','0001_initial','2018-04-11 12:42:40.167846'),(14,'myadmin','0001_initial','2018-04-11 12:42:40.617646'),(15,'sessions','0001_initial','2018-04-11 12:42:40.913489'),(16,'myadmin','0002_auto_20180412_1543','2018-04-12 07:43:23.660608'),(17,'myadmin','0003_auto_20180412_1942','2018-04-12 11:42:20.528613'),(18,'myadmin','0004_auto_20180413_1955','2018-04-13 13:05:54.931408'),(19,'myadmin','0005_auto_20180413_2105','2018-04-13 13:05:55.115954'),(20,'home','0002_delete_home_user','2018-04-19 08:27:43.685316'),(21,'myadmin','0006_auto_20180420_1500','2018-04-20 07:01:01.736402'),(22,'myadmin','0007_orders_nums','2018-04-20 07:33:41.034930'),(23,'myadmin','0006_orders','2018-04-23 01:55:35.743404'),(24,'myadmin','0007_detail','2018-04-23 01:56:24.965378'),(25,'myadmin','0008_auto_20180423_1006','2018-04-23 02:06:25.641431'),(26,'myadmin','0009_auto_20180423_1014','2018-04-23 02:15:00.294811'),(27,'myadmin','0010_turnimg','2018-04-23 16:04:34.338318');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('81y3lykkoy6xwnwmlhi6f3wfswd6i7j2','MzJjMzY0ZWIwOGFkZWJiNWNhNzkyMmUxYTc1MGQxZThiNDJlMjY5ODp7IlZpcFVzZXIiOnsidXNlcm5hbWUiOiJ6aGFuZ3NhbiIsInVpZCI6NDYsImltZyI6InN0YXRpYy9wdWJsaWMvaW1nL2RhZmdzZ2ZnZnZ6dmYuanBnIn0sImNhcnQiOnsiMTkiOnsiaWQiOjE5LCJnb29kcyI6Ilx1OWI0NVx1ODRkZCBBNSIsInBpY25hbWUiOiIvc3RhdGljL3B1YmxpYy9pbWcvMTUyMzg4NTg5Mi40ODAyOTguanBnIiwicHJpY2UiOjMzNTUuMCwibnVtIjoxfSwiNiI6eyJpZCI6NiwiZ29vZHMiOiJcdTliNDVcdTg0ZGQgTm90ZTUyMiIsInBpY25hbWUiOiIvc3RhdGljL3B1YmxpYy9pbWcvMTUyNDU0MTU4Ny41MzU2OTIuanBnIiwicHJpY2UiOjQyOTkuMCwibnVtIjo0fX19','2018-05-10 14:06:35.732825'),('k7acf9nowbiq0hzffr3g5n0kjo6fg09m','MmZhZDZkM2ZkZmI3OWJhNjMyY2ZhY2NkOWQ3OWU1NWNhY2Y3MDEzOTp7IlZpcFVzZXIiOnsidWlkIjo0NiwiaW1nIjoic3RhdGljL3B1YmxpYy9pbWcvZGFmZ3NnZmdmdnp2Zi5qcGciLCJ1c2VybmFtZSI6InpoYW5nc2FuIn19','2018-04-25 11:03:40.893481'),('lmf4ggvphrj1r4xtubd0pydddle1ijee','NTViOTdkOGY2OGE1Y2VlNGE2NTk4ZjY2NzBiM2UwZjBjNjNiN2RkNTp7InZlcmlmeWNvZGUiOiIxODg5IiwiQWRtaW5Mb2dpblMiOnsidWlkIjozMSwiaW1nIjoic3RhdGljL3B1YmxpYy9pbWcvZmZmZmZmZmRkZGRzc2RhZl8zSEI2NW5JLmpwZyIsInVzZXJuYW1lIjoiXHU0ZTFjXHU0ZTFjIn0sIlZpcFVzZXIiOnsidWlkIjo0NiwiaW1nIjoic3RhdGljL3B1YmxpYy9pbWcvZGFmZ3NnZmdmdnp2Zi5qcGciLCJ1c2VybmFtZSI6InpoYW5nc2FuIn0sImNhcnQiOnsiMTIiOnsiZ29vZHMiOiJcdTliNDVcdTg0ZGQgWDYiLCJwaWNuYW1lIjoiL3N0YXRpYy9wdWJsaWMvaW1nLzE1MjM4ODYwMTEuNDM2NDc4NC5qcGciLCJpZCI6MTIsInByaWNlIjozMzMzLjAsIm51bSI6Mn19fQ==','2018-04-25 11:03:04.509078'),('x82lp04q00xpgyfbacx2is1asou1dja3','MTYzODZlZmFkMGMyYjRiNWJjMWQ0MDNlNzEwZjY3NDQ4MDlkZWNmMDp7ImNhcnQiOnsiMTkiOnsiZ29vZHMiOiJcdTliNDVcdTg0ZGQgQTUiLCJwaWNuYW1lIjoiL3N0YXRpYy9wdWJsaWMvaW1nLzE1MjM4ODU4OTIuNDgwMjk4LmpwZyIsImlkIjoxOSwicHJpY2UiOjMzNTUuMCwibnVtIjoyfX19','2018-04-25 11:03:51.330103'),('z7j9ksnwm1vh8wztbeww1kwz5w2u6rw4','NGE5NTIyNzVmZjQ2YzFlY2EwOWY3MTg3NzgyNTk4MWNmMTQ1YzJlNDp7ImNhcnQiOnt9LCJ2ZXJpZnljb2RlIjoiMzk0OCIsIlZpcFVzZXIiOnt9LCJBZG1pbkxvZ2luUyI6eyJpbWciOiJzdGF0aWMvcHVibGljL2ltZy80MzU2ODlmZ2h0eXVrbC5qcGciLCJ1aWQiOjQ5LCJ1c2VybmFtZSI6ImxpeGlhb2xpdSJ9fQ==','2018-05-17 12:08:39.742653');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_detail`
--

DROP TABLE IF EXISTS `myadmin_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goodsid_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `num` int(11) NOT NULL,
  `orderid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orderid_id` (`orderid_id`),
  KEY `myadmin_detail_goodsid_id_931d8f56` (`goodsid_id`),
  CONSTRAINT `myadmin_detail_goodsid_id_931d8f56_fk_myadmin_goods_id` FOREIGN KEY (`goodsid_id`) REFERENCES `myadmin_goods` (`id`),
  CONSTRAINT `myadmin_detail_orderid_id_531207d0_fk_myadmin_orders_id` FOREIGN KEY (`orderid_id`) REFERENCES `myadmin_orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_detail`
--

LOCK TABLES `myadmin_detail` WRITE;
/*!40000 ALTER TABLE `myadmin_detail` DISABLE KEYS */;
INSERT INTO `myadmin_detail` VALUES (1,19,'',3355.00,2,4),(3,12,'',3333.00,1,6),(5,12,'',3333.00,1,7),(7,6,'',4299.00,1,8),(8,12,'',3333.00,2,9),(9,13,'魅蓝 X7',3444.00,1,10),(10,19,'魅蓝 A5',3355.00,3,11),(11,6,'魅蓝 Note5',4299.00,1,12),(12,19,'魅蓝 A5',3355.00,1,13),(13,12,'魅蓝 X6',3333.00,1,14),(14,12,'魅蓝 X6',3333.00,3,15),(15,12,'魅蓝 X6',3333.00,3,16);
/*!40000 ALTER TABLE `myadmin_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_goods`
--

DROP TABLE IF EXISTS `myadmin_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid_id` int(11) NOT NULL,
  `goods` varchar(32) NOT NULL,
  `company` varchar(50) DEFAULT NULL,
  `descr` longtext,
  `price` decimal(6,2) NOT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `state` int(11) NOT NULL,
  `store` int(11) NOT NULL,
  `clicknum` int(11) DEFAULT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_goods_typeid_id_a0810d57` (`typeid_id`),
  CONSTRAINT `myadmin_goods_typeid_id_a0810d57_fk_myadmin_types_id` FOREIGN KEY (`typeid_id`) REFERENCES `myadmin_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_goods`
--

LOCK TABLES `myadmin_goods` WRITE;
/*!40000 ALTER TABLE `myadmin_goods` DISABLE KEYS */;
INSERT INTO `myadmin_goods` VALUES (6,26,'魅蓝 Note522',NULL,NULL,4299.00,'/static/public/img/1524541587.535692.jpg',1,22,0,'2018-04-14 00:05:51.111006'),(7,27,'魅蓝 Note4',NULL,NULL,4955.00,'/static/public/img/1523885159.3244195.png',1,20,0,'2018-04-14 00:06:10.917865'),(8,26,'魅蓝 Note3',NULL,NULL,4333.00,'/static/public/img/1523885205.3580694.jpg',1,33,0,'2018-04-14 00:06:43.409668'),(9,26,'魅蓝 Note1',NULL,NULL,4556.00,'/static/public/img/1523885239.6895185.jpg',1,44,0,'2018-04-14 00:24:19.266613'),(10,26,'魅蓝 Note2',NULL,NULL,4222.00,'/static/public/img/1523885377.952371.jpg',1,22,0,'2018-04-16 13:01:45.826776'),(11,27,'魅蓝 Note6',NULL,NULL,4533.00,'/static/public/img/1523885423.3041704.jpg',1,11,0,'2018-04-16 13:02:45.079813'),(12,29,'魅蓝 X6',NULL,NULL,3333.00,'/static/public/img/1523886011.4364784.jpg',1,11,0,'2018-04-16 13:32:17.057272'),(13,30,'魅蓝 X7',NULL,NULL,3444.00,'/static/public/img/1523885584.6227083.jpg',2,22,0,'2018-04-16 13:33:04.624855'),(14,31,'魅蓝 X3',NULL,NULL,3222.00,'/static/public/img/1523885622.854606.jpg',2,11,0,'2018-04-16 13:33:42.856136'),(15,32,'魅蓝 D5',NULL,NULL,4422.00,'/static/public/img/1523885671.510884.jpg',2,22,0,'2018-04-16 13:34:31.511353'),(17,29,'魅蓝 A9',NULL,NULL,3333.00,'/static/public/img/1523885792.198914.jpg',1,22,0,'2018-04-16 13:36:32.200306'),(18,26,'魅蓝 A8',NULL,NULL,4553.00,'/static/public/img/1523885829.7490358.jpg',1,12,0,'2018-04-16 13:37:09.752677'),(19,29,'魅蓝 A5',NULL,NULL,3355.00,'/static/public/img/1523885892.480298.jpg',1,11,0,'2018-04-16 13:38:12.482340'),(20,27,'opp3',NULL,'<p>gaga</p>',2222.00,'/static/public/img/1524541617.0240316.jpg',1,222,0,'2018-04-24 03:46:57.025500');
/*!40000 ALTER TABLE `myadmin_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_orders`
--

DROP TABLE IF EXISTS `myadmin_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `linkman` varchar(32) NOT NULL,
  `address` varchar(255) NOT NULL,
  `code` varchar(6) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `total` decimal(8,2) NOT NULL,
  `nums` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_orders_uid_id_cfc716ee_fk_myadmin_users_id` (`uid_id`),
  CONSTRAINT `myadmin_orders_uid_id_cfc716ee_fk_myadmin_users_id` FOREIGN KEY (`uid_id`) REFERENCES `myadmin_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_orders`
--

LOCK TABLES `myadmin_orders` WRITE;
/*!40000 ALTER TABLE `myadmin_orders` DISABLE KEYS */;
INSERT INTO `myadmin_orders` VALUES (1,'abcd ','kajgakg kl','234567','124567','2018-04-23 02:07:16.905084',6710.00,2,2,31),(2,'wangwu ','alkkgalk ','234567','123456','2018-04-23 02:08:12.376503',6710.00,2,0,31),(3,'liuliu','aklgj jklajg','234567','1234567','2018-04-23 02:11:55.421811',6710.00,2,1,31),(4,'六七啊','备件是','234567','1234567','2018-04-23 02:16:13.115841',6710.00,2,1,31),(5,'张三','北京市','100101','122','2018-04-23 02:47:42.561492',2222.00,1,1,31),(6,'lixiaoliuqigg','beijingshi','111111','12345602','2018-04-23 03:20:57.928260',7632.00,2,1,45),(7,'lixiaoliu','beijingshi','111111','123456','2018-04-23 03:34:28.487852',7632.00,2,1,45),(8,'lisan','beijing','112111','121','2018-04-23 03:36:41.338033',4299.00,1,0,45),(9,'王五dd','beijinag','123456','12394500663d','2018-04-23 13:19:53.807986',6666.00,2,1,46),(10,'王小二','北京市昌平区','111223','110','2018-04-23 13:43:50.657856',3444.00,1,1,46),(11,'李柳','北京市丰台区','123456','1234567','2018-04-23 14:46:25.657055',10065.00,3,1,45),(12,'王小五','北京市','100010','110','2018-04-24 02:55:44.498161',4299.00,1,1,45),(13,'李四','北京市','123456','119','2018-04-24 02:58:39.640162',3355.00,1,1,45),(14,'王五','北京市','123456','123','2018-04-24 02:59:39.925291',3333.00,1,1,45),(15,'wangxiaowu ','baijiagnaig','123456','112','2018-04-24 03:53:19.241751',9999.00,3,1,46),(16,'张三','北京市公安局','100000','110','2018-05-03 11:51:39.786590',9999.00,3,1,46);
/*!40000 ALTER TABLE `myadmin_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_turnimg`
--

DROP TABLE IF EXISTS `myadmin_turnimg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_turnimg` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_turnimg`
--

LOCK TABLES `myadmin_turnimg` WRITE;
/*!40000 ALTER TABLE `myadmin_turnimg` DISABLE KEYS */;
INSERT INTO `myadmin_turnimg` VALUES (0,'static/public/front/public/img/banner2.jpg'),(1,'static/public/front/public/img/banner3.jpg'),(2,'static/public/front/public/img/banner1_N4p61cU.jpg');
/*!40000 ALTER TABLE `myadmin_turnimg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_types`
--

DROP TABLE IF EXISTS `myadmin_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `pid` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_types`
--

LOCK TABLES `myadmin_types` WRITE;
/*!40000 ALTER TABLE `myadmin_types` DISABLE KEYS */;
INSERT INTO `myadmin_types` VALUES (23,'高档手机2',0,'0,'),(25,'中档手机',0,'0,'),(26,'魅族 PRO 7',23,'0,23,'),(27,'魅族 PRO 8',23,'0,23,'),(29,'魅族 PRO 6',25,'0,25,'),(30,'魅族 PRO 5',25,'0,25,'),(31,'魅族 PRO 4',25,'0,25,'),(32,'魅族 PRO 9',23,'0,23,'),(33,'低档手机',0,'0,'),(34,'魅族 PRO 3',33,'0,33,'),(35,'魅族 PRO 2',33,'0,33,');
/*!40000 ALTER TABLE `myadmin_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_types_copy`
--

DROP TABLE IF EXISTS `myadmin_types_copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_types_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `pid` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_types_copy`
--

LOCK TABLES `myadmin_types_copy` WRITE;
/*!40000 ALTER TABLE `myadmin_types_copy` DISABLE KEYS */;
INSERT INTO `myadmin_types_copy` VALUES (1,'服装',0,'0'),(2,'数码',0,'0'),(3,'食品',0,'0'),(4,'男装',1,'0,1,'),(5,'女装',1,'0,1,'),(6,'相机',2,'0,2,'),(7,'电脑',2,'0,2,'),(8,'笔记本',7,'0,2,7,'),(9,'台式机',7,'0,2,7,'),(10,'掌上电脑',7,'0,2,7,'),(11,'联想笔记本',8,'0,2,7,8,');
/*!40000 ALTER TABLE `myadmin_types_copy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myadmin_users`
--

DROP TABLE IF EXISTS `myadmin_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myadmin_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `password` varchar(80) NOT NULL,
  `sex` varchar(1) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` varchar(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `state` int(11) DEFAULT NULL,
  `img` varchar(100) NOT NULL,
  `addtime` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myadmin_users`
--

LOCK TABLES `myadmin_users` WRITE;
/*!40000 ALTER TABLE `myadmin_users` DISABLE KEYS */;
INSERT INTO `myadmin_users` VALUES (31,'东东',NULL,'pbkdf2_sha256$36000$iAtXJGSnGUvi$suGNus7ghs4Ua6Ea218xZUTDEXrGAyzWs75+EfjOTEs=',NULL,NULL,NULL,NULL,'dongdong@qq.com',0,'static/public/img/fffffffddddssdaf_3HB65nI.jpg','2018-04-15'),(45,'wangxiaowu',NULL,'pbkdf2_sha256$36000$BAQw2WVQoMlM$pm0PiuZf4zceuoMdCq11qeB1GocA+c+gDdhoDKgL504=',NULL,NULL,NULL,NULL,'wangxiaowu@qq.com',1,'static/public/img/ertyuiuoikjhgfdfgh_yoTanBI.jpg','2018-04-23'),(46,'zhangsan',NULL,'pbkdf2_sha256$36000$Pxwyx1KIFodR$wKncVye66xFdh0cgSyzWidI0o5zRnjydCXmwTKFNusY=',NULL,NULL,NULL,NULL,'zhangsan@qq.com',1,'static/public/img/dafgsgfgfvzvf.jpg','2018-04-23'),(49,'lixiaoliu',NULL,'pbkdf2_sha256$36000$zpv4bRnCxjfE$c5XoptbryOCRvobu6Y1G4yUsxcIt1Xy7SCxJUPK3h38=',NULL,NULL,NULL,NULL,'lixiaowu@qq.com',0,'static/public/img/435689fghtyukl.jpg','2018-04-24');
/*!40000 ALTER TABLE `myadmin_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-03 20:11:24
