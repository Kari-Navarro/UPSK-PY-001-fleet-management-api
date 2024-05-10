#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Taxis, Trajectories

# Create your views here.


def taxi_list(request):
    list_taxis = Taxis.objects.all().order_by('id')#orderby necesario para la clase Paginator
    page_size = 15
    paginator = Paginator(list_taxis, page_size)#clase 
    page_number = request.GET.get('page')#metodo para acceder y recuperar los parametros de consulta en la URL ?page=8
    page_obj = paginator.get_page(page_number)#metodo que retorna un objeto Page. Si es negativo o mas grande que el numero total de paginas retorna la ultima pagina
    data_taxis = list(page_obj.object_list.values())
    return JsonResponse({
        'taxis': data_taxis,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'next': page_obj.has_next(),#booleano
        'previous': page_obj.has_previous(),
    })

def trajectories_list(request):
    list_trajectories = Trajectories.objects.all().order_by('taxi_id')
    page_size = 15
    paginator = Paginator(list_trajectories, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data_trajectories = list(page_obj.object_list.values())
    return JsonResponse({
        'trajectories': data_trajectories,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'next': page_obj.has_next(),
        'previous': page_obj.has_previous(),
    })

def trajectories_ID(request):
    taxi_id = request.GET.get('taxi_id')
    #if not taxi_id:
    #    return JsonResponse({'Error':'Proporiciona el ID del taxi'}, status=400)#mala solicitud del cliente
    trajectoriesid= Trajectories.objects.filter(taxi_id=taxi_id).order_by('taxi_id')
    page_size = 15
    paginator = Paginator(trajectoriesid, page_size)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data_trajectories_id = list(page_obj.object_list.values())
    return JsonResponse({
        'trajectories by ID': data_trajectories_id,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'next': page_obj.has_next(),
        'previous': page_obj.has_previous(),
    })










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





####################################################

#class ListTaxis(View):
#    page_size = 5
#    def get(self, request):
        #get..
#        taxilist = Taxis.objects.all()
#        paginator = Paginator(taxilist, self.page_size)
#        page_number = request.GET.get('page',1)
#        try:
#            page = paginator.page(page_number)
#        except EmptyPage:
#            return HttpResponseBadRequest("ERROR: PÁGINA SOLICITADA INCORRECTA")
#        return JsonResponse(list(page.object_list.values()), safe=False)

#class ListTrajectories(View):
#    page_size = 5
#    def get(self, request):
        #get
#        trajelist=Trajectories.objects.all()#.order_by('id')#[:5]
#        paginator = Paginator(trajelist, self.page_size)
#        page_number = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_number)
#        except EmptyPage:
#            return HttpResponseBadRequest("ERROR: PÁGINA SOLICITADA INCORRECTA")
#        return JsonResponse(list(page.object_list.values()), safe=False)
#class ListTrajectoriesByID(View):
#    '''obtener taxis por id'''
#    page_size = 5 
#    def get(self, request):
#        '''filtrar por id del taxi'''
#        taxi_id = request.GET.get('taxi_id')
#        if not taxi_id:
#            return JsonResponse({'Error': 'Por favor, proporciona el ID del taxi'}, status=400)
#    
#        trajectoriesid = Trajectories.objects.filter(taxi_id=taxi_id)
#        paginator = Paginator(trajectoriesid, self.page_size)
#        page_number = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_number)
#        except EmptyPage:
#            page = []
            # no hay parámetro de taxi_id lanza error
#        return JsonResponse(list(page.object_list.values()), safe=False)