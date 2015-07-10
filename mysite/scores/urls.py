from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #ex: /scores/
    url(r'^$', views.index, name='index'),
    # ex: /login/
    url(r'^login/$', views.login, name='login'),
    # ex: /user/name
    url(r'^user/$', views.user, name='user'),
    #url(r'^user/name:(?P<user_name>[0-9a-zA-Z_]+)password(?P<user_pwd>[0-9a-zA-Z_])/$', view.user, name='user')

    #url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/Users/Garfield/Web/mysite/media/'})
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
