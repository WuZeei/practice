import sqlalchemy


pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )
db = init_connection_engine()

conn = db.connect()
query = 'SELECT * from login where account ="{}" and password ="{}" limit 1;'.format(acc,wd)
query_results = conn.execute(query)
conn.close()
if len(query_results.fetchall()) == 0:
    print(False)
else:
    print(True)