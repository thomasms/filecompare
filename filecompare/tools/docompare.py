from filecompare.compare.filelinecomparewithfloattolerance import FileLineCompareWithFloatTolerance
import sys
import argparse


def main():
    # Command line argument support
    parser = argparse.ArgumentParser(description='File Comparison')
    parser.add_argument('original', type=argparse.FileType('r'), help='The absolute path to the file which is deemed the original')
    parser.add_argument('compare', type=argparse.FileType('r'), help='The absolute path to the file which is going to be compared')
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")
    parser.add_argument("-t", "--tolerance", type=float,
                        help="set the relative tolerance applied to all floats, i.e 1% = 0.01")
    args = parser.parse_args()

    file_original = args.original.name
    file_compare = args.compare.name

    if args.verbosity is None:
        args.verbosity = 0

    if args.tolerance is None:
        args.tolerance = 0.0

    if args.verbosity == 1:
        print("Original file: ", file_original)
        print("Compare file: ", file_compare)

    # Ignore timestamps
    ignore = [
              'timestamp',
              'fispact run time',
              'Current time:',
              '/nuclear_data/'
              ]

    try:
        # use the file line comparison with float tolerance
        op = FileLineCompareWithFloatTolerance(relative_tolerance=args.tolerance, absolute_tolerance=0.0)
        result = op(file_original, file_compare, ignore=ignore)

        if result:
            if args.verbosity >= 1:
                print("Files are the same")
        else:
            if args.verbosity >= 1:
                print("Files are not the same.")
                print("Differences: (original line, compare line)")
                for d in op.diffs:
                    print(d)

        if args.verbosity >= 2:
            print(op.contents(file_original))

        if args.verbosity >= 2:
            print(op.contents(file_compare))

        assert result is True

    except OSError as err:
        if args.verbosity >= 1:
            print("OS error: {0}".format(err))
    except ValueError as err:
        if args.verbosity >= 1:
            print(err)
    except:
        if args.verbosity >= 1:
            print("Unexpected error:", sys.exc_info()[0])

        raise

if __name__ == "__main__":
    main()
