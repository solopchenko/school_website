from core.models import Site

def site(request):
    site = Site.objects.all().first()
    return {'site': site}
