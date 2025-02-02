from django.urls import path
from nxtbn.discount.api.dashboard import views as discount_views

urlpatterns = [
    path('promocodes/', discount_views.PromoCodeListCreateAPIView.as_view(), name='promo-code-list-create'),
    path('promocodes/<int:id>/', discount_views.PromoCodeUpdateRetrieveDeleteView.as_view(), name='promo-code-update-delete')
]
