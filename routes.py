
def generate_routes(all_routes):
    grouped_routes = {}
    a = 0
    for route in all_routes:

        grouped_routes[a] = [all_routes[(route[0]) - 1]]

        route_for_comparison = all_routes[a][2]

        for x in range(3):

            for comparing_route in all_routes:
                if route_for_comparison == all_routes[(comparing_route[0]) - 1][1]:

                    route_for_comparison = all_routes[(comparing_route[0]) - 1][2]

                    grouped_routes[a].append(all_routes[(comparing_route[0]) - 1])
                    break

        a += 1

    return grouped_routes
