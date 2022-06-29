import json
import os
from time import time

import orjson
import psycopg2

from serializers import OverloadSerializer, OverloadListSerializer

db_host = os.environ["DB_HOST"]
db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]

# table over 1M records
sql = (
    "select id, client_guid, created_at, updated_at, action_type, db_table, row_id, model_name, user_id, is_active "
    "from overload "
    "where created_at between '2019-01-01' and '2022-06-01' "
    "order by user_id "
    "limit 100000"
)


def main():
    connection = psycopg2.connect(
        "host={} dbname={} user={} password={}".format(
            db_host, db_name, db_user, db_pass
        )
    )
    cursor = connection.cursor()

    t1 = time()
    cursor.execute(sql)
    print("Cursor return {} records".format(cursor.rowcount))
    print("sql query: ", time() - t1, "\n")

    t1 = time()
    result = []
    for record in cursor.fetchall():
        result.append(
            {
                "id": record[0],
                "client_guid": record[1],
                "created_at": record[2].strftime("%Y-%m-%d, %H:%M:%S"),
                "date": record[3].strftime("%Y-%m-%d, %H:%M:%S"),
                "action_type": record[4],
                "db_table": record[5],
                "row_id": record[6],
                "model_name": record[7],
                "user_id": record[8],
                "is_active": record[9],
            }
        )

    json.dumps(result)
    print("json dumps: ", time() - t1, "\n")

    t1 = time()
    orjson.dumps(result)
    print("orjson dumps: ", time() - t1, "\n")

    t1 = time()
    cursor.execute(sql)
    print("Cursor return {} records".format(cursor.rowcount))
    print("sql query again: ", time() - t1, "\n")

    t1 = time()
    result = [
        OverloadSerializer(
            **{
                key: record[i]
                for i, key in enumerate(OverloadSerializer.__fields__.keys())
            }
        )
        for record in cursor.fetchall()
    ]
    OverloadListSerializer(detected_users=result).json()
    print("pydantic json: ", time() - t1)


if __name__ == "__main__":
    main()
