CREATE EXTENSION IF NOT EXISTS aws_s3 CASCADE;

CREATE TEMP TABLE Wikipedia_Page_temp (LIKE Wikipedia_Page);

SELECT
    aws_s3.table_import_from_s3(
        'Wikipedia_Page_temp',
        '',
        '(format csv, header true)',
        '{bucket_name}',
        'Philosophy-bronze.csv',
        '{region}',
        '{access_key}',
        '{secret_key}'
    );