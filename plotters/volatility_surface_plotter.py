import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_surface(surface):
    K=np.sort(surface.index).tolist()
    T = np.sort(surface.columns).tolist()
    KK,TT = np.meshgrid(K,T)
    VV = np.array(
            [[surface.loc[k,t] for k in K] for t in T]
            )
    fig = plt.figure(figsize=plt.figaspect(0.5))
    
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    surf = ax1.plot_surface(KK, TT, VV, rstride=1, cstride=1, cmap=cm.magma, linewidth=0.1)
    
    ax1.set_zlim(0, float(max(surface.values.flatten())))
    ax1.set_title('volatiltiy surface')
    ax1.set_xlabel('strike')
    ax1.set_ylabel('maturity')
    
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.plot_wireframe(KK, TT, VV, rstride=1, cstride=1,color='black')
    ax2.set_zlim(0, float(max(surface.values.flatten())))
    ax2.set_title('volatiltiy wireframe')
    ax2.set_xlabel('strike')
    ax2.set_ylabel('maturity')
    
    plt.tight_layout()
    plt.show()
    plt.clf()