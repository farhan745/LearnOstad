-- Active: 1728316517915@@127.0.0.1@3306@modulenine


SELECT 2+2 as sum;
--Hello World Print
SELECT "Hello World" as msg1,10+20 as sum1,10-4 as sub1,10*10 as mul;

--Basic Arithmetic Operation
SET @num1=10;SET @num2=20;
SELECT @num1+@num2 as sum,@num1-@num2 as sub,@num1 * @num2 as mull,@num2/@num1 as divid;

--Power
SELECT POWER(@num2,3) as PowerNum1Square;

--Square Root
SET @sqrtMain=100;
SELECT SQRT(@sqrtMain) as sqrtNum1;

--Logarithm

SELECT LOG(@num1) as logNum1;

--Lower Case/Upper Case
SELECT UPPER("Hello World") as UpperCase;
SELECT LOWER("Hello World") as lowerCase;

--Reversee/Length

SELECT REVERSE("Hello World") as ReverseString;

--Length
SELECT LENGTH("Hello World") as LengthString;

--Current Time
SELECT NOW() as currnt;
SELECT DATEDIFF() as currnt;