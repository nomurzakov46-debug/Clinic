from django.contrib import admin
from .models import Direction,Doctor,Promotion,Equipment,EquipmentFeature,Appointment,CallRequest
from pages.models import OmsRequest,Review


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name','position','direction','show_on_home',)
    list_filter = ('direction','show_on_home',)
    search_fields = ('full_name',)
    save_as =True

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title','end_date','is_big','order')
    list_editable = ('order',)

class EquipmentFeatureInline(admin.TabularInline):
    model = EquipmentFeature
    extra = 3

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    inlines = [EquipmentFeatureInline]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone','direction','created_at','is_processed','doctor')
    list_filter = ('doctor','direction')
    search_fields = ('full_name','phone')

@admin.register(CallRequest)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone','created_at','is_processed',)
    list_filter = ('is_processed',)



@admin.register(OmsRequest)
class OmsRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number','created_at','is_processed',)
    list_filter = ('is_processed',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author','rating','doctor','created_at','is_approved',)
    list_filter = ('is_approved',)