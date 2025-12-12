import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'securebank.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# 🔐 TEMP: auto-create superuser on Render (Free plan workaround)
if os.environ.get("CREATE_SUPERUSER") == "True":
    from django.contrib.auth import get_user_model
    User = get_user_model()

    try:
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
            print("✅ Superuser created")
    except Exception as e:
        print("❌ Superuser creation failed:", e)
