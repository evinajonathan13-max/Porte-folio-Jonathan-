class GeometricETH:
    def __init__(self, *args, **kwargs):
        pass
    def threshold(self, region, grad_curvature=0.0):
        # seuil de cohérence local par région ; exterior décohère plus vite
        base = {"bulk": 0.15, "shell": 0.10, "exterior": 0.35}.get(region, 0.10)
        return base + 0.10 * grad_curvature

def _measure_psig_with_local_coherence(brain, *args, **kwargs):
    from kernel.ttf.lct_law import measure_lct
    m = measure_lct(brain, theta=0.0)
    return m.P_sig
