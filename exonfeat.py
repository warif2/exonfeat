# Import modules
import sys
import argparse
import license

if __name__ == '__main__':
    # Check license
    license.check_status()

    # Setup of argparse for script arguments
    class licenseAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print("License status: %s" % license.message())
            sys.exit()

    parser = argparse.ArgumentParser(description="run exonfeat analysis", prog="exonfeat.py")
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-rf", type=str, default=None, metavar="<rmats_file>",
                          help="specify path to rmats output file", required=True)
    required.add_argument("-o", type=str, default=None, metavar="<out_path>",
                          help="specify path to output directory", required=True)
    required.add_argument("-db", type=str, default=None, metavar="<tx_db>",
                          help="specify path to transcript database", required=True)
    optional.add_argument("-l", "--license", action=licenseAction, metavar="", nargs=0,
                          help='show license status and exit')
    parser._action_groups.append(optional)
    args = parser.parse_args()

    # Perform exon feature analysis
    license.exon_feature(args.rf, args.o, args.db, sys.argv)
