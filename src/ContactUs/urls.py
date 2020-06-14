from django.urls import path
from ContactUs.views import contact_us


app_name = 'ContactUs'

urlpatterns = [
    path('ContactUs/', contact_us, name="ContactUs"),
    path('', contact_us, name="contact_us"),
