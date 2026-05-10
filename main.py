import models.product
import models.sell
import models.sellDetail

from services.kiosko_service import KioskoService


if __name__ == "__main__":
    app = KioskoService()
    app.menu()