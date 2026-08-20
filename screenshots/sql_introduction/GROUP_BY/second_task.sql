SELECT
    item,
    COUNT(*),
    -- Решил попробовать округлить, но 416,66 не получилось
    ROUND(AVG(amount), 2) AS avg_amount
FROM orders
GROUP BY item;
