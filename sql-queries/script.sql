CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    order_date DATE
);

INSERT INTO orders (customer, amount, order_date) VALUES
('Alice', 5000, '2025-03-01'),
('Bob', 8000, '2024-03-05'),
('Alice', 3000, '2024-03-15'),
('Charlie', 7000, '2024-02-20'),
('Alice', 10000, '2024-02-28'),
('Bob', 4000, '2024-02-10'),
('Charlie', 9000, '2024-03-22'),
('Alice', 2000, '2024-03-30'),
('Alice', 2000, '2025-05-12'),
('Alice', 3400, '2024-02-18'),
('Max', 1500, '2024-01-10');

-- Task 1: Calculate the total sales volume for March 2024
SELECT SUM(amount) AS volume_march
FROM orders
WHERE order_date BETWEEN '2024-03-01' AND '2024-03-31';

-- Task 2: Find the customer who spent the most overall (i.e., the highest total amount across all orders)
SELECT 
    customer,
    SUM(amount) AS total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;

-- Task 3: Calculate the average order value for the last three months relative to the current date
SELECT ROUND(AVG(amount), 2) AS orders_avg
FROM orders
WHERE DATE(order_date) BETWEEN DATE('now', '-3 months') AND DATE('now');