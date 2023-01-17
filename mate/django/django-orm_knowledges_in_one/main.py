import init_django_orm # noqa F401
from models import Movies, Persons


def main():
    Movies.objects.create(name="Treasure Island", release_date=1988)
    Movies.objects.create("Mr. Robot", 2015)

    Movies(name="American psycho", release_date=2000).save()
    Movies("Western World", 2016).save()

    Persons.objects.create(
        first_name="Doctor",
        last_name="Livesey",
        age=41,
        gender=1,
        character="good",
        additional_info="white side",
        movie=Movies.objects.get("Treasure Island"),
        youtube_link="https://www.youtube.com/watch?v=sG_mmj_h4t4&ab_channel=STEELAN",
    )

    Persons.objects.create(
        first_name="John",
        last_name="Silver",
        movie=Movies.objects.get("Treasure Island"),
        youtube_link="https://www.youtube.com/watch?v=eE30-a8sOJo&ab_channel=%F0%9D%90%8E%F0%9D%90%A6%F0%9D%90%A2%F0%9D%90%A2%F0%9D%90%A6%F0%9D%90%9A%F0%9D%90%9C%F0%9D%90%A2%F0%9D%90%AC%F0%9D%90%AD%E8%A9%B1%E4%BB%8A"
    )


if __name__ == '__main__':
    main()

