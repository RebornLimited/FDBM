import pymysql

class Database:
    def manager():
        try:
            host = input("Enter host from database: ")
            port = int(input("Enter port from database: "))
            user = input("Enter username from database: ")
            password = input("Enter password from database: ")
            dbname = input("Enter the name of the database: ")

            connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=dbname,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected!")

            try:
                with connection.cursor() as cursor:
                    command = input("Enter the command: ")
                    use_commit = input("Use commit?(Y/n): ").lower()

                    if use_commit == "y":
                        cursor.execute(command)
                        connection.commit()
                        print("Operation completed successfully!")
                        print("Check your database.")
                    else:
                        cursor.execute(command)
                        print("Operation completed successfully!")
                        print("Check your database.")
            finally:
                connection.close()
        except Exception as ex:
            print("Connection failed...")
            print("Cause: {}".format(ex))
