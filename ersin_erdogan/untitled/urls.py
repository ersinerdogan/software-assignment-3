from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from bloggg.views import show_blog, get_blog
from todo.views import show_todo, get_todo
from users.views import signup
from tags.views import show_tag
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/entries/$', show_blog),
    url(r'^blog/entries/(?P<entry_id>[0-9]+)', get_blog),
    url(r'^todo$', show_todo),
    url(r'^accounts/profile/$', show_blog),
    url(r'^todo/(?P<todo_id>[0-9]+)', get_todo),
    url(r'^register/$', signup),
    url(r'users/', include("django.contrib.auth.urls")),
    url(r'^$', show_tag),

]

