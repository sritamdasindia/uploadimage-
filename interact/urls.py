from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from interactive import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url(r'^$',views.login,name="login"),
    url(r'^signup$',views.signup,name="signup"),
    url(r'^error$',views.error,name="error"),
    url(r'^dashboard',views.dashboard,name="dashboard")


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
