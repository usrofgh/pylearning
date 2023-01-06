from models import LiteraryFormat
from managers import LiteraryFormatManager

if __name__ == '__main__':
    # создание менеджера для LFormat для работы с БД
    LiteraryFormat.manager = LiteraryFormatManager()
    print(LiteraryFormat.manager.all())
