
def generate_routes(all_courses):
    """
    Generate routes from given courses with max length of 4 courses
    :param all_courses: all courses provided in database
    :return:
    """
    
    grouped_courses = {}
    a = 0
    for course in all_courses:

        grouped_courses[a] = [all_courses[(course[0]) - 1]]

        course_for_comparison = all_courses[a][2]

        for x in range(3):

            for comparing_course in all_courses:
                if course_for_comparison == all_courses[(comparing_course[0]) - 1][1]:

                    course_for_comparison = all_courses[(comparing_course[0]) - 1][2]

                    grouped_courses[a].append(all_courses[(comparing_course[0]) - 1])
                    break

        a += 1

    return grouped_courses
