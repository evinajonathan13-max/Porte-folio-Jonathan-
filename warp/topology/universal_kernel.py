import math
import numpy as np

UNIVERSAL_KERNEL_P_SIG = 1.80

def warp_shell_coords(R=1.0, eps=0.3, n_shell=50, n_bulk=24, n_exterior=12, seed=42):
    rng = np.random.RandomState(seed)
    shell = []
    for i in range(n_shell):
        th = rng.uniform(0, 2 * math.pi)
        ph = rng.uniform(0, math.pi)
        shell.append([R * math.sin(ph) * math.cos(th), R * math.sin(ph) * math.sin(th), R * math.cos(ph)])
    bulk = rng.uniform(-eps, eps, size=(n_bulk, 3)).tolist()
    exterior = rng.uniform(1.2, 2.0, size=(n_exterior, 3)).tolist()
    return np.array(shell + bulk + exterior), {"shell": n_shell, "bulk": n_bulk, "exterior": n_exterior}

def build_warp_brain(coords, t=1.0, J=0.3, max_edge=2.0):
    from kernel.ttf.ttf_compute import TTFBrain
    return TTFBrain(coords=coords, omega=math.pi / 2, t=t, J=J, max_edge=max_edge, Dc=0.5, seed=42)
