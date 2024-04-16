from django.urls import path

from .apis import (
    CustomerDetailAPI,
    CustomerListAPI,
    CustomerPaymentListAPI,
    DonateCreateAPI,
    ForumView,
    MyBalanceAPI,
)

app_name = "donation"

urlpatterns = [
    path("", ForumView.as_view(), name="index"),
    path("my_balance/", MyBalanceAPI.as_view(), name="my-balance"),
    path("create/", DonateCreateAPI.as_view(), name="donate-create"),
]

# customer
urlpatterns += [
    path("customers/", CustomerListAPI.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetailAPI.as_view(), name="customer-detail"),
    path("customers/<int:pk>/payments/", CustomerPaymentListAPI.as_view(), name="customer-payments"),
]
