from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("profile", views.ProfileUserViewSet)
router.register("login", views.LoginViewSet, basename="login")
router.register("feed", views.UserProfileFeedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
