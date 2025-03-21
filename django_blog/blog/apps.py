from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    #ensure that signals are registered and connected
    def ready(self):
        import blog.signals
