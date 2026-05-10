import models.product
import models.sell
import models.sellDetail

from services.kiosco_service import KioscoService


if __name__ == "__main__":
    app = KioscoService()
    app.menu()