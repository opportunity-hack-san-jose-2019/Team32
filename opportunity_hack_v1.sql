DROP TABLE IF EXISTS `assignments`;
CREATE TABLE IF NOT EXISTS `assignments` (
  `volunteerid` int(11) NOT NULL,
  `caseid` int(11) NOT NULL,
  PRIMARY KEY (`volunteerid`,`caseid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `cases`
--
DROP TABLE IF EXISTS `cases`;
CREATE TABLE IF NOT EXISTS `cases` (
  `caseid` int(11) NOT NULL AUTO_INCREMENT,
  `problem_description` varchar(4096) NOT NULL,
  `priority` ENUM('low', 'medium', 'high') NOT NULL,
  `assigned_priority` ENUM('low', 'medium', 'high') NOT NULL,
  `help_type` ENUM('family-service', 'disaster-service') NOT NULL,
  `name` varchar(500) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `address` varchar(1024) NOT NULL,
  PRIMARY KEY (`caseid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `donors`
--
DROP TABLE IF EXISTS `donors`;
CREATE TABLE IF NOT EXISTS `donors` (
  `donorid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `email` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`donorid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `inventory`
--
DROP TABLE IF EXISTS `inventory`;
CREATE TABLE IF NOT EXISTS `inventory` (
  `itemid` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(1024) NOT NULL,
  `quantity` int(11) NOT NULL,
  `category` ENUM('clothes', 'food', 'health-care', 'other') NOT NULL,
  PRIMARY KEY (`itemid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(256) NOT NULL,
  `lastname` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `address` varchar(2048) NOT NULL,
  `primary_contact` varchar(20) NOT NULL,
  `secondary_contact` varchar(20) DEFAULT NULL,
  `role` ENUM('admin', 'volunteer', 'donor') NOT NULL NOT NULL,
  `username` varchar(50) NOT NULL,
  `pwd` varchar(130) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;
