-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 08, 2022 at 03:07 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1facefingdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `attentb`
--

CREATE TABLE `attentb` (
  `id` bigint(250) NOT NULL auto_increment,
  `Date` varchar(250) NOT NULL,
  `Time` varchar(250) NOT NULL,
  `UserId` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `attentb`
--

INSERT INTO `attentb` (`id`, `Date`, `Time`, `UserId`, `Status`) VALUES
(20, '2022-05-08', '08:31:17', '5535', '1');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `UserId` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Phone` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Finger` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`UserId`, `Name`, `Gender`, `Age`, `Email`, `Phone`, `Address`, `Finger`) VALUES
('5535', 'san', 'male', '20', 'san@gmail.com', '9486365535', 'trichy', '12.jpg');
