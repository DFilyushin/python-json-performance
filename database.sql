CREATE DATABASE test_db;

CREATE TABLE overload
(
    id          SERIAL PRIMARY KEY,
    client_guid varchar(80),
    created_at  timestamp,
    updated_at  timestamp,
    action_type VARCHAR(10) NOT NULL,
    db_table    VARCHAR(80) NOT NULL,
    row_id      int,
    model_name  VARCHAR(255),
    user_id     int,
    is_active   BOOLEAN
);

CREATE INDEX IF NOT EXISTS idx_created_at ON overload (created_at);
CREATE INDEX IF NOT EXISTS idx_db_table ON overload (db_table);

INSERT INTO overload(client_guid, created_at, updated_at, action_type, db_table, row_id, model_name, user_id, is_active)
SELECT
       uuid_in(md5(random()::text || random()::text)::cstring),
       timestamp '2019-01-01 20:12:00' +
       random() * (timestamp '2022-01-01 20:00:00' -
                   timestamp '2019-12-31 10:00:00'),
       timestamp '2019-01-01 20:12:00' +
       random() * (timestamp '2022-01-01 20:00:00' -
                   timestamp '2019-12-31 10:00:00'),

       'act_' || (
           CASE (RANDOM() * 4)::INT
               WHEN 0 THEN 'happy'
               WHEN 1 THEN 'sad'
               WHEN 2 THEN 'bad'
               WHEN 3 THEN 'tired'
               WHEN 4 THEN 'boring'
               END
           ),
       (
           CASE (RANDOM() * 4)::INT
               WHEN 0 THEN 'LOGS'
               WHEN 1 THEN 'PAYMENT'
               WHEN 2 THEN 'SALDO'
               WHEN 3 THEN 'WITHDRAWS'
               WHEN 4 THEN 'REQUESTS'
               END
           ),
       random() * 10000 ::int,
        random()::text || random()::text,
       random() * 100 ::int,
       True
FROM GENERATE_SERIES(1, 1000000) seq;
