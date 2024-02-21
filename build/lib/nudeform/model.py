import numpy as np
import scipy.special as sp

def initial_radius(A):#A is the number of nucleons
    return 1.2*A**(1/3)
def spherical_harmonics_scipy(m,l,phi,theta):
    return sp.sph_harm(m, l, phi, theta).real
def deformed_radius_scipy(beta, m, l, phi, theta):
    return beta * spherical_harmonics_scipy(m, l, phi, theta)
def total_radius(r0,*r):
    radius = 0
    for deformed_radius in r:
        radius += deformed_radius
    return r0*(1+radius)
def x(r, theta, phi):
    return r * np.sin(theta) * np.cos(phi)
def y(r, theta, phi):
    return r * np.sin(theta) * np.sin(phi)
def z(r, theta):
    return r * np.cos(theta)
def xyz(r,theta,phi):
    return x(r, theta, phi), y(r, theta, phi), z(r, theta)
def radius(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)
def quadrupole_shape_scipy(phi,theta, beta = 1,gamma = 0):
    #deformation coeficients
    beta22 = beta*np.sin(gamma)/np.sqrt(2)
    beta21 = 0
    beta20 = beta*np.cos(gamma)
    beta21m = beta21
    beta22m = beta22
    #deformed quadrupolar radius
    r22 = deformed_radius_scipy(beta22, 2, 2,phi, theta)
    r21 = deformed_radius_scipy(beta21, 1, 2,phi, theta) #0
    r20 = deformed_radius_scipy(beta20, 0, 2,phi, theta)
    r21m = deformed_radius_scipy(beta21m, -1, 2,phi, theta) #0
    r22m = deformed_radius_scipy(beta22m, -2, 2,phi, theta)
    return r22+r21+r20+r21m+r22m
def lambda_shape(phi,theta, beta = [1],gamma = 0, lambda_ = 1):
    labda_rb = []
    for betai in beta:
        lambda_r = 0
        for m in range(-lambda_,lambda_+1):
            lambda_r += deformed_radius_scipy(betai, m, lambda_,phi, theta)
        labda_rb = np.append(labda_rb, lambda_r)
    return np.reshape(labda_rb, (len(beta),360,360))