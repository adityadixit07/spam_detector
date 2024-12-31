from users.models import User
from contacts.models import Contact
from faker import Faker
import random

def populate_db():
    fake = Faker()
    for _ in range(100):
        user = User.objects.create_user(
            username=fake.user_name(),
            phone_number=fake.phone_number(),
            email=fake.email(),
            password='password123'
        )

        for _ in range(random.randint(5, 15)):
            Contact.objects.create(
                user=user,
                name=fake.name(),
                phone_number=fake.phone_number(),
                is_spam=random.choice([True, False])
            )
