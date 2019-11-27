from django.contrib import admin
from .models import candidates

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','current_ctc','expected_ctc','notice_period']

admin.site.register(candidates, CandidateAdmin)
