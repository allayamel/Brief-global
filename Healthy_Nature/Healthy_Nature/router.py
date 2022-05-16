from Healthy_NatureAPP.viewsets import PersonnelsViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('personnels',PersonnelsViewsets)