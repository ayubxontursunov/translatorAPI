import sqlite3


class helperDB:
    def __init__(self, dbname: str = 'tech.db'):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()
        self.table_name = ''

    def setup(self, table_name: str = 'customer'):
        self.table_name = table_name
        sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uz_word TEXT,
                en_word TEXT
            );"""
        self.cur.execute(sql)
        self.conn.commit()

    def add_item(self, uz_word: str, en_word: str):
        sql = f"""INSERT INTO {self.table_name} (uz_word,en_word) VALUES (?,?)"""
        self.cur.execute(sql, (uz_word, en_word,))
        self.conn.commit()

    # def get_en_word(self,uz_word: str):
    #     sql = f"SELECT * FROM {self.table_name} where uz_word = ?;"
    #     self.cur.execute(sql,uz_word)
    #     rows = self.cur.fetchall()
    #     return rows is None
    #
    # def check_uz_word(self, uz_word: str):
    #     sql = f"SELECT * FROM {self.table_name} WHERE uz_word = ?;"
    #     self.cur.execute(sql, (uz_word,))
    #     rows = self.cur.fetchall()
    #     return rows is None

    def check_uz_word(self, uz_word: str):
        sql = f"SELECT * FROM {self.table_name} WHERE uz_word = ?;"
        self.cur.execute(sql, (uz_word,))
        rows = self.cur.fetchall()
        return len(rows) != 0

    def check_en_word(self, en_word: str):
        sql = f"SELECT * FROM {self.table_name} WHERE en_word = ?;"
        self.cur.execute(sql, (en_word,))
        rows = self.cur.fetchall()
        return len(rows) != 0

    def get_words_en(self, en_word: str):
        sql = f"SELECT * FROM {self.table_name} WHERE en_word = ?;"
        self.cur.execute(sql, (en_word,))
        rows = self.cur.fetchall()
        return rows

    def get_words_uz(self, uz_word: str):
        sql = f"SELECT * FROM {self.table_name} WHERE uz_word = ?;"
        self.cur.execute(sql, (uz_word,))
        rows = self.cur.fetchall()
        return rows

    def update_item(self, uz_word: str, en_word: str, id):
        sql = f"update {self.table_name} set uz_word = ?, en_word = ? where id = ?;"
        self.cur.execute(sql, (uz_word, en_word, id,))
        self.conn.commit()

    # """update other method
    # def update_item(self,data):
    #     sql = f"update {self.table_name} set data = ? where id = ?;"
    #     self.cur.execute(sql,data)
    #     self.conn.commit()
    #
    # database = helperDB('shop.db')
    # database.setup('customer')
    # database.update_item(('24421',2))
    # print(database.get_item())
    # """

    def remove_item(self, id):
        sql = f"delete from {self.table_name} where id = {id};"
        self.cur.execute(sql)
        self.conn.commit()

    def close_db(self):
        self.conn.close()


# shop = helperDB('shop.db')
# shop.setup('customer')
# shop.add_item('234')
# shop.add_item('124')
# print(shop.get_item())
#
# shop.setup('orders')
# shop.add_item('42565437')
# shop.add_item('76354723')
# print(shop.get_item())
#
# dashboard = helperDB('dashboard.db')
# dashboard.setup('admins')
# dashboard.add_item('234234324')
# dashboard.add_item('546345235')
# print(dashboard.get_item())
# print('Query executed successfully')

# print()
# database = helperDB('shop.db')
# database.setup('customer')
# # database.update_item('24421',3)
# database.remove_item(3)
# print(database.get_item())


# base = helperDB('dictionary.db')
# base.setup('uz_en')
#
# base.update_item("og'iz", 'mouth',12)

# base.add_item('Lamborghini')
# base.add_item('Porsche')
# base.add_item('moshina','car')
# base.add_item('BMW')
# base.remove_item(5)

# print(base.check_uz_word('car'))
# print("---------------------------")
# print(base.check_en_word('pen'))
# print("____________________________")
# uz = base.get_words("car")
# print(uz[0][2])

print("query executed succesfully")
