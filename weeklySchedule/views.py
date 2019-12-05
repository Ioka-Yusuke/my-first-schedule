from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import TimeTable

#ページ表示
def timetable_list(request):
    timetables = TimeTable.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'weeklySchedule/timetable_list.html', {'timetables': timetables})

#ページ表示
def results(request, pk):
    timetables = TimeTable.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'weeklySchedule/timetable_list.html', {'timetables': timetables})

#出欠確認
def mon1_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_1st_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_1st_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def mon2_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_2nd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_2nd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def mon3_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_3rd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_3rd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def mon4_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_4th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_4th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def mon5_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_5th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.mon_5th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def tue1_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_1st_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_1st_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def tue2_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_2nd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_2nd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def tue3_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_3rd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_3rd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def tue4_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_4th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_4th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def tue5_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_5th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.tue_5th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def wed1_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_1st_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_1st_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def wed2_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_2nd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_2nd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def wed3_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_3rd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_3rd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def wed4_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_4th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_4th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def wed5_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_5th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.wed_5th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def thu1_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_1st_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_1st_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def thu2_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_2nd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_2nd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def thu3_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_3rd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_3rd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def thu4_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_4th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_4th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def thu5_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_5th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.thu_5th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def fri1_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_1st_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_1st_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def fri2_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_2nd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_2nd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def fri3_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_3rd_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_3rd_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def fri4_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_4th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_4th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

def fri5_form(request, pk):
    if 'button1' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_5th_attend += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))

    elif 'button2' in request.POST:
        timetable = get_object_or_404(TimeTable, pk=pk)
        timetable.fri_5th_abesen += 1
        timetable.save()

        return HttpResponseRedirect(reverse('results', args=(pk,)))
