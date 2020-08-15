from db_connection import create_connection, select_all_tasks


def main():
    database = r"/Users/oskarsakol/PycharmProjects/bombardier/obiekt_kolejowy.tdb2"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query all tasks")
        all_routes = select_all_tasks(conn)

    print(all_routes[1][0])


if __name__ == '__main__':
    main()