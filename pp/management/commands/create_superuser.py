from accounts.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email='volerej@gmail.com').exists():
            User.objects.create_superuser('volerej@gmail.com', 'Valery', 'Davydov', 'admin') #брать из конфига
        else:
            self.stderr.write(
                self.style.ERROR('Superuser already exists.')
            )

