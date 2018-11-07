SELECT COUNT(*),c1.sid
FROM carries c1
WHERE NOT EXISTS (SELECT c2.sid
FROM carries c2
WHERE c1.pid=c2.pid AND
c1.sid<>c2.sid)
GROUP BY c1.sid;
