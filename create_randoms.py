import randoms as rg
from astropy.utils.compat import argparse
from os import path
def create(args=None):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-Nf', default=1, metavar='Nf', help='Nrandom/Nobject', type=int)
    parser.add_argument('-i', '--inputname', default=None, type=str, metavar='data', help='Input data file')
    parser.add_argument('-o', '--outputname', default=None, type=str, metavar='outfile', help='Output random file')
    parser.add_argument('-rsd', default=True, type=bool, metavar='rsd', help='Include RSD')
    parser.add_argument('-view', action='store_true', help='Visualize the random map')
    parser.add_argument('-nside', default=32, type=int, help='Mask resolution')
    args = parser.parse_args(args)
    name, ext = path.splitext(args.outputname)
    print args.nside 
    if(ext!='fits'):
        fmt='ascii'
    else:
        fmt='fits'
    rg.make_random(args.nside,args.inputname,args.Nf,outfile=args.outputname,viewmap=args.view,fmt=fmt,rsd=args.rsd)
create()
