SELECT DISTINCT o.cid
FROM olines ol, orders o
WHERE o.oid=ol.oid AND
	datetime('now','-7 day')<=o.odate AND
d.uprice<=(SELECT g.uprice 
FROM goodprice g WHERE d.pid=g.pid);
