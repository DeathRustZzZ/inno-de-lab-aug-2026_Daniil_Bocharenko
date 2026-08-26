-- 1. Сколько автомобилей находится в активном владении?
SELECT
    SUM(is_current) AS active_ownerships
FROM fact_vehicle_ownership;


-- 2. Количество новых владений по годам
SELECT
    d.year,
    SUM(f.ownership_count) AS total_ownerships
FROM fact_vehicle_ownership AS f
JOIN dim_date AS d
    ON f.start_date_key = d.date_key
GROUP BY d.year
ORDER BY d.year;

-- 3. Средняя продолжительность завершённого владения
SELECT
    ROUND(AVG(duration_days), 2) AS avg_duration_days
FROM fact_vehicle_ownership
WHERE is_current = 0;

-- 4. Количество владений по маркам автомобилей
SELECT
    v.brand,
    SUM(f.ownership_count) AS total_ownerships
FROM fact_vehicle_ownership AS f
JOIN dim_vehicle AS v
    ON f.vehicle_key = v.vehicle_key
GROUP BY v.brand
ORDER BY total_ownerships DESC;

-- 5. Распределение владений по типам автомобилей
SELECT
    ownership_type,
    SUM(ownership_count) AS total_ownerships
FROM fact_vehicle_ownership
GROUP BY ownership_type
ORDER BY total_ownerships DESC;
