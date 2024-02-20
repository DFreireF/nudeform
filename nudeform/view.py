import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors

def plot_radius_polar_coordinates(R, phi, theta):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot([phi[0] for phi in phi], R[0])
    plt.show()
    fig, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
    ax2.plot([theta for theta in theta[0]], R[0])
    plt.show()    
def shape_plot_3D(x,y,z,R,limAxis=10):
    fig, ax3 = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(12, 8))
    #plt.subplots_adjust(bottom=0.30, top=0.99)
    im = ax3.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(R/R.max()), shade=True)

    ax3.axes.set_xlim3d(left=-1*limAxis, right=limAxis)
    ax3.axes.set_ylim3d(bottom=-1*limAxis, top=limAxis)
    ax3.axes.set_zlim3d(bottom=-1*limAxis, top=limAxis)

    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(R)
    m.set_clim(vmin=1, vmax=100)
    fig.colorbar(m)