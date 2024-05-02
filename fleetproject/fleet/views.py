#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage
from .models import Taxis, Trajectories

# Create your views here.

class ListTaxis(View):
    page_size = 5
    def get(self, request):
        #get..
        taxilist = Taxis.objects.all()
        paginator = Paginator(taxilist, self.page_size)
        page_number = request.GET.get('page',1)
        try:
            page = paginator.page(page_number)
        except EmptyPage:
            return HttpResponseBadRequest("ERROR: PÁGINA SOLICITADA INCORRECTA")
        return JsonResponse(list(page.object_list.values()), safe=False)

class ListTrajectories(View):
    page_size = 5
    def get(self, request):
        #get
        trajelist=Trajectories.objects.all()#.order_by('id')#[:5]
        paginator = Paginator(trajelist, self.page_size)
        page_number = request.GET.get('page', 1)
        try:
            page = paginator.page(page_number)
        except EmptyPage:
            return HttpResponseBadRequest("ERROR: PÁGINA SOLICITADA INCORRECTA")
        return JsonResponse(list(page.object_list.values()), safe=False)
      
class ListTrajectoriesByID(View):
    '''obtener taxis por id'''
    page_size = 5 
    def get(self, request):
        '''filtrar por id del taxi'''
        taxi_id = request.GET.get('taxi_id')

        if not taxi_id:
            return JsonResponse({'Error': 'Por favor, proporciona el ID del taxi'}, status=400)
        
        trajectoriesid = Trajectories.objects.filter(taxi_id=taxi_id)

        paginator = Paginator(trajectoriesid, self.page_size)

        page_number = request.GET.get('page', 1)

        try:
            page = paginator.page(page_number)

        except EmptyPage:
            page = []
            # Si no hay parámetro de taxi_id lanza error
        return JsonResponse(list(page.object_list.values()), safe=False)

class ListTrajectoriesPlate(View):
    '''se obtenddrán taxis por id y placa'''
    def get(self,request):
        '''filtrar por placa y id'''
        plate_taxi= request.GET.get('plate')
        if plate_taxi:
            platetaxi = Taxis.objects.filter(plate=plate_taxi)
            return JsonResponse(list(platetaxi.values()),safe = False)
        else:
            return JsonResponse({'error': 'Por favor, proporciona la placa del taxi'}, status=400)
