from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
    
    path('timetable/<int:pk>/mon1_form/', views.mon1_form, name='mon1_form'),
    path('timetable/<int:pk>/mon2_form/', views.mon2_form, name='mon2_form'),
    path('timetable/<int:pk>/mon3_form/', views.mon3_form, name='mon3_form'),
    path('timetable/<int:pk>/mon4_form/', views.mon4_form, name='mon4_form'),
    path('timetable/<int:pk>/mon5_form/', views.mon5_form, name='mon5_form'),

    path('timetable/<int:pk>/tue1_form/', views.tue1_form, name='tue1_form'),
    path('timetable/<int:pk>/tue2_form/', views.tue2_form, name='tue2_form'),
    path('timetable/<int:pk>/tue3_form/', views.tue3_form, name='tue3_form'),
    path('timetable/<int:pk>/tue4_form/', views.tue4_form, name='tue4_form'),
    path('timetable/<int:pk>/tue5_form/', views.tue5_form, name='tue5_form'),

    path('timetable/<int:pk>/wed1_form/', views.wed1_form, name='wed1_form'),
    path('timetable/<int:pk>/wed2_form/', views.wed2_form, name='wed2_form'),
    path('timetable/<int:pk>/wed3_form/', views.wed3_form, name='wed3_form'),
    path('timetable/<int:pk>/wed4_form/', views.wed4_form, name='wed4_form'),
    path('timetable/<int:pk>/wed5_form/', views.wed5_form, name='wed5_form'),

    path('timetable/<int:pk>/thu1_form/', views.thu1_form, name='thu1_form'),
    path('timetable/<int:pk>/thu2_form/', views.thu2_form, name='thu2_form'),
    path('timetable/<int:pk>/thu3_form/', views.thu3_form, name='thu3_form'),
    path('timetable/<int:pk>/thu4_form/', views.thu4_form, name='thu4_form'),
    path('timetable/<int:pk>/thu5_form/', views.thu5_form, name='thu5_form'),

    path('timetable/<int:pk>/fri1_form/', views.fri1_form, name='fri1_form'),
    path('timetable/<int:pk>/fri2_form/', views.fri2_form, name='fri2_form'),
    path('timetable/<int:pk>/fri3_form/', views.fri3_form, name='fri3_form'),
    path('timetable/<int:pk>/fri4_form/', views.fri4_form, name='fri4_form'),
    path('timetable/<int:pk>/fri5_form/', views.fri5_form, name='fri5_form'),
    
    path('timetable/<int:pk>/results/', views.results, name='results'),
]
