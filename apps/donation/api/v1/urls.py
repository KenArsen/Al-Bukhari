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

from apps.donation.api.v1.apis.test import create_checkout_session, HomePageView, SuccessView, \
    CancelledView, stripe_webhook

urlpatterns += [
    path('create-checkout-session/', create_checkout_session),
    path('home/', HomePageView.as_view(), name='home'),
    path('success/', SuccessView.as_view()),  # new
    path('cancelled/', CancelledView.as_view()),  # new
    path('webhook/', stripe_webhook),
]
