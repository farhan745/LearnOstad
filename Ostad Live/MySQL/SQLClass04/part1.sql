
SELECT "Hello World" as msg

SELECT 2+2 as sum

SELECT "Hello world" as msg1, 2+2 as sum1 , 10-4 as sub1 , 10*10 as mul1 


--- Declare and assign values to variables
SET @num1=10; SET @num2=20; SET @num3=30;
-- Basic Arithmetic Operations
SELECT
@num1+@num2 AS Addition,
@num1-@num2 AS Subtraction,
@num1*@num2 AS Multiplication,
@num1/@num2 AS Division,
@num3 % @num2 AS Modulus

-- Power/ Square Root/ Round values
SELECT 
POWER(@num1,2) AS PowerNum1Squared,
SQRT(@num3) AS SquareRootNum3, 
ROUND(@num3 / @num2, 2) AS RoundedDivision


SELECT LOWER("HELLO WORLD") AS lower_case
SELECT REVERSE("HELLO WORLD") AS reverse_string


SELECT NOW() as currentTime
SELECT DATEDIFF('2024-12-25', '2024-10-03') AS DaysDifference;
SELECT MINUTE('2024-10-03 14:30:10') AS MinuteValue;




