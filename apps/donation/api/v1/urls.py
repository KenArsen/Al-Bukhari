from django.urls import path

from .apis import (
    CancelledView,
    CustomerDetailAPI,
    CustomerListAPI,
    CustomerPaymentListAPI,
    ForumView,
    MyBalanceAPI,
    PaymentView,
    SuccessView,
)

app_name = "donation"

urlpatterns = [
    path("", ForumView.as_view(), name="index"),
    path("my_balance/", MyBalanceAPI.as_view(), name="my-balance"),
    path("create-checkout-session/", PaymentView.as_view(), name="create-checkout-session"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancelled/", CancelledView.as_view(), name="cancelled"),
]

# customer
urlpatterns += [
    path("customers/", CustomerListAPI.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetailAPI.as_view(), name="customer-detail"),
    path("customers/<int:pk>/payments/", CustomerPaymentListAPI.as_view(), name="customer-payments"),
]
