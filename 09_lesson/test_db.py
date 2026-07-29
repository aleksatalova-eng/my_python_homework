import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


@pytest.fixture(scope="session")
def db_engine():
    """Создает движок БД и таблицы один раз за сессию тестов."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)  # Удаляет таблицы после всех тестов


@pytest.fixture(scope="function")
def db_session(db_engine):
    """Предоставляет сессию и очищает данные после каждого теста."""
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()  # Откатывает любые изменения, сделанные в тесте
    connection.close()


# ТЕСТ 1: Добавление сущности
def test_add_student(db_session):
    new_student = Student(name="Иван Петров", age=20)
    db_session.add(new_student)
    db_session.commit()

    # Проверяем, что студент появился в БД
    saved_student = db_session.query(Student).filter_by(
        name="Иван Петров").first()
    assert saved_student is not None
    assert saved_student.age == 20


# ТЕСТ 2: Изменение сущности
def test_update_student(db_session):
    # Сначала создаем студента для модификации
    student = Student(name="Анна Сидорова", age=19)
    db_session.add(student)
    db_session.commit()

    # Изменяем данные
    student.age = 21
    db_session.commit()

    # Проверяем изменения
    updated_student = db_session.query(Student).filter_by(
        name="Анна Сидорова").first()
    assert updated_student.age == 21


# ТЕСТ 3: Удаление сущности
def test_delete_student(db_session):
    # Сначала создаем студента для удаления
    student = Student(name="Олег Николаев", age=22)
    db_session.add(student)
    db_session.commit()

    # Удаляем студента
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студент больше не существует
    deleted_student = db_session.query(Student).filter_by(
        name="Олег Николаев").first()
    assert deleted_student is None
