from db_management import create_connection
from railway_control import establish_route, release_route, get_signal_state


def signal_test(generated_routes, db):

    conn = create_connection(db)

    c = conn.cursor()

    for key in generated_routes:

        route_length = len(generated_routes[key])

        testing_courses_ids = []
        for course in range(route_length):
            testing_courses_ids.append(generated_routes[key][course][0])

        establish_test, establish_note = establish_route_test(generated_routes[key], route_length)
        release_test, release_note = release_route_test(generated_routes[key], route_length)

        note = establish_note + ", " + release_note

        if establish_test and release_test is True:
            c.execute('''INSERT INTO results
                         VALUES(?,?,?,?)''', (key, str(testing_courses_ids), "PASS", note))
            conn.commit()
            print("cool")
        else:
            c.execute('''INSERT INTO results
                         VALUES(?,?,?,?)''', (key, str(testing_courses_ids), "FAIL", note))
            conn.commit()
            print("boooooo")


def establish_route_test(generated_route, route_length):

    for course in range(route_length):
        establish_route(generated_route[course][0])
        starting_semaphore_signal = get_signal_state(generated_route[course][1])
        finishing_semaphore_signal = get_signal_state(generated_route[course][2])
        if starting_semaphore_signal != "SX" or finishing_semaphore_signal != "S1":
            note = "Failed at Establishing"
            return False, note
        note = "Passed at Establishing"
        return True, note


def release_route_test(generated_route, route_length):

    for course in range(route_length, 0, -1):

        release_route(generated_route[course - 1][0])
        starting_semaphore_signal = get_signal_state(generated_route[course - 1][1])
        finishing_semaphore_signal = get_signal_state(generated_route[course - 1][2])
        if starting_semaphore_signal != "S1" or finishing_semaphore_signal != "S1":
            note = "Failed at Releasing"
            return False, note
    note = "Passed at Releasing"
    return True, note
