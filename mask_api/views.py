from django.shortcuts import render
from django.db.models import Count, Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mask_api.models import PharMacies, Mask, OpeningHour, User, PurchaseHistory
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
    
@api_view(['GET'])
def find_pharm_num_mask_price_range(request):
    req_num = request.query_params.get('num')
    req_compare = request.query_params.get('compare')
    req_low_price = request.query_params.get('low_price')
    req_high_price = request.query_params.get('high_price')
    """
    {
        "low_price": 10
        "high_price": 30,
        "num": 2,
        "compare": more or less
    }
    """
    # List each pharm name and count number of mask
    pharm_num_of_mask = \
        PharMacies.objects.values('name') \
        .filter(mask__price__gte=int(req_low_price), mask__price__lte=int(req_high_price)) \
        .annotate(c=Count("mask")) \
    # compare 
    if req_compare == "more": 
        pharm_num_of_mask_count =pharm_num_of_mask.filter(c__gt=int(req_num))
    elif req_compare == "less": 
        pharm_num_of_mask_count =pharm_num_of_mask.filter(c__lt=int(req_num))

    pharm_name = list(map(lambda phar: phar['name'], pharm_num_of_mask_count))

    return Response({ 
            "num_of_mask_count_pharm_name": pharm_name,
            "request_data": request.query_params
            })


@api_view(['GET'])
def find_user_date_range_top_total_amount(request):
    req_low_day = request.query_params.get('low_day')
    req_high_day = request.query_params.get('high_day')
    req_num = request.query_params.get('num')
    """
    { 
        "low_day": 2021-01-27,
        "high_day": 2021-04-01,
        "num": 2
    }
    """
    # list masks transaction amount
    user_date_range_amount_total = \
        User.objects.values('name') \
        .filter(purchasehistory__trans_date__range=[req_low_day, req_high_day]) \
        .annotate(trans_amount_sum=Sum('purchasehistory__trans_amount'))

    # user_amount_limit_num
    user_total_amount_limit_num = \
        user_date_range_amount_total \
        .order_by('-trans_amount_sum')[:int(req_num)]

    return Response({ 
            "user_top_amount": [user['name'] for user in user_total_amount_limit_num],
            "request_data": request.query_params
            })


