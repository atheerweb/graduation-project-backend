from django.contrib.auth.models import User

user = User.objects.create_superuser("admin", "admin@example.com", "admin")

user.save()
