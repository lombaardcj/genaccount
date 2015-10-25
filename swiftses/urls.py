from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'swiftses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^genaccount/', include('genaccount.urls', namespace="genaccount")),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_title = 'Swiftses Administration'
admin.site.site_header = 'Swiftses administration'
