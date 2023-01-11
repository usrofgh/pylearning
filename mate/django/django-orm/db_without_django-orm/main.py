from models import LiteraryFormat
from managers import LiteraryFormatManager

if __name__ == '__main__':
    # Создание менеджера для LFormat для работы с БД (решение для избежания рекурсивного импорта)
    LiteraryFormat.objects = LiteraryFormatManager()
    print(LiteraryFormat.objects.all())

