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
SELECT 
    p.product_name, SUM(o.unit)
FROM
    orders o
        INNER JOIN
    products p ON p.product_id = o.product_id
WHERE
    order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100;

```

27. 
```
SELECT 
    *
FROM
    Users
WHERE
    REGEXP_LIKE(mail,
            '^[a-zA-Z][a-zA-Z0-9\_.-]*@leetcode.com');

```
28. 
```
SELECT 
    o.customer_id, c.name
FROM
    orders o
        INNER JOIN
    product p ON p.product_id = o.product_id
        INNER JOIN
    Customers c ON c.customer_id = o.customer_id
WHERE
    o.order_date BETWEEN '2020-07-01' AND '2020-07-31'
GROUP BY o.customer_id
    AND o.customer_id IN (SELECT 
        o.customer_id
    FROM
        orders o
            INNER JOIN
        product p ON p.product_id = o.product_id
            INNER JOIN
        Customers c ON c.customer_id = o.customer_id
    WHERE
        o.order_date BETWEEN '2020-06-01' AND '2020-06-30'
    GROUP BY o.customer_id);

```
29. 
```
SELECT 
    c.title
FROM
    content c
        INNER JOIN
    TVProgram t ON t.content_id = c.content_id
WHERE
    c.kids_content = 'Y'
        AND t.program_date BETWEEN '2020-06-01 00:00' AND '2020-06-30 23:59';

```
30. 
```
SELECT 
    q.*, IFNULL(n.npv, 0)
FROM
    queries q
        LEFT JOIN
    npv n ON q.id = n.id AND q.year = n.year;

```

31. 
```
SELECT 
    q.*, IFNULL(n.npv, 0)
FROM
    queries q
        LEFT JOIN
    npv n ON q.id = n.id AND q.year = n.year;

```

32. 
```
SELECT 
    u.unique_id, e.name
FROM
    employees e
        LEFT JOIN
    employeeUNI u ON e.id = u.id;

```

33. 
```
SELECT 
    u.name, IFNULL(SUM(r.distance), 0)
FROM
    rides r
        RIGHT JOIN
    users u ON u.id = r.user_id
GROUP BY u.id
ORDER BY SUM(r.distance) DESC , u.name;

```

34. 

```
SELECT 
    a.product_name, SUM(unit) AS unit
FROM
    Products a
        LEFT JOIN
    Orders b ON a.product_id = b.product_id
WHERE
    b.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY a.product_id
HAVING SUM(unit) >= 100

```

35. 
```
SELECT 
    user_name AS results
FROM
    (SELECT 
        a.name AS user_name, COUNT(*) AS counts
    FROM
        Rating AS b
    JOIN Users AS a ON a.user_id = b.user_id
    GROUP BY b.user_id
    ORDER BY counts DESC , user_name ASC
    LIMIT 1) first_query 
UNION SELECT 
    movie_name AS results
FROM
    (SELECT 
        c.title AS movie_name, AVG(d.rating) AS rate
    FROM
        Rating AS d
    JOIN Movies AS c ON c.movie_id = d.movie_id
    WHERE
        SUBSTR(d.created_at, 1, 7) = '2020-02'
    GROUP BY d.movie_id
    ORDER BY rate DESC , movie_name ASC
    LIMIT 1) second_query;

```

36. 
```
SELECT 
    name, SUM(IFNULL(distance, 0)) AS travelled_distance
FROM
    rides r
        RIGHT JOIN
    users u ON r.user_id = u.id
GROUP BY name
ORDER BY 2 DESC , 1 ASC;

```

37. 
```
SELECT 
    u.unique_id, e.name
FROM
    employees e
        LEFT JOIN
    employeeUNI u ON e.id = u.id;

```

38. 
```
SELECT 
    id, name
FROM
    students
WHERE
    department_id NOT IN (SELECT 
            id
        FROM
            departments);

```

39. 
```


```

40. 
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

41. 
```
SELECT 
    w.name,
    SUM(p.width * p.length * p.height * w.units) AS total_volume
FROM
    products p
        INNER JOIN
    warehouse w ON p.product_id = w.product_id
GROUP BY w.name;

```

42. 
```


```