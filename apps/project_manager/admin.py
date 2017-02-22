from django.contrib import admin
from .models import Task, Plan, Competitor

class AdminPlan(admin.ModelAdmin):
	list_display = ('name', 'organizer')

class AdminTask(admin.ModelAdmin):
	list_display = ('user', 'plan', 'status')
	list_editable = ('status',)

class AdminCompetitor(admin.ModelAdmin):
	pass

admin.site.register(Task, AdminTask)
admin.site.register(Plan, AdminPlan)
admin.site.register(Competitor, AdminCompetitor)