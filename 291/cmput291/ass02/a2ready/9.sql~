.print Question 9 -zpang
DROP view goodprices;
CREATE VIEW goodprices
AS SELECT s.name, c.pid, c.sid, c.qty, c.uprice
FROM carries c, stores s
WHERE c.qty>0 AND
s.sid=c.sid AND
c.uprice=(SELECT MIN(comp.uprice)
FROM carries comp
GROUP BY comp.pid
HAVING comp.pid=c.pid);
SELECT *
FROM goodprices;
