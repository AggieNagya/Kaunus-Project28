from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from excavation.models import *
pagination_value = 6


class IndexListView(generic.ListView):
    model = HomePage

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = HomePage.objects.filter(Q(name__icontains=query))
        else:
            object_list = HomePage.objects.all()
        return object_list


class AboutListView(generic.ListView):
    model = About

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = About.objects.filter(Q(name__icontains=query))
        else:
            object_list = About.objects.all()
        return object_list


class ContactListView(generic.ListView):
    model = Contact

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Contact.objects.filter(Q(name__icontains=query))
        else:
            object_list = Contact.objects.all()
        return object_list


class TopographyListView(generic.ListView):
    model = Topography

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Topography.objects.filter(Q(name__icontains=query))
        else:
            object_list = Topography.objects.all()
        return object_list


class HistoryListView(generic.ListView):
    model = History

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = History.objects.filter(Q(name__icontains=query))
        else:
            object_list = History.objects.all()
        return object_list


class MonumentsListView(generic.ListView):
    model = Monument

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Monument.objects.filter(Q(name__icontains=query))
        else:
            object_list = Monument.objects.all()
        return object_list

    '''
    If you want to pass any variables to the ListView class
    override the get_content data method and add the variables to the 
    method and return the variables.
    The variable are then accessible in the templates.
    '''

    def get_context_data(self, **kwargs):
        ctx = super(MonumentsListView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword')
        return ctx


class MonumentsDetailView(generic.DetailView):
    model = Monument


"""
    This class will be used for the searches of the ListView
    The search criteria is identical for most class and if we 
    need to change a search criteria we can add a method here 
    and reuse the class instead of creating functions for each 
    Model search
    
    The class PostManager inherits from Manager which does the querying
    of the database
    get_queryset() - This is the method that does the querying and
    return a Query set object - assigned q 
    query - This is our search item
    Q - allows to perform complicated searches or more than one item search
    distint  - this avoids duplication of returned data
"""

"""
    ListView return a query set from def get_queryset(self) function
"""


class FindListView(PermissionRequiredMixin, generic.ListView):
    model = Find
    permission_required = 'excavation.view_find'
    paginate_by = pagination_value

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Find.objects.filter(Q(name__icontains=query))
        else:
            object_list = Find.objects.all()
        return object_list

    '''
    If you want to pass any variables to the ListView class
    override the get_content data method and add the variables to the 
    method and return the variables.
    The variable are then accessible in the templates.
    '''

    def get_context_data(self, **kwargs):
        ctx = super(FindListView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword')
        return ctx


class FindDetailView(generic.DetailView):
    model = Find


class FindingListView(PermissionRequiredMixin, generic.ListView):
    model = Finding
    permission_required = 'excavation.view_finding'
    paginate_by = pagination_value

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Finding.objects.filter(Q(name__icontains=query))
        else:
            object_list = Finding.objects.all()
        return object_list

    '''
    If you want to pass any variables to the ListView class
    override the get_content data method and add the variables to the 
    method and return the variables.
    The variable are then accessible in the templates.
    '''

    def get_context_data(self, **kwargs):
        ctx = super(FindingListView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword')
        return ctx


class FindingDetailView(generic.DetailView):
    model = Finding


class BuildingListView(PermissionRequiredMixin, generic.ListView):
    model = Building
    permission_required = 'excavation.view_building'
    paginate_by = pagination_value

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Building.objects.filter(Q(name__icontains=query))
        else:
            object_list = Building.objects.all()
        return object_list

    '''
    If you want to pass any variables to the ListView class
    override the get_content data method and add the variables to the 
    method and return the variables.
    The variable are then accessible in the templates.
    '''

    def get_context_data(self, **kwargs):
        ctx = super(BuildingListView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword')
        return ctx


class BuildingDetailView(generic.DetailView):
    model = Building


class TrenchListView(PermissionRequiredMixin, generic.ListView):
    model = Trench
    permission_required = 'excavation.view_trench'
    paginate_by = pagination_value

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Trench.objects.filter(Q(name__icontains=query))
        else:
            object_list = Trench.objects.all()
        return object_list

    '''
    If you want to pass any variables to the ListView class
    override the get_content data method and add the variables to the 
    method and return the variables.
    The variable are then accessible in the templates.
    '''

    def get_context_data(self, **kwargs):
        ctx = super(TrenchListView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword')
        return ctx


class TrenchDetailView(generic.DetailView):
    model = Trench


class AreaListView(PermissionRequiredMixin, generic.ListView):
    model = Area
    permission_required = 'excavation.view_area'
    paginate_by = pagination_value

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = Area.objects.filter(Q(name__icontains=query))
        else:
            object_list = Area.objects.all()
        return object_list

    '''
    If you want to pass any variables to the ListView class
    override the get_content data method and add the variables to the 
    method and return the variables.
    The variable are then accessible in the templates.
    '''

    def get_context_data(self, **kwargs):
        ctx = super(AreaListView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword')
        return ctx


class AreaDetailView(generic.DetailView):
    model = Area
