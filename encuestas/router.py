from core.api.views import UsuarioViewSet,PreguntasViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register('users', UsuarioViewSet),
router.register('questions', PreguntasViewSet)

