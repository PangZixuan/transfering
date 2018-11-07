SELECT e.studentID,s.studentName,AVG(e.grade),SUM(c.credits)
FROM enroll e,students s,courses c 
WHERE e.studentID=s.studentID AND
e.courseID=c.courseID
GROUP BY e.studentID
HAVING AVG(e.grade)>3 AND
SUM(c.credits)>9;
