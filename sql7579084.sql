-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Φιλοξενητής: sql7.freesqldatabase.com
-- Χρόνος δημιουργίας: 23 Νοε 2022 στις 18:37:11
-- Έκδοση διακομιστή: 5.5.62-0ubuntu0.14.04.1
-- Έκδοση PHP: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `sql7579084`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
--

CREATE TABLE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (
  `ΤΙΤΛΟΣ` varchar(100) NOT NULL,
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` varchar(6) NOT NULL,
  `ΓΛΩΣΣΑ` varchar(12) NOT NULL,
  `ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ` date NOT NULL,
  `ΗΜΕΡΟΜΗΝΙΑ ΠΡΟΣΘΗΚΗΣ` date NOT NULL,
  `OPEN_URL` varchar(100) NOT NULL,
  `DOWNLOAD_URL` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
--

INSERT INTO `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΤΙΤΛΟΣ`, `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΓΛΩΣΣΑ`, `ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ`, `ΗΜΕΡΟΜΗΝΙΑ ΠΡΟΣΘΗΚΗΣ`, `OPEN_URL`, `DOWNLOAD_URL`) VALUES
('Uncertainty', '400001', 'αγγλικά', '2019-12-01', '2019-12-18', 'https://drive.google.com/file/d/1TwFaqjhbRCbCkja5I__bYnK4CShKdAjs/view?usp=sharing', '1TwFaqjhbRCbCkja5I__bYnK4CShKdAjs'),
('Human action annotation, modeling and analysis based on implicit user interaction ', '400002', 'αγγλικά', '2009-10-09', '2019-12-15', 'https://drive.google.com/file/d/1iBzl6XRqhG51zUxOVrraBwrIrrsFJJ-q/view?usp=sharing', '1iBzl6XRqhG51zUxOVrraBwrIrrsFJJ-q'),
('Measurable events indexed by trees', '400003', 'αγγλικά', '2012-03-12', '2019-12-26', 'https://drive.google.com/file/d/1PRGRzQ6D_Bbr7Y9n2E4qSS1v_3k_oih_/view?usp=sharing', '1PRGRzQ6D_Bbr7Y9n2E4qSS1v_3k_oih_'),
('The copula echo state network', '400004', 'αγγλικά', '2011-07-19', '2019-12-27', 'https://drive.google.com/file/d/1-OtQr-Ou5nj3KBYLyuCIckoU3PU-oYqa/view?usp=sharing', '1-OtQr-Ou5nj3KBYLyuCIckoU3PU-oYqa'),
('When investing in learning technology, look at value, not just ROI', '400005', 'αγγλικά', '2004-06-01', '2019-12-15', 'https://drive.google.com/file/d/1HJ1JpE6wD2lK_8HtQu_J09XfVaNoSggs/view?usp=sharing', '1HJ1JpE6wD2lK_8HtQu_J09XfVaNoSggs'),
('E-learning at Boston College: classic education meets 21st-century technology', '400006', 'αγγλικά', '2005-07-01', '2019-12-26', 'https://drive.google.com/file/d/1N4jsm-EJganK0Ac2RnZ0moRQBpjSTWhr/view?usp=sharing', '1N4jsm-EJganK0Ac2RnZ0moRQBpjSTWhr'),
('India: is IT the future?', '400007', 'αγγλικά', '2000-06-04', '2019-12-13', 'https://drive.google.com/file/d/1j_yzleIGE3XeYIGciyt7ld_yb3IEZ04v/view?usp=sharing', '1j_yzleIGE3XeYIGciyt7ld_yb3IEZ04v'),
('The somatic engineer', '400008', 'αγγλικά', '2002-09-23', '2019-12-18', 'https://drive.google.com/file/d/1_8UWg4xh_P6D7GfIg78Ijv6_LjghnZgY/view?usp=sharing', '1_8UWg4xh_P6D7GfIg78Ijv6_LjghnZgY'),
('Cell Signaling: Uncovering the secret life of Rho GTPases', '400009', 'αγγλικά', '2019-12-13', '2019-12-22', 'https://drive.google.com/file/d/19yA-5vVomxcnRgHGBCV913Bbk7MEA2zR/view?usp=sharing', '19yA-5vVomxcnRgHGBCV913Bbk7MEA2zR'),
('Neurodegeneration: Fly model sheds light on brain disease', '400010', 'αγγλικά', '2019-12-06', '2019-12-14', 'https://drive.google.com/file/d/1183HenxLFbbV1EdxHOUQ1_01dh8iNMp3/view?usp=sharing', '1183HenxLFbbV1EdxHOUQ1_01dh8iNMp3'),
('A Drosophila model of neuronal ceroid lipofuscinosis CLN4 reveals a hypermorphic gain of function me', '400011', 'αγγλικά', '2019-10-30', '2019-12-19', 'https://drive.google.com/file/d/1G8NePWhayRVYxmKd9RD6BwcGWyanKWUG/view?usp=sharing', '1G8NePWhayRVYxmKd9RD6BwcGWyanKWUG'),
('Philosophy of Biology: Characterizing causality in cancer', '400012', 'αγγλικά', '2019-12-06', '2019-12-26', 'https://drive.google.com/file/d/1vDq_OETqRvWocYLIVguOoKgz03aSymz7/view?usp=sharing', '1vDq_OETqRvWocYLIVguOoKgz03aSymz7'),
('Axon-like protrusions promote small cell lung cancer migration and metastasis', '400013', 'αγγλικά', '2019-12-13', '2019-12-17', 'https://drive.google.com/file/d/1qIqYmD7rCpu32U03aZY-FDxnHqxFc_o0/view?usp=sharing', '1qIqYmD7rCpu32U03aZY-FDxnHqxFc_o0'),
('Winning at Innovation', '400014', 'αγγλικά', '2018-10-01', '2019-12-20', 'https://drive.google.com/file/d/1SJ-o0CJhI4xuBzy_gaFWFBpRU7GzQahb/view?usp=sharing', '1SJ-o0CJhI4xuBzy_gaFWFBpRU7GzQahb'),
('Human pathology in NCL', '400015', 'αγγλικά', '2013-11-03', '2019-12-20', 'https://drive.google.com/file/d/1QNyMsVlVPSQUeli4OeiO2CtZAy5iyvbf/view?usp=sharing', '1QNyMsVlVPSQUeli4OeiO2CtZAy5iyvbf'),
('Analysis and retrieval of events/actions and workflows in video streams', '400016', 'αγγλικά', '2010-04-01', '2019-12-15', 'https://drive.google.com/file/d/1i5VnkvxuzFE7I_xN0tSiYdcg968N2oPx/view?usp=sharing', '1i5VnkvxuzFE7I_xN0tSiYdcg968N2oPx'),
('The beginner\'s creed', '400017', 'αγγλικά', '2017-07-03', '2019-12-18', 'https://drive.google.com/file/d/1L17CclWZbjIHN3jnU0O0N_QCyBD_533Z/view?usp=sharing', '1L17CclWZbjIHN3jnU0O0N_QCyBD_533Z'),
('A Coupled Indian Buffet Process Model for Collaborative Filtering', '400018', 'αγγλικά', '2012-05-01', '2019-12-20', 'https://drive.google.com/file/d/1NeDmzSgSoaYaFpuMPX-FKBH28NJF8gYg/view?usp=sharing', '1NeDmzSgSoaYaFpuMPX-FKBH28NJF8gYg'),
('Do distance and location matter in e-learning?', '400019', 'αγγλικά', '2007-10-01', '2019-12-17', 'https://drive.google.com/file/d/1sg_ZYvDmzdmcoGdDiHB7FQzLXxIk3RHW/view?usp=sharing', '1sg_ZYvDmzdmcoGdDiHB7FQzLXxIk3RHW'),
('Back to the future: multiple perspectives on \r\nhistorical exhibits', '400020', 'αγγλικά', '2008-03-01', '2019-12-26', 'https://drive.google.com/file/d/1-6jgP06HmJYR5g2p4i0dBlu0V5b-A5XB/view?usp=sharing', '1-6jgP06HmJYR5g2p4i0dBlu0V5b-A5XB'),
('Ask Jack: negotiating\r\n', '400021', 'αγγλικά', '1997-03-01', '2019-12-24', 'https://drive.google.com/file/d/1j56dIluJl54MO-8tQ_JB0sHHehCWZhIE/view?usp=sharing', '1j56dIluJl54MO-8tQ_JB0sHHehCWZhIE'),
('Ask Jack: job search in cyberspace\r\n', '400022', 'αγγλικά', '1998-05-01', '2019-12-25', 'https://drive.google.com/file/d/1LHld2ENcVoE44lR9JxZ4m9SaaqPn8SIP/view?usp=sharing', '1LHld2ENcVoE44lR9JxZ4m9SaaqPn8SIP'),
('Ask Jack: skill development\r\n', '400023', 'αγγλικά', '2007-11-01', '2019-12-28', 'https://drive.google.com/file/d/1aG_2FlFlKd4ToBxajpi_P-uhcbv3jAnY/view?usp=sharing', '1aG_2FlFlKd4ToBxajpi_P-uhcbv3jAnY'),
('Unconditional families in Banach spaces', '400024', 'αγγλικά', '2007-11-01', '2019-12-19', 'https://drive.google.com/file/d/1OYZiNC24UwiUcZlL6k5Y2rVs24VlQGtw/view?usp=sharing', '1OYZiNC24UwiUcZlL6k5Y2rVs24VlQGtw'),
('Video-object oriented biometrics hiding for user authentication under error-prone transmissions\r\n', '400025', 'αγγλικά', '2011-01-03', '2019-12-16', 'https://drive.google.com/file/d/16IMhZlxqBdza5WCMqhddEHhSU3wIhmeY/view?usp=sharing', '16IMhZlxqBdza5WCMqhddEHhSU3wIhmeY'),
('How Robotic Blacksmithing Could Change Manufacturing Forever', '400026', 'αγγλικά', '2019-12-12', '2019-12-26', 'https://drive.google.com/file/d/1L7jOfnLh1eref85h8x5UtQKUcwlQbp2y/view?usp=sharing', '1L7jOfnLh1eref85h8x5UtQKUcwlQbp2y'),
('\'Robotic blacksmithing\': A technology that could revive US manufacturing', '400027', 'αγγλικά', '2019-12-11', '2019-12-22', 'https://drive.google.com/file/d/18QB67NJUeqEA3CnS9Ik9D20P0KxT9Pge/view?usp=sharing', '18QB67NJUeqEA3CnS9Ik9D20P0KxT9Pge'),
('NASA solar probe confirms asteroid source of Geminids meteor shower', '400028', 'αγγλικά', '2019-12-12', '2019-12-18', 'https://drive.google.com/file/d/12J58pPDm6syUFGSBE4Rwc5TmWM1C5LFk/view?usp=sharing', '12J58pPDm6syUFGSBE4Rwc5TmWM1C5LFk'),
('Mars 2020\'s landing site could be a good place to hunt for fossils', '400029', 'αγγλικά', '2019-12-12', '2019-12-25', 'https://drive.google.com/file/d/1IXlxEzeLEYjICAUHAdOrjSq7ssLsBlYv/view?usp=sharing', '1IXlxEzeLEYjICAUHAdOrjSq7ssLsBlYv'),
('NASA\'s Juno probe just discovered a Texas-sized cyclone on Jupiter', '400030', 'αγγλικά', '2019-12-12', '2019-12-15', 'https://drive.google.com/file/d/1BUvh1UOA1x5G7fKA_GQLHvVosrpWkc9c/view?usp=sharing', '1BUvh1UOA1x5G7fKA_GQLHvVosrpWkc9c');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`
--

CREATE TABLE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` (
  `ΟΝΟΜΑ` varchar(50) NOT NULL,
  `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`
--

INSERT INTO `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` (`ΟΝΟΜΑ`, `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`) VALUES
('Computer Science', '600001'),
('Education', '600002'),
('Computing Occupation', '600003'),
('Biochemistry and Chemical Biology', '600004'),
('Neuroscience', '600005'),
('Cancer Biology', '600006'),
('User Interaction', '600007'),
('Servers', '600008'),
('Human object detection ', '600009'),
('Algorithms', '600010'),
('Neural networks', '600011'),
('Cell Biology', '600012'),
('Software and its engineering', '600013'),
('Finite subsets', '600014'),
('Genetics and Genomics', '600015'),
('Video streaming', '600016'),
('Learning systems', '600017'),
('Human Computer Interraction', '600018'),
('Infinite Subtrees', '600019'),
('Biorthogonal Systems', '600020'),
('Banach space', '600021'),
('Ramsay Theorem', '600022'),
('Cryptography', '600023'),
('Biometric identification', '600024'),
('Machine Learning', '600025'),
('Astronomy', '600026');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΠΑΡΑΠΟΜΠΗ`
--

CREATE TABLE `ΠΑΡΑΠΟΜΠΗ` (
  `ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ` varchar(6) NOT NULL,
  `ΤΙΤΛΟΣ ΑΡΘΡΟΥ` varchar(100) DEFAULT NULL,
  `ΟΝΟΜΑ ΤΕΚΜΗΡΙΟΥ` varchar(100) DEFAULT NULL,
  `ΕΤΟΣ ΚΥΚΛΟΦΟΡΙΑΣ` int(4) NOT NULL,
  `ΣΕΛΙΔΕΣ` varchar(12) DEFAULT NULL,
  `ΕΚΔΟΤΗΣ` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΠΑΡΑΠΟΜΠΗ`
--

INSERT INTO `ΠΑΡΑΠΟΜΠΗ` (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`, `ΤΙΤΛΟΣ ΑΡΘΡΟΥ`, `ΟΝΟΜΑ ΤΕΚΜΗΡΙΟΥ`, `ΕΤΟΣ ΚΥΚΛΟΦΟΡΙΑΣ`, `ΣΕΛΙΔΕΣ`, `ΕΚΔΟΤΗΣ`) VALUES
('410101', NULL, 'How Nature Works: The Science of Self-Organized Criticality', 1996, NULL, 'Springer-Verlag'),
('410102', NULL, 'Bak’s Sand Pile: Strategies for a\r\nCatastrophic World', 2011, '382', 'Agile Press'),
('410201', 'Semantic annotation of sports videos', 'IEEE Multimedia vol.9, iss.2', 2002, '52-60', 'IEEE'),
('410202', 'Evaluation of relevance feedback schemes in content-based retrieval\r\nsystems', 'Signal Process Image Comm 21(4)', 2006, '334-357', NULL),
('410203', 'Non-sequential video content representation using temporal\r\nvariation of feature vectors', 'IEEE Trans Consum Electron 46(3)', 2000, '758–768', 'IEEE'),
('410301', 'A partition theorem for perfect sets', 'Proc. Amer. Math. Soc. 82', 1981, '271–277', NULL),
('410302', 'Some unifying principles in Ramsey Theory', 'Discrete Math, 68', 1988, '117–169', NULL),
('410303', 'A density version of the Halpern–\r\nL¨auchli theorem', NULL, 2010, NULL, NULL),
('410401', 'Neural learning of chaotic dynamics', 'NeuralProces-\r\nsing Letters2(2)', 1995, '23–26', NULL),
('410901', 'RhoGTPase activity zones and transient contractile arrays', 'BioEssays 28', 2006, '983–993', NULL),
('410902', 'Concentric zones of\r\nactive RhoA and Cdc42 around single cell wounds', 'Journal of Cell Biology 168', 2005, '429–439', NULL),
('411001', 'Primary fibroblasts from\r\nCSPa mutation carriers recapitulate hallmarks of the\r\nadult onset neuronal', 'Scientific Reports 7', 2007, '6332', NULL),
('411002', NULL, 'The neuronal ceroid-lipofuscinoses.\r\nJournal of Neuropathology & Experimental Neurology\r\n62', 2003, '1–13', NULL),
('411101', 'Amyloid-beta as a positive endogenous\r\nregulator of release probability at hippocampal synapses', 'Nature Neuroscience 12', 2009, '1567–1576', NULL),
('411102', 'Exome-sequencing confirms DNAJC5 mutations as cause of adult neuronal ceroid-lipofuscinosis', 'PLOS ONE 6:e26741', 2011, NULL, NULL),
('411201', 'Hierarchies and causal\r\nrelationships in interpretative models of the neoplastic\r\nprocess', 'History and Philosophy of the Life Sciences\r\n33', 2011, '515–535', NULL),
('411202', 'Immunological\r\nconsequences of epithelial-mesenchymal transition in\r\ntumor progression.', 'Journal of Immunology 197', 2016, '691– 698', NULL),
('411401', NULL, 'The\r\nInnovator’s Way: Essential Practices\r\nfor Successful Innovation', 2010, NULL, 'The\r\nInnovator’s Way: Essential Practices\r\nfor Successful Innovation'),
('411402', 'Emergent Innovation', 'CACM, vol. 58,\r\nno. 6', 2015, '28-31', 'ACM'),
('411501', 'The ultrastructural variability of non-specific lipopigments', 'Acta Neuropathol, 48', 1979, '227-230', NULL),
('411701', 'Learning to learn', 'CACM vol.59,iss. 12', 2016, '32-36', NULL),
('411702', NULL, 'Learning to Learn and the Navigation of\r\nMoods', 2016, NULL, 'Pluralistic Networks Publishing'),
('411801', NULL, 'Pattern Recognition and Machine Learning', 2006, NULL, 'Springer'),
('411802', 'Signal modeling and classification using\r\na robust latent space model based on t distributions.', 'IEEE Trans. Signal Processing, 56\r\n(3)', 2008, '949-963', 'IEEE'),
('412201', NULL, 'Electronic Job Search Revolution', 1995, NULL, 'Wiley & Sons, Inc'),
('412202', NULL, 'Electronic Resume Revolution', 1995, NULL, 'Wiley & Sons, Inc'),
('412203', NULL, 'Finding a Job on the Internet', 1995, NULL, 'McGraw Hill, Inc.'),
('412401', 'A proof of Halpern-Läuchli Partition Theorem', 'Eur. J. Comb. 23', 2002, '1-10', NULL),
('412402', 'A partition for perfect sets', 'Proc. Amer. Math. Soc. 82', 1981, '271–277', NULL),
('412501', 'Password authentication with insecure communication', 'CACM vol. 24, no. 11', 1982, '770-772', 'ACM'),
('412502', NULL, 'The S/KEY one-time password system,” in Proceedings\r\nof the ISOC Symposium onNetwork andDistributed ', 1991, '151-157', NULL);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΠΕΡΙΟΔΙΚΟ`
--

CREATE TABLE `ΠΕΡΙΟΔΙΚΟ` (
  `ΟΝΟΜΑ` varchar(100) NOT NULL,
  `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` varchar(6) NOT NULL,
  `ΕΚΔΟΤΗΣ` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΠΕΡΙΟΔΙΚΟ`
--

INSERT INTO `ΠΕΡΙΟΔΙΚΟ` (`ΟΝΟΜΑ`, `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`, `ΕΚΔΟΤΗΣ`) VALUES
('CACM', '100001', 'ACM'),
('Inroads', '100002', 'ACM'),
('XRDS', '100003', 'ACM'),
('Multimedia Tools and Applications', '100004', 'SPRINGER'),
('Combinatorics Probability and Computing', '100005', 'Cambridge University Press'),
('Pattern Recognition', '100006', 'Elsevier'),
('e-Learn', '100007', 'ACM'),
('Ubiquity', '100008', 'ACM'),
('SCI', '100009', 'ASM'),
('Science et pseudo-sciences', '100010', 'Pegasus-Publisheres'),
('Biochimica et Biophysica Acta (BBA) - Molecular Basis of Disease', '100011', 'ELSEVIER'),
('Journal of Machine Learning Research', '100012', 'JMLR'),
('Mathematische Annalen', '100013', 'SPRINGER'),
('Eurasip journal on information security', '100014', 'SPRINGER'),
('Astronomy', '100015', 'Kalmbach Media'),
('POPULAR MECHANICS', '100016', 'Hearst Communications'),
('The Conversation', '100017', NULL),
('IEEE Computer', '100018', 'IEEE');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
--

CREATE TABLE `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ` (
  `ΕΠΩΝΥΜΟ ΣΥΓΓΡΑΦΕΑ` varchar(15) NOT NULL,
  `ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
--

INSERT INTO `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ` (`ΕΠΩΝΥΜΟ ΣΥΓΓΡΑΦΕΑ`, `ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`) VALUES
('Bak', '410101'),
('Assfalg', '410102'),
('Bertini', '410102'),
('Bimbo', '410102'),
('Colombo', '410102'),
('Lewis', '410102'),
('Doulamis A.', '410202'),
('Doulamis N.', '410202'),
('Doulamis A.', '410203'),
('Doulamis N.', '410203'),
('Blass A.', '410301'),
('Carlson', '410302'),
('Dodos', '410303'),
('Kanellopoulos ', '410303'),
('Deco', '410401'),
('Schurmann', '410401'),
('Bement', '410901'),
('Miller AL', '410901'),
('von Dassow', '410901'),
('Bement', '410902'),
('Benink', '410902'),
('Benitez', '411001'),
('Sands', '411001'),
('Haltia', '411002'),
('Abramov', '411101'),
('Dolev', '411101'),
('Benitez', '411102'),
('Bertolaso', '411201'),
('Chockley', '411202'),
('Keshamouni', '411202'),
('Denning', '411401'),
('Dunham', '411401'),
('Denning', '411402'),
('Flores', '411402'),
('Goebel', '411501'),
('Schulz', '411501'),
('Denning', '411701'),
('Flores', '411701'),
('Flores', '411702'),
('Bishop', '411801'),
('Chatzis', '411802'),
('Kosmopoulos', '411802'),
('Kennedy', '412201'),
('Morrow', '412201'),
('Kennedy', '412202'),
('Morrow', '412202'),
('Glossbrenner A.', '412203'),
('Glossbrenner E.', '412203'),
('Argyros', '412401'),
('Kanellopoulos', '412401'),
('Blass A.', '412402'),
('Lamport', '412501'),
('Haller', '412502');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΣΥΓΓΡΑΦΕΑΣ`
--

CREATE TABLE `ΣΥΓΓΡΑΦΕΑΣ` (
  `ΟΝΟΜΑ` varchar(12) NOT NULL,
  `ΕΠΩΝΥΜΟ` varchar(15) NOT NULL,
  `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` varchar(6) NOT NULL,
  `ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΣΥΓΓΡΑΦΕΑΣ`
--

INSERT INTO `ΣΥΓΓΡΑΦΕΑΣ` (`ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`, `ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ`) VALUES
('Peter', 'Denning', '200001', 'Η.Π.Α.'),
('Lisa', 'Neal', '200002', 'Η.Π.Α.'),
('Jack', 'Wilson', '200003', 'Η.Π.Α.'),
('Ted', 'Lewis', '200004', 'Η.Π.Α.'),
('Nikolaos', 'Doulamis', '200005', 'Ελλάδα'),
('Anastasios', 'Doulamis', '200006', 'Ελλάδα'),
('Nicolas', 'Tsapatsoulis', '200007', 'Κύπρος'),
('Klimis', 'Ntalianis', '200008', 'Ελλάδα'),
('Pantelis', 'Dodos', '200009', 'Ελλάδα'),
('Yiannis', 'Demiris', '200010', 'Ελλάδα'),
('Kostas', 'Tyros', '200011', 'Ελλάδα'),
('Vasilis', 'Kanellopooulos', '200012', 'Ελλάδα'),
('Sotirios', 'Chatzis', '200013', 'Ελλάδα'),
('Dan', 'Kossman', '200014', 'Η.Π.Α.'),
('Rita', 'Owens', '200015', 'Η.Π.Α.'),
('Rahid', 'Raghuraman', '200016', 'Ινδία'),
('Jenna', 'Perry', '200017', 'Αγγλία'),
('Martin', 'Berryer', '200018', 'Η.Π.Α.'),
('Elliot', 'Imler', '200019', 'Αγγλία'),
('Elena', 'Rondeau', '200020', 'Γαλλία'),
('Dian', 'Yang', '200021', 'Κορέα'),
('Glenn', 'Anderson', '200022', 'Αγγλία'),
('Alessandro', 'Simonati', '200023', 'Ιταλία'),
('Fangfei', 'Qu', '200024', 'Κορέα'),
('Barbara', 'Gruner', '200025', 'Γερμάνια'),
('Lindy', 'Barrett', '200026', 'Η.Π.Α.'),
('Lynne', 'Spichiger', '200027', 'Γερμανία'),
('Hailey', 'McLaughlin', '200028', 'Αγγλία'),
('Peter', 'Hemsworth', '200029', 'Αγγλία'),
('Erika', 'Carlson ', '200030', 'Η.Π.Α.'),
('Caurtney', 'Linder', '200031', 'Η.Π.Α.'),
('Glenn', 'Daehn', '200032', 'Η.Π.Α.');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΤΕΥΧΟΣ`
--

CREATE TABLE `ΤΕΥΧΟΣ` (
  `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` varchar(6) NOT NULL,
  `VOLUME` varchar(20) NOT NULL,
  `ISSUE` varchar(20) NOT NULL,
  `ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ ΤΕΥΧΟΥΣ` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΤΕΥΧΟΣ`
--

INSERT INTO `ΤΕΥΧΟΣ` (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`, `VOLUME`, `ISSUE`, `ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ ΤΕΥΧΟΥΣ`) VALUES
('100001', '60', '7', '2017-07-03'),
('100001', '62', '12', '2019-12-01'),
('100003', '3', '3', '1997-03-01'),
('100003', '4', '1', '1997-09-01'),
('100003', '4', '4', '1998-05-01'),
('100004', '2009', '50', '2009-10-09'),
('100004', '2010', '50', '2010-04-01'),
('100005', '21', '3', '2012-05-06'),
('100006', '45', '1', '2012-01-01'),
('100007', '2004', '6', '2004-06-01'),
('100007', '2005', '7', '2005-07-01'),
('100007', '2007', '10', '2007-10-01'),
('100007', '2008', '3', '2008-03-01'),
('100008', '2000', 'May', '2000-05-01'),
('100008', '2002', 'September', '2002-09-01'),
('100009', '15', '1', '2019-10-06'),
('100009', '17', '1', '2019-12-06'),
('100010', '89', '11', '2019-12-06'),
('100010', '89', '12', '2019-12-13'),
('100011', '1832', '11', '2013-11-01'),
('100012', '2012', '25', '2012-05-01'),
('100013', '2008', '341', '2007-11-01'),
('100014', '2011', '45', '2011-01-03'),
('100015', '2019', 'December', '2019-12-12'),
('100016', '2019', 'December', '2019-12-01'),
('100017', '2019', 'December', '2019-12-06'),
('100018', '2018', '10', '2018-10-01');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ΦΟΡΕΑΣ`
--

CREATE TABLE `ΦΟΡΕΑΣ` (
  `ΟΝΟΜΑ` varchar(100) NOT NULL,
  `ΚΩΔΙΚΟΣ ΦΟΡΕΑ` varchar(6) NOT NULL,
  `ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ` varchar(20) NOT NULL,
  `ΧΩΡΑ` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `ΦΟΡΕΑΣ`
--

INSERT INTO `ΦΟΡΕΑΣ` (`ΟΝΟΜΑ`, `ΚΩΔΙΚΟΣ ΦΟΡΕΑ`, `ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ`, `ΧΩΡΑ`) VALUES
('Cyprous University of Technology', '300001', 'Εκπαίδευτικό Ίδρυμα', 'Κύπρος'),
('National Technical University of Athens', '300002', 'Εκπαιδευτικό Ίδρυμα', 'Ελλάδα'),
('Imperial College London', '300003', 'Εκπαιδευτικό Ίδρυμα', 'Αγγλία'),
('OutStart', '300004', 'Εταιρία', 'Η.Π.Α.'),
('Boston College', '300005', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Texas Instruments Ltd., Bangalore', '300006', 'Εταιρία', 'Ινδία'),
('University of North Carolina', '300007', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α'),
('Broad Institute of MIT and Harvard', '300008', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α'),
('University of Arizona', '300009', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α'),
('University of Cambridge', '300010', 'Εκπαιδευτικό Ίδρυμα', 'Αγγλία'),
('University of Bordeaux', '300011', 'Εκπαιδευτικό Ίδρυμα', 'Γαλλία'),
('Stanford University School of Medicine,', '300012', 'Εκπαιδευτικό Ίδρυμα', 'Αγγλία'),
('University of Verona', '300013', 'Εκπαιδευτικό Ίδρυμα', 'Ιταλία'),
('USADepartment of Medical Oncology', '300014', 'Ερευνητικό Κέντρο', 'Η.Π.Α'),
('German Cancer Consortium (DKTK)', '300015', 'Ερευνητικό Κέντρο', 'Γερμανία'),
('Naval Postgranduate School in Monterey', '300016', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Springfield Technical Community College', '300017', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Massachusetts Institute of Technology', '300018', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Princeton University', '300019', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('NASA Ames Research Center', '300020', 'Ερευνητικό Κέντρο', 'Η.Π.Α.'),
('Stanley Center for Psychiatric Research', '300021', 'Ερευνητικό Κέντρο', 'Η.Π.Α.'),
('Harvard University', '300022', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Yale University', '300023', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('University of South Alabama', '300024', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Ohio State University', '300025', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.'),
('Great Ormond Street Hospital, Department of Histopathology', '300026', 'Ερευνητικό Κέντρο', 'Αγγλία'),
('Technical University of Crete', '300027', 'Εκπαιδευτικό Ίδρυμα', 'Ελλάδα'),
('University of Athens', '300028', 'Εκπαιδευτικό Ίδρυμα', 'Ελλάδα'),
('University of Toronto', '300029', 'Εκπαιδευτικό Ίδρυμα', 'Καναδάς'),
('ACM', '300030', 'Εταιρία', NULL),
('University of Pittsburgh', '300031', 'Εκπαιδευτικό Ίδρυμα', 'Η.Π.Α.');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `αναφέρεται`
--

CREATE TABLE `αναφέρεται` (
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` varchar(6) NOT NULL,
  `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `αναφέρεται`
--

INSERT INTO `αναφέρεται` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`) VALUES
('400001', '600013'),
('400002', '600001'),
('400002', '600007'),
('400002', '600008'),
('400002', '600009'),
('400002', '600016'),
('400003', '600001'),
('400003', '600010'),
('400003', '600014'),
('400004', '600001'),
('400004', '600010'),
('400004', '600011'),
('400005', '600002'),
('400006', '600002'),
('400007', '600003'),
('400008', '600003'),
('400009', '600004'),
('400009', '600012'),
('400010', '600005'),
('400011', '600005'),
('400012', '600006'),
('400012', '600012'),
('400012', '600015'),
('400013', '600006'),
('400014', '600001'),
('400015', '600005'),
('400016', '600016'),
('400017', '600002'),
('400018', '600001'),
('400018', '600017'),
('400019', '600002'),
('400020', '600002'),
('400021', '600003'),
('400022', '600018'),
('400023', '600002'),
('400024', '600019'),
('400024', '600020'),
('400024', '600021'),
('400024', '600022'),
('400025', '600023'),
('400025', '600024'),
('400026', '600017'),
('400026', '600023'),
('400026', '600025'),
('400027', '600017'),
('400027', '600025'),
('400028', '600026'),
('400029', '600026'),
('400030', '600026');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `παραπέμπει εκτός`
--

CREATE TABLE `παραπέμπει εκτός` (
  `ΚΩΔΙΚΟΣ ΠΑΡΑΠΜΠΗΣ` varchar(6) NOT NULL,
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `παραπέμπει εκτός`
--

INSERT INTO `παραπέμπει εκτός` (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΜΠΗΣ`, `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`) VALUES
('410101', '400001'),
('410102', '400001'),
('410201', '400002'),
('410202', '400002'),
('410203', '400002'),
('410301', '400003'),
('410302', '400003'),
('410303', '400003'),
('410401', '400004'),
('410901', '400009'),
('410902', '400009'),
('411001', '400010'),
('411002', '400010'),
('411101', '400011'),
('411102', '400011'),
('411201', '400012'),
('411202', '400012'),
('411401', '400014'),
('411402', '400014'),
('411501', '400015'),
('411701', '400017'),
('411702', '400017'),
('411801', '400018'),
('411802', '400018'),
('412201', '400022'),
('412202', '400022'),
('412203', '400022'),
('412401', '400024'),
('412402', '400024'),
('412501', '400025'),
('412502', '400025');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `παραπέμπει εντός`
--

CREATE TABLE `παραπέμπει εντός` (
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΠΡΩΤΟΥ` varchar(6) NOT NULL,
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `παραπέμπει εντός`
--

INSERT INTO `παραπέμπει εντός` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΠΡΩΤΟΥ`, `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ`) VALUES
('400010', '400011'),
('400001', '400014'),
('400011', '400015');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `περιλαμβάνεται`
--

CREATE TABLE `περιλαμβάνεται` (
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` varchar(6) NOT NULL,
  `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` varchar(6) NOT NULL,
  `VOLUME` varchar(20) NOT NULL,
  `ISSUE` varchar(20) NOT NULL,
  `ΣΕΛΙΔΕΣ` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `περιλαμβάνεται`
--

INSERT INTO `περιλαμβάνεται` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`, `VOLUME`, `ISSUE`, `ΣΕΛΙΔΕΣ`) VALUES
('400001', '100001', '62', '12', '26-28'),
('400002', '100004', '2010', '50', '1-6'),
('400003', '100005', '21', '3', '374-411'),
('400004', '100006', '45', '1', '570-577'),
('400005', '100007', '2004', '6', '125'),
('400006', '100007', '2005', '7', '3'),
('400007', '100008', '2000', 'May', '58'),
('400008', '100008', '2002', 'September', '32-38'),
('400009', '100009', '17', '1', '10-12'),
('400010', '100009', '17', '1', '20-21'),
('400011', '100009', '15', '1', '100-133'),
('400012', '100010', '89', '11', '26-32'),
('400013', '100010', '89', '12', '6-19'),
('400014', '100018', '2018', '10', '32-39'),
('400015', '100011', '1832', '11', '1807-1826'),
('400016', '100004', '2009', '50', '199-225'),
('400017', '100001', '60', '7', '30-31'),
('400018', '100012', '2012', '25', '65-79'),
('400019', '100007', '2007', '10', '1'),
('400020', '100007', '2008', '3', '18'),
('400021', '100003', '3', '3', '29'),
('400022', '100003', '4', '4', '29-31'),
('400023', '100003', '4', '1', '26'),
('400024', '100013', '2008', '341', '15-38'),
('400025', '100014', '2011', '45', '15-27'),
('400026', '100016', '2019', 'December', '20-26'),
('400027', '100017', '2019', 'December', '160-164'),
('400028', '100015', '2019', 'December', '5-7'),
('400029', '100015', '2019', 'December', '10-11'),
('400030', '100015', '2019', 'December', '18-20');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `συγγράφει`
--

CREATE TABLE `συγγράφει` (
  `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` varchar(6) NOT NULL,
  `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` varchar(6) NOT NULL,
  `ΚΩΔΙΚΟΣ ΦΟΡΕΑ` varchar(6) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Άδειασμα δεδομένων του πίνακα `συγγράφει`
--

INSERT INTO `συγγράφει` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`, `ΚΩΔΙΚΟΣ ΦΟΡΕΑ`) VALUES
('400001', '200001', '300016'),
('400008', '200001', '300019'),
('400014', '200001', '300016'),
('400017', '200001', '300016'),
('400019', '200002', '300017'),
('400020', '200002', '300017'),
('400021', '200003', '300030'),
('400022', '200003', '300030'),
('400023', '200003', '300030'),
('400001', '200004', '300016'),
('400002', '200005', '300002'),
('400016', '200005', '300027'),
('400002', '200006', '300027'),
('400016', '200006', '300027'),
('400002', '200007', '300001'),
('400025', '200007', '300001'),
('400002', '200008', '300002'),
('400025', '200008', '300001'),
('400003', '200009', '300028'),
('400024', '200009', '300002'),
('400004', '200010', '300003'),
('400003', '200011', '300002'),
('400003', '200012', '300029'),
('400024', '200012', '300002'),
('400004', '200013', '300003'),
('400018', '200013', '300001'),
('400005', '200014', '300004'),
('400006', '200015', '300005'),
('400007', '200016', '300006'),
('400009', '200017', '300007'),
('400010', '200018', '300008'),
('400010', '200018', '300021'),
('400010', '200018', '300022'),
('400011', '200019', '300009'),
('400011', '200019', '300023'),
('400012', '200020', '300008'),
('400012', '200020', '300011'),
('400013', '200021', '300012'),
('400013', '200021', '300024'),
('400015', '200022', '300026'),
('400015', '200023', '300013'),
('400013', '200024', '300012'),
('400013', '200024', '300024'),
('400013', '200025', '300012'),
('400013', '200025', '300014'),
('400013', '200025', '300015'),
('400010', '200026', '300008'),
('400010', '200026', '300021'),
('400010', '200026', '300022'),
('400020', '200027', '300017'),
('400028', '200028', '300005'),
('400029', '200030', '300020'),
('400030', '200030', '300020'),
('400026', '200031', '300031'),
('400027', '200032', '300025');

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
--
ALTER TABLE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`);

--
-- Ευρετήρια για πίνακα `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`
--
ALTER TABLE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`);

--
-- Ευρετήρια για πίνακα `ΠΑΡΑΠΟΜΠΗ`
--
ALTER TABLE `ΠΑΡΑΠΟΜΠΗ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`);

--
-- Ευρετήρια για πίνακα `ΠΕΡΙΟΔΙΚΟ`
--
ALTER TABLE `ΠΕΡΙΟΔΙΚΟ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`);

--
-- Ευρετήρια για πίνακα `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
--
ALTER TABLE `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
  ADD PRIMARY KEY (`ΕΠΩΝΥΜΟ ΣΥΓΓΡΑΦΕΑ`,`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`),
  ADD KEY `ΣΥΓΓΡΑΦΕΙΣ ΠΑΡΑΠΟΜΠΩΝ_fk0` (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`);

--
-- Ευρετήρια για πίνακα `ΣΥΓΓΡΑΦΕΑΣ`
--
ALTER TABLE `ΣΥΓΓΡΑΦΕΑΣ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`);

--
-- Ευρετήρια για πίνακα `ΤΕΥΧΟΣ`
--
ALTER TABLE `ΤΕΥΧΟΣ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`,`VOLUME`,`ISSUE`),
  ADD KEY `ΤΕΥΧΟΣ_fk0` (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`);

--
-- Ευρετήρια για πίνακα `ΦΟΡΕΑΣ`
--
ALTER TABLE `ΦΟΡΕΑΣ`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`);

--
-- Ευρετήρια για πίνακα `αναφέρεται`
--
ALTER TABLE `αναφέρεται`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`,`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`),
  ADD KEY `αναφέρεται_fk0` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD KEY `αναφέρεται_fk1` (`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`);

--
-- Ευρετήρια για πίνακα `παραπέμπει εκτός`
--
ALTER TABLE `παραπέμπει εκτός`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΜΠΗΣ`,`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD KEY `παραπέμπει εκτός_fk1` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD KEY `παραπέμπει εκτός_fk0` (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΜΠΗΣ`);

--
-- Ευρετήρια για πίνακα `παραπέμπει εντός`
--
ALTER TABLE `παραπέμπει εντός`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΠΡΩΤΟΥ`,`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ`),
  ADD KEY `παραπέμπει εντός_fk1` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ`),
  ADD KEY `παραπέμπει εντός_fk0` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΠΡΩΤΟΥ`);

--
-- Ευρετήρια για πίνακα `περιλαμβάνεται`
--
ALTER TABLE `περιλαμβάνεται`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`,`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`,`VOLUME`,`ISSUE`),
  ADD KEY `περιλαμβάνεται_fk1` (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`,`VOLUME`,`ISSUE`),
  ADD KEY `περιλαμβάνεται_fk0` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`);

--
-- Ευρετήρια για πίνακα `συγγράφει`
--
ALTER TABLE `συγγράφει`
  ADD PRIMARY KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`,`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`,`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`),
  ADD KEY `συγγράφει_fk1` (`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`),
  ADD KEY `συγγράφει_fk2` (`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`),
  ADD KEY `συγγράφει_fk0` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`);

--
-- Περιορισμοί για άχρηστους πίνακες
--

--
-- Περιορισμοί για πίνακα `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
--
ALTER TABLE `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
  ADD CONSTRAINT `ΣΥΓΓΡΑΦΕΙΣ ΠΑΡΑΠΟΜΠΩΝ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`) REFERENCES `ΠΑΡΑΠΟΜΠΗ` (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`);

--
-- Περιορισμοί για πίνακα `ΤΕΥΧΟΣ`
--
ALTER TABLE `ΤΕΥΧΟΣ`
  ADD CONSTRAINT `ΤΕΥΧΟΣ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`) REFERENCES `ΠΕΡΙΟΔΙΚΟ` (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`);

--
-- Περιορισμοί για πίνακα `αναφέρεται`
--
ALTER TABLE `αναφέρεται`
  ADD CONSTRAINT `αναφέρεται_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD CONSTRAINT `αναφέρεται_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` (`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`);

--
-- Περιορισμοί για πίνακα `παραπέμπει εκτός`
--
ALTER TABLE `παραπέμπει εκτός`
  ADD CONSTRAINT `παραπέμπει εκτός_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΜΠΗΣ`) REFERENCES `ΠΑΡΑΠΟΜΠΗ` (`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`),
  ADD CONSTRAINT `παραπέμπει εκτός_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`);

--
-- Περιορισμοί για πίνακα `παραπέμπει εντός`
--
ALTER TABLE `παραπέμπει εντός`
  ADD CONSTRAINT `παραπέμπει εντός_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΠΡΩΤΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD CONSTRAINT `παραπέμπει εντός_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`);

--
-- Περιορισμοί για πίνακα `περιλαμβάνεται`
--
ALTER TABLE `περιλαμβάνεται`
  ADD CONSTRAINT `περιλαμβάνεται_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD CONSTRAINT `περιλαμβάνεται_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`,`VOLUME`,`ISSUE`) REFERENCES `ΤΕΥΧΟΣ` (`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`, `VOLUME`, `ISSUE`);

--
-- Περιορισμοί για πίνακα `συγγράφει`
--
ALTER TABLE `συγγράφει`
  ADD CONSTRAINT `συγγράφει_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`) REFERENCES `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` (`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`),
  ADD CONSTRAINT `συγγράφει_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`) REFERENCES `ΣΥΓΓΡΑΦΕΑΣ` (`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`),
  ADD CONSTRAINT `συγγράφει_fk2` FOREIGN KEY (`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`) REFERENCES `ΦΟΡΕΑΣ` (`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
