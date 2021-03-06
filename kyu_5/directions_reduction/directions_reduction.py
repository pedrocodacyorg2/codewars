#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def dirReduc(arr: list) -> list:
    """
    A function dirReduc which will take an array of strings
    and returns an array of strings with the needless
    directions removed (W<->E or S<->N side by side).

    The Haskell version takes a list of directions with data
    Direction = North | East | West | South.

    The Clojure version returns nil when the path is reduced
    to nothing.

    The Rust version takes a slice of enum Direction
    {NORTH, SOUTH, EAST, WEST}.
    :param arr:
    :return:
    """

    pairs = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i, a in enumerate(arr):
            if i + 1 < len(arr):
                if pairs[a] == arr[i + 1]:
                    del arr[i + 1]
                    del arr[i]
                    is_sorted = False
                    break

    return arr
