CREATE TABLE sample_data (
    first_name TEXT,
    last_name TEXT,
    company_name TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip INT,
    phone1 TEXT,
    phone2 TEXT,
    email TEXT,
    department TEXT
);

COPY sample_data
FROM '/docker-entrypoint-initdb.d/Sample.csv'
DELIMITER ','
CSV HEADER;

ALTER TABLE sample_data ADD COLUMN id SERIAL PRIMARY KEY;