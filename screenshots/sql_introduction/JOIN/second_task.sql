SELECT s.status, c.first_name, c.last_name
FROM customers AS c
JOIN shippings AS s
	ON c.customer_id = s.customer;
