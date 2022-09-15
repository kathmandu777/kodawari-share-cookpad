from django.urls import path

from .views import (
    AddCouponView,
    CheckoutView,
    HomeView,
    ItemDetailView,
    OrderSummaryView,
    PaymentView,
    RequestRefundView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = "ecommerce"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("order-summary/", OrderSummaryView.as_view(), name="order-summary"),
    path("product/<uuid:pk>/", ItemDetailView.as_view(), name="product"),
    path("add-to-cart/<uuid:pk>/", add_to_cart, name="add-to-cart"),
    path("add-coupon/", AddCouponView.as_view(), name="add-coupon"),
    path("remove-from-cart/<uuid:pk>/", remove_from_cart, name="remove-from-cart"),
    path("remove-item-from-cart/<uuid:pk>/", remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path("payment/<payment_option>/", PaymentView.as_view(), name="payment"),
    path("request-refund/", RequestRefundView.as_view(), name="request-refund"),
]
