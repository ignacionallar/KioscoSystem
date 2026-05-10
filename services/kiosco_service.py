from db.connection import create_db_and_tables, get_session

from repositories.product_repository import ProductRepository
from repositories.sell_repository import SellRepository
from repositories.sellDetail_repository import SellDetailRepository

from models.product import ProductCreate
from models.sell import SellCreate, SellUpdate
from models.sellDetail import SellDetailCreate


class KioscoService:

    def __init__(self):
        self.product_repo = ProductRepository()
        self.sell_repo = SellRepository()
        self.item_repo = SellDetailRepository()

    def agregar_producto(self):
        print("\n-- Agregar producto --")

        name = input("Nombre: ").strip()
        price = float(input("Precio: "))
        stock = int(input("Stock: "))

        with get_session() as session:
            product = self.product_repo.create(
                session,
                ProductCreate(
                    name=name,
                    price=price,
                    stock=stock
                )
            )

        print(
            f"Producto creado: "
            f"[{product.id}] {product.name} "
            f"- ${product.price} "
            f"(stock: {product.stock})"
        )

    def agregar_venta(self):
        print("\n-- Agregar venta --")

        with get_session() as session:
            sell = self.sell_repo.create(
                session,
                SellCreate()
            )

        print(
            f"Venta creada con ID {sell.id} "
            f"({sell.date.strftime('%Y-%m-%d %H:%M')})"
        )

    def agregar_item(self):
        print("\n-- Agregar item a venta --")

        with get_session() as session:
            products = self.product_repo.get_all(session)
            sells = self.sell_repo.get_all(session)

        if not products:
            print("No hay productos cargados.")
            return

        print("Productos disponibles:")
        for p in products:
            print(f"  [{p.id}] {p.name} - ${p.price}")

        if not sells:
            print("No hay ventas creadas.")
            return

        print("\nVentas disponibles:")
        for s in sells:
            print(
                f"  [{s.id}] "
                f"{s.date.strftime('%Y-%m-%d %H:%M')} "
                f"- Total: ${s.total:.2f}"
            )

        product_id = int(input("\nID del producto: "))
        sell_id = int(input("ID de la venta: "))
        quantity = int(input("Cantidad: "))

        product = next(
            (p for p in products if p.id == product_id),
            None
        )

        if not product:
            print("Producto no encontrado.")
            return

        if quantity <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        if product.stock < quantity:
            print("Stock insuficiente.")
            return

        unit_price = product.price
        subtotal = unit_price * quantity

        with get_session() as session:

            sell = self.sell_repo.get_by_id(
                session,
                sell_id
            )

            if not sell:
                print("Venta no encontrada.")
                return

            self.item_repo.create(
                session,
                SellDetailCreate(
                    product_id=product_id,
                    sell_id=sell_id,
                    quantity=quantity,
                    unit_price=unit_price
                )
            )

            new_total = sell.total + subtotal

            self.sell_repo.update(
                session,
                sell_id,
                SellUpdate(total=new_total)
            )

            db_product = self.product_repo.get_by_id(
            session,
            product_id
            )

            new_stock = db_product.stock - quantity

            from models.product import ProductUpdate

            self.product_repo.update(
                session,
                product_id,
                ProductUpdate(stock=new_stock)
            )
        print(
            f"Item agregado: "
            f"{quantity}x {product.name} "
            f"a ${unit_price:.2f} "
            f"= ${subtotal:.2f}"
        )

        print(
            f"Total actualizado de venta "
            f"{sell_id}: ${new_total:.2f}"
        )

    def listar_productos(self):
        print("\n-- Productos --")

        with get_session() as session:
            products = self.product_repo.get_all(session)

        if not products:
            print("No hay productos cargados.")
            return

        print(f"{'ID':>4} {'Nombre':<20} {'Precio':>10} {'Stock':>7}")
        print("-" * 45)

        for p in products:
            print(
                f"{p.id:>4} "
                f"{p.name:<20} "
                f"{p.price:>10.2f} "
                f"{p.stock:>7}"
            )

    def resumen_venta(self):

        with get_session() as session:
            sells = self.sell_repo.get_all(session)

        if not sells:
            print("No hay ventas creadas.")
            return

        print("\nVentas disponibles:")

        for s in sells:
            print(
                f"  [{s.id}] "
                f"{s.date.strftime('%Y-%m-%d %H:%M')} "
                f"- Total: ${s.total:.2f}"
            )

        print("\n-- Resumen de venta --")

        sell_id = int(input("ID de la venta: "))

        with get_session() as session:

            sell = self.sell_repo.get_by_id(
                session,
                sell_id
            )

            if not sell:
                print("Venta no encontrada.")
                return

            items = self.item_repo.get_by_sell(
                session,
                sell_id
            )

            product_ids = {i.product_id for i in items}

            products = {
                p.id: p
                for p in self.product_repo.get_all(session)
                if p.id in product_ids
            }

        print(
            f"\nVenta #{sell.id} "
            f"— {sell.date.strftime('%Y-%m-%d %H:%M')}"
        )

        print(
            f"{'Producto':<20} "
            f"{'Cantidad':>8} "
            f"{'Precio unit.':>13} "
            f"{'Subtotal':>10}"
        )

        print("-" * 55)

        for item in items:

            product_name = (
                products[item.product_id].name
                if item.product_id in products
                else "?"
            )

            subtotal = item.quantity * item.unit_price

            print(
                f"{product_name:<20} "
                f"{item.quantity:>8} "
                f"{item.unit_price:>13.2f} "
                f"{subtotal:>10.2f}"
            )

        print("-" * 55)

        print(f"{'TOTAL':>43} {sell.total:>10.2f}")

    def menu(self):

        create_db_and_tables()

        opciones = {
            "1": ("Agregar producto", self.agregar_producto),
            "2": ("Agregar venta", self.agregar_venta),
            "3": ("Agregar item a venta", self.agregar_item),
            "4": ("Resumen de venta", self.resumen_venta),
            "5": ("Listar productos", self.listar_productos),
            "0": ("Salir", None),
        }

        while True:

            print("\n===== KIOSCO =====")

            for key, (label, _) in opciones.items():
                print(f"  {key}. {label}")

            opcion = input("Opcion: ").strip()

            if opcion == "0":
                print("Saliendo...")
                break

            elif opcion in opciones:
                opciones[opcion][1]()

            else:
                print("Opcion invalida.")