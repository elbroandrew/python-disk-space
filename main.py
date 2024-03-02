from shutil import disk_usage
from texttable import Texttable

"""
script for getting disk stats.
"""

# TODO#1
"""
$ python3 script.py --arg1 disk   --> shows disk usage
$ python3 script.py --arg1 am --arg2 path_to_file --arg3 new_name --arg4 destination_dir  --> archives file and moves to a directory
$ python3 script.py --arg1 rem --arg2 path_to_file  --> removes file
"""

def get_disk_stats(path: str) -> dict:
    # TODO#2 определить в Мб или Гб выдавать инфу.
    # TODO#2 все диски вывести, а не один.
    total, used, free = disk_usage(path)
    total = '{:.2f}'.format(total / 1024 / 1024 / 1024)
    used = '{:.2f}'.format(used / 1024 / 1024 / 1024)
    free = '{:.2f}'.format(free / 1024 / 1024 / 1024)

    return dict(total=total, used=used, free=free)


def draw_stats_table(dic: dict):
    table = Texttable()
    table.set_cols_align(["c", "c", "c"])
    table.set_cols_valign(["m", "m", "m"])
    table.set_precision(1)
    table.add_rows([["Total", "Used", "Free"],
                    [dic["total"],
                     dic["used"],
                     dic["free"]]
                    ])
    print(table.draw())

"""
+-------+-------+-------+-------+
| Mountpath | Total | Used  | Free  |
+===========+=======+=======+=======+
| /dev/sda1 | 610.2 | 321.0 | 321.0 |
+-----------+-------+-------+-------+
/dev/sda2
/dev/sdb
.......
"""

def main():
    disk_info = get_disk_stats("C:")
    draw_stats_table(disk_info)


if __name__ == '__main__':
    main()
