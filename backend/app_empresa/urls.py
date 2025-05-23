from django.urls import path, include
from app_empresa.api.viewsets import CreateUserAPIViewSet, PatrimonioViewSet, AmbienteViewSet, OrdemDeServicoViewSet, AreaViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app_empresa.api.viewsets import CreateUserAPIViewSet, PatrimonioList, AreaList, AmbienteList, OrdemDeServicoList
from rest_framework.routers import DefaultRouter
from .views import upload_ambiente, upload_area, upload_patrimonio, buscar_ambiente_por_id

router = DefaultRouter()
router.register(r'patrimonios', PatrimonioViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'ambientes', AmbienteViewSet)
router.register(r'ordens', OrdemDeServicoViewSet)

urlpatterns = [
    path('api/create_user/', CreateUserAPIViewSet.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/patrimonios/', PatrimonioList.as_view(), name='patrimonios'),
    path('api/areas/', AreaList.as_view(), name='areas'),
    path('ambiente/<int:idSearch>/', buscar_ambiente_por_id, name='buscar_ambiente_por_id'),
    path('api/ambientes/', AmbienteList.as_view(), name='ambientes'),
    path('api/ordens/', OrdemDeServicoList.as_view(), name='ordensdeservico'),
    path('api/upload_area/', upload_area, name='upload_area'),
    path('api/upload_ambiente/', upload_ambiente, name='upload_ambiente'),
    path('api/upload_patrimonio/', upload_patrimonio, name='upload_patrimonio'),
]
