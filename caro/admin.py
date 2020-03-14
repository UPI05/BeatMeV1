from django.contrib import admin
from caro.models import botInfo, alertDt
# Register your models here.
class manageBot(admin.ModelAdmin):
    list_display = ['id', 'win', 'lose', 'draw', 'elo']
    list_filter = ['elo']
class manageAlert(admin.ModelAdmin):
    list_display = ['id', 'status', 'text']
    list_filter = ['status']
admin.site.register(botInfo, manageBot);
admin.site.register(alertDt, manageAlert);