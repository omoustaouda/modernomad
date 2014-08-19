from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
import registration.backends.default.urls
from core.views import Registration
from django.conf import settings
import core.forms

# Add the user registration and account management patters from the
# django-registration package, overriding the initial registration
# view to collect our additional user profile information.
urlpatterns = patterns('',
	url(r'^register/$', Registration.as_view(form_class = core.forms.UserProfileForm), name='registration_register'),
)
urlpatterns += registration.backends.default.urls.urlpatterns

urlpatterns += patterns('core.views',
	url(r'^$', 'ListUsers', name='user_list'),
	url(r'^daterange/$', 'PeopleDaterangeQuery', name='people_daterange'),
	url(r'^(?P<username>(?!logout)(?!login)(?!register)[\w\d\-\.@+_]+)/$', 'GetUser', name='user_detail'),
	url(r'^(?P<username>[\w\d\-\.@+_]+)/edit/$', 'UserEdit', name='user_edit'),
	url(r'^(?P<username>[\w\d\-\.@+_]+)/addcard/$', 'UserAddCard', name='user_add_card'),
	url(r'^(?P<username>[\w\d\-\.@+_]+)/deletecard/$', 'UserDeleteCard', name='user_delete_card'),
)

urlpatterns += patterns('',
	url(r'^password/reset/$', password_reset, name="password_reset"),
	url(r'^password/done/$', password_reset_done, name="password_reset_done"),
	url(r'^password/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
	url(r'^password/complete/$', password_reset_complete, name="password_reset_complete"),
)

# XXX can this be extracted and put into the gather app?
urlpatterns += url(r'^(?P<username>[\w\d\-\.@+_]+)/events/$', 'gather.views.user_events', name='user_events'),


