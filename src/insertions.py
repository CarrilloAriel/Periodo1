from mysql.connector import Error
import mysql_connector


try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='S3rver',
        db='python_inserciones_masivas'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO tabla (col,col,col) 
                                VALUES (%s,%s,%s)""",data)
        print(cursor.rowcount)
        print(len(data))
        if (len(data)==cursor.rowcount()):
            connection.commit()
            print("{} rows inserted.".format (len(data)))
        else:
            connection.rollback()


except Error as ex:
    print("Error during connection: {}".format(ex))
finally:
    if connection.is_closed():
        connection.close()
        print("Connection closed.")