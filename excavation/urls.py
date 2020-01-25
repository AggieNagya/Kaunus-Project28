from django.urls import path
from . import views


"""
  name is the paths below have to reflect the same name in the
  href name in the base_generic.hmtl
  paths for the detail list view of the catalogue items - are the _DetailView
"""

urlpatterns = [

    path('', views.IndexListView.as_view(), name='index'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
    path('topography/', views.TopographyListView.as_view(), name='topography'),
    path('history/', views.HistoryListView.as_view(), name='history'),
    path('monuments/', views.MonumentsListView.as_view(), name='monuments'),
    path('finds/', views.FindListView.as_view(), name='finds'),
    path('findings/', views.FindingListView.as_view(), name='findings'),
    path('buildings/', views.BuildingListView.as_view(), name='buildings'),
    path('trenches/', views.TrenchListView.as_view(), name='trenches'),
    path('areas/', views.AreaListView.as_view(), name='areas'),
    path('monuments/<slug:slug>', views.MonumentsDetailView.as_view(), name='monument_detail'),
    path('areas/<slug:slug>', views.AreaDetailView.as_view(), name='area_detail'),
    path('trench/<slug:slug>', views.TrenchDetailView.as_view(), name='trench_detail'),
    path('buildings/<slug:slug>', views.BuildingDetailView.as_view(), name='building_detail'),
    path('findings/<slug:slug>', views.FindingDetailView.as_view(), name='finding_detail'),
    path('finds/<slug:slug>', views.FindDetailView.as_view(), name='find_detail'),
]
