import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def ScatterSurface(X,Y,Z):
    """
    X: numpy array
    Y: numpy array
    Z: 2D numpy array of values with X as rows and Y as columns
    """
    X, Y = np.meshgrid(X, Y)
    Z = Z.T
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Flatten the arrays to pass them into scatter
    ax.scatter(X.ravel(), Y.ravel(), Z.ravel(), c=Z.ravel(), cmap='viridis', marker='o')
    # Labeling the axes
    ax.set_xlabel('strike')
    ax.set_ylabel('maturity')
    ax.set_zlabel('implied volatility')
    plt.show()