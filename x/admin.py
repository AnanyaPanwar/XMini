from django.contrib import admin

from .models import X


@admin.register(X)
class XAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "short_text",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "text",
        "user__username",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def short_text(self, obj):
        if len(obj.text) > 50:
            return f"{obj.text[:50]}..."

        return obj.text

    short_text.short_description = "Post"