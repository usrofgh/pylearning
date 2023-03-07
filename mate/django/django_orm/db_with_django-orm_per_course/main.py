import init_django_orm  # noqa: F401

from db.models import LiteraryFormat


def main():
    LiteraryFormat.objects.filter().delete()
    print(LiteraryFormat.objects.all())  # <QuerySet [<LiteraryFormat: LiteraryFormat object (1)>]>
    print(LiteraryFormat.objects.create(
        format="drama",
    ))  # LiteraryFormat object (2)

    new_format = LiteraryFormat.objects.create(
        format="poem"
    )
    print(new_format.format)  # poem
    print(LiteraryFormat.objects.get(format="poem").format)  # poem
    filtered_formats = LiteraryFormat.objects.filter(format="poem")
    print(filtered_formats)  # <QuerySet [<LiteraryFormat: LiteraryFormat object (10)>]>


if __name__ == '__main__':
    main()
