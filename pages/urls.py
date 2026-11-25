from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('patients/',views.patients, name='patients'),
    path('patients/oms/',views.oms,name='oms'),
    path('patients/dms/',views.dms,name='dms'),
    path('patients/info/',views.info,name='info'),
    path('analyses/',views.analyses,name='analyses'),
    path('promotions/',views.promotion_list,name='promotion_list'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contacts'),
    path('review_plural/',views.review_plural,name='review_plural'),
    path('diagnostic/',views.diagnostic,name='diagnostic'),
    path('service/',views.service,name='service')
]