from core.models import Site, Menu

def site(request):
    site = Site.objects.all().first()

    top_menu = Menu.objects.top()
    footer_menu = Menu.objects.footer()

    return {'site': site, 'top_menu': top_menu, 'footer_menu': footer_menu}
