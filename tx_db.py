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

    parser = argparse.ArgumentParser(description="create gff database for exonfeat analysis", prog="tx_db.py")
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-gff", type=str, default=None, metavar="<gff_file>",
                          help="specify path to gff file", required=True)
    required.add_argument("-fa", type=str, default=None, metavar="<fasta_file>", help="specify path to the fasta file",
                          required=True)
    required.add_argument("-out", type=str, default=None, metavar="<output_name>", help="label for output directory",
                          required=True)
    optional.add_argument("-t", "--threads", nargs='?', const=1, type=int, default=1, metavar="",
                          help='number of threads to utilize (default = 1)')
    optional.add_argument("-l", "--license", action=licenseAction, metavar="", nargs=0,
                          help='show license status and exit')
    parser._action_groups.append(optional)
    args = parser.parse_args()

    # Build tx database
    license.txdb_builder(args.gff, args.fa, args.out, args.threads, sys.argv)
