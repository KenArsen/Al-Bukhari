from django.urls import path

from .apis import (
    CustomerDetailAPI,
    CustomerListAPI,
    CustomerPaymentAPI,
    DonateCreateAPI,
    DonateListAPI,
    ForumView,
)

app_name = "donation"

urlpatterns = [
    path("", ForumView.as_view(), name="index"),
    path("list/", DonateListAPI.as_view(), name="donation-list"),
    path("create/", DonateCreateAPI.as_view(), name="donate-create"),
]

# customer
urlpatterns += [
    path("customers/", CustomerListAPI.as_view(), name="customer-list"),
    path("customers/<int:pk>/payments/", CustomerPaymentAPI.as_view(), name="customer-payments"),
    path("customers/<int:pk>/", CustomerDetailAPI.as_view(), name="customer-detail"),
]
