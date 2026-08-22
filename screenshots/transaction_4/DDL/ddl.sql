-- Создаём таблицу Departments
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

-- Добавляем Email в Employees
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);

-- Заполняем Email существующих сотрудников
UPDATE Employees
SET Email = 'alice.smith@example.com'
WHERE EmployeeID = 1;

UPDATE Employees
SET Email = 'bob.johnson@example.com'
WHERE EmployeeID = 2;

UPDATE Employees
SET Email = 'charlie.brown@example.com'
WHERE EmployeeID = 3;

UPDATE Employees
SET Email = 'diana.prince@example.com'
WHERE EmployeeID = 4;

UPDATE Employees
SET Email = 'eve.davis@example.com'
WHERE EmployeeID = 5;

UPDATE Employees
SET Email = 'john.wilson@example.com'
WHERE EmployeeID = 6;

UPDATE Employees
SET Email = 'anna.taylor@example.com'
WHERE EmployeeID = 7;

-- Добавляем UNIQUE для Email
ALTER TABLE Employees
ADD CONSTRAINT unique_employee_email UNIQUE (Email);

--  Переименовываем Location
ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;

--  Для проверки итогового состояния таблиц
SELECT *
FROM Employees;

SELECT *
FROM Departments;
