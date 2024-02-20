import numpy as np
import scipy.special as sp

def initial_radius(A):#A is the number of nucleons
    return 1.2*A**(1/3)
def spherical_harmonics(m,l,theta):
    return np.sqrt(((2*l+1)*sp.factorial(l-m))/(4*np.pi*sp.factorial(l+m)))*((-1)**m)*sp.lpmv(m,l,theta)
def spherical_harmonics_scipy(m,l,phi,theta):
    return sph_harm(m, l, phi, theta).real
def deformed_radius(beta, m, l, theta):
    return beta * spherical_harmonics(m,l,np.cos(theta))
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
def quadrupole_shape(theta, beta = 1,gamma = 0):
    #deformation coeficients
    beta22 = beta*np.sin(gamma)/np.sqrt(2)
    beta21 = 0
    beta20 = beta*np.cos(gamma)
    beta21m = beta21
    beta22m = beta22
    #deformed quadrupolar radius
    r22 = deformed_radius(beta22, 2, 2, theta)
    r21 = deformed_radius(beta21, 1, 2, theta) #0
    r20 = deformed_radius(beta20, 0, 2, theta)
    r21m = deformed_radius(beta21m, -1, 2, theta) #0
    r22m = deformed_radius(beta22m, -2, 2, theta)
    return r22+r21+r20+r21m+r22m
