DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS budgets;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    activated BOOlEAN
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    activated BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    merchant_id SERIAL REFERENCES merchants(id),
    tag_id SERIAL REFERENCES tags(id),
    trans_time TIMESTAMP
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    amount FLOAT
);
