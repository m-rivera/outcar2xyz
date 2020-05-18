#!/usr/bin/env python3
"""Script to turn OUTCAR geometries from VASP into .xyz"""

import argparse
import sys
import fromage as fro

def main(args):
    traj = fro.traj_from_file(args.in_name)
    traj.write_xyz(args.out_name)

if __name__ == "__main__":
    # parse the input
    parser = argparse.ArgumentParser(description="Turn OUTCAR into an xyz file")
    parser.add_argument("in_name", nargs='?', help="Input OUTCAR file. Default 'OUTCAR'", default = "OUTCAR")
    parser.add_argument("out_name", nargs='?', help="Output .xyz file. Default 'outcar.xyz'", default = "outcar.xyz")

    user_input = sys.argv[1:]
    args = parser.parse_args(user_input)
    main(args)
