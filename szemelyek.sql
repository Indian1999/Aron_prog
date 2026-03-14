/*select * from személyek
-- 1. feladat: Listázzuk ki azokat az embereket akik 2000 után születtek
/*
SELECT * FROM személyek
WHERE szuletesi_ev > 2000;

-- 2. feladat: Listázzuk azon személyek nevét és email címét akik citromail.hu email címmel rendelkeznek

SELECT vezeteknev, keresztnev, email FROM személyek 
WHERE email like "%@citromail.hu%";


-- 3. feladat: Hány olyan ember van aki Nyíregyházi és 1990 előtt született?

SELECT count(id) FROM személyek
WHERE varos = "Nyíregyháza" and szuletesi_ev < 1990

-- 4. feladat: Mekkora az átlagos életkora azoknak a férfiaknak akik citromail-es email címmel rendelkeznek?
SELECT year(now()) - avg(szuletesi_ev) FROM személyek
WHERE email like "%@citromail.hu" and nem = "férfi"



-- 5. feladat: Csoportosítsuk az adatokat foglalkozás szerint, minden foglalkozáshoz jelenítsük meg az átlagos keresetet!

SELECT foglalkozas, avg(fizetes_huf) FROM személyek
GROUP BY foglalkozas

-- 6. Hány olyan ember van akinek a telefonszámában szerepel 666
SELECT count(id) FROM személyek
WHERE telefonszam like "%6%"

-- 7. feladat: Hány olyan ember van aki 2004-ben született, férfi és miskolci


SELECT count(id) FROM személyek
WHERE szuletesi_ev = 2004 and nem = "ferfi" and varos = "Miskolc"


-- 8. feladat: Írd ki hogy városonként mekkora az átlagos fizetés!
SELECT varos, avg(fizetes_huf) FROM személyek
GROUP BY varos
ORDER BY avg(fizetes_huf) desc
*/

-- 9. feladat: Írjuk ki hogy melyik email domain-t hányan használják, használati szerint csökkenő sorrendbe
SELECT substring_index(email, "@", -1) as domain, 
count(id)  as felhasznalok
FROM személyek
group by domain
order by felhasznalok desc






















