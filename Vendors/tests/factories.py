
import factory
from django.contrib.auth.models import User
from Vendors.models import Vendor
from faker import Factory

faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.LazyAttribute(lambda _: faker.user_name())
    email = factory.LazyAttribute(lambda _: faker.email())
    password = factory.LazyAttribute(lambda _: faker.password())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        password = kwargs.pop("password", None)
        obj = super(UserFactory, cls)._create(model_class, *args, **kwargs)
        # Ensure the raw password gets set after the initial save
        obj.set_password(password)
        obj.save()
        return obj

class VendorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vendor

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('pystr', min_chars=10, max_chars=10)
    contact_details = factory.Faker('random_number', digits=10)
    address = factory.Faker('pystr', min_chars=20, max_chars=50)
    vendor_code = factory.Faker('random_number', digits=10)
    on_time_delivery_rate = factory.Faker('pyfloat', positive=True)
    quality_rating_avg = factory.Faker('pyfloat', positive=True)
    average_response_time = factory.Faker('pyfloat', positive=True)
    fulfillment_rate = factory.Faker('pyfloat', positive=True)


    # user = factory.SubFactory(UserFactory)
    # name = factory.LazyAttribute(lambda _: faker.pystr(min_chars=10, max_chars=10))
    # contact_details = factory.LazyAttribute(lambda _: faker.random_number(10))
    # address = factory.LazyAttribute(lambda _: faker.pystr(min_chars=20, max_chars=50))
    # vendor_code = factory.LazyAttribute(lambda _: faker.random_number(10))
    # on_time_delivery_rate = factory.Faker('pyfloat', positive=True)
    # quality_rating_avg = factory.Faker('pyfloat', positive=True)
    # average_response_time = factory.Faker('pyfloat', positive=True)
    # fulfillment_rate = factory.Faker('pyfloat', positive=True)





