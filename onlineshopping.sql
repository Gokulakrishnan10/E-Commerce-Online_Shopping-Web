-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2020 at 03:15 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onlineshopping`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(25) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `password`) VALUES
('Gokulakrishnan', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `buyed_product`
--

CREATE TABLE `buyed_product` (
  `cust_id` varchar(20) NOT NULL,
  `itemid` varchar(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `address` text NOT NULL,
  `Ordered_date` date NOT NULL,
  `Delivery_Date` date NOT NULL,
  `status` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `buyed_product`
--

INSERT INTO `buyed_product` (`cust_id`, `itemid`, `quantity`, `address`, `Ordered_date`, `Delivery_Date`, `status`) VALUES
('cust_01', 'item03', 1, '17/1,Angalamman Kovil Street,Diamond Bazzar,Try-620008', '0000-00-00', '2020-06-23', 'Not Delivered'),
('cust_01', 'item04', 1, '17/1,Angalamman Kovil Street,Diamond Bazzar,Try-620008', '2020-06-16', '2020-06-23', 'Delivered'),
('cust_01', 'item01', 3, '17/1,Angalamman Kovil Street,Diamond Bazzar,Try-620008', '2020-06-30', '2020-07-07', 'Not Delivered'),
('cust_01', 'item03', 2, '17/1,Angalamman Kovil Street,Diamond Bazzar,Try-620008', '2020-06-30', '2020-07-07', 'Not Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `itemid` varchar(20) NOT NULL,
  `cust_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`itemid`, `cust_id`) VALUES
('item01', 'cust_01'),
('item03', 'cust_01'),
('item04', 'cust_01'),
('item01', 'cust_01');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Name` varchar(20) NOT NULL,
  `Cust_id` varchar(11) NOT NULL,
  `Phone_no` int(30) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Name`, `Cust_id`, `Phone_no`, `Password`, `Address`) VALUES
('Gokulakrishnan', 'cust_01', 2147483647, 'gokul1234', '17/1,Angalamman Kovil Street,Diamond Bazzar,Try-620008'),
('Santhosh', 'Cust_2', 2147483647, 'santhosh', '17/1,Angalamman Kovil st');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `itemid` varchar(20) NOT NULL,
  `itemname` varchar(20) NOT NULL,
  `quantity` int(10) NOT NULL,
  `price` int(20) NOT NULL,
  `spec` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`itemid`, `itemname`, `quantity`, `price`, `spec`) VALUES
('item01', 'Samsung_tv', 4, 100000, NULL),
('item02', 'coolpadn5', 6, 24000, '2Gb/16gb-4Mp+16Mp'),
('item03', 'sony_tv32inch', 0, 100000, 'smart tv'),
('item04', 'Lenova_Lap', 1, 45000, 'intel_i5,8thGen,Radeon_graphics');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Cust_id`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD UNIQUE KEY `itemid` (`itemid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
