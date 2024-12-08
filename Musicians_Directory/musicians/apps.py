from django.apps import AppConfig

class MusicianConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'musicians'  # Ensure this matches the folder name
