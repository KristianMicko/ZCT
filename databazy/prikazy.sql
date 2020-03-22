create database zct;
use zct;


CREATE TABLE `data` (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  `zamestnanci` text,
  `pozicia` text,
  `zaciatok` text,
  `posledny` text,
  `email` text,
  `vek` int(11) DEFAULT NULL,
  `adresa` text,
  `karta` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `prihlasenie` (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `meno` text,
  `heslo` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `prihlasenie` (`ID`, `meno`, `heslo`) VALUES(1, 'Jozef@ss.com', 'tajny');

INSERT INTO `data` (`ID`, `zamestnanci`, `pozicia`, `zaciatok`, `posledny`, `email`, `vek`, `adresa`, `karta`) VALUES
(1, 'Brandon Green', 'CMOF', '16 Nov 2012', '16 Nov 2017', 'brandon94@example.com', 30, 'New York City, NY', '424242xxxxxx6262');