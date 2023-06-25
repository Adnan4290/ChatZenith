-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 25, 2023 at 06:49 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ChatZenith`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id_no` int(255) NOT NULL,
  `email` varchar(60) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `password` varchar(26) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id_no`, `email`, `first_name`, `last_name`, `password`) VALUES
(1, 'wh236849@gmail.com', 'Waleed', 'Hassan', 'mostsecretpass'),
(2, 'shahzadadnan429@gmail.com', 'Adnan', 'Shazad', 'test123'),
(3, 'bifoj94941@syinxun.com', 'Dummy', 'Test', 'topsecret'),
(5, 'silif11355@saeoil.com', 'Dummy2', 'Test2', 'TOPSECRET2');

-- --------------------------------------------------------

--
-- Table structure for table `chats`
--

CREATE TABLE `chats` (
  `chat_id` int(255) NOT NULL,
  `chatroute` int(255) NOT NULL,
  `userid` int(255) NOT NULL,
  `chatfrom` int(255) NOT NULL,
  `chatTitle` varchar(50) NOT NULL,
  `last_msg` varchar(50) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chats`
--

INSERT INTO `chats` (`chat_id`, `chatroute`, `userid`, `chatfrom`, `chatTitle`, `last_msg`, `datetime`) VALUES
(3, 1, 1, 2, 'Adnan Shazad', 'Hello', '2023-06-22 22:34:04'),
(4, 1, 2, 1, 'Waleed Hassan', 'Hi', '2023-06-22 22:34:04');

-- --------------------------------------------------------

--
-- Table structure for table `chatting`
--

CREATE TABLE `chatting` (
  `msgid` int(255) NOT NULL,
  `chatroute` int(255) NOT NULL,
  `chattingid` int(255) NOT NULL,
  `userid` int(255) NOT NULL,
  `chatfrom` int(255) NOT NULL,
  `chatTitle` varchar(50) NOT NULL,
  `msg` varchar(255) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chatting`
--

INSERT INTO `chatting` (`msgid`, `chatroute`, `chattingid`, `userid`, `chatfrom`, `chatTitle`, `msg`, `datetime`) VALUES
(1, 1, 3, 2, 2, 'Waleed Hassan', 'HI', '2023-06-23 16:47:44'),
(2, 1, 4, 1, 1, 'Adnan Shazad', 'Hello', '2023-06-23 16:47:44'),
(4, 1, 3, 1, 1, 'Adnan Shazad', 'First message', '2023-06-23 22:12:41'),
(5, 1, 3, 1, 1, 'Adnan Shazad', 'Second message', '2023-06-24 10:58:51'),
(6, 1, 3, 1, 1, 'Adnan Shazad', 'Aoa kia haal ha', '2023-06-25 21:08:53'),
(7, 1, 4, 2, 2, 'Waleed Hassan', 'w.salaam Allah ka shukar', '2023-06-25 21:09:44'),
(8, 1, 4, 2, 2, 'Waleed Hassan', 'aap sunao', '2023-06-25 21:09:56'),
(9, 1, 4, 2, 2, 'Waleed Hassan', 'aap sunao', '2023-06-25 21:09:56'),
(10, 1, 3, 1, 1, 'Adnan Shazad', 'app ko refresh krna prta ha everytime to receive messages', '2023-06-25 21:10:23'),
(11, 1, 3, 1, 1, 'Adnan Shazad', 'cheaking the fix', '2023-06-25 21:37:45'),
(12, 1, 4, 2, 2, 'Waleed Hassan', 'Fixed?', '2023-06-25 21:38:17'),
(13, 1, 3, 1, 1, 'Adnan Shazad', 'yes fixed', '2023-06-25 21:40:49'),
(14, 1, 4, 2, 2, 'Waleed Hassan', 'Great', '2023-06-25 21:41:23'),
(15, 1, 3, 1, 1, 'Adnan Shazad', 'aagay ho?', '2023-06-25 21:44:20'),
(16, 1, 4, 2, 2, 'Waleed Hassan', 'hey', '2023-06-25 21:44:31'),
(17, 1, 4, 2, 2, 'Waleed Hassan', 'hey', '2023-06-25 21:44:55'),
(18, 1, 4, 2, 2, 'Waleed Hassan', 'hey', '2023-06-25 21:44:59'),
(19, 1, 3, 1, 1, 'Adnan Shazad', 'yes it worked', '2023-06-25 21:45:12'),
(20, 1, 4, 2, 2, 'Waleed Hassan', 'agya bro', '2023-06-25 21:45:31'),
(21, 1, 3, 1, 1, 'Adnan Shazad', 'ab frontend mslaa kr rha ha shi se rendering nhi ho rhi', '2023-06-25 21:45:46'),
(22, 1, 3, 1, 1, 'Adnan Shazad', 'krdia message', '2023-06-25 21:47:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id_no`);

--
-- Indexes for table `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`chat_id`),
  ADD UNIQUE KEY `chatfrom_2` (`chatfrom`),
  ADD UNIQUE KEY `chatfrom_3` (`chatfrom`),
  ADD UNIQUE KEY `chatfrom_4` (`chatfrom`),
  ADD UNIQUE KEY `chat_id` (`chat_id`),
  ADD KEY `userid` (`userid`),
  ADD KEY `chatfrom` (`chatfrom`);

--
-- Indexes for table `chatting`
--
ALTER TABLE `chatting`
  ADD PRIMARY KEY (`msgid`),
  ADD UNIQUE KEY `msgid` (`msgid`),
  ADD KEY `msgid_2` (`msgid`),
  ADD KEY `userid` (`userid`),
  ADD KEY `useridno` (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `chatting`
--
ALTER TABLE `chatting`
  MODIFY `msgid` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chats`
--
ALTER TABLE `chats`
  ADD CONSTRAINT `chats_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `accounts` (`id_no`),
  ADD CONSTRAINT `chats_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `accounts` (`id_no`),
  ADD CONSTRAINT `chats_ibfk_3` FOREIGN KEY (`chatfrom`) REFERENCES `accounts` (`id_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
