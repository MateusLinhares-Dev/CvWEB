from django.contrib import admin
from .models import Profile, Experience, Project, Testemunho, Skill, Contact
from django.contrib import messages
from django.utils.translation import ngettext

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["title", "company", "description"]
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["start", "current_work","end"]
            },
        ),
    ]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "bio", "photo", "email"]
            },
        )
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["title", "description", "link"]
            },
        )
    ]

@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'confirm', 'date_create')
    list_filter = ('confirm', 'date_create')
    search_fields = ('name', 'message')
    actions = ['confirm_message']

    
    @admin.action(description="Marcar como selecionado o testemunho")
    def confirm_message(self, request, queryset):
        updated = queryset.update(confirm=True)
        self.message_user(
            request,
            ngettext(
                "%d Testemunha aprovada!",
                "%d Testemunha publicada com sucesso!",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'classification', 'points')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'phone_number')
    search_fields = ('name','phone_number')
    list_filter = ('name','phone_number')
    