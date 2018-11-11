from django.urls import path
from . import views, apps

app_name = apps.AuditConfig.name
urlpatterns = [
    # ex: /audit/
    path('', views.login, name='login'),
    # ex: /audit/defect/
    path('defect/', views.DefectIndexView.as_view(), name='defect'),
    # ex: /audit/defect/add/
    path('defect/add/', views.DefectAddView.as_view(), name='defect_add'),
    # ex: /audit/defect/update/5/
    path('defect/update/<int:defect_id>',
         views.DefectUpdateView.as_view(), name='defect_update'),
    # ex: /audit/defect/remove/5/
    path('defect/remove/<int:defect_id>', views.remove, name='defect_remove'),
]
