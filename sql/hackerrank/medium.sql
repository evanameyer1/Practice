-- the pads --

select 
    concat(name, '(', left(occupation, 1), ')') as name
    from occupations
    order by name asc;
    
select 
    concat('There are a total of', ' ', sub.count, ' ', lower(sub.occupation), 's.')
    from (
        select
        occupation, count(occupation) as "count"
        from occupations
        group by occupation
        order by count asc, occupation asc
        ) sub;

-- occupations -- 

select 
    min(doctor), 
    min(professor), 
    min(singer), 
    min(actor) 
    from (
    select 
    case when occupation = 'doctor' then name end as doctor,
    case when occupation = 'professor' then name end as professor,
    case when occupation = 'singer' then name end as singer, 
    case when occupation = 'actor' then name end as actor, 
    row_number() over (partition by occupation order by name) as ran 
    from occupations
    ) sub
    group by sub.ran;

-- new companies --

select 
    c.company_code, 
    c.founder, 
    count(distinct(lm.lead_manager_code)), 
    count(distinct(sm.senior_manager_code)), 
    count(distinct(m.manager_code)), 
    count(distinct(e.employee_code)) 
    from company c
    join lead_manager lm
        using(company_code)
    join senior_manager sm
        using(company_code)
    join manager m
        using(company_code)
    join employee e
        using(company_code)
    group by c.company_code, c.founder
    order by company_code asc;

-- weather observation station 20 -- 

with t1 as (
select 
    count(sub.rn) as count
    from(
        select 
            lat_n as latitude,
            row_number() over (order by lat_n) as rn
            from station
            order by 1
    ) sub
),

t2 as(
    select 
        lat_n as latitude,
        row_number() over (order by lat_n) as rn
        from station
        order by 1
)

select
    round(t2.latitude, 4)
    from t1, t2
    where rn = t1.count / 2

-- top competitors -- 

SELECT hack.hacker_id as hacker_idf, 
    hack.name as hacker_name
    
    FROM hackers as hack   
    JOIN submissions as s 
        on hack.hacker_id = s.hacker_id
    JOIN challenges as c 
        on s.challenge_id = c.challenge_id
    JOIN difficulty as d 
        on d.difficulty_level = c.difficulty_level
    WHERE s.score = d.score   
    GROUP BY hacker_idf, hacker_name
    HAVING count(hack.name) > 1
    ORDER BY count(hack.hacker_id) DESC, hacker_idf ASC 