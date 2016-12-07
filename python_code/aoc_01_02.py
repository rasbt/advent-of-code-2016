import collections


"""
source: http://adventofcode.com/2016/day/1

DESCRIPTION

Santa's sleigh uses a very high-precision clock to guide its movements, and the
clock's oscillator is regulated by stars. Unfortunately, the stars have been
stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve
all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the
Easter Bunny Recruiting Document the Elves intercepted start here,
and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates
(where you just landed) and face North. Then, follow the provided sequence:
either turn left (L) or right (R) 90 degrees, then walk forward the given
number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on
the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North,
or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position,
which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?"""

p_input = """R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2,
L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3,
R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2,
L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4,
R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3,
R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5,
R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4,
R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1"""

"""
--- Part Two ---

Then, you notice the instructions continue on the back of the
Recruiting Document. Easter Bunny HQ is actually at the first
location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first
location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""


def walk(input_string):
    end_position = [0, 0]
    all_positions = set()
    first_pos_visited_twice = ()
    dq = collections.deque('NESW')
    curr_direction = dq[0]
    input_list = input_string.split(',')

    def visit_all():
        nonlocal first_pos_visited_twice
        if not first_pos_visited_twice:
            curr_pos = tuple(end_position)
            if curr_pos in all_positions:
                first_pos_visited_twice = curr_pos
            else:
                all_positions.add(curr_pos)


    for i in input_list:
        i = i.strip()
        turn, strides = i[0], int(i[1:])

        if turn == 'R':
            dq.rotate(-1)
        else:
            dq.rotate()
        curr_direction = dq[0]

        for i in range(strides):

            if curr_direction == 'N':
                end_position[1] += 1

            elif curr_direction == 'E':
                end_position[0] += 1

            elif curr_direction == 'S':
                end_position[1] -= 1

            else:
                end_position[0] -= 1

            visit_all()

    return end_position, first_pos_visited_twice


def compute_manhattan_dist(end_position):
    mdist = abs(0 - end_position[0]) + abs(0 - end_position[1])
    return mdist


def test_1():
    test_input = "R8, R4, R4, R8"
    end_pos, first_pos_visited_twice = walk(test_input)
    mdist = compute_manhattan_dist(first_pos_visited_twice)
    assert mdist == 4





def quiz_solution_p2():
    end_pos, first_pos_visited_twice = walk(p_input)
    mdist = compute_manhattan_dist(first_pos_visited_twice)
    print('Quiz solution part 2:', mdist)

if __name__ == "__main__":
    test_1()
    quiz_solution_p2()
