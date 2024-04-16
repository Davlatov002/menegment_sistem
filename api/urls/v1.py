from django.urls import path, include

urlpatterns = [
    path('account/', include(('api.account.urls', 'apps.account'))),
    path('branch/', include(('api.branch.urls', 'apps.branch'))),
    path('group/', include(('api.group.urls', 'apps.group'))),
]