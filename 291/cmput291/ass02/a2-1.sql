SELECT DISTINCT cid
FROM customers
EXCEPT
SELECT o.cid
FROM orders o,olines ol,products p
WHERE o.oid=ol.oid AND
ol.pid=p.pid AND
p.cat='dai';
