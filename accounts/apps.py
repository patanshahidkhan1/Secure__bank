from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.contrib.auth import get_user_model
        import os

        def create_admin(sender, **kwargs):
            if os.environ.get("CREATE_SUPERUSER") == "True":
                User = get_user_model()
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        email="admin@example.com",
                        password="admin123"
                    )

        post_migrate.connect(create_admin, sender=self)
