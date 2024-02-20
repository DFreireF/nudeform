import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
import numpy as np
from matplotlib.colors import Normalize

def plot_radius_polar_coordinates(R,r0, phi, theta, save = False, dpi=300, string = ''):
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 6))

    # Plot R(phi, theta=0) on the first subplot
    ax1.plot([phi[0] for phi in phi], R[0], color = 'blue')
    ax1.plot([phi[0] for phi in phi], r0[0], color = 'orange')

    ax1.set_title(r"$R(\phi, \theta=0)$")

    # Plot R(phi=0, theta) on the second subplot
    ax2.plot([theta for theta in theta[0]], R[0], color = 'blue')
    ax2.plot([theta + np.pi for theta in theta[0]], R[0], color = 'blue')
    ax2.plot([theta for theta in theta[0]], r0[0], color = 'orange')
    ax2.plot([theta + np.pi for theta in theta[0]], r0[0], color = 'orange') # In order to display better the whole symmetry.
    ax2.set_title(r"$R(\phi=0, \theta)$")

    #radians ticks
    xT=plt.xticks()[0]
    xL=['0',r'$\frac{\pi}{4}$',r'$\frac{\pi}{2}$',r'$\frac{3\pi}{4}$',\
    r'$\pi$',r'$\frac{5\pi}{4}$',r'$\frac{3\pi}{2}$',r'$\frac{7\pi}{4}$']
    ax1.set_xticks(xT, xL)
    ax2.set_xticks(xT, xL)

    if save:
        plt.savefig('img/radial_plot'+string+'.png', dpi=dpi)
    plt.show()
    
def shape_plot_3D(x,y,z,R, save=False, dpi=300, string=''):
    fig, ax3 = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(12, 8))
    norm = R/R.max()
    im = ax3.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(norm), shade=True)
    limAxisx,limAxisy,limAxisz = x.max()+0.5,y.max()+0.5,z.max()+0.5
    ax3.axes.set_xlim3d(left=-1*limAxisx, right=limAxisx)
    ax3.axes.set_ylim3d(bottom=-1*limAxisy, top=limAxisy)
    ax3.axes.set_zlim3d(bottom=-1*limAxisz, top=limAxisz)

    ax3.set_xlabel('x (fm)')
    ax3.set_ylabel('y (fm)')
    ax3.set_zlabel('z (fm)')

    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(R)
    m.set_clim(vmin=0, vmax=30)
    fig.colorbar(m)

    if save:
        plt.savefig('img/deform_plot'+string+'.png', dpi=dpi)
    else:
        plt.show()