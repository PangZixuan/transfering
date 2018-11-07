SELECT o.cid, ol.sid
FROM olines ol, orders o
WHERE ol.oid=o.oid
GROUP BY o.cid,ol.sid
HAVING COUNT(o.oid)>=0.5*(SELECT COUNT (c.oid)
			FROM orders c
			WHERE c.cid=o.cid);
