.print Question 10 -zpang
SELECT DISTINCT o.cid
FROM orders o, olines ol,goodprices gp
WHERE o.oid=ol.oid AND
o.odate<=datetime('now','-7 day') AND
ol.pid=gp.pid AND
ol.uprice<=gp.uprice;
