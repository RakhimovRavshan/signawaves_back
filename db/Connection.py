import logging
import psycopg2
from psycopg2.extras import LoggingConnection


class Connection(object):
    _instance = None
    _db = None

    @staticmethod
    def instance():
        if Connection._instance is None:
            Connection._instance = Connection()
        return Connection._instance

    def __init__(self):
        self._db = connection = psycopg2.connect(
            user="signawaves", password="waves",
            host="127.0.0.1", database="signawaves")

    def execute_query(self, query, address):
        try:
            connection = psycopg2.connect(
                user="signawaves", password="waves",
                host="127.0.0.1", database="signawaves")
            print(connection)
            cursor = connection.cursor()
            print(address)
            cursor.execute(query, (address,))
            return cursor.fetchall()
            print("You are connected to - ", row, "\n")
        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                if cursor:
                    cursor.close()
                    connection.close()

    def execute_query1(self, query, id):
        try:
            connection = psycopg2.connect(
                user="signawaves", password="waves",
                host="127.0.0.1", database="signawaves")
            print(connection)
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchone()
            print("You are connected to - ", row, "\n")
        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                if cursor:
                    cursor.close()
                    connection.close()

    def execute_query2(self, query, address):
        try:
            connection = psycopg2.connect(
                user="signawaves", password="waves",
                host="127.0.0.1", database="signawaves")
            print(connection)
            cursor = connection.cursor()
            cursor.execute(query, (address,))
            return cursor.fetchall()
            print("You are connected to - ", row, "\n")
        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                if cursor:
                    cursor.close()
                    connection.close()

    def execute_query3(self, query, address):
        try:
            connection = psycopg2.connect(
                user="signawaves", password="waves",
                host="127.0.0.1", database="signawaves")
            print(connection)
            cursor = connection.cursor()
            cursor.execute(query, (address,))
            return cursor.fetchone()
            print("You are connected to - ", row, "\n")
        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                if cursor:
                    cursor.close()
                    connection.close()

    def execute_query4(self, query, id, owner_id, title, description):
        try:
            connection = psycopg2.connect(
                user="signawaves", password="waves",
                host="127.0.0.1", database="signawaves")
            print(connection)
            cursor = connection.cursor()
            cursor.execute(query, (id, owner_id, title, description))
            connection.commit()
            print("You are connected to - ", "\n")
        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                if cursor:
                    cursor.close()
                    connection.close()

    def execute_query5(self, query, document_id, address):
        try:
            logging.basicConfig(level=logging.DEBUG)
            logger = logging.getLogger(__name__)
            connection = psycopg2.connect(
                connection_factory=LoggingConnection,
                user="signawaves", password="waves",
                host="127.0.0.1", database="signawaves")
            connection.initialize(logger)

            print(connection)
            cursor = connection.cursor()
            cursor.execute(query, (document_id, address))
            connection.commit()
            print("You are connected to - ", "\n")
        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                if cursor:
                    cursor.close()
                    connection.close()

        def execute_query6(self, query, document_id, address):

            try:
                logging.basicConfig(level=logging.DEBUG)
                logger = logging.getLogger(__name__)
                connection = psycopg2.connect(
                    connection_factory=LoggingConnection,
                    user="signawaves", password="waves",
                    host="127.0.0.1", database="signawaves")
                connection.initialize(logger)

                print(connection)
                cursor = connection.cursor()
                cursor.execute(query, (document_id, address))
                connection.commit()
                print("You are connected to - ", "\n")
            except psycopg2.Error as error:
                print("Error while connecting to PostgreSQL", error)
            finally:
                if connection:
                    if cursor:
                        cursor.close()
                        connection.close()
