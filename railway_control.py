import logging
import random


logger = logging.getLogger(__name__)


def establish_route(_id: int, generated_route, route_length):
    logger.info(f"trying to establish route {_id}!")

    for course in range(route_length):

        starting_semaphore_signal = get_signal_state(generated_route[course][1])
        finishing_semaphore_signal = get_signal_state(generated_route[course][2])

        if starting_semaphore_signal != "SX" or finishing_semaphore_signal != "S1":
            note = "Failed at Establishing"
            return False, note
        note = "Passed at Establishing"
        return True, note


def release_route(_id: int, generated_route, route_length):
    logger.info(f"trying to release route {_id}!")

    for course in range(route_length, 0, -1):

        starting_semaphore_signal = get_signal_state(generated_route[course - 1][1])
        finishing_semaphore_signal = get_signal_state(generated_route[course - 1][2])

        if starting_semaphore_signal != "S1" or finishing_semaphore_signal != "S1":
            note = "Failed at Releasing"
            return False, note

    note = "Passed at Releasing"
    return True, note


def get_signal_state(name: str):
    return random.choice(["SX", "S1"])
