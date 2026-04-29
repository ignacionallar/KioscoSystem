import sqlite3
from product import Product

class ProductRepository:
    def __init__(self, db="kiosco.db"):
        self._db=db
        self.create_table()

    def connect(self):
        return sqlite3.connect(self._db)
    
    def create_table(self):
        with self.connect() as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXIST products(
                    id integer primery key autoincrement,
                    name text not null,
                    price real not null,
                    stock integer not null default 0
                )
                """
            )

    def insert_product(self, producto:Product):
        with self.connect() as con:
            cur= con.execute(" INSERT INTO products(name, price, stock) values (?,?,?)",
                (
                    producto.name, producto.price, producto.stock
                )
            )
            return True
        
    def get_all_products(self):
        with self.connect() as con:
            con.row_factory= sqlite3.Row
            rows= con.execute("SELECT * FROM products").fetchall()
            productos=[]
            for fila in rows:
                productos.append(Product(fila["name"],fila["stock"],fila["id"]))
            return productos
        
    def get_stock_product(self,id):
        with self.connect() as con:
            con.row_factory= sqlite3.Row
            row= con.execute(f"SELECT stock FROM products where id= {id}").fetchone()
            return row["stock"]
        
    def delete_product(self,id):
        try:
            with self.connect() as con:
                con.row_factory= sqlite3.Row
                row= con.execute(f"DELETE FROM products where id= {id}")
                return True
        except:
            return False