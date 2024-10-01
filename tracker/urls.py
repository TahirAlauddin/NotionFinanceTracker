from django.urls import path
from tracker import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sync/', views.sync_notion_data, name='sync_notion_data'),
    path('create/', views.create_record_view, name='create_record'),
    path('update/<int:pk>/', views.update_record_view, name='update_record'),
    path('delete/<int:pk>/', views.delete_record_view, name='delete_record'),
    path('', views.dashboard_view, name='dashboard'),  # Placeholder for dashboard
]
