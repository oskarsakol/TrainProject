from db_management import create_connection, select_all_tasks, delete_all_tasks
from routes import generate_routes
from signal_test import signal_test


def main():

    database = r"/Users/oskarsakol/PycharmProjects/bombardier/obiekt_kolejowy.tdb2"
    database_results = r"/Users/oskarsakol/PycharmProjects/bombardier/obiekt_kolejowy_results.db"
    # create a database connection
    conn = create_connection(database)

    with conn:
        all_routes = select_all_tasks(conn)

    if conn:
        conn.close()

    conn = create_connection(database_results)

    delete_all_tasks(conn)

    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS results
                 ([route_id] INTEGER PRIMARY KEY,[courses_ids] text, [test_result] text, [log] text)''')

    if conn:
        conn.close()

    generated_routes = generate_routes(all_routes)

    signal_test(generated_routes, database_results)


if __name__ == '__main__':
    main()

