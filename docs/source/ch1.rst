Chapter 1 Recurrent Problems
============================

Problem 1: All horses are the same color ::

    The assumption fails for n = 2.
    Given n=1 is true, it is impossible to prove the solution for n=2.
    If it is given that the solution works for n=2,
    for all pair of horses, then the hypothesis becomes true.


Problem 2: Find the shortest sequence of moves that transfers ::

    Position of towers:
    A   C   B

    Let L(n) be the solution for n disks.
    L(0) = 0
    L(1) = 2; moves,
        i.e. 1. Move disk from tower A to tower C.
             2. Move disk from tower C to tower B.
    L(2) = 8;
        i.e. 1. Perform L(1) for disk 1. (2 steps)
             2. Move disk 2 from tower A to tower C. (1 step)
             3. Perform reverse L(1) for disk 1. (2 steps)
             4. Move disk 2 from tower C to tower B. (1 step)
             5. Perform L(1) for disk 1. (2 steps)
         = L(1) + 1 + L(1) + 1 + L(1)
         = 3 * L(1) + 2

    Similarly for L(3), L(3) = 3 * L(2) + 2, and so on.

    therefore,
        let, U(n) = L(n) + 1
        then, L(n) + 1 = 3 * L(n-1) + 3
        => U(n) = 3 * U(n-1)
        since, L(0) = 0 => U(0) = 1
        => U(n) = 3^n
        => L(n) = 3^n - 1. QED

    Note: Also includes python solution in code/ch1/problem_2.py

Problem 3: Show that, in the process of transferring a tower ::

    There are 3 possible configurations for each disk (A, B and C).
    If we have only 1 disk, it can stay on tower A, B or C.
        L(1) = 3 = 3^1
    Now in case of 2 disks,
    disk 1 can be in 3 different position for each position of disk 2.
    therefore,
        L(2) = 3 * L(1) = 9 = 3^2
    Same can be proven for more disks.
    Since the solution of Q2 = 3^n - 1
    and we start at position 0 and we do not repeat
    any position (efficient solution),
    we can conclude that each and every configuration
    was traversed exactly once. QED

    Note: Also includes python solution in code/ch1/problem_3.py
