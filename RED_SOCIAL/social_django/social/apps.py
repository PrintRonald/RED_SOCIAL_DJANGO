from django.apps import AppConfig


class SocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social'
    # modificamos esta parte para la señal que nos crea el perfil de usuario
    def ready(self):
        import social.signals
