SELECT p.pid, p.name, COUNT(DISTINCT ol.sid)
FROM products p, olines ol
WHERE p.pid=ol.pid
GROUP BY p.pid,p.name
ORDER BY COUNT(ol.oid) DESC
LIMIT 5;
