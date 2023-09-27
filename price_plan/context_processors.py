from .models import PaymentGateWaySettings
from django.contrib.auth.models import AnonymousUser
 
def payment_info(request):
    try:
        # payment_info = request.session.get('payment_plan', None)
        payment_info = request.COOKIES.get('payment_plan', None)
        print(payment_info)
    except:
        payment_info = None
    return {'payment_info': payment_info}