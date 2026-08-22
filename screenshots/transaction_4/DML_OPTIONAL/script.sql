-- 1. Находим проекты, в которых Bob Johnson работал более 150 часов
SELECT p.ProjectName
FROM Projects AS p
JOIN EmployeeProjects AS ep
    ON p.ProjectID = ep.ProjectID
JOIN Employees AS e
    ON e.EmployeeID = ep.EmployeeID
WHERE e.FirstName = 'Bob'
  AND e.LastName = 'Johnson'
  AND ep.HoursWorked > 150;


-- 2. Увеличиваем бюджет проектов на 10%,
-- если на проект назначен хотя бы один сотрудник из отдела IT
UPDATE Projects AS p
SET Budget = Budget * 1.10
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects AS ep
    JOIN Employees AS e
        ON e.EmployeeID = ep.EmployeeID
    WHERE ep.ProjectID = p.ProjectID
      AND e.Department = 'IT'
);

-- Проверка
SELECT ProjectID, ProjectName, Budget
FROM Projects;


-- 3. Устанавливаем EndDate на один год позже StartDate,
-- если EndDate ещё не указана
UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;

-- Проверка
SELECT ProjectID, ProjectName, StartDate, EndDate
FROM Projects;


-- 4. Добавляем нового сотрудника и сразу назначаем
-- его на проект Website Redesign
-- Разбирал решение с AI
BEGIN;

WITH new_employee AS (
    INSERT INTO Employees (
        FirstName,
        LastName,
        Department,
        Salary,
        Email
    )
    VALUES (
        'John',
        'Doe',
        'Marketing',
        60000.00,
        'john.doe@example.com'
    )
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (
    EmployeeID,
    ProjectID,
    HoursWorked
)
SELECT
    new_employee.EmployeeID,
    p.ProjectID,
    80
FROM new_employee
JOIN Projects AS p
    ON p.ProjectName = 'Website Redesign';

COMMIT;

-- Проверка
SELECT *
FROM Employees
WHERE Email = 'john.doe@example.com';

SELECT
    e.FirstName,
    e.LastName,
    p.ProjectName,
    ep.HoursWorked
FROM EmployeeProjects AS ep
JOIN Employees AS e
    ON e.EmployeeID = ep.EmployeeID
JOIN Projects AS p
    ON p.ProjectID = ep.ProjectID
WHERE e.Email = 'john.doe@example.com';
