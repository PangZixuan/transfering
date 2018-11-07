SELECT professorName
FROM professors p, courses c
WHERE c.professorID=p.professorID AND
c.seatsAvailable > 150;
