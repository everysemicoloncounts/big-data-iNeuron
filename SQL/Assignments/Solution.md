1. 
```
SELECT * FROM city
WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;

```

2. 
``` 
SELECT NAME FROM city
WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;

```

3. 
``` 
SELECT * FROM city;

```

4. 

```
SELECT * FROM city
WHERE ID = 1661;

```

5. 
```
SELECT * FROM city
WHERE COUNTRYCODE = 'JPN';

```

6. 
```
SELECT NAME FROM city
WHERE COUNTRYCODE = 'JPN';

```
7. 
```
SELECT CITY, STATE FROM STATION;

```

8. 
```
SELECT DISTINCT(CITY)
FROM STATION
WHERE ID % 2 = 0
ORDER BY CITY;

```

9. 
```
SELECT COUNT(CITY) - COUNT(DISTINCT(CITY))
FROM STATION;

```

10. 
```
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY ASC
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) ASC, CITY ASC
LIMIT 1;

```

11. 
```
SELECT DISTINCT (city)
FROM station
WHERE city REGEXP "^[aeiou].*";

```

12. 
```
SELECT DISTINCT city
FROM station
WHERE city REGEXP "[aeiou]$";

```

13. 
```
SELECT DISTINCT (city)
FROM station
WHERE city NOT REGEXP "^[aeiou].*";

```

14. 
```
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP "[aeiou]$";

```

15. 
```
SELECT DISTINCT (city)
FROM station
WHERE city NOT REGEXP "^[aeiou].*" OR CITY NOT REGEXP "[aeiou]$";

```

16. 
```
SELECT DISTINCT (city)
FROM station
WHERE city NOT REGEXP "^[aeiou].*" AND CITY NOT REGEXP "[aeiou]$";

```

17. 
```
SELECT p.PRODUCT_ID, p.PRODUCT_NAME
FROM PRODUCT p
INNER JOIN SALES s
ON p.PRODUCT_ID = s.PRODUCT_ID
WHERE s.SALE_DATE BETWEEN '2019-01-01' AND '2019-03-31'
AND p.PRODUCT_ID NOT IN (
	SELECT p.PRODUCT_ID
	FROM PRODUCT p
	INNER JOIN SALES s
	ON p.PRODUCT_ID = s.PRODUCT_ID
	WHERE s.SALE_DATE BETWEEN '2019-04-01' AND '2019-12-31'
);

```

18. 
```
SELECT DISTINCT AUTHOR_ID AS ID
FROM views
WHERE AUTHOR_ID = VIEWER_ID;

```

19. 
```
SELECT (COUNT(DELIVERY_ID)*100/ (SELECT COUNT(*) FROM DELIVERY)) AS immediate_percentage
FROM DELIVERY
WHERE order_date = customer_pref_delivery_date;

```

20. 
```
SELECT DISTINCT
    ad_id,
    IFNULL(ROUND(SUM(action = 'Clicked') / (SUM(action = 'Clicked') + SUM(action = 'Viewed')) * 100,
                    2),
            0) AS ctr
FROM
    Ads
GROUP BY ad_id
ORDER BY ctr DESC , ad_id;

```

21. 
```
select employee_id, count(team_id) over ( partition by team_id) from employee order by employee_id;

```

22. 
```
SELECT 
    C.COUNTRY_NAME,
    CASE
        WHEN AVG(W.WEATHER_STATE) <= 15 THEN 'COLD'
        WHEN AVG(W.WEATHER_STATE) >= 25 THEN 'HOT'
        ELSE 'WARM'
    END AS WEATHER_TYPE
FROM
    WEATHER W
        INNER JOIN
    Countries C ON C.COUNTRY_ID = W.COUNTRY_ID
WHERE
    W.DATES BETWEEN '2019-11-01' AND '2019-11-30'
GROUP BY C.COUNTRY_ID;

```

23. 
```
SELECT 
    P.PRODUCT_ID,
    ROUND(SUM(U.UNITS * P.PRICE) / SUM(U.UNITS), 2) AS AVERAGE_PRICE
FROM
    PRICES P
        INNER JOIN
    UNITSSOLD U ON P.PRODUCT_ID = U.PRODUCT_ID
WHERE
    U.PURCHASE_DATE BETWEEN P.START_DATE AND P.END_DATE
GROUP BY 1;

```

24. 
```
select tmp.player_id, tmp.event_date as first_login from 
(select *, row_number() over (partition by player_id order by event_date) as row_num from activity) tmp where tmp.row_num = 1;

```

25. 
```
select tmp.player_id, tmp.device_id from
(select *, row_number() over (partition by player_id order by event_date) as row_num from activity) tmp where tmp.row_num = 1;

```

26. 
```


```