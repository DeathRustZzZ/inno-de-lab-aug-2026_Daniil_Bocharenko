-- Добавляем двух сотрудников
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES
    ('John', 'Wilson', 'Marketing', 55000.00),
    ('Anna', 'Taylor', 'Finance', 63000.00);
-- Выбираем всех сотрудников
SELECT *
FROM Employees;
-- Выбираем имя и фамилию сотрудников отдела IT
SELECT FirstName, LastName
FROM Employees
WHERE Department = 'IT';
-- Изменяем зарплату Alice Smith
UPDATE Employees
SET Salary = 65000.00
WHERE FirstName = 'Alice'
  AND LastName = 'Smith';
-- Удаляем Eve Davis
DELETE FROM Employees
WHERE FirstName = 'Eve'
  AND LastName = 'Davis';
-- Проверяем итоговое состояние таблицы
SELECT *
FROM Employees;
