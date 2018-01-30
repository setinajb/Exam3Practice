"""
PRACTICE Test 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in PRINTING-TO-CONSOLE problems.  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jaclyn Setina.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 2 question.
#     5 is a "typical" Test 2 question.
#     7 is a "hard" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
########################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: r=7')
    shape(7)

    print()
    print('Test 2 of shape: r=4')
    shape(4)

    print()
    print('Test 3 of shape: r=2')
    shape(2)


def shape(r):
    """
    Prints a shape with r rows that looks like this example where r=7:
                        Num +    Spaces    ! Point     Dashes   r    k
    +++++++!7654321       7         0         1          0      7    0
     ++++++!654321-       6         1         1          1      7    1
      +++++!54321--       5         2         1          2      7    2
       ++++!4321---       4         3         1          3      7    3
        +++!321----       3         4         1          4
         ++!21-----       2         5         1          5
          +!1------       1         6         1          6

    Another example, where r=4:
    ++++!4321
     +++!321-
      ++!21--
       +!1---

    Preconditions:  r is a positive number.
    For purposes of "lining up", assume r is a single digit.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    ####################################################################
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  15 minutes.
    # ------------------------------------------------------------------
    # for k in range(r):
    #     for space in range(k):
    #         print(' ', end='')
    #     for plus in range(r, 0, -1):
    #         print('+', end='')
    #     for exc in range(1):
    #         print('!', end='')
    #     for n in range(r, 0, -1):
    #         print(n, end='')
    #     for dash in range(k):
    #         print('-', end='')
    #     print()

    for k in range(r):
        num_plusses = r - k
        num_spaces = k
        starting_num = num_plusses
        num_dashes = num_spaces

        for j in range(num_spaces):
            print(' ', end='')

        for j in range(num_plusses):
            print('+', end='')

        print('!', end='')

        for j in range(starting_num, 0, -1):
            print(j, end='')

        for j in range(num_dashes):
            print('-', end='')

        print()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
