import psycopg2, mysql.connector

class Html:
    
    def __init__(self, uuid, content) :
        self.uuid = uuid
        self.content = content
        
    def __str__(self):
        return f"uuid: {self.uuid}\ncontent: {self.content}"


def list_html(cursor):
    cursor.execute("SELECT * FROM HTML")
    results = cursor.fetchall()
    
    for result in results:
        html = Html( result[0], result[1] );
        print(str(html))


def get_page(cursor, uuid):
    cursor.execute("SELECT * FROM HTML WHERE uuid=%s", (uuid, ))
    result = cursor.fetchone()
    html = Html(result[0], result[1])
    return html
    
    
if __name__ == "__main__":
    
    uuid = "550e8400-e29b-41d4-a716-446655440000"
    
    mysql_conn = mysql.connector.connect(database = "hstestdb", host = "localhost", user = "hsdb", password = "hsdbpass", port = 3306)
    postgresql_conn = psycopg2.connect(database = "hstestdb", host = "localhost", user = "hsdb", password = "hsdbpass", port = 5432)
    
    connection = postgresql_conn
    cursor = connection.cursor()
    
    print(get_page(cursor, uuid))
    list_html(cursor)
