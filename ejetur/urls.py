from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^persona/',include ('apps.persona.urls', namespace='persona'), name='persona_url'),
    url(r'^', include ('apps.loby.urls', )),
    url(r'^ingreso/', include('registration.backends.default.urls')),
]
