import init_django_orm  # noqa F401
from db.models import Caffe, Place


def main():
    place = Place.objects.create(
        address="136. The Ramblass",
        post_index="123456",
    )

    caffe1 = Caffe.objects.create(
        name="Best ever caffe",
        place=place
    )

    print(Caffe.objects.all())


if __name__ == '__main__':
    main()
