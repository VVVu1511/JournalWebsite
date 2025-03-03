from django.urls import include,path


app_name = 'users'
url_pattern = [
    path('',include('django.contrib.auth.urls'))
]