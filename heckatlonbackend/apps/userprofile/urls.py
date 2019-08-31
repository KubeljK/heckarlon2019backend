from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from apps.userprofile import views

urlpatterns = [
    # Registration and login
    path("/register", views.RegisterUsers.as_view(), name="user-register"),
    path("/login", jwt_views.TokenObtainPairView.as_view(), name="user-login"),
    path("/login/refresh", jwt_views.TokenRefreshView.as_view(), name="user-refresh-token"),

    # Users and profile
    path("", views.UsersList.as_view(), name="user-list"),
    path("/<int:pk>", views.UserDetail.as_view(), name="user-detail"),
    path("/profile", views.EditProfile.as_view(), name="user-profile"),

    # Inventories
    path("/profile/inventories", views.InventoryList.as_view(), name="inventory-list"),
    path("/profile/inventories/<int:pk>", views.InventoryDetails.as_view(), name="inventory-detail"),
    path("/profile/inventories/<int:inventory_id>/ingredient/<int:pk>", views.InventoryIngredientUpdate.as_view(), name="inventoryingredient-details"),
]
