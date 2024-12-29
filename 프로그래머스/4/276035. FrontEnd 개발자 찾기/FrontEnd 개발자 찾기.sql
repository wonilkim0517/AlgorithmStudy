SELECT DISTINCT
    D.ID,
    D.EMAIL,
    D.FIRST_NAME,
    D.LAST_NAME
FROM SKILLCODES AS S
JOIN DEVELOPERS AS D
ON S.CODE & D.SKILL_CODE > 0
WHERE S.CATEGORY = 'Front End'
ORDER BY D.ID ASC