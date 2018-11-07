SELECT DISTINCT o.oid
FROM olines o,olines j, products p1, products p2
WHERE o.oid=j.oid AND
o.sid<>j.sid AND
o.pid=p1.pid AND
j.pid=p2.pid AND
p1.cat='dai' AND
p2.cat=p1.cat;


