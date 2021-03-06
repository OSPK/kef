-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 25, 2016 at 05:08 PM
-- Server version: 5.7.12-0ubuntu1
-- PHP Version: 7.0.4-7ubuntu2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `karwan`
--

-- --------------------------------------------------------

--
-- Table structure for table `universities`
--

CREATE TABLE `universities` (
  `id` int(11) NOT NULL,
  `uni_name` varchar(512) COLLATE utf32_bin NOT NULL,
  `city` varchar(512) COLLATE utf32_bin NOT NULL,
  `province` varchar(512) COLLATE utf32_bin NOT NULL,
  `pub_pri` varchar(32) COLLATE utf32_bin NOT NULL,
  `website` varchar(512) COLLATE utf32_bin DEFAULT NULL,
  `govt` varchar(512) COLLATE utf32_bin NOT NULL,
  `campuses` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_bin;

--
-- Dumping data for table `universities`
--

INSERT INTO `universities` (`id`, `uni_name`, `city`, `province`, `pub_pri`, `website`, `govt`, `campuses`) VALUES
(1, 'Air University, Islamabad', 'Islamabad', 'Islamabad ', 'Public', 'www.au.edu.pk', 'Gov of Pakistan', 1),
(2, 'Allama Iqbal Open University, Islamabad (AIOU)', 'Islamabad', 'Islamabad', 'Public', 'www.aiou.edu.pk', 'Gov of Pakistan', 0),
(3, 'Bahria University, Islamabad', 'Islamabad', 'Islamabad', 'Public', 'www.bahria.edu.pk', 'Gov of Pakistan', 2),
(4, 'COMSATS Institute of Information Technology, Islamabad', 'Islamabad', 'Islamabad', 'Public', 'www.ciit.edu.pk', 'Gov of Pakistan', 7),
(5, 'Dawood College of Engineering & Technology, Karachi ', 'Karachi', 'Sindh', 'Public', 'www.dcet.edu.pk', 'Gov of Pakistan', 0),
(6, 'Federal Urdu University of Arts, Sciences & Technology, Islamabad', 'Islamabad', 'Islamabad', 'Public', 'www.fuuast.edu.pk', 'Gov of Pakistan', 1),
(7, 'Institute of Space Technology, Islamabad (IST)', 'Islamabad', 'Islamabad', 'Public', 'www.ist.edu.pk', 'Gov of Pakistan', 0),
(8, 'International Islamic University, Islamabad', 'Islamabad', 'Islamabad', 'Public', 'www.iiu.edu.pk', 'Gov of Pakistan', 0),
(9, 'Karakurum International University, Gilgit, Gilgit Baltistan', 'Gilgit', 'Gilgit-Baltistan', 'Public', 'www.kiu.edu.pk', 'Gov of Pakistan', 0),
(10, 'National College of Arts, Lahore (NCA)', 'Lahore', 'Punjab', 'Public', 'www.nca.edu.pk', 'Gov of Pakistan', 0),
(11, 'National Defense University, Islamabad (NDU)', 'Islamabad', 'Islamabad', 'Public', 'www.ndu.edu.pk', 'Gov of Pakistan', 0),
(12, 'National Textile University, Faisalabad', 'Faisalabad', 'Punjab', 'Public', 'www.ntu.edu.pk', 'Gov of Pakistan', 0),
(13, 'National University of Modern Languages, Islamabad (NUML)', 'Islamabad', 'Islamabad', 'Public', 'www.numl.edu.pk', 'Gov of Pakistan', 7),
(14, 'National University of Sciences & Technology, Rawalpindi/ Islamabad (NUST)', 'Islamabad', 'Islamabad', 'Public', 'www.nust.edu.pk', 'Gov of Pakistan', 0),
(15, 'National University of Medical Sciences, Islamabad', '', 'Islamabad', 'Public', '', 'Gov of Pakistan', 0),
(16, 'NFC Institute of Engineering & Technology, Multan', 'Multan', 'Punjab', 'Public', 'www.nfciet.edu.pk', 'Gov of Pakistan', 0),
(17, 'Pakistan Institute of Development Economics (PIDE), Islamabad', 'Islamabad', 'Islamabad', 'Public', 'www.pide.org.pk', 'Gov of Pakistan', 0),
(18, 'Pakistan Institute of Engineering & Applied Sciences, Islamabad (PIEAS)', 'Islamabad', 'Islamabad', 'Public', 'www.pieas.edu.pk', 'Gov of Pakistan', 0),
(19, 'Pakistan Institute of Fashion and Design, Lahore', 'Lahore', 'Punjab', 'Public', 'www.pifd.edu.pk', 'Gov of Pakistan', 0),
(20, 'Pakistan Military Academy, Abbottabad (PMA)', 'Abbottabad', 'Khyber Pakhtunkhwa', 'Public', 'Not Available', 'Gov of Pakistan', 0),
(21, 'Pakistan Naval Academy, Karachi', 'Karachi', 'Sindh', 'Public', 'www.paknavy.gov.pk', 'Gov of Pakistan', 0),
(22, 'Shaheed Zulfiqar Ali Bhutto Medical University, Islamabad', 'Islamabad', 'Islamabad', 'Public', '', 'Gov of Pakistan', 0),
(23, 'Quaid-i-Azam University, Islamabad', 'Islamabad', 'Islamabad', 'Public', 'www.qau.edu.pk', 'Gov of Pakistan', 0),
(24, 'University of FATA, Kohat ', 'Kohat', 'Khyber Pakhtunkhwa', 'Public', '', 'Gov of Pakistan', 0),
(25, 'Virtual University of Pakistan, Lahore', 'Lahore', 'Punjab', 'Public', 'www.vu.edu.pk', 'Gov of Pakistan', 16),
(26, 'Aga Khan University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.aku.edu', 'Gov of Pakistan', 0),
(27, 'Capital University of Science and Technology, Islamabad', 'Islamabad', 'Islamabad', ' Private', 'www.cust.edu.pk', 'Gov of Pakistan', 0),
(28, 'Foundation University, Islamabad', 'Islamabad', 'Islamabad', ' Private', 'www.fui.edu.pk', 'Gov of Pakistan', 0),
(29, 'Lahore University of Management Sciences (LUMS), Lahore', 'Lahore', 'Punjab', ' Private', 'www.lums.edu.pk', 'Gov of Pakistan', 0),
(30, 'MY University, Islamabad', 'Islamabad', 'Islamabad', ' Private', 'www.myu.edu.pk', 'Gov of Pakistan', 0),
(31, 'National University of Computer and Emerging Sciences, Islamabad', 'Islamabad', 'Islamabad', ' Private', 'www.nu.edu.pk', 'Gov of Pakistan', 5),
(32, 'Riphah International University, Islamabad', 'Islamabad', 'Islamabad', ' Private', 'www.riphah.edu.pk', 'Gov of Pakistan', 2),
(33, 'Shifa Tameer-e-Millat University, Islamabad', 'Islamabad', 'Islamabad', ' Private', 'www.stmu.edu.pk', 'Gov of Pakistan', 0),
(34, 'Bahauddin Zakariya University, Multan', 'Multan', 'Punjab', 'Public', 'www.bzu.edu.pk', 'Gov of Punjab ', 2),
(35, 'Fatima Jinnah Women University, Rawalpindi', 'Rawalpindi', 'Punjab', 'Public', 'www.fjwu.edu.pk', 'Gov of Punjab ', 0),
(36, 'Government College University, Faisalabad ', 'Faisalabad', 'Punjab', 'Public', 'www.gcuf.edu.pk', 'Gov of Punjab ', 0),
(37, 'Government College University, Lahore', 'Lahore', 'Punjab', 'Public', 'www.gcu.edu.pk', 'Gov of Punjab ', 0),
(38, 'Government College for Women University, Faisalabad', 'Faisalabad', 'Punjab', 'Public', 'www.gcuf.edu.pk', 'Gov of Punjab ', 0),
(39, 'Government College Women University, Sialkot', 'Sialkot', 'Punjab', 'Public', 'www.gcwus.edu.pk/', 'Gov of Punjab ', 0),
(40, 'Ghazi University, Dera Ghazi Khan', 'Dera Ghazi Khan', 'Punjab', 'Public', '', 'Gov of Punjab ', 0),
(41, 'Government Sadiq College Women University, Bahawalpur', 'Bahawalpur', 'Punjab', 'Public', '', 'Gov of Punjab ', 0),
(42, 'Islamia University, Bahawalpur', 'Bahawalpur', 'Punjab', 'Public', 'www.iub.edu.pk', 'Gov of Punjab ', 2),
(43, 'Information Technology University of the Punjab, Lahore', 'Lahore', 'Punjab', 'Public', 'www.itu.edu.pk', 'Gov of Punjab ', 0),
(44, 'King Edward Medical University, Lahore ', 'Lahore', 'Punjab', 'Public', 'www.kemu.edu.pk ', 'Gov of Punjab ', 0),
(45, 'Kinnaird College for Women, Lahore', 'Lahore', 'Punjab', 'Public', 'www.kinnaird.edu.pk', 'Gov of Punjab ', 0),
(46, 'Khawaja Fareed University of Engineering & Information Technology, Rahim Yar Khan', 'Rahim Yar Khan', 'Punjab', 'Public', 'Under construction', 'Gov of Punjab ', 0),
(47, 'Lahore College for Women University, Lahore', 'Lahore', 'Punjab', 'Public', 'www.lcwu.edu.pk', 'Gov of Punjab ', 1),
(48, 'Muhammad Nawaz Shareef University of Agriculture, Multan', 'Multan', 'Punjab', 'Public', 'www.mnsuam.edu.pk', 'Gov of Punjab ', 0),
(49, 'Pir Mehr Ali Shah Arid Agriculture, University Rawalpindi', 'Rawalpindi', 'Punjab', 'Public', 'www.uaar.edu.pk', 'Gov of Punjab ', 0),
(50, 'University of Agriculture, Faisalabad', 'Faisalabad', 'Punjab', 'Public', 'www.uaf.edu.pk', 'Gov of Punjab ', 2),
(51, 'University of Education, Lahore', 'Lahore', 'Punjab', 'Public', 'www.ue.edu.pk', 'Gov of Punjab ', 6),
(52, 'University of Engineering & Technology, Lahore', 'Lahore', 'Punjab', 'Public', 'www.uet.edu.pk', 'Gov of Punjab ', 4),
(53, 'University of Engineering & Technology, Taxila ', 'Taxila', 'Punjab', 'Public', 'www.uettaxila.edu.pk', 'Gov of Punjab ', 1),
(54, 'University of Gujrat, Gujrat ', 'Gujrat', 'Punjab', 'Public', 'www.uog.edu.pk', 'Gov of Punjab ', 0),
(55, 'University of Health Sciences, Lahore', 'Lahore', 'Punjab', 'Public', 'www.uhs.edu.pk', 'Gov of Punjab ', 0),
(56, 'University of Sargodha, Sargodha', 'Sargodha', 'Punjab', 'Public', 'www.uos.edu.pk', 'Gov of Punjab ', 0),
(57, 'University of the Punjab, Lahore', 'Lahore', 'Punjab', 'Public', 'www.pu.edu.pk', 'Gov of Punjab ', 1),
(58, 'University of Veterinary & Animal Sciences, Lahore', 'Lahore', 'Punjab', 'Public', 'www.uvas.edu.pk', 'Gov of Punjab ', 2),
(59, 'The Women University, Multan ', 'Multan', 'Punjab', 'Public', 'www.wum.edu.pk', 'Gov of Punjab ', 0),
(60, ' Muhammad Nawaz Sharif University of   Engineering & Technology, Multan', 'Multan', 'Punjab', 'Public', 'www.uet.edu.pk/mns', 'Gov of Punjab ', 0),
(61, 'Ali Institute of Education', 'Lahore', 'Punjab', ' Private', 'www.aie.edu.pk', 'Gov of Punjab ', 0),
(62, 'Beaconhouse National University, Lahore', 'Lahore', 'Punjab', ' Private', 'www.bnu.edu.pk', 'Gov of Punjab ', 0),
(63, 'Forman Christian College, Lahore (university status)', 'Lahore', 'Punjab', ' Private', 'www.fccollege.edu.pk', 'Gov of Punjab ', 0),
(64, 'Global Institute, Lahore', 'Lahore', 'Punjab', ' Private', 'www.global.edu.pk', 'Gov of Punjab ', 0),
(65, 'Hajvery University, Lahore', 'Lahore', 'Punjab', ' Private', 'www.hajvery.edu.pk', 'Gov of Punjab ', 0),
(66, 'HITEC University, Taxila', 'Taxila', 'Punjab', ' Private', 'www.hitecuni.edu.pk', 'Gov of Punjab ', 0),
(67, 'Imperial College of Business Studies, Lahore', 'Lahore', 'Punjab', ' Private', 'www.imperial.edu.pk', 'Gov of Punjab ', 0),
(68, 'Institute of Management Sciences, Lahore', 'Lahore', 'Punjab', ' Private', 'www.pakaims.edu.pk', 'Gov of Punjab ', 0),
(69, 'Institute of Southern Punjab, Multan', 'Multan', 'Punjab', ' Private', 'www.usp.edu.pk', 'Gov of Punjab ', 0),
(70, 'Lahore Leads University, Lahore', 'Lahore', 'Punjab', ' Private', 'www.leads.edu.pk', 'Gov of Punjab ', 0),
(71, 'Lahore School of Economics, Lahore', 'Lahore', 'Punjab', ' Private', 'www.lahoreschoolofeconomics.edu.pk', 'Gov of Punjab ', 0),
(72, 'Lahore Garrison University, Lahore', 'Lahore', 'Punjab', ' Private', 'www.lgu.edu.pk', 'Gov of Punjab ', 0),
(73, 'Minhaj University, Lahore ', 'Lahore', 'Punjab', ' Private', 'www.mul.edu.pk', 'Gov of Punjab ', 0),
(74, 'National College of Business Administration & Economics, Lahore', 'Lahore', 'Punjab', ' Private', 'www.ncbae.edu.pk', 'Gov of Punjab ', 1),
(75, 'Nur International University, Lahore', 'Lahore', 'Punjab', ' Private', '', 'Gov of Punjab ', 0),
(76, 'Qarshi University', 'Lahore', 'Punjab', ' Private', 'www.qu.edu.pk', 'Gov of Punjab ', 0),
(77, 'The GIFT University, Gujranwala', 'Gujranwala', 'Punjab', ' Private', 'www.gift.edu.pk', 'Gov of Punjab ', 0),
(78, 'The Superior College, Lahore ', 'Lahore', 'Punjab', ' Private', 'www.superior.edu.pk', 'Gov of Punjab ', 0),
(79, 'The University of Faisalabad, Faisalabad', 'Faisalabad', 'Punjab', ' Private', 'www.tuf.edu.pk', 'Gov of Punjab ', 0),
(80, 'University of Central Punjab, Lahore', 'Lahore', 'Punjab', ' Private', 'www.ucp.edu.pk', 'Gov of Punjab ', 0),
(81, 'University of Lahore, Lahore', 'Lahore', 'Punjab', ' Private', 'www.uol.edu.pk ', 'Gov of Punjab ', 3),
(82, 'University of Management & Technology, Lahore', 'Lahore', 'Punjab', ' Private', 'www.umt.edu.pk', 'Gov of Punjab ', 1),
(83, 'University of South Asia, Lahore', 'Lahore', 'Punjab', ' Private', 'www.usa.edu.pk', 'Gov of Punjab ', 0),
(84, 'University of Wah, Wah', 'Wah', 'Punjab', ' Private', 'www.uw.edu.pk', 'Gov of Punjab ', 0),
(85, 'Benazir Bhutto Shaheed University Lyari, Karachi', 'Karachi', 'Sindh', 'Public', 'www.bbsul.edu.pk', 'Gov of sindh', 0),
(86, 'DOW University of Health Sciences, Karachi ', 'Karachi', 'Sindh', 'Public', 'www.duhs.edu.pk', 'Gov of sindh', 0),
(87, 'Gambat Institute of Medical Sciences, Khairpur', 'Khairpur', 'Sindh', 'Public', '', 'Gov of sindh', 0),
(88, 'Institute of Business Administration, Karachi', 'Karachi', 'Sindh', 'Public', 'www.iba.edu.pk', 'Gov of sindh', 0),
(89, 'Jinnah Sindh Medical University', 'Karachi', 'Sindh', 'Public', 'www.jsmu.edu.pk', 'Gov of sindh', 0),
(90, 'Liaquat University of Medical and Health Sciences, Jamshoro Sindh.', 'Jamshoro', 'Sindh', 'Public', 'www.lumhs.edu.pk', 'Gov of sindh', 0),
(91, 'Mehran University of Engineering & Technology, Jamshoro', 'Jamshoro', 'Sindh', 'Public', 'www.muet.edu.pk', 'Gov of sindh', 1),
(92, 'NED University of Engineering & Technology, Karachi', 'Karachi', 'Sindh', 'Public', 'www.neduet.edu.pk', 'Gov of sindh', 0),
(93, 'Peoples University of Medical and Health Sciences for Women, Nawabshah (Shaheed Benazirabad) ', 'Nawabshah', 'Sindh', 'Public', 'www.pumhs.edu.pk', 'Gov of sindh', 0),
(94, 'Quaid-e-Awam University of Engineering, Sciences & Technology, Nawabshah', 'Nawabshah', 'Sindh', 'Public', 'www.quest.edu.pk', 'Gov of sindh', 1),
(95, 'Shah Abdul Latif University, Khairpur', 'Khairpur', 'Sindh', 'Public', 'www.salu.edu.pk', 'Gov of sindh', 1),
(96, 'Shahaeed Mohtarma Benazir Bhutto Medical University, Larkana', 'Larkana', 'Sindh', 'Public', 'www.smbbmu.edu.pk', 'Gov of sindh', 0),
(97, 'Sindh Agriculture University, Tandojam', 'Tandojam', 'Sindh', 'Public', 'www.sau.edu.pk', 'Gov of sindh', 0),
(98, 'Sukkur Institute of Business Administration, Sukkur ', 'Sukkur', 'Sindh', 'Public', 'www.iba-suk.edu.pk', 'Gov of sindh', 0),
(99, 'Sindh Madresatul Islam University, Karachi', 'Karachi', 'Sindh', 'Public', 'www.smiu.edu.pk', 'Gov of sindh', 0),
(100, 'Shaheed Benazir Bhutto University Shaheed Benazirabad', 'Nawabshah', 'Sindh', 'Public', 'www.sbbusba.edu.pk', 'Gov of sindh', 0),
(101, 'Shaheed Zulfiqar Ali Bhutto University of Law, Karachi', 'Karachi', 'Sindh', 'Public', '', 'Gov of sindh', 0),
(102, 'University of Karachi, Karachi ', 'Karachi', 'Sindh', 'Public', 'www.uok.edu.pk', 'Gov of sindh', 0),
(103, 'University of Sindh, Jamshoro', 'Jamshoro', 'Sindh', 'Public', 'www.usindh.edu.pk', 'Gov of sindh', 3),
(104, 'Shaheed Benazir Bhutto University of Veterinary And Animal Sciences Sakrand', ' Sakrand', 'Sindh', 'Public', 'www.sbbuvas.edu.pk', 'Gov of sindh', 0),
(105, 'Baqai Medical University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.baqai.edu.pk', 'Gov of sindh', 0),
(106, 'Commeces Institute of Business & Emerging Sciences, Karachi', 'Karachi', 'Sindh', ' Private', 'www.commecsinstitute.edu.pk', 'Gov of sindh', 0),
(107, 'Dadabhoy Institute of Higher Education,Karachi', 'Karachi', 'Sindh', ' Private', 'www.dadabhoy.edu.pk', 'Gov of sindh', 0),
(108, 'DHA Suffa University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.dsu.edu.pk', 'Gov of sindh', 0),
(109, 'Greenwich University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.greenwichuniversity.edu.pk', 'Gov of sindh', 0),
(110, 'Hamdard University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.hamdard.edu.pk', 'Gov of sindh', 1),
(111, 'Habib University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.habib.edu.pk ', 'Gov of sindh', 0),
(112, '  Indus University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.indus.edu.pk', 'Gov of sindh', 0),
(113, 'Indus Valley School of Art and Architecture, Karachi', 'Karachi', 'Sindh', ' Private', 'www.indusvalley.edu.pk', 'Gov of sindh', 0),
(114, 'Institute of Business Management, Karachi', 'Karachi', 'Sindh', ' Private', 'www.iobm.edu.pk', 'Gov of sindh', 0),
(115, 'Institute of Business and Technology, Karachi', 'Karachi', 'Sindh', ' Private', 'www.biztek.edu.pk', 'Gov of sindh', 0),
(116, 'Iqra University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.iqra.edu.pk', 'Gov of sindh', 2),
(117, 'Isra University, Hyderabad', 'Hyderabad', 'Sindh', ' Private', 'www.isra.edu.pk', 'Gov of sindh', 2),
(118, 'Jinnah University for Women, Karachi', 'Karachi', 'Sindh', ' Private', 'www.juw.edu.pk', 'Gov of sindh', 0),
(119, 'Karachi Institute of Economics & Technology, Karachi', 'Karachi', 'Sindh', ' Private', 'www.pafkiet.edu.pk', 'Gov of sindh', 0),
(120, 'KASB Institute of Technology, Karachi', 'Karachi', 'Sindh', ' Private', 'www.kasbit.edu.pk', 'Gov of sindh', 0),
(121, 'Karachi School for Business & Leadership', 'Karachi', 'Sindh', ' Private', 'www.ksbl.edu.pk', 'Gov of sindh', 0),
(122, 'Muhammad Ali Jinnah University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.jinnah.edu', 'Gov of sindh', 1),
(123, 'Newport Institute of Communications & Economics, Karachi', 'Karachi', 'Sindh', ' Private', 'www.newports.edu.pk', 'Gov of sindh', 0),
(124, 'Preston Institute of Management, Science and Technology, Karachi', 'Karachi', 'Sindh', ' Private', 'pimsat-khi.edu.pk', 'Gov of sindh', 0),
(125, 'Preston University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.preston.edu.pk', 'Gov of sindh', 0),
(126, 'Shaheed Zulfikar Ali Bhutto Institute of Sc. & Technology (SZABIST), Karachi', 'Karachi', 'Sindh', ' Private', 'www.szabist.edu.pk', 'Gov of sindh', 4),
(127, 'Shaheed Benazir Bhutto City University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.sbbcu.edu.pk', 'Gov of sindh', 0),
(128, 'Sir Syed University of Engg. & Technology, Karachi', 'Karachi', 'Sindh', ' Private', 'www.ssuet.edu.pk', 'Gov of sindh', 0),
(129, 'Sindh Institute of Medical Sciences, Karachi', 'Karachi', 'Sindh', ' Private', 'www.siut.org', 'Gov of sindh', 0),
(130, 'Textile Institute of Pakistan, Karachi', 'Karachi', 'Sindh', ' Private', 'www.tip.edu.pk', 'Gov of sindh', 0),
(131, 'Nazeer Hussain University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.nhu.edu.pk', 'Gov of sindh', 0),
(132, 'Zia-ud-Din University, Karachi', 'Karachi', 'Sindh', ' Private', 'www.zu.edu.pk', 'Gov of sindh', 0),
(133, 'Shaheed Benazir Bhutto Dewan University, Karachi', 'Karachi', 'Sindh', ' Private', '', 'Gov of sindh', 0),
(134, 'Abdul Wali Khan University, Mardan', 'Mardan', 'Khyber Pakhtunkhwa', 'Public', 'www.awkum.edu.pk', 'Gov of KPK', 0),
(135, 'Bacha Khan University, Charsadda', 'Charsadda', 'Khyber Pakhtunkhwa', 'Public', 'www.bkuc.edu.pk/', 'Gov of KPK', 0),
(136, 'Frontier Women University, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.fwu.edu.pk', 'Gov of KPK', 0),
(137, 'Gomal University, D.I. Khan', 'D.I.Khan', 'Khyber Pakhtunkhwa', 'Public', 'www.gu.edu.pk/', 'Gov of KPK', 0),
(138, 'Hazara University, Dodhial, Mansehra', 'Manshera', 'Khyber Pakhtunkhwa', 'Public', 'www.hu.edu.pk/', 'Gov of KPK', 0),
(139, 'Institute of Management Science, Peshawar (IMS)', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.imsciences.edu.pk', 'Gov of KPK', 0),
(140, 'Islamia College University, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.icp.edu.pk', 'Gov of KPK', 0),
(141, 'Khyber Medical University, Peshawar ', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.kmu.edu.pk', 'Gov of KPK', 0),
(142, 'Kohat University of Science and Technology, Kohat', 'Kohat', 'Khyber Pakhtunkhwa', 'Public', 'www.kust.edu.pk', 'Gov of KPK', 0),
(143, 'Khushal Khan Khattak University, Karak', 'Karak', 'Khyber Pakhtunkhwa', 'Public', 'Under construction', 'Gov of KPK', 0),
(144, 'Khyber Pakhtunkhwa Agricultural University, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.aup.edu.pk', 'Gov of KPK', 0),
(145, 'University of Engineering & Technology, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.uetpeshawar.edu.pk', 'Gov of KPK', 4),
(146, 'Shaheed Benazir Bhutto University, Sheringal, Dir', 'Dir', 'Khyber Pakhtunkhwa', 'Public', 'www.sbbu.edu.pk', 'Gov of KPK', 0),
(147, 'University of Malakand, Chakdara, Dir, Malakand', 'Malakand', 'Khyber Pakhtunkhwa', 'Public', 'www.uom.edu.pk', 'Gov of KPK', 0),
(148, 'University of Peshawar, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', 'Public', 'www.upesh.edu.pk', 'Gov of KPK', 0),
(149, 'University of Science & Technology, Bannu', 'Bannu', 'Khyber Pakhtunkhwa', 'Public', 'www.ustb.edu.pk', 'Gov of KPK', 0),
(150, 'University of Swat, Swat', 'Swat', 'Khyber Pakhtunkhwa', 'Public', 'www.swatuniversity.edu.pk/', 'Gov of KPK', 0),
(151, 'University of Haripur, Haripur', 'Haripur', 'Khyber Pakhtunkhwa', 'Public', 'www.uoh.edu.pk/‎ ', 'Gov of KPK', 0),
(152, 'University of Swabi,Swabi', 'Swabi', 'Khyber Pakhtunkhwa', 'Public', 'www.uoswabi.edu.pk/', 'Gov of KPK', 0),
(153, 'Abasyn University, Peshawar ', 'Peshawar', 'Khyber Pakhtunkhwa', ' Private', 'www.abasyn.edu.pk', 'Gov of KPK', 1),
(154, 'CECOS University of Information Technology and Emerging Sciences, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', ' Private', 'www.cecos.edu.pk', 'Gov of KPK', 0),
(155, 'City University of Science and Information Technology, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', ' Private', 'www.cityuniversity.edu.pk', 'Gov of KPK', 0),
(156, 'Gandhara University, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', ' Private', 'www.gandhara.edu.pk', 'Gov of KPK', 0),
(157, 'Ghulam Ishaq Khan Institute of Engineering Sciences & Technology, Topi', 'Topi', 'Khyber Pakhtunkhwa', ' Private', 'www.giki.edu.pk', 'Gov of KPK', 0),
(158, 'Iqra National University, Peshawar', 'Peshawar', 'Khyber Pakhtunkhwa', ' Private', 'www.iqrapsh.edu.pk', 'Gov of KPK', 0),
(159, 'Northern University, Nowshera', 'Nowshera', 'Khyber Pakhtunkhwa', ' Private', 'www.northern.edu.pk', 'Gov of KPK', 0),
(160, 'Preston University, Kohat', 'Kohat', 'Khyber Pakhtunkhwa', ' Private', 'www.preston.edu.pk', 'Gov of KPK', 4),
(161, 'Qurtaba University of Science and Information Technology, D.I. Khan', 'D.I.Khan', 'Khyber Pakhtunkhwa', ' Private', 'www.qurtuba.edu.pk', 'Gov of KPK', 1),
(162, 'Sarhad University of Science and Information Technology, Peshawar ', 'Peshawar', 'Khyber Pakhtunkhwa', ' Private', 'www.suit.edu.pk', 'Gov of KPK', 0),
(163, 'Balochistan University of Engineering & Technology, Khuzdar', 'Khuzdar', 'Balochistan', 'Public', 'buetk.edu.pk', 'Gov of Balochistan', 0),
(164, 'Balochistan University of Information Technology & Management Sciences, Quetta', 'Quetta', 'Balochistan', 'Public', 'www.buitms.edu.pk', 'Gov of Balochistan', 0),
(165, 'Lasbela University of Agriculture, Water and Marine Sciences', 'Lasbela', 'Balochistan', 'Public', 'www.luawms.edu.pk', 'Gov of Balochistan', 0),
(166, 'Sardar Bahadur Khan Women University, Quetta', 'Quetta', 'Balochistan', 'Public', 'www.sbkwu.edu.pk', 'Gov of Balochistan', 0),
(167, 'University of Balochistan, Quetta', 'Quetta', 'Balochistan', 'Public', 'www.uob.edu.pk', 'Gov of Balochistan', 1),
(168, 'University of Turbat, Turbat', 'Turbat', 'Balochistan', 'Public', 'www.uot.edu.pk', 'Gov of Balochistan', 0),
(169, 'University of Loralai, Loralai', 'Loralai', 'Balochistan', 'Public', 'http://www.uoli.edu.pk/', 'Gov of Balochistan', 0),
(170, 'Al-Hamd Islamic University, Quetta', 'Quetta', 'Balochistan', ' Private', 'http://www.aiu.edu.pk', 'Gov of Balochistan', 1),
(171, 'Mirpur University of Science and Technology (MUST), AJ&K', 'Mirpur', 'Azad Jammu and Kashmir', 'Public', 'www.must.edu.pk', 'Gov of AJK', 0),
(172, 'University of Azad Jammu & Kashmir, Muzaffarabad, Azad Kashmir, Muzaffarabad', 'Muzaffarabad', 'Azad Jammu and Kashmir', 'Public', 'www.ajku.edu.pk', 'Gov of AJK', 0),
(173, 'University of Poonch, Rawalakot', 'Rawalakot', 'Azad Jammu and Kashmir', 'Public', 'www.upr.edu.pk', 'Gov of AJK', 0),
(174, 'Women University of Azad Jammu and Kashmir Bagh', 'Bagh', 'Azad Jammu and Kashmir', 'Public', '      under construction', 'Gov of AJK', 0),
(175, 'University of Management Sciences and Information Technology, Kotli', 'Kotli', 'Azad Jammu and Kashmir', 'Public', 'under construction', 'Gov of AJK', 0),
(176, 'Al-Khair University, AJ&K ', 'Bhimber', 'Azad Jammu and Kashmir', ' Private', 'www.alkhair.edu.pk', 'Gov of AJK', 0),
(177, 'Mohi-ud-Din Islamic University, AJK ', 'Nerain Sharif', 'Azad Jammu and Kashmir', ' Private', 'http://www.miu.edu.pk', 'Gov of AJK', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
