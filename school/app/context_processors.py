from core.models import Site, Organisation

def organisation(request):
    site = Site.objects.all().first()
    organisation = Organisation.objects.all().first()

    return {'site': site, 'organisation': organisation}
