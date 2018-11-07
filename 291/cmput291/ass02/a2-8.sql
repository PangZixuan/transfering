SELECT o.cid
FROM orders o, olines ol, stores s
WHERE o.oid=ol.oid AND
ol.sid=s.sid
GROUP BY o.cid
HAVING COUNT(DISTINCT ol.sid)=1 and (s.name<>'Walmart'); 
