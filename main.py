from db_management import create_connection, select_all_tasks, delete_all_tasks
from routes import generate_routes
from signal_test import signal_test


# Dobra ja to rozumiem tak, establish sprawdzanie od początku od końca, releaserskiej od końca do początku, przy tym i tym trzeba odpalić ich funkcje
# do logowania wydarzenia gdzie na inputcie trzeba podać id całej trasy, gdzie wszystkie trasy gdzieś trzymamy już złożone. Przy każdym teście zarówno
# establish jak i release musimy użyć ich funkcji get_signal_state, żeby dla każdego semafora danej trasy wygenerować stan. Następnie sprawdzamy czy każdy
# element drogi ( oni to nazywają przebieg) jest ustawiony dobrze czyli dla establish musi być na pierwszym semaforze SX a na drugim S1, gdzie w release musi
# być na wszystkich semaforach S1


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

