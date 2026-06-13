from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('scrap-prices/', views.scrap_prices, name='scrap_prices'),

    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),

    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('request-pickup/', views.request_pickup, name='request_pickup'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('my-transactions/', views.my_transactions, name='my_transactions'),
    path('notifications/', views.notifications, name='notifications'),

    path('collector-dashboard/', views.collector_dashboard, name='collector_dashboard'),
    path('assigned-pickups/', views.assigned_pickups, name='assigned_pickups'),
    path('update-collection/', views.update_collection, name='update_collection'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-scrap/', views.manage_scrap, name='manage_scrap'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('manage-collections/', views.manage_collections, name='manage_collections'),
    path('manage-transactions/', views.manage_transactions, name='manage_transactions'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('reports/', views.reports, name='reports'),
    path('help/', views.help_page, name='help'),
]