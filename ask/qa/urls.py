from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login/', views.login_user, name=login),
                       url(r'^signup/', views.signup, name='signup'),
                       url(r'^question/(?P<id>[^/]+)', views.one_quest),
                       url(r'^popular/', views.popular_quests),
                       url(r'^new/', views.test),
                       url(r'^ask/', views.ask_add),
                       url(r'^answer/', views.answer_add),
                       url(r'^logout/', views.logout_user),
                       )
