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
SELECT 
    from_id AS person1,
    to_id AS person2,
    COUNT(duration) AS call_count,
    SUM(duration) AS total_duration
FROM
    (SELECT 
        *
    FROM
        Calls UNION ALL SELECT 
        to_id, from_id, duration
    FROM
        Calls) t1
WHERE
    from_id < to_id
GROUP BY person1 , person2;

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
SELECT 
    a.sale_date, a.sold_num - b.sold_num
FROM
    Sales a
        LEFT JOIN
    Sales b ON a.sale_date = b.sale_date
WHERE
    a.fruit = 'apples'
        AND b.fruit = 'oranges';

```

43. 
```
WITH cte AS (
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
)

SELECT ROUND(SUM(CASE WHEN DATEDIFF(event_date, first_login)=1 THEN 1 ELSE 0  END) / COUNT(DISTINCT cte.player_id), 2) as fraction
FROM Activity as a
JOIN cte 
ON a.player_id = cte.player_id;

```

44. 
```
SELECT 
    Name
FROM
    Employee AS t1
        JOIN
    (SELECT 
        ManagerId
    FROM
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS t2 ON t1.Id = t2.ManagerId;

```

45. 
```
SELECT 
    dept_name, COUNT(student_id) AS student_number
FROM
    department
        LEFT OUTER JOIN
    student ON department.dept_id = student.dept_id
GROUP BY department.dept_name
ORDER BY student_number DESC , department.dept_name;

```

46. 
```
SELECT 
    customer_id
FROM
    customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT 
        COUNT(*)
    FROM
        product);

```

47. 
```
SELECT 
    project_id, employee_id
FROM
    Project
        JOIN
    Employee USING (employee_id)
WHERE
    (project_id , experience_years) IN (SELECT 
            project_id, MAX(experience_years)
        FROM
            Project
                JOIN
            Employee USING (employee_id)
        GROUP BY project_id);

```

48. 
```
SELECT 
    book_id, name
FROM
    books
WHERE
    book_id NOT IN (SELECT 
            book_id
        FROM
            orders
        WHERE
            (dispatch_date BETWEEN DATE_SUB('2019-06-23', INTERVAL 1 YEAR) AND '2019-06-23')
        GROUP BY (book_id)
        HAVING SUM(quantity) >= 10)
        AND available_from < DATE_SUB('2019-06-23', INTERVAL 1 MONTH);

```

49. 
```
SELECT 
    e1.student_id, MIN(e1.course_id) AS course_id, e1.grade
FROM
    Enrollments e1
WHERE
    e1.grade = (SELECT 
            MAX(grade) AS max_grade
        FROM
            Enrollments e2
        WHERE
            e1.student_id = e2.student_id)
GROUP BY e1.student_id
ORDER BY e1.student_id;

```

50. 
```
SELECT 
    group_id, player_id
FROM
    (SELECT 
        p.group_id, ps.player_id, SUM(ps.score) AS score
    FROM
        players p
    INNER JOIN (SELECT 
        first_player AS player_id, first_score AS score
    FROM
        matches UNION ALL SELECT 
        second_player AS player_id, second_score AS score
    FROM
        matches) ps ON p.player_id = ps.player_id
    GROUP BY ps.player_id
    ORDER BY group_id , score DESC , player_id) top_scores
GROUP BY group_id;

```

51. 
```
SELECT 
    name, population, area
FROM
    world
WHERE
    area >= 3000000 
UNION SELECT 
    name, population, area
FROM
    world
WHERE
    population >= 25000000;

```

52. 
```
SELECT 
    name
FROM
    customer
WHERE
    referee_id <> 2 OR referee_id IS NULL;

```

53. 
```
SELECT 
    customers.name AS 'Customers'
FROM
    customers
WHERE
    customers.id NOT IN (SELECT 
            customerid
        FROM
            orders);

```

54. 
```
SELECT 
    e1.employee_id, COUNT(*) AS team_size
FROM
    Employee e1
        LEFT JOIN
    Employee e2 ON e1.team_id = e2.team_id
GROUP BY e1.employee_id;

```

55. 
```
SELECT 
    c.name AS country
FROM
    Person p
        INNER JOIN
    Country c ON LEFT(p.phone_number, 3) = c.country_code
        INNER JOIN
    (SELECT 
        caller_id AS id, duration
    FROM
        Calls UNION ALL SELECT 
        callee_id AS id, duration
    FROM
        Calls) phn ON p.id = phn.id
GROUP BY country
HAVING AVG(duration) > (SELECT 
        AVG(duration)
    FROM
        Calls);

```

56. 
```
SELECT 
    a.player_id, MIN(a.event_date) AS first_login
FROM
    Activity a
GROUP BY a.player_id;

```

57. 
```
SELECT 
    customer_number
FROM
    orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

```

58. 
```
SELECT
    DISTINCT t1.seat_id
FROM cinema AS t1 JOIN cinema AS t2
ON abs(t1.seat_id - t2.seat_id) = 1
AND t1.free = 1 AND t2.free = 1
ORDER BY 1;

```

59. 
```
SELECT 
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (SELECT 
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED');

```

60. 
```
SELECT 
    x,
    y,
    z,
    IF(x + y > z AND y + z > x AND z + x > y,
        'Yes',
        'No') triangle
FROM
    triangle;

```

61. 
```
SELECT 
    MIN(ABS(p2.x - p1.x)) AS shortest
FROM
    point p1,
    point p2
WHERE
    p1.x != p2.x;

```

62. 
```
SELECT 
    actor_id, director_id
FROM
    ActorDirector
GROUP BY actor_id , director_id
HAVING COUNT(*) >= 3;

```

63. 
```
SELECT 
    p.product_name, s.year, s.price
FROM
    Sales s
        LEFT JOIN
    Product p ON s.product_id = p.product_id;

```

64. 
```
SELECT 
    p.project_id,
    ROUND(SUM(e.experience_years) / COUNT(p.project_id),
            2) AS average_years
FROM
    Project p
        LEFT JOIN
    Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;

```

65. 
```
SELECT DISTINCT
    seller_id
FROM
    Sales
GROUP BY seller_id
HAVING SUM(price) = (SELECT 
        SUM(price) AS max_price
    FROM
        Sales
    GROUP BY seller_id
    ORDER BY max_price DESC
    LIMIT 1);

```

66. 
```
SELECT DISTINCT
    s.buyer_id
FROM
    Product p
        JOIN
    Sales s ON p.product_id = s.product_id
GROUP BY buyer_id
HAVING SUM(p.product_name = 'S8') > 0
    AND SUM(p.product_name = 'iPhone') = 0;

```

67. 
```
SELECT 
    c1.visited_on,
    SUM(c2.amount) AS amount,
    ROUND(AVG(c2.amount), 2) AS average_amount
FROM
    (SELECT 
        visited_on, SUM(amount) AS amount
    FROM
        customer
    GROUP BY visited_on) c1
        JOIN
    (SELECT 
        visited_on, SUM(amount) AS amount
    FROM
        customer
    GROUP BY visited_on) c2 ON DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
GROUP BY c1.visited_on
HAVING COUNT(c2.amount) = 7;

```

68. 
```
SELECT
    gender,
    day,
    SUM(score_points) OVER(PARTITION BY gender ORDER BY day) as total
FROM Scores;

```

69. 
```
select min(log_id) as start_id, max(log_id) as end_id
from (select l.log_id, (l.log_id - l.row_num) as diff
      from (select log_id, row_number() over() as row_num from Logs) l
      ) l2
group by diff;

```

70. 
```
SELECT 
    t.student_id,
    t.student_name,
    t.subject_name,
    IF(e.attended_exams IS NULL,
        0,
        e.attended_exams) AS attended_exams
FROM
    (SELECT 
        *
    FROM
        Students
    CROSS JOIN Subjects) t
        LEFT JOIN
    (SELECT 
        *, COUNT(*) AS attended_exams
    FROM
        Examinations
    GROUP BY student_id , subject_name) e ON t.student_id = e.student_id
        AND t.subject_name = e.subject_name
ORDER BY student_id , subject_name;

```

71. 
```
SELECT 
    a.employee_id AS EMPLOYEE_ID
FROM
    Employees AS a
        LEFT JOIN
    Employees AS b ON a.manager_id = b.employee_id
        LEFT JOIN
    Employees AS c ON b.manager_id = c.employee_id
        LEFT JOIN
    Employees AS d ON c.manager_id = d.employee_id
WHERE
    a.employee_id != 1 AND d.employee_id = 1;

```

72. 
```
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(id) AS trans_count,
    SUM(CASE
        WHEN state = 'approved' THEN 1
        ELSE 0
    END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE
        WHEN state = 'approved' THEN amount
        ELSE 0
    END) AS approved_total_amount
FROM
    transactions
GROUP BY month , country;

```

73. 
```
SELECT 
    ROUND(AVG(daily_count), 2) AS average_daily_percent
FROM
    (SELECT 
        COUNT(DISTINCT b.post_id) / COUNT(DISTINCT a.post_id) * 100 AS daily_count
    FROM
        actions a
    LEFT JOIN removals b ON a.post_id = b.post_id
    WHERE
        extra = 'spam'
    GROUP BY action_date) b;

```

74. 
```
WITH cte AS (
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
)

SELECT ROUND(SUM(CASE WHEN DATEDIFF(event_date, first_login)=1 THEN 1 ELSE 0  END) / COUNT(DISTINCT cte.player_id), 2) as fraction
FROM Activity as a
JOIN cte 
ON a.player_id = cte.player_id;

```

75. 
```
WITH cte AS (
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
)

SELECT ROUND(SUM(CASE WHEN DATEDIFF(event_date, first_login)=1 THEN 1 ELSE 0  END) / COUNT(DISTINCT cte.player_id), 2) as fraction
FROM Activity as a
JOIN cte 
ON a.player_id = cte.player_id;

```

76. 
```
SELECT 
    s.company_id,
    s.employee_id,
    s.employee_name,
    ROUND((CASE
                WHEN tmp.max_salary < 1000 THEN salary
                WHEN tmp.max_salary BETWEEN 1000 AND 10000 THEN salary * 0.76
                ELSE salary * 0.51
            END),
            0) AS salary
FROM
    Salaries s
        JOIN
    (SELECT 
        m.company_id, MAX(m.salary) AS max_salary
    FROM
        salaries m
    GROUP BY m.company_id) tmp ON s.company_id = tmp.company_id;

```

77. 
```
SELECT 
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '<' THEN IF(l.value < r.value, 'true', 'false')
        WHEN e.operator = '>' THEN IF(l.value > r.value, 'true', 'false')
        ELSE IF(l.value = r.value, 'true', 'false')
    END AS value
FROM
    expressions e
        LEFT JOIN
    variables l ON e.left_operand = l.name
        LEFT JOIN
    variables r ON e.right_operand = r.name;

```

78. 
```
SELECT 
    c.name AS country
FROM
    Person p
        INNER JOIN
    Country c ON LEFT(p.phone_number, 3) = c.country_code
        INNER JOIN
    (SELECT 
        caller_id AS id, duration
    FROM
        Calls UNION ALL SELECT 
        callee_id AS id, duration
    FROM
        Calls) phn ON p.id = phn.id
GROUP BY country
HAVING AVG(duration) > (SELECT 
        AVG(duration)
    FROM
        Calls);

```
79. 
```
SELECT name FROM Employee ORDER BY name;

```

80. 
```


```