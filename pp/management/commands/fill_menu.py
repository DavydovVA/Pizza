from django.core.management import BaseCommand
import os
from random import choice
from pp.models import Pizza


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            help='path to Directory with images',
            dest='directory',
        )
        parser.add_argument(
            '-rus',
            help='set \'True\' if filenames contain Russian',
            dest='rus',
        )

    def handle(self, directory, rus=False, *args, **options):
        if os.path.exists(directory):
            files = [os.path.join(directory, d) for d in os.listdir(directory) if
                     os.path.isfile(os.path.join(directory, d))]

            if not Pizza.objects.all():
                for f in files:
                    obj = Pizza(title=f'{os.path.basename(f)[:-4]}'.capitalize().replace('_', ' '),
                                body='"Pizza Description"', price=choice(['10.0', '9.99', '5.55', '12.50']))
                    obj.image.save(f'{os.path.basename(f)}', open(f, 'rb'))
                    if rus == 'True':
                        try:
                            obj.custom_save()
                        except:
                            # ???
                            self.stderr.write(
                                self.style.ERROR(
                                    f'Name \'{os.path.basename(f)}\' contains only roman letters. Using regular save()')
                            )
                            obj.save()
                    else:
                        obj.save()
            else:
                self.stderr.write(
                    self.style.ERROR(f'Menu is already filled.')
                )
                return

            self.stdout.write(
                self.style.SUCCESS(f'Pizza list was filled successfully.')
            )
        else:
            self.stderr.write(
                self.style.ERROR(f'Directory path "{directory}" not found.')
            )

            return
