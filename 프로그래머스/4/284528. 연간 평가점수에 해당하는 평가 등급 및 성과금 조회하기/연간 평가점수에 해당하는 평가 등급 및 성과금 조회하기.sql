-- 코드를 작성해주세요

select e.EMP_NO, e.EMP_NAME, (case 
                              when avg(g.score) >= 96 then 'S'
                              when avg(g.score) >= 90 then 'A'
                              when avg(g.score) >= 80 then 'B'
                              else 'C'
                              end
                             ) as GRADE, 
                             (case 
                              when avg(g.score) >= 96 then 0.2 * e.sal
                              when avg(g.score) >= 90 then 0.15 * e.sal
                              when avg(g.score) >= 80 then 0.1 * e.sal
                              else 0
                              end
                             ) as BONUS
from hr_employees e
join hr_grade g on e.emp_no = g.emp_no
group by e.emp_no
order by e.emp_no asc