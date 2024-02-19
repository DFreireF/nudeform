import argparse
import sys
import numpy as np
from nudeform.model import *
from nudeform.view import *

def main():
    parser = argparse.ArgumentParser(description="Plot the shape of a deformed nucleus.")

    # Define command-line arguments
    parser.add_argument("-A", type=int, help="Number of nucleons")
    parser.add_argument("--beta", type=float, help="Deformation factor")
    parser.add_argument("--gamma", type=float, help="Gamma value")
    parser.add_argument("--granularity", type=int, default=360, help="Granularity of the plot (default: 360)")

    # Parse arguments
    args = parser.parse_args()

    phi, theta = np.mgrid[0:2*np.pi:(args.granularity)*1j, 0:np.pi:(args.granularity)*1j]
    Rquadr = quadrupole_shape(theta, beta = args.beta, gamma = args.gamma)
    r0 = initial_radius(args.A)
    R = r0*(1+Rquadr)
    x,y,z = xyz(R,theta,phi)

    shape_plot_3D(x,y,z,R)
    plt.show()

    plot_radius_polar_coordinates(R, phi, theta)

if __name__ == "__main__":
    main()