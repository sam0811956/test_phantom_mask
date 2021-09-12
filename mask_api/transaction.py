from mask_api.models import *
from datetime import datetime
from django.db import transaction
import logging

@transaction.atomic
def user_purchase(req_user, req_pharm, req_mask):
    _user = User.objects.get(name=req_user)
    _pharm = PharMacies.objects.get(name=req_pharm)
    _mask =Mask.objects.filter(name=req_mask).get(pharmacies__name=req_pharm)
    # user buy mask , if user have money,扣款 - cashbalance
    if(_user.cashbalance - _mask.price) < 0:
        raise ValueError("餘額不足")
    _user.save()
    _pharm.save()
    sid = transaction.savepoint()

    try:
        _user.cashbalance -= _mask.price
        _user.save()
        _pharm.cashbalance += _mask.price
        _pharm.save()
        User.objects.get(name=_user.name) \
                    .purchasehistory.create(
                            pharmacies_name = _pharm.name,
                            mask_name = _mask.name,
                            trans_amount = _mask.price,
                            trans_date = datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S")
                    )
        transaction.savepoint_commit(sid)
        return "Success"

    except ValueError as e:
        logging.error("%s",e)
        transaction.rollback()
    except:
        logging.error("Error")
        transaction.rollback()
