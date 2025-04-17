from django.urls import path, include
from app_empresa.api.viewsets import CreateUserAPIViewSet, PatrimonioViewSet, AmbienteViewSet, GestorViewSet, ManutentorViewSet, OrdemDeServicoViewSet, AreaViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app_empresa.api.viewsets import CreateUserAPIViewSet, PatrimonioList, AreaList, GestorList, AmbienteList, OrdemDeServicoList, ManutentorList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patrimonios', PatrimonioViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'gestores', GestorViewSet)
router.register(r'ambientes', AmbienteViewSet)
router.register(r'ordens', OrdemDeServicoViewSet)
router.register(r'manutentores', ManutentorViewSet)

urlpatterns = [
    path('api/create_user/', CreateUserAPIViewSet.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/patrimonios/', PatrimonioList.as_view(), name='patrimonios'),
    path('api/areas/', AreaList.as_view(), name='areas'),
    path('api/gestores/', GestorList.as_view(), name='gestores'),
    path('api/ambientes/', AmbienteList.as_view(), name='ambientes'),
    path('api/ordens/', OrdemDeServicoList.as_view(), name='ordensdeservico'),
    path('api/manutentores/', ManutentorList.as_view(), name='manutentores'),
]
