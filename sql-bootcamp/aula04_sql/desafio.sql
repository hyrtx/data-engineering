-- Faça a classificação dos produtos mais vendidos usando usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- Essa questão tem 2 implementações, veja uma que utiliza subquery e uma que não utiliza.
WITH cte AS (
	SELECT 
		o.product_id,
		p.product_name,
		ROUND(SUM((o.unit_price * o.quantity)):: NUMERIC, 1) AS total_sales
	FROM order_details AS o
	INNER JOIN products AS p
		USING(product_id)
	GROUP BY
		o.product_id,
		p.product_name
	ORDER BY total_sales DESC
)

SELECT 
	product_id,
	product_name,
	total_sales,
	RANK() OVER (ORDER BY total_sales DESC) AS r_sales_rank,
	DENSE_RANK() OVER (ORDER BY total_sales DESC) AS dr_sales_rank,
	ROW_NUMBER() OVER (ORDER BY total_sales DESC) AS rn_sales_rank
FROM cte;

-- Listar funcionários dividindo-os em 3 grupos usando NTILE
-- FROM employees;

SELECT 
	last_name || ' ' || first_name AS employee,
	NTILE(3) OVER (ORDER BY employee_id ASC) AS group
FROM employees;

-- Ordenando os custos de envio pagos pelos clientes de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
-- FROM orders JOIN shippers ON shippers.shipper_id = orders.ship_via;

SELECT
	o.order_date,
	c.company_name,
	o.freight,
	LAG(o.freight) OVER (PARTITION BY c.company_name ORDER BY o.order_date ASC) AS previous_freight,
	LEAD(o.freight) OVER (PARTITION BY c.company_name ORDER BY o.order_date ASC) AS previous_freight
FROM orders AS o
LEFT JOIN customers AS c
	USING(customer_id)