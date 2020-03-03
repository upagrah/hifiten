from django.conf.urls import url
from .viewsf.register.register import register_view
from .viewsf.login.login import login_view,logout_view
# from .viewsf.register import (
#     login_view,
#     register_view,
#     logout_view,
# )

urlpatterns = [
    url(r"^login/$", login_view, name = "login"),
    url(r"^register/$", register_view, name = "register"),
    url(r'^logout/$', logout_view, name = "logout"),
]
