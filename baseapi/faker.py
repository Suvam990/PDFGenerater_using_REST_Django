from .models import *
from faker import Faker
fake = Faker()
import random


def generate_fake_data(num_records=10):
    [Student.objects.create(
        name=fake.name(),
        age=random.randint(18, 30),
        phone=fake.phone_number(),
        email=fake.email(),
    ) for i in range(num_records)]
    return Student.objects.all() 