import psycopg2


class Dbmanage:
    def __init__(self, name, user, password, host="localhost"):
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.conn = None

    def connect(self):
        try:
            connect_str = """dbname={} user={} host={} password={}"""\
                .format(self.name, self.user, self.host, self.password)
            self.conn = psycopg2.connect(connect_str)
            self.conn.autocommit = True
            print("connected :D")
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)

    def runner(self, query):
        new_list = []
        cursor = self.conn.cursor()
        cursor.execute(query)
        for element in cursor.fetchall():
            element = list(element)
            new_list.append(element)
        return new_list
