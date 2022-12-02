import click

from solvers.day1 import day1


@click.group()
def main():
    pass


main.add_command(day1)

if __name__ == '__main__':
    main()
