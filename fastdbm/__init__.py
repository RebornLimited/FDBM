from time import sleep
from tqdm import tqdm
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
            print("Connecting...")
            for i in tqdm(range(100), colour="green"):
                sleep(0.02)
            print("Successfully connected!")

            try:
                with connection.cursor() as cursor:
                    command = input("Enter the command: ")
                    use_commit = input("Use commit?(Y/n): ").lower()

                    if use_commit == "y":
                        if "SELECT" in command:
                            cursor.execute(command)
                            connection.commit()
                            rows = cursor.fetchall()
                            for row in rows:
                                print("Output: {}".format(row))
                        else:
                            cursor.execute(command)
                            connection.commit()
                            print("Operation completed successfully!")
                            print("Check your database.")
                    else:
                        if "SELECT" in command:
                            cursor.execute(command)
                            rows = cursor.fetchall()
                            for row in rows:
                                print("Output: {}".format(row))
                        else:
                            cursor.execute(command)
                            print("Operation completed successfully!")
                            print("Check your database.")
            finally:
                connection.close()
        except Exception as ex:
            print("Something went wrong...")
            print("Cause: {}".format(ex))
