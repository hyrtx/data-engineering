-- 1. Cria um relatório para todos os pedidos de 1996 e seus clientes (152 linhas)
SELECT 
	o.order_date,
	o.order_id,
	c.company_name,
	c.city,
	c.country,
	o.freight
FROM orders AS o
INNER JOIN customers AS c
	ON o.customer_id = c.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 1996
ORDER BY o.order_id;

-- 2. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
SELECT
	e.city,
	COUNT(DISTINCT e.employee_id) AS n_employees,
	COUNT(DISTINCT c.customer_id) AS n_clients
FROM employees AS e
LEFT JOIN customers AS c
	ON e.city = c.city
GROUP BY e.city
ORDER BY e.city;

-- 3. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
SELECT
	c.city,
	COUNT(DISTINCT c.customer_id) AS n_clients,
	COUNT(DISTINCT e.employee_id) AS n_employees
FROM customers AS c
LEFT JOIN employees AS e
	ON c.city = e.city
GROUP BY c.city
ORDER BY 
	n_clients DESC,
	n_employees DESC,
	c.city;

-- 4.Cria um relatório que mostra o número de funcionários e clientes de cada cidade (71 linhas)
SELECT
	COALESCE(c.city, e.city) AS city,
	COUNT(DISTINCT c.customer_id) AS n_clients,
	COUNT(DISTINCT e.employee_id) AS n_employees
FROM customers AS c
FULL JOIN employees AS e
	ON c.city = e.city
GROUP BY c.city, e.city
ORDER BY 
	n_clients DESC,
	n_employees DESC,
	city;

-- 5. Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)
SELECT
	o.product_id,
	p.product_name,
	SUM(o.quantity) AS quantity
FROM order_details AS o
INNER JOIN products AS p
	ON o.product_id = p.product_id
GROUP BY
	o.product_id,
	p.product_name
HAVING SUM(o.quantity) < 200
ORDER BY quantity DESC;

-- 6. Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
-- O relatório deve retornar apenas linhas para as quais o total de pedidos é maior que 15 (5 linhas)
SELECT
	o.customer_id,
	c.company_name,
	COUNT(o.order_id) AS n_orders
FROM orders AS o
INNER JOIN customers AS c
	ON o.customer_id = c.customer_id
WHERE o.order_date > '31/12/1996'
GROUP BY 
	o.customer_id,
	c.company_name
HAVING COUNT(o.order_id) > 15
ORDER BY n_orders DESC