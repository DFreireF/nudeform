import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors

def plot_radius_polar_coordinates(R, phi, theta, save = False, dpi=300, string = ''):
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 6))

    # Plot R(phi, theta=0) on the first subplot
    ax1.plot([phi[0] for phi in phi], R[0])
    ax1.set_title("R(phi, theta=0)")

    # Plot R(phi=0, theta) on the second subplot
    ax2.plot([theta for theta in theta[0]], R[0])
    ax2.set_title("R(phi=0, theta)")
    if save:
        plt.savefig('img/radial_plot'+string+'.png', dpi=dpi)
    plt.show()
    
def shape_plot_3D(x,y,z,R,limAxis=10, save=False, dpi=300, string=''):
    fig, ax3 = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(12, 8))
    im = ax3.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(R/R.max()), shade=True)

    ax3.axes.set_xlim3d(left=-1*limAxis, right=limAxis)
    ax3.axes.set_ylim3d(bottom=-1*limAxis, top=limAxis)
    ax3.axes.set_zlim3d(bottom=-1*limAxis, top=limAxis)

    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(R)
    m.set_clim(vmin=1, vmax=100)
    fig.colorbar(m)

    if save:
        plt.savefig('img/deform_plot'+string+'.png', dpi=dpi)
    else:
        plt.show()