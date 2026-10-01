from django.contrib import admin
from django.urls import path
from api.views import ask_gemini_ai

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/ask-ai/", ask_gemini_ai
    ),  # এই লিংকেই Flutter বা ওয়েবসাইট রিকোয়েস্ট পাঠাবে
]