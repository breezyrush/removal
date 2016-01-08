from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^addpassengerA/$', 'app.views.addpassengerA', name='addpassengerA'),
    url(r'^addpassengerB/$', 'app.views.addpassengerB', name='addpassengerB'),     
    url(r'^add_success/$', 'app.views.success', name='success'),
    url(r'^home/$', 'app.views.home', name ='home'),
    url(r'^full/$', 'app/views.full', name='full')

)