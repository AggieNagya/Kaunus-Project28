from django.test import SimpleTestCase
from django.urls import reverse, resolve
from excavation.views import *

"""
 - The test case for url first checks the url based on name provided
 - For example, url = reverse('index') checks for url based on name = 'index'
 - The reverse function returns the url, for above would be /excavation/index/
 - The resolve function takes in the url and returns a tuple list, one of the list 
 - members is the function name run when the path /excavation/index/ is choosen by the 
 - user
 - This function is compared against the function name located in the view.py in this case index()
 - The two functions are compared against each other to make sure they match

"""


class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, IndexListView)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func.view_class, AboutListView)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactListView)

    def test_topography_url_resolves(self):
        url = reverse('topography')
        self.assertEquals(resolve(url).func.view_class, TopographyListView)

    def test_history_url_resolves(self):
        url = reverse('history')
        self.assertEquals(resolve(url).func.view_class, HistoryListView)

    def test_monuments_url_resolves(self):
        url = reverse('monuments')
        self.assertEquals(resolve(url).func.view_class, MonumentsListView)

    def test_finds_url_resolves(self):
        url = reverse('finds')
        self.assertEquals(resolve(url).func.view_class, FindListView)

    def test_findings_url_resolves(self):
        url = reverse('findings')
        self.assertEquals(resolve(url).func.view_class, FindingListView)

    def test_buildings_url_resolves(self):
        url = reverse('buildings')
        self.assertEquals(resolve(url).func.view_class, BuildingListView)

    def test_trenches_url_resolves(self):
        url = reverse('trenches')
        self.assertEquals(resolve(url).func.view_class, TrenchListView)

    def test_areas_url_resolves(self):
        url = reverse('areas')
        self.assertEquals(resolve(url).func.view_class, AreaListView)

    def test_monuments_detail_url_resolves(self):
        url = reverse('monument_detail', args=['slug_value'])
        self.assertEquals(resolve(url).func.view_class, MonumentsDetailView)

    def test_area_detail_url_resolves(self):
        url = reverse('area_detail', args=['slug_value'])
        self.assertEquals(resolve(url).func.view_class, AreaDetailView)

    def test_trench_detail_url_resolves(self):
        url = reverse('trench_detail', args=['slug_value'])
        self.assertEquals(resolve(url).func.view_class, TrenchDetailView)

    def test_building_detail_url_resolves(self):
        url = reverse('building_detail', args=['slug_value'])
        self.assertEquals(resolve(url).func.view_class, BuildingDetailView)

    def test_finding_detail_url_resolves(self):
        url = reverse('finding_detail', args=['slug_value'])
        self.assertEquals(resolve(url).func.view_class, FindingDetailView)

    def test_find_detail_url_resolves(self):
        url = reverse('find_detail', args=['slug_value'])
        self.assertEquals(resolve(url).func.view_class, FindDetailView)
