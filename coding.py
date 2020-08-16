from db_connection import create_connection, select_all_tasks
from routes import generate_routes
from signal_test import signal_generator


def main():
    database = r"/Users/oskarsakol/PycharmProjects/bombardier/obiekt_kolejowy.tdb2"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query all tasks")
        all_routes = select_all_tasks(conn)

    print(all_routes[1][1])

    generated_routes = generate_routes(all_routes)
    print(generated_routes)

    signal_generator(generated_routes)


if __name__ == '__main__':
    main()

