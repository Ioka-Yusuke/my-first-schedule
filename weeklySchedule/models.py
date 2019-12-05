from django.conf import settings
from django.db import models
from django.utils import timezone


class TimeTable(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    mon_1st        = models.CharField(max_length=200, null=True)
    mon_2nd        = models.CharField(max_length=200, null=True)
    mon_3rd        = models.CharField(max_length=200, null=True)
    mon_4th        = models.CharField(max_length=200, null=True)
    mon_5th        = models.CharField(max_length=200, null=True)
    
    tue_1st        = models.CharField(max_length=200, null=True)
    tue_2nd        = models.CharField(max_length=200, null=True)
    tue_3rd        = models.CharField(max_length=200, null=True)
    tue_4th        = models.CharField(max_length=200, null=True)
    tue_5th        = models.CharField(max_length=200, null=True)

    wed_1st        = models.CharField(max_length=200, null=True)
    wed_2nd        = models.CharField(max_length=200, null=True)
    wed_3rd        = models.CharField(max_length=200, null=True)
    wed_4th        = models.CharField(max_length=200, null=True)
    wed_5th        = models.CharField(max_length=200, null=True)

    thu_1st        = models.CharField(max_length=200, null=True)
    thu_2nd        = models.CharField(max_length=200, null=True)
    thu_3rd        = models.CharField(max_length=200, null=True)
    thu_4th        = models.CharField(max_length=200, null=True)
    thu_5th        = models.CharField(max_length=200, null=True)

    fri_1st        = models.CharField(max_length=200, null=True)
    fri_2nd        = models.CharField(max_length=200, null=True)
    fri_3rd        = models.CharField(max_length=200, null=True)
    fri_4th        = models.CharField(max_length=200, null=True)
    fri_5th        = models.CharField(max_length=200, null=True)
 
    mon_1st_name   = models.CharField(max_length=200, null=True)
    mon_2nd_name   = models.CharField(max_length=200, null=True)
    mon_3rd_name   = models.CharField(max_length=200, null=True)
    mon_4th_name   = models.CharField(max_length=200, null=True)
    mon_5th_name   = models.CharField(max_length=200, null=True)
    
    tue_1st_name   = models.CharField(max_length=200, null=True)
    tue_2nd_name   = models.CharField(max_length=200, null=True)
    tue_3rd_name   = models.CharField(max_length=200, null=True)
    tue_4th_name   = models.CharField(max_length=200, null=True)
    tue_5th_name   = models.CharField(max_length=200, null=True)

    wed_1st_name   = models.CharField(max_length=200, null=True)
    wed_2nd_name   = models.CharField(max_length=200, null=True)
    wed_3rd_name   = models.CharField(max_length=200, null=True)
    wed_4th_name   = models.CharField(max_length=200, null=True)
    wed_5th_name   = models.CharField(max_length=200, null=True)

    thu_1st_name   = models.CharField(max_length=200, null=True)
    thu_2nd_name   = models.CharField(max_length=200, null=True)
    thu_3rd_name   = models.CharField(max_length=200, null=True)
    thu_4th_name   = models.CharField(max_length=200, null=True)
    thu_5th_name   = models.CharField(max_length=200, null=True)

    fri_1st_name   = models.CharField(max_length=200, null=True)
    fri_2nd_name   = models.CharField(max_length=200, null=True)
    fri_3rd_name   = models.CharField(max_length=200, null=True)
    fri_4th_name   = models.CharField(max_length=200, null=True)
    fri_5th_name   = models.CharField(max_length=200, null=True)
 
    mon_1st_attend = models.IntegerField(default=0)
    mon_2nd_attend = models.IntegerField(default=0)
    mon_3rd_attend = models.IntegerField(default=0)
    mon_4th_attend = models.IntegerField(default=0)
    mon_5th_attend = models.IntegerField(default=0)
    
    tue_1st_attend = models.IntegerField(default=0)
    tue_2nd_attend = models.IntegerField(default=0)
    tue_3rd_attend = models.IntegerField(default=0)
    tue_4th_attend = models.IntegerField(default=0)
    tue_5th_attend = models.IntegerField(default=0)

    wed_1st_attend = models.IntegerField(default=0)
    wed_2nd_attend = models.IntegerField(default=0)
    wed_3rd_attend = models.IntegerField(default=0)
    wed_4th_attend = models.IntegerField(default=0)
    wed_5th_attend = models.IntegerField(default=0)

    thu_1st_attend = models.IntegerField(default=0) 
    thu_2nd_attend = models.IntegerField(default=0)
    thu_3rd_attend = models.IntegerField(default=0)
    thu_4th_attend = models.IntegerField(default=0)
    thu_5th_attend = models.IntegerField(default=0)

    fri_1st_attend = models.IntegerField(default=0)
    fri_2nd_attend = models.IntegerField(default=0)
    fri_3rd_attend = models.IntegerField(default=0)
    fri_4th_attend = models.IntegerField(default=0)
    fri_5th_attend = models.IntegerField(default=0)

    mon_1st_abesen = models.IntegerField(default=0)
    mon_2nd_abesen = models.IntegerField(default=0)
    mon_3rd_abesen = models.IntegerField(default=0)
    mon_4th_abesen = models.IntegerField(default=0)
    mon_5th_abesen = models.IntegerField(default=0)
    
    tue_1st_abesen = models.IntegerField(default=0)
    tue_2nd_abesen = models.IntegerField(default=0)
    tue_3rd_abesen = models.IntegerField(default=0)
    tue_4th_abesen = models.IntegerField(default=0)
    tue_5th_abesen = models.IntegerField(default=0)

    wed_1st_abesen = models.IntegerField(default=0)
    wed_2nd_abesen = models.IntegerField(default=0)
    wed_3rd_abesen = models.IntegerField(default=0)
    wed_4th_abesen = models.IntegerField(default=0)
    wed_5th_abesen = models.IntegerField(default=0)

    thu_1st_abesen = models.IntegerField(default=0)
    thu_2nd_abesen = models.IntegerField(default=0)
    thu_3rd_abesen = models.IntegerField(default=0)
    thu_4th_abesen = models.IntegerField(default=0)
    thu_5th_abesen = models.IntegerField(default=0)

    fri_1st_abesen = models.IntegerField(default=0)
    fri_2nd_abesen = models.IntegerField(default=0)
    fri_3rd_abesen = models.IntegerField(default=0)
    fri_4th_abesen = models.IntegerField(default=0)
    fri_5th_abesen = models.IntegerField(default=0)

  


    

    def publish(self):
        self.published_date = timezone.now()
        self.save()
