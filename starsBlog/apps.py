from django.apps import AppConfig


class StarsblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'starsBlog'
def ready(self):
        import starsBlog.signals  # استيراد ملف الإشارة