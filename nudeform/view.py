import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
import numpy as np
from matplotlib.colors import Normalize

def plot_radius_polar_coordinates(R,r0, phi, theta, save = False, dpi=300, string = ''):
    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, subplot_kw={'projection': 'polar'}, figsize=(18, 6))

    # Plot R(phi, theta=pi/2) on the first subplot
    # 180 = granularity/2
    ax1.plot(phi[:,0], R[:,179], color = 'blue', linewidth=2)
    ax1.plot(phi[:,0], r0[:,179], color = 'orange', linewidth=2)

    ax1.set_title(r"$R(\phi, \theta=\pi/2)$ | xy plane", fontsize = 20,pad = 25)

    # Plot R(phi=0, theta) on the second subplot
    ax2.plot(theta[0,:], R[0], color = 'blue', linewidth=2)
    ax2.plot(theta[0,:] + np.pi , R[0][::-1], color = 'blue', linewidth=2)
    ax2.plot(theta[0,:], r0[0], color = 'orange', linewidth=2)
    ax2.plot(theta[0,:] + np.pi, r0[0][::-1], color = 'orange', linewidth=2) # In order to display better the whole symmetry.
    ax2.set_title(r"$R(\phi=0, \theta)$ | xz plane", fontsize = 20,pad = 25)

    # Plot R(phi=pi/2, theta) on the second subplot
    ax3.plot(theta[0,:], R[89], color = 'blue', linewidth=2)
    ax3.plot(theta[0,:] + np.pi , R[89][::-1], color = 'blue', linewidth=2)
    ax3.plot(theta[0,:], r0[89], color = 'orange', linewidth=2)
    ax3.plot(theta[0,:] + np.pi, r0[89][::-1], color = 'orange', linewidth=2) # In order to display better the whole symmetry.
    ax3.set_title(r"$R(\phi=\pi/2, \theta)$ | yz plane", fontsize = 20,pad = 25)

    #radians ticks Lund convention
    x_ticks = np.arange(0, 2*np.pi + np.pi/3, np.pi/3)
    x_tick_labels = ['$0$', r'$\frac{\pi}{3}$', r'$\frac{2\pi}{3}$', 
                    r'$\pi$', r'$\frac{4\pi}{3}$', r'$\frac{5\pi}{3}$', '']
    ax1.set_xticks(x_ticks)
    ax1.set_xticklabels(x_tick_labels, fontsize = 25)
    ax1.tick_params(axis='y', labelsize=17)  # Change the label size of radial ticks

    ax2.set_xticks(x_ticks)
    ax2.set_xticklabels(x_tick_labels, fontsize = 25)
    ax2.tick_params(axis='y', labelsize=17)  # Change the label size of radial ticks

    ax3.set_xticks(x_ticks)
    ax3.set_xticklabels(x_tick_labels, fontsize = 25)
    ax3.tick_params(axis='y', labelsize=17)  # Change the label size of radial ticks

    fig.subplots_adjust(wspace=0.3)
    
    if save:
        plt.savefig('radial_plot'+string+'.png', dpi=dpi)
    
    plt.show()
 
def shape_plot_3D(x,y,z,R, save=False, dpi=300, string='', panes = True, axis = True):
    fig, ax3 = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(12, 8))
    norm = R/R.max()
    im = ax3.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(norm), shade=True, alpha = 0.2)
    limAxis = max([x.max()+0.5,y.max()+0.5,z.max()+0.5])
    ax3.axes.set_xlim3d(left=-1*limAxis, right=limAxis)
    ax3.axes.set_ylim3d(bottom=-1*limAxis, top=limAxis)
    ax3.axes.set_zlim3d(bottom=-1*limAxis, top=limAxis)
    if not panes:# make the panes transparent
        ax3.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax3.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax3.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    if not axis:#off axis
        ax3.set_axis_off()

    ax3.set_xlabel('x (fm)')
    ax3.set_ylabel('y (fm)')
    ax3.set_zlabel('z (fm)')

    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(R)
    m.set_clim(vmin=0, vmax=30)
    #fig.colorbar(m)

    if save:
        plt.savefig('deform_plot'+string+'.png', dpi=dpi)
    plt.show()

def plot_radius_polar_coordinates_superposition(r0, phi, theta, save = False, dpi=300, string = '', mradius = []):
    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, subplot_kw={'projection': 'polar'}, figsize=(18, 6))
    ax1.plot(phi[:,0], r0[:,179], color = 'orange', linewidth=2)
    ax1.set_title(r"$R(\phi, \theta=\pi/2)$ | xy plane", fontsize = 20,pad = 25)

    # Plot R(phi=0, theta) on the second subplot
    ax2.plot(theta[0,:], r0[0], color = 'orange', linewidth=2)
    ax2.plot(theta[0,:] + np.pi, r0[0][::-1], color = 'orange', linewidth=2) # In order to display better the whole symmetry.
    ax2.set_title(r"$R(\phi=0, \theta)$ | xz plane", fontsize = 20,pad = 25)

    # Plot R(phi=pi/2, theta) on the second subplot
    ax3.plot(theta[0,:], r0[89], color = 'orange', linewidth=2)
    ax3.plot(theta[0,:] + np.pi, r0[89][::-1], color = 'orange', linewidth=2) # In order to display better the whole symmetry.
    ax3.set_title(r"$R(\phi=\pi/2, \theta)$ | yz plane", fontsize = 20,pad = 25)
    cmap = plt.get_cmap('viridis')
    for i,R in enumerate(mradius):
    # Plot R(phi, theta=pi/2) on the first subplot
    # 180 = granularity/2
        color = cmap(i / len(mradius))
        ax1.plot(phi[:,0], R[:,179], linewidth=2, color = color)
        ax2.plot(theta[0,:], R[0], linewidth=2, color = color)
        ax2.plot(theta[0,:] + np.pi , R[0][::-1], linewidth=2, color = color)
        ax3.plot(theta[0,:], R[89], linewidth=2, color = color)
        ax3.plot(theta[0,:] + np.pi , R[89][::-1], linewidth=2, color = color)
    #radians ticks Lund convention
    x_ticks = np.arange(0, 2*np.pi + np.pi/3, np.pi/3)
    x_tick_labels = ['$0$', r'$\frac{\pi}{3}$', r'$\frac{2\pi}{3}$', 
                    r'$\pi$', r'$\frac{4\pi}{3}$', r'$\frac{5\pi}{3}$', '']
    ax1.set_xticks(x_ticks)
    ax1.set_xticklabels(x_tick_labels, fontsize = 25)
    ax1.tick_params(axis='y', labelsize=17)  # Change the label size of radial ticks

    ax2.set_xticks(x_ticks)
    ax2.set_xticklabels(x_tick_labels, fontsize = 25)
    ax2.tick_params(axis='y', labelsize=17)  # Change the label size of radial ticks

    ax3.set_xticks(x_ticks)
    ax3.set_xticklabels(x_tick_labels, fontsize = 25)
    ax3.tick_params(axis='y', labelsize=17)  # Change the label size of radial ticks

    fig.subplots_adjust(wspace=0.3)
    
    if save:
        plt.savefig('radial_plot'+string+'.png', dpi=dpi)
    
    plt.show()