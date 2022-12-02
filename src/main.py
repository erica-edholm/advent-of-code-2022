import click

from solvers.day1 import day1
from solvers.day2 import day2


@click.group()
def main():
    pass


main.add_command(day1)
main.add_command(day2)

if __name__ == '__main__':
    main()
