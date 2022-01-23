from shutil import disk_usage

"""
script for getting disk stats.
"""


def get_disk_stats(path: str) -> dict:
    # TODO определить в Мб или Гб выдавать инфу
    total, used, free = disk_usage(path)
    total = '{:.2f}'.format(total / 1024 / 1024 / 1024)
    used = '{:.2f}'.format(used / 1024 / 1024 / 1024)
    free = '{:.2f}'.format(free / 1024 / 1024 / 1024)

    return dict(total=total, used=used, free=free)


def main():
    disk_info = get_disk_stats("C:")
    print(disk_info)


if __name__ == '__main__':
    main()
