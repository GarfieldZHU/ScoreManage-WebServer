from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #ex: /scores/
    url(r'^$', views.index, name='index'),
    # ex: /login/
    url(r'^login$', views.login, name='login'),
    # ex: /user/
    url(r'^student$', views.student, name='student'),
    # ex: /logout/
    url(r'^teacher$', views.teacher, name='teacher'),

    url(r'^manage$', views.manage, name='manage'),

    url(r'^logout$', views.logout, name='logout'),

    url(r'^password$', views.password, name='password'),

    url(r'^grade$', views.grade, name='grade'),

    url(r'^course$', views.course, name='course'),

    url(r'^human$', views.human, name='human'),

    #url(r'^user/name:(?P<user_name>[0-9a-zA-Z_]+)password(?P<user_pwd>[0-9a-zA-Z_])/$', view.user, name='user')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
