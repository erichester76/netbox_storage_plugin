from django.urls import path
import views

app_name = 'netbox_storage_plugin'

urlpatterns = [
    path('volumes/', views.VolumeListView.as_view(), name='volume_list'),
    path('volumes/<int:pk>/', views.VolumeView.as_view(), name='volume_detail'),
    path('volumes/add/', views.VolumeEditView.as_view(), name='volume_add'),
    path('volumes/<int:pk>/edit/', views.VolumeEditView.as_view(), name='volume_edit'),
    path('volumes/<int:pk>/delete/', views.VolumeDeleteView.as_view(), name='volume_delete'),
    path('volumes/import/',views. VolumeImportView.as_view(), name='volume_import'),
    path('volumes/bulk-edit/', views.VolumeBulkEditView.as_view(), name='volume_bulk_edit'),
    path('volumes/bulk-delete/',views.VolumeBulkDeleteView.as_view(), name='volume_bulk_delete'),
    path('volumes/<int:pk>/changelog/', views.VolumeChangeLogView.as_view(), name='volume_changelog'),
    path('volumes/get-details-form/', views.GetDetailsFormView.as_view(), name='get_details_form'),
]