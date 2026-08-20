SELECT c.first_name, c.last_name, o.item, o.amount
FROM customers AS c
JOIN orders AS o
	ON c.customer_id = o.customer_id;
