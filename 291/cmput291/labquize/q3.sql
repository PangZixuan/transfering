SELECT s.studentID, s.studentName,AVG(e.grade)
FROM students s, enroll e,courses c
WHERE s.studentID=e.studentID AND
e.courseID=c.courseID AND
c.credits>9 AND
GROUP BY s.studentID;
