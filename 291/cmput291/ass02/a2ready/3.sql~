.print Question 3 -zpang
SELECT DISTINCT trackingNo
FROM deliveries d, orders o, customers c
WHERE
c.name='John Doe' AND
c.cid=o.cid AND
o.oid=d.oid AND(
d.pickUpTime>=datetime('now','-1 day')OR
d.pickUpTime>=datetime('now','-24 hours'))AND
d.dropOffTime is null;
