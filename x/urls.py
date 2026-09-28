from django.urls import path

from . import views


urlpatterns = [
    path("", views.x_list, name="x_list"),

    path(
        "create/",
        views.x_create,
        name="x_create",
    ),

    path(
        "<int:x_id>/edit/",
        views.x_edit,
        name="x_edit",
    ),

    path(
        "<int:x_id>/delete/",
        views.x_delete,
        name="x_delete",
    ),

    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "profile/<str:username>/",
        views.user_profile,
        name="user_profile",
    ),
]