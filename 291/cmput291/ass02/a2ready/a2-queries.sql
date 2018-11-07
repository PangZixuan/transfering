.echo on
--Question 1
SELECT DISTINCT cid
FROM customers
EXCEPT
SELECT o.cid
FROM orders o,olines ol,products p
WHERE o.oid=ol.oid AND
ol.pid=p.pid AND
p.cat='dai';


--Question 2
SELECT DISTINCT o1.oid
FROM olines o1,olines o2,products p1, products p2
WHERE o1.oid=o2.oid AND
o1.pid=p1.pid AND
o2.pid=p2.pid AND
p1.cat='dai' AND
p2.cat=p1.cat AND
o1.sid<>o2.sid;




--Question 3
SELECT DISTINCT trackingNo
FROM deliveries d, orders o, customers c
WHERE
c.name='John Doe' AND
c.cid=o.cid AND
o.oid=d.oid AND(
d.pickUpTime>=datetime('now','-1 day')OR
d.pickUpTime>=datetime('now','-24 hours'))AND
d.dropOffTime is null;



--Question 4
SELECT COUNT(*),c1.sid
FROM carries c1
WHERE NOT EXISTS (SELECT c2.sid
FROM carries c2
WHERE c1.pid=c2.pid AND
c1.sid<>c2.sid)
GROUP BY c1.sid;


--Question 5
SELECT o.cid, ol.sid
FROM olines ol, orders o
WHERE ol.oid=o.oid
GROUP BY o.cid,ol.sid
HAVING COUNT(o.oid)>=0.5*(SELECT COUNT (c.oid)
			FROM orders c
			WHERE c.cid=o.cid);


--Question 6
SELECT c.cat,ifnull(COUNT(DISTINCT p.pid),0),ifnull(COUNT(DISTINCT car.sid),0),ifnull(COUNT(DISTINCT o.oid),0)
FROM categories c LEFT OUTER JOIN products p ON (c.cat=p.cat)
		LEFT OUTER JOIN carries car  ON (p.pid=car.pid)
		LEFT OUTER JOIN olines o ON (p.pid=o.pid)
GROUP BY c.cat;



--Question 7
SELECT p.pid, p.name, COUNT(DISTINCT ol.sid)
FROM products p, olines ol
WHERE p.pid=ol.pid
GROUP BY p.pid,p.name
ORDER BY COUNT(ol.oid) DESC
LIMIT 5;




--Question 8 
SELECT o.cid
FROM orders o, olines ol, stores s
WHERE o.oid=ol.oid AND
ol.sid=s.sid
GROUP BY o.cid
HAVING COUNT(DISTINCT ol.sid)=1 and (s.name<>'Walmart'); 


--Question 9
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



--Question 10
SELECT DISTINCT o.cid
FROM orders o, olines ol,goodprices gp
WHERE o.oid=ol.oid AND
o.odate<=datetime('now','-7 day') AND
ol.pid=gp.pid AND
ol.uprice<=gp.uprice;

