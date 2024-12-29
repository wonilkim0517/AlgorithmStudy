SELECT
    A.AUTHOR_ID,
    A.AUTHOR_NAME,
    B.CATEGORY,
    SUM(B.PRICE * S.SALES) AS TOTAL_SALES
FROM BOOK AS B
JOIN AUTHOR AS A
ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES AS S
ON B.BOOK_ID = S.BOOK_ID
WHERE YEAR(S.SALES_DATE) = 2022 AND MONTH(S.SALES_DATE) = 1
GROUP BY A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
ORDER BY A.AUTHOR_ID ASC, B.CATEGORY DESC;