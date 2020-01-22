"""
Tower of hanoi, configurations
"""
from math import pow
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


@given(strategies.integers(min_value=0, max_value=10))
def test_regular_toh(disk_count):
    print(f"for {disk_count} disks")
    assert (
        regular_toh(disk_count, [d for d in range(disk_count, 0, -1)], [], [])
        == pow(2, disk_count) - 1
    )
