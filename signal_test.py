import random


def get_signal_state():
    return random.choice(["SX", "S1"])


def signal_generator(generated_routes):

    for key in generated_routes:
        generated_route_with_signals = []
        route_length = len(generated_routes[key])

        if route_length > 1:

            for route in generated_routes[key]:
                route = route + (get_signal_state(), )

                generated_route_with_signals.append(route)
        else:
            continue
        print(generated_route_with_signals)
        signal_test(generated_route_with_signals, route_length)


def signal_test(generated_routes_with_signals, route_length):

    return True
