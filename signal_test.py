from db_management import create_connection
from railway_control import establish_route, release_route, get_signal_state


def signal_test(generated_routes, db):
    """
    Testing establish and release of previously generated routes
    :param generated_routes: all routes composed from courses
    :param db: name of database used for storing results
    :return:
    """

    conn = create_connection(db)

    c = conn.cursor()

    for key in generated_routes:

        route_length = len(generated_routes[key])

        testing_courses_ids = []

        [testing_courses_ids.append(generated_routes[key][course][0]) for course in range(route_length)]

        establish_test, establish_note = establish_route(key, generated_routes[key], route_length)
        release_test, release_note = release_route(key, generated_routes[key], route_length)

        note = establish_note + ", " + release_note

        if establish_test and release_test is True:
            c.execute('''INSERT INTO results
                         VALUES(?,?,?,?)''', (key, str(testing_courses_ids), "PASS", note))
            conn.commit()
        else:
            c.execute('''INSERT INTO results
                         VALUES(?,?,?,?)''', (key, str(testing_courses_ids), "FAIL", note))
            conn.commit()
