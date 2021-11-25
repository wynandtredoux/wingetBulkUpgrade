from argparse import ArgumentParser
from os import system

# take in a list of packages to upgrade using "winget --upgrade <packages>"
def winBulk(packages):
    # for each package
    for package in packages:
        print(f'\nUpgrading {package}...')  # print which package is being upgraded
        system(f'cmd /c "winget upgrade \"{package}\""')  # winget upgrade
    return


if __name__ == '__main__':
    # parse command line arguments
    parser = ArgumentParser(description='Update multiple winget packages')
    parser.add_argument('packages'
                        , help='A list of package names, comma delimited, no spaces between commas', type=str)
    args = parser.parse_args()
    # perform bulk upgrade with given package names
    winBulk(args.packages.split(','))  # split argument string into list of package names
