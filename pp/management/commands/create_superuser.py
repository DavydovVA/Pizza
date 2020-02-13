from accounts.models import User
from django.core.management import BaseCommand

from custom_settings import su_email, su_first_name, su_last_name, su_password


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email=su_email).exists():
            User.objects.create_superuser(su_email, su_first_name, su_last_name, su_password)
            self.stdout.write(
                self.style.SUCCESS('Superuser created.')
            )
        else:
            self.stderr.write(
                self.style.ERROR('Superuser already exists.')
            )

