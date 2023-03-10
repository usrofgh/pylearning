from models import LiteraryFormat
from managers import LiteraryFormatManager

if __name__ == '__main__':
    # даєемо LF атрібут менеджер для праці з БД
    LiteraryFormat.objects = LiteraryFormatManager()
    LiteraryFormat.objects.create("triller")
    LiteraryFormat.objects.all()
