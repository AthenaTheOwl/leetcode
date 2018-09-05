CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
SELECT Salary as 'getNthHighestSalary(2)' FROM Employee as a
      where N-1=(SELECT COUNT(DISTINCT salary) FROM Employee as b WHERE b.salary > a.salary) limit 1
  );
END