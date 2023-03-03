from src.database import SessionLocal, engine, Base
from src.models import User, Post
from sqlalchemy import text


Base.metadata.create_all(bind=engine)


def create_user(name, email):
    #Initial database connection
    db = SessionLocal()
    user = User(name=name, email=email, is_active=True)
    # add user
    db.add(user)
    db.commit()
    print("Created user")


def get_user_by_name(name):
    with engine.connect() as connection:
        result = connection.execute(text(f"select * from users where name = '{name}'"))
        id_name = None

        for row in result:
            id_name = row.id

        connection.close()
        return id_name


#get_user_by_name("test_name")

def create_post_by_user(name, title):
    db = SessionLocal()
    user = get_user_by_name(name)
    post = Post(title=title, author_id=user)
    db.add(post)
    db.commit()
    print("Created post")


def get_posts_by_user(user_id):
    connection = engine.connect()
    result = connection.execute(text(f'select u.name, p.title from posts p inner join users u on p.author_id = u.id where p.author_id = {user_id}'))
    #print(result.all())
    for row in result:
        print(row)
    connection.close()

    #este deberia devolverme el nombre del usuario y todos los titulos de post asociados a este


get_posts_by_user(1)
get_posts_by_user(2)

"""create_user(name="test_name_1", email="test_email_1")
create_user(name="test_name_2", email="test_email_2")
create_user(name="test_name_3", email="test_email_3")
create_user(name="test_name_4", email="test_email_4")
create_user(name="test_name_5", email="test_email_5")"""

"""create_post_by_user(name="test_name", title="test_post_name")
create_post_by_user(name="test_name", title="test_post_name_1")
create_post_by_user(name="test_name", title="test_post_name_2")
"""

