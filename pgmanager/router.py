from rest_framework import routers
from accounts.viewset import EnterpriseViewset



router = routers.DefaultRouter()
router.register("enterprises", EnterpriseViewset)


# https://127.0.0.1:8000/api/enterprises
