# Write your MySQL query statement below
WITH DailySummary AS (
    SELECT 
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
MovingMetrics AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER(
            ORDER BY visited_on 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(AVG(daily_amount) OVER(
            ORDER BY visited_on 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ), 2) AS average_amount
    FROM DailySummary
)
SELECT visited_on, amount, average_amount
FROM MovingMetrics
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + INTERVAL 6 DAY
ORDER BY visited_on ASC;