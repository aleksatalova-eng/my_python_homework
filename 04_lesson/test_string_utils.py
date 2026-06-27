import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# ==========================================
# Тесты для метода capitalize
# ==========================================


# Позитивные сценарии
@pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        # Обычная строка в нижнем регистре
        ("SKYPRO", "Skypro"),
        # Строка в верхнем регистре (приводится к Skypro)
        ("123", "123"),
        # Числа как строка
        ("04 апреля 2023", "04 апреля 2023"),
        # Строка с пробелами и цифрами
        ("skypro university", "Skypro university"),
        # Несколько слов (капитализируется только первое)
    ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Негативные сценарии и граничные случаи
@pytest.mark.parametrize("input_str, expected", [
        ("", ""),                     # Пустая строка
        (" ", " "),                   # Строка из одного пробела
        ("   ", "   "),               # Строка из нескольких пробелов
    ])
def test_capitalize_edge_cases(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    # Проверка обработки невалидного типа данных (None)
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

# ==========================================
# Тесты для метода trim
# ==========================================


# Позитивные сценарии
@pytest.mark.parametrize("input_str, expected", [
        (" skypro", "skypro"),
        # Один пробел в начале
        ("   skypro", "skypro"),
        # Несколько пробелов в начале
        ("skypro ", "skypro "),
        # Пробел только в конце (не должен удаляться)
        (" skypro ", "skypro "),
        # Пробелы и в начале, и в конце (удаляются только в начале)
        (" 123", "123"),
        # Числа как строка с пробелом
        (" 04 апреля 2023", "04 апреля 2023"),
        # Строка с пробелами
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Негативные сценарии и граничные случаи
@pytest.mark.parametrize("input_str, expected", [
        ("", ""),                     # Пустая строка
    ])
def test_trim_edge_cases(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_none():
    # Проверка обработки невалидного типа данных (None)
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА contains
# =====================================================================

@pytest.mark.parametrize("string, symbol, expected", [
    # Позитивные сценарии
    ("SkyPro", "S", True),               # Буква в начале (из примера)
    ("SkyPro", "o", True),               # Буква в конце
    ("123", "2", True),                  # Числа как строка
    ("04 апреля 2023", "апреля", True),  # Строка со словами и пробелами
    ("   ", " ", True),                  # Поиск пробела в строке с пробелами

    # Негативные сценарии
    ("SkyPro", "U", False),              # Отсутствующий символ (из примера)
    ("SkyPro", "s", False),              # Чувствительность к регистру (S != s)
    ("", "S", False),                    # Пустая строка (граничное значение)
])
def test_contains(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol", [
    (None, "S"),       # Передача None вместо строки
    ("SkyPro", None),  # Передача None вместо символа
])
def test_contains_negative_none(string, symbol):
    # Метод упадет с AttributeError или TypeError при None,
    # проверяем это поведение
    with pytest.raises((AttributeError, TypeError)):
        string_utils.contains(string, symbol)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА delete_symbol
# =====================================================================

@pytest.mark.parametrize("string, symbol, expected", [
    # Позитивные сценарии
    ("SkyPro", "k", "SyPro"),
    # Удаление одного символа (из примера)
    ("SkyPro", "Pro", "Sky"),
    # Удаление подстроки (из примера)
    ("SkyProSkyPro", "Sky", "ProPro"),
    # Удаление всех вхождений подстроки
    ("123", "2", "13"),
    # Числа как строка
    ("04 апреля 2023", " 2023", "04 апреля"),
    # Строка с пробелами

    # Негативные сценарии (строка не должна измениться)
    ("SkyPro", "U", "SkyPro"),
    # Удаление отсутствующего символа
    ("SkyPro", "s", "SkyPro"),
    # Чувствительность к регистру
    ("", "k", ""),
    # Пустая строка
    ("   ", " ", ""),
    # Удаление пробелов из строки пробелов
])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol", [
    (None, "k"),
    ("SkyPro", None)
])
def test_delete_symbol_negative_none(string, symbol):
    # Проверяем корректную обработку None (ожидаем исключение)
    with pytest.raises((AttributeError, TypeError)):
        string_utils.delete_symbol(string, symbol)
