from .models import User
from django.conf import settings
from django.db.models import Q

def all_profiles(request):
    all_profiles = User.objects.all()#.exclude(Q(user=request.user.profile))#| Q(id=settings.ANONYMOUS_USER) )
    return {'all_profiles': all_profiles} # NOMBRE DEL OBJETO LLAMABLE DEBEN SER IGUALES