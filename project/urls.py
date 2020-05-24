from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from welcome.robot_control import get_state, set_state

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get_state$', get_state),
    url(r'^set_state$', set_state),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
