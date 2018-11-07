SELECT c.cat,ifnull(COUNT(DISTINCT p.pid),0),ifnull(COUNT(DISTINCT car.sid),0),ifnull(COUNT(DISTINCT o.oid),0)
FROM categories c LEFT OUTER JOIN products p ON (c.cat=p.cat)
		LEFT OUTER JOIN carries car  ON (p.pid=car.pid)
		LEFT OUTER JOIN olines o ON (p.pid=o.pid)
GROUP BY c.cat;
