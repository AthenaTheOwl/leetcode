# Write your MySQL query statement below
select distinct a.email from person as a, person as b where a.email=b.email and a.id<>b.id