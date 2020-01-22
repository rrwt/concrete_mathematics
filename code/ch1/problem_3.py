"""
Tower of hanoi, configurations
"""
import math
from itertools import zip_longest

from hypothesis import strategies, given, assume


def regular_toh(
    disk_count: int,
    src: list,
    dst: list,
    aux: list,
    src_title: str = "src",
    dst_title: str = "dst",
    aux_title: str = "aux",
) -> None:
    total_moves = 0
    if disk_count < 1:
        return total_moves

    if disk_count > 1:
        total_moves += regular_toh(disk_count - 1, src, aux, dst, src_title, aux_title, dst_title)
        print(f"move disk {src[-1]} from {src_title} to {dst_title}")
        dst.append(src.pop())
        total_moves += regular_toh(disk_count - 1, aux, dst, src, aux_title, dst_title, src_title)
    else:
        print(f"move disk {src[-1]} from {src_title} to {dst_title}")
        dst.append(src.pop())

    total_moves += 1
    return total_moves


def special_toh(
    disk_count: int,
    src: list,
    dst: list,
    aux: list,
    src_title: str = "src",
    dst_title: str = "dst",
    aux_title: str = "aux",
) -> None:
    def print_toh(from_to: str) -> None:
        print()
        print(f"{from_to} State")
        print(src_title, dst_title, aux_title)

        for s, d, a in zip_longest(src, dst, aux, fillvalue=" "):
            print(s, d, a, sep="   ")

        print("-----")

    total_moves = 0

    if disk_count < 1:
        return total_moves

    if disk_count > 1:
        total_moves += special_toh(disk_count - 1, src, dst, aux, src_title, dst_title, aux_title)
        print(f"move disk {src[-1]} from {src_title} to {aux_title}")
        print_toh("from")
        aux.append(src.pop())
        print_toh("to")
        total_moves += special_toh(disk_count - 1, dst, src, aux, dst_title, src_title, aux_title)
        print(f"move disk {aux[-1]} from {aux_title} to {dst_title}")
        print_toh("from")
        dst.append(aux.pop())
        print_toh("to")
        total_moves += special_toh(disk_count - 1, src, dst, aux, src_title, dst_title, aux_title)
    else:
        print(f"move disk {src[-1]} from {src_title} to {aux_title}")
        print_toh("from")
        aux.append(src.pop())
        print_toh("to")
        print(f"move disk {aux[-1]} from {aux_title} to {dst_title}")
        print_toh("from")
        dst.append(aux.pop())
        print_toh("to")

    total_moves += 2
    return total_moves


@given(strategies.integers(min_value=0, max_value=10))
def test_regular_toh(disk_count):
    print(f"for {disk_count} disks")
    assert (
        regular_toh(disk_count, [d for d in range(disk_count, 0, -1)], [], [])
        == math.pow(2, disk_count) - 1
    )


for i in range(1, 5):
    print("---------------------------------------------")
    print(f"Solution for {i} disks")
    print("total moves: ", special_toh(i, [x for x in range(i, 0, -1)], [], []))
