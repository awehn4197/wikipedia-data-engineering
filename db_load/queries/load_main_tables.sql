BEGIN TRANSACTION;

-- Delete rows through inner join
DELETE FROM
    Wikipedia_Page USING Wikipedia_Page_temp
WHERE
    Wikipedia_Page.article_key = Wikipedia_Page_temp.article_key;

-- Move data from temp table to main tables
INSERT INTO
    Wikipedia_Page
SELECT
    *
FROM
    Wikipedia_Page_temp;

END TRANSACTION;

-- Drop temp tables
DROP TABLE Wikipedia_Page_temp;