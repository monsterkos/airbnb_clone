from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command creates facilities"

    """  
    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times do you want to test?")
    """

    def handle(self, *args, **options):
        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.SUCCESS("test"))  # SUCCESS WARNING ERROR
        facilities = [
            "Private entrance",
            "Paid parking on Premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
