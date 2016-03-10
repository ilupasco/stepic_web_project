# ask URL Configuration
from django.conf.urls import url
from ask.qa import views

from django.conf.urls import url
try:
    from stepic_web.ask.qa import views
except ImportError:
    import sys
    sys.path.append("/home/box")
    from web.ask.qa import views


urlpatterns = (url("^$", views.get_questions, name="first_page", kwargs={"question_type": "new"}),
               url("^login/$",  views.test, name="login"),
               url("^signup/$",  views.test, name="signup"),
               url("^question/(?P<id>\d+)/$",  views.get_current_question, name="question"),
               url("^ask/",  views.ask_question, name="ask"),
               url("^popular/$",  views.get_questions, name="popular", kwargs={"question_type": "popular"}),
               url("^new/$",  views.get_questions, name="new", kwargs={"question_type": "new"}))

