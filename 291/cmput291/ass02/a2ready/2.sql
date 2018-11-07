.print Question 2 -zpang
SELECT DISTINCT o1.oid
FROM olines o1,olines o2,products p1, products p2
WHERE o1.oid=o2.oid AND
o1.pid=p1.pid AND
o2.pid=p2.pid AND
p1.cat='dai' AND
p2.cat=p1.cat AND
o1.sid<>o2.sid;


