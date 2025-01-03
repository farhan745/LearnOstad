-- DELETE 
DELETE FROM users WHERE id=10

-- UPDATE 
UPDATE users SET firstName='Rabbil', lastName='Hasan' WHERE id=1


-- INSERT 
INSERT INTO users
(firstName,lastName,email,mobile,password,otp)
VALUES
('A','B','C1','D','E','0'),
('A','B','C2','D','E','0'),
('A','B','C3','D','E','0'),
('A','B','C4','D','E','0'),
('A','B','C5','D','E','0'),
('A','B','C6','D','E','0')