from rest_framework import routers
from news.viewsets import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)