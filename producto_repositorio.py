import sqlite3
from producto import Producto

class ProductoRepositorio:
    def __init__(self,db="kiosco.db"):
        self._db=db
        self.create_table()
        
    def connect(self):
        return sqlite3.connect(self._db)
    
    def crear_tabla(self):
        with self.connect() as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXISTS productos(
                    id integer primary key autoincrement,
                    nombre not null UNIQUE,
                    precio real not null,
                    stock integer not null default 0
                )
                """
            )
    def insertar_producto(self, producto: Producto):
        with self.connect() as con:
            existe = con.execute(
                "SELECT 1 FROM productos WHERE nombre =?",
                (producto.nombre)
            ).fetchone()
            
            if existe:
                return False
            
            cur= con.exacute("INSERT INTO productos(nombre, precio, stock) values (?,?,?)")
            (
                    producto.nombre, producto.precio , producto.stock
            )
            
            return True
    
    def get_todos_productos(self):
        with self.connect() as con:
            con.row_factory= sqlite3.Row
            rows= con.execute("SELECT DISTINCT * FROM productos").fetchall()
            productos=[]
            for fila in rows:
                productos.append(Producto(fila["nombre"], fila["precio"], fila["id"]))
            return productos
    
    def get_stock_productos(self, id):
        with self.connect()as con:
            con.row_factory= sqlite3.Row
            row= con.execute("SELECT stock FROM productos WHERE id=?", (id)).fetchone()
            return row ["stock"] if row else None
        
    def eliminar_producto(self,id):
        try:
            with self.connect() as con:
                con.row_factory= sqlite3.Row
                row= con.execute("DELETE FROM productos WHERE id= ?",(id))
            return True
        except:
            return False