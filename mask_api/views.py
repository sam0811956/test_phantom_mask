from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mask_api.models import PharMacies, Mask, OpeningHour
from django.core import serializers


@api_view(['GET'])
def index(request):
    return Response({"message": "Hello world"})


@api_view(['GET'])
def find_pharm_op_weekday_hour(request):
    '''
    {
        'weekday':'Mon',
        'hour': '10',
        'min' : '10'
    }
    '''
    req_weekday = request.query_params.get('weekday')
    req_hour = request.query_params.get('hour')
    req_min = request.query_params.get('min')
    # Mon (10:6 - 14:26)
    # Mon (4:8 - 20:52)
    open_weekday_hour = \
            OpeningHour.objects \
            .filter(week_day = req_weekday) \
            .filter(start_hour__lte=req_hour, start_min__lte=req_min) \
            .filter(end_hour__gte=req_hour, end_min__gte=req_min)
    # get open id, [57,61] 
    open_weekday_hour_list_id = list(map(lambda open: open.id, open_weekday_hour))
    # Pharmacies.filter(weekday).filter(hour_min)
    pharmacies_op_name = list(map(lambda open_id: PharMacies.objects.get(openinghour__id=open_id).name, open_weekday_hour_list_id))
   
    return Response({ 
            "open_pharmacies": pharmacies_op_name,
            "request_data": request.query_params
            })

    
@api_view(['GET'])
def find_pharm_sold_mask_sort(request):
    req_pharm_name = request.query_params.get('pharm')
    req_sort = request.query_params.get('sort')
    """
    {
      "pharm":"Cash Saver Pharmacy",
      "sort": "name"
    }
    """
    """ 
    {
      "pharm":"Cash Saver Pharmacy",
      "sort": "price"
    }

    """
    mask_sort = list(map(lambda mask: str(mask), \
                Mask.objects.filter(pharmacies__name=req_pharm_name) \
                .order_by(req_sort))
                )

    return Response({ 
            "mask_sort": mask_sort,
            "request_data": request.query_params
            })
    

