# importcategories.py
import csv

from django.core.management.base import BaseCommand, CommandError

from channels.models import Channel, Category


def read_csv_file(csv_file):
    """
    Read a csv file and return each line as a list

    :param csv_file: a string path of a csv file
    :return: generator in the form `['Books', 'Computers', 'Database']`
    """
    with open(csv_file) as f:
        heading = next(f) # get csv file heading
        for row in csv.reader(f, delimiter='/'):
            row = [e.strip() for e in row] # remove blank spaces from elements
            yield row # return a category row in list format


class Command(BaseCommand):
    help = 'Import channels\' categories from CSV file'

    def add_arguments(self, parser):
        # postitional arguments
        parser.add_argument('channel_name')
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        channel_name = options['channel_name']
        csv_file = options['csv_file']

        # try to get channel, if not exist, create it
        channel, created = Channel.objects.get_or_create(name=channel_name)
        if created:
            self.stdout.write('Created {} channel'.format(channel_name))

        for row in read_csv_file(csv_file):
            # if length is 1, there is only the root category
            # and no parent
            if len(row) == 1:
                category_name = row[0]
                parent = None

                category, created = Category.objects.update_or_create(
                    name=category_name, parent=parent, channel=channel)

                # root category, parent and the last parent category used are
                # all referenced to the category updated or created
                root, parent, last = category, category, category

            else:
                # the last index of the row is the category_name and
                # the penultimate index is the parent_name
                category_name = row[len(row) - 1]
                parent_name = row[len(row) - 2]

                # check if the parent_name is parent category
                if parent_name == parent.name:
                    # the last parent used was created in the last operation
                    last = parent

                    category, created = Category.objects.update_or_create(
                        name=category_name, parent=parent, channel=channel)

                    parent = category

                # or if the parent_name is last parent category used
                elif parent_name == last.name:
                    category, created = Category.objects.update_or_create(
                        name=category_name, parent=last, channel=channel)

                    parent = category

                # otherwise the parent will be the root category
                else:
                    last = root

                    category, created = Category.objects.update_or_create(
                        name=category_name, parent=root, channel=channel)

                    parent = category


            if created:
                self.stdout.write('Created {} category'.format(category.name))
            else:
                self.stdout.write('Updated {} category'.format(category.name))
