SELECT DISTINCT(model)
FROM pc
WHERE pc.speed>150
UNION
SELECT DISTINCT(model)
FROM laptop
WHERE laptop.speed>133;
