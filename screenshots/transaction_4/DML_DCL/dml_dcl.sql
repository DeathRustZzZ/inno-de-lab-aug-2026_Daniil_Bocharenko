-- 1. Увеличиваем Salary сотрудников HR на 10%
UPDATE Employees
SET Salary = Salary * 1.10
WHERE Department = 'HR';

SELECT EmployeeID, FirstName, LastName, Department, Salary
FROM Employees
WHERE Department = 'HR';

-- 2. Меняем Department сотрудникам с Salary > 70000
UPDATE Employees
SET Department = 'Senior IT'
WHERE Salary > 70000.00;

SELECT EmployeeID, FirstName, LastName, Department, Salary
FROM Employees
WHERE Department = 'Senior IT';

-- 3. Удаляем сотрудников, не назначенных ни на один проект
DELETE FROM Employees AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM EmployeeProjects AS ep
    WHERE ep.EmployeeID = e.EmployeeID
);

SELECT *
FROM Employees;

-- 4. Создаём проект и назначаем двух сотрудников
BEGIN;

INSERT INTO Projects (
    ProjectName,
    Budget,
    StartDate,
    EndDate
)
VALUES (
    'PitGO',
    120000.00,
    '2026-08-10',
    '2027-09-07'
);

INSERT INTO EmployeeProjects (
    EmployeeID,
    ProjectID,
    HoursWorked
)
VALUES
    (2, 4, 100),
    (4, 4, 80);

COMMIT;

-- Проверка
SELECT *
FROM EmployeeProjects
WHERE ProjectID = 4;
