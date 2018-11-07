SELECT s.studentID, s.studentName
FROM students s,professors p,enroll e,courses c
WHERE s.program='Computing Science' AND
s.studentID=e.studentID AND
e. term='Fall 2016' AND
e.courseID =c.courseID AND
c.professorID=p.professorID AND
p.department != 'Computing Science'
order by s.studentID ;
