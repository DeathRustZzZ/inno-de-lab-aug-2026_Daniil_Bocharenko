-- Разбирал решение с AI
-- CREATE OR REPLACE использовал для удобства повторного тестирования скрипта.

-- 1. Создаём функцию расчёта бонуса
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    employee_id INT,
    salary DECIMAL
)
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN salary * 0.10;
END;
$$;


-- 2. Проверяем функцию для каждого сотрудника
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary,
    CalculateAnnualBonus(EmployeeID, Salary) AS AnnualBonus
FROM Employees;


-- 3. Создаём представление сотрудников IT

create or replace VIEW IT_Department_View AS
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM Employees
WHERE Department = 'IT'; -- Я в четвертом задании менял на Senior IT поэтому результат пустой (скрин не делал)


-- 4. Получаем данные из представления
SELECT *
FROM IT_Department_View;
