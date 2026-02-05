from django.urls import path
from .views import (
    delete_analysis_view,
    home_view,
    history_view,
    analysis_detail_view,
    download_summary_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('historial/', history_view, name='history'),
    path('analisis/<int:analysis_id>/', analysis_detail_view, name='analysis_detail'),
    path('descargar/<int:analysis_id>/', download_summary_view, name='download_summary'),
    path("delete/<int:analysis_id>/", delete_analysis_view, name="delete_analysis")
]
