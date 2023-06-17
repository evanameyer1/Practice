-- revising the select query i --

SELECT *
    FROM city
    WHERE population > 100000 AND 
    countrycode = 'USA';

-- revising the select query ii --

select name
    from city
    where population > 120000 and
    countrycode = 'USA';

-- select by id --

select *
    from city
    where id = 1661;

-- japanese cities' attributes -- 

select *
    from city
    where countrycode = 'JPN';

-- japanese cities' names --

select name
    from city
    where countrycode = 'JPN';

-- weather observation station 1 --

select city, state
    from station

-- weather observation station 3 --

select distinct city
    from station
    where id like '%2' OR id like '%4' OR id like '%6' OR id like '%8' OR id like '%0';

-- weather observation 4 --

select 
    count(city) - count(distinct(city))
    from station;

-- weather observation 5 --

select city, length(city) 
    from station 
    order by length(city) asc, city asc 
    limit 1; 

select city, length(city) 
    from station 
    order by length(city) desc 
    limit 1;

-- weather observation 6 --

select distinct city
    from station
    where city like 'a%' OR city like 'e%' OR city like 'i%' OR city like 'o%' OR city like 'u%'; 

-- weather observation 7 --

select distinct city
    from station
    where city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';

-- weather observation 8 --

select distinct city
    from station
    where (city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u') 
        and (city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%')

-- weather observation 9 --

select distinct city
    from station
    where not (city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%');

-- weather observation 10 --

select distinct city
    from station
    where not (city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u');

-- weather observation 11 --

select distinct city
    from station
    where (not (city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u')) 
    OR (not (city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%'));

-- weather observation 12 --

select distinct city
    from station
    where (not (city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u')) 
    AND (not (city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%'));

-- higher than 75 marks --

select name
    from students
    where marks > 75
    order by right(name, 3), ID asc;

-- employee names --

select name
    from employee
    order by name asc;

-- employee salaries --

select name
    from employee
    where salary > 2000 
        AND months < 10
    order by employee_id ASC;

-- type of triangle -- 

SELECT 
CASE 
   
    WHEN A+B<=C OR B+C<=A OR C+A<=B THEN 'Not A Triangle'
    WHEN A=B AND B=C THEN 'Equilateral' 
    WHEN A!=B AND B!=C AND C!=A THEN 'Scalene'
    ELSE 'Isosceles'
END
FROM TRIANGLES;

-- top earners --

select
    salary * months,
    count(salary)
    from employee
    group by 1
    order by 1 desc
    limit 1