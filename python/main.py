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


def prepare_plan(cursor, plan_name, query):
    plan_query = "PREPARE " + plan_name + " AS " + query
    #cursor.execute( "PREPARE %s AS %s", (str(plan_name), query) )
    cursor.execute (plan_query)

def execute_plan(cursor, plan_name, param):
    execute_query = "EXECUTE " + plan_name + " (%s)"
    #cursor.execute( "EXECUTE %s (%s)", (plan_name, param) )
    cursor.execute(execute_query, (param, ))
    result = cursor.fetchone()
    html = Html( result[0], result[1] )
    return html
    
    
    
if __name__ == "__main__":
    
    
    mysql_conn = mysql.connector.connect(
                                        database = "hstestdb", 
                                        host = "localhost", 
                                        user = "hsdb", 
                                        password = "hsdbpass", 
                                        port = 3306 )
    
    postgresql_conn = psycopg2.connect(
                                        database = "hstestdb", 
                                        host = "localhost", 
                                        user = "hsdb", 
                                        password = "hsdbpass", 
                                        port = 5432)
    
    connection = mysql_conn
    
    try:
        cursor = connection.cursor(prepared=True)
    except TypeError:
        print("Prepared Statements not supported")
        cursor = connection.cursor()
        
    list_html(cursor)

    uuid = "550e8400-e29b-41d4-a716-446655440000"
    print(get_page(cursor, uuid))


    # Prepared statement for PostgreSQL
    connection = postgresql_conn
    cursor = connection.cursor()
    
    query = "SELECT * FROM HTML WHERE uuid=$1"
    prepare_plan( cursor, "select_where_uuid", query )
    html = execute_plan( cursor, "select_where_uuid", uuid )
    print( html )
    
    
    