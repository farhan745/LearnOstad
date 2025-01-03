-- Active: 1728316517915@@127.0.0.1@3306@test

--Table
--SELECT count(*) as Total_Customers,CITY,POSTAL_CODE,STATE FROM CUSTOMER GROUP BY CITY, POSTAL_CODE;


--Group
--SELECT * FROM CUSTOMER Where ( City = "Salem" AND POSTAL_CODE  IN ("03079","03080") ) OR (City="Wilmington" AND POSTAL_CODE='01887');


--Multi data connect
SELECT INDIVIDUAL.CUST_ID,individual.FIRST_NAME,individual.`LAST_NAME`,customer.`POSTAL_CODE` FROM customer,individual WHERE city='Salem' AND customer.`CUST_ID`=individual.`CUST_ID`;

--Join ON [Its better then comma(,)]
SELECT INDIVIDUAL.CUST_ID,individual.FIRST_NAME,individual.`LAST_NAME`,customer.`POSTAL_CODE` FROM customer JOIN individual ON customer.`CUST_ID`=individual.`CUST_ID`   ;

--Sum
SELECT SUM(AVAIL_BALANCE),CUST_ID,OPEN_BRANCH_ID FROM ACCOUNT GROUP BY CUST_ID,OPEN_BRANCH_ID;