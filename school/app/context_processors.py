from core.models import Organisation

def organisation(request):
    organisation = Organisation.objects.all().first()
    return {'organisation': organisation}
