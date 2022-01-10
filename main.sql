WITH temp AS (
    SELECT * FROM event
    WHERE event_name in ('launch', 'purchase')
)

SELECT
	CAST(event_time AS DATE),
	COUNT(*),
	SUM(event_value) / COUNT(*) AS ARPDAU
FROM temp
GROUP BY CAST(event_time AS DATE)
ORDER BY CAST(event_time AS DATE)