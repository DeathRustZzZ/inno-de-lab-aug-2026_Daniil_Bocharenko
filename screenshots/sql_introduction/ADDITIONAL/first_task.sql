SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE EXISTS (
    SELECT 1
    FROM shippings AS s
    WHERE s.customer = c.customer_id
      AND s.status = 'Delivered'
)
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country
HAVING COUNT(o.order_id) >= 2;
