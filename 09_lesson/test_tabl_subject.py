from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:1968@localhost:5432/SNEZHANA"
db = create_engine(db_connection_string)


def test_db_connection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == ('subject')


# Добавление
def test_insert_subjects():
    # Получить количество предметов
    connection = db.connect()
    res = connection.execute("select count(*) from subject").fetchone()[0]

    # Добавить новый предмет
    sql = text("insert into subject(\"subject_title\") VALUES (:new_subject)")
    connection.execute(sql, {"new_subject": "Физра"})
    res2 = connection.execute("select count(*) from subject").fetchone()[0]

    # Проверить, что предметов стало на 1 больше
    assert res == res2-1

    # Удалить добавленный предмет
    sql = text("delete from subject where subject_title='Физра'")
    connection.execute(sql)
    res3 = connection.execute("select count(*) from subject").fetchone()[0]

    # Проверить, что предметов стало на 1 меньше
    assert res3 == res
    connection.close()


# Удаленение
def test_update_subjects():
    # Получить количество предметов
    connection = db.connect()
    res = connection.execute("select count(*) from subject").fetchone()[0]

    # Добавить новый предмет
    sql = text("insert into subject(\"subject_title\") VALUES (:new_subject)")
    connection.execute(sql, {"new_subject": "НВП"})
    res2 = connection.execute("select count(*) from subject").fetchone()[0]

    # Проверить, что предметов стало на 1 больше
    assert res == res2 - 1
    connection = db.connect()

    # Удалить предмет
    sql = text("delete from subject where subject_title='НВП'")
    connection.execute(sql)
    res3 = connection.execute("select count(*) from subject").fetchone()[0]

    # Проверить, что предметов стало на 1 меньше
    assert res3 == res
    connection.close()
