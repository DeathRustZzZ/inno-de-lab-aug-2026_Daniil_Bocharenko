-- Создание пользователя
CREATE USER hr_user
WITH PASSWORD 'test';

-- Предоставляем право чтения Employees
GRANT SELECT
ON TABLE Employees
TO hr_user;

-- После тестов предоставляем дополнительные права
GRANT INSERT, UPDATE
ON TABLE Employees
TO hr_user;

-- (Подсказка AI) Как я понял, это нужно для того, чтобы hr_user мог использовать счётчик SERIAL
GRANT USAGE, SELECT
ON SEQUENCE employees_employeeid_seq
TO hr_user;
