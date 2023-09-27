from .models import RegisterInfoModel
from django.contrib.auth.models import AnonymousUser
 
def register_info(request):
    if not isinstance(request.user, AnonymousUser):
        try:
            register_info = RegisterInfoModel.objects.get(user=request.user)
        except RegisterInfoModel.DoesNotExist:
            register_info = None
        return {'register_info': register_info}
    else:
        return {'register_info': None}