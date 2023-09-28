from .models import PaymentGateWaySettings
from price_plan.models import PricePlanModel
 
def payment_info(request):
    try:
        payment_info = PricePlanModel.objects.get(user = request.user)
    except:
        payment_info = None
    return {'payment_info': payment_info}