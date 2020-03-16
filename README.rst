****
polytope-sampling
****
This package provides functions to uniformly sample points subject to a system of linear inequality constraints, :math:`A_1 x <= b_1` (convex polytope), and linear equality constraints, :math:`A_2 x <= b_2` (affine subspace).

Example
-------
Let's consider the example of sampling :math:`x \in \mathbb{R}^2` subject to
.. math
    0.1 \leq x_1 &\leq 0.9
    0.2 \leq x_2 &\leq 1
    1/2 x_1 + x_2 &\leq 1
    0.2 \leq -2/3 x_1 + x_2

.. code-block:: python
    import polytope

    X = polytope.sample(
        n_points=1000,
        lower=[-0.1, -0.2],
        upper=[0.7, 0.9],
        A1=np.array([[1 / 2, 1], [2 / 3, -1]]),
        b1=np.array([1, -0.2])
    )

.. |sampling_examples| image:: examples/example.png

References
----------
A comparison of MCMC algorithms to generate uniform samples over a convex polytope is
given in [Chen2018]_. Here, we use the Hit & Run algorithm described in [Smith1984]_.
The R-package `hitandrun`_ provides similar functionality to this module.

.. [Chen2018] Chen Y., Dwivedi, R., Wainwright, M., Yu B. (2018) Fast MCMC Sampling
    Algorithms on Polytopes. JMLR, 19(55):1−86
    https://arxiv.org/abs/1710.08165
.. [Smith1984] Smith, R. (1984). Efficient Monte Carlo Procedures for Generating
    Points Uniformly Distributed Over Bounded Regions. Operations Research,
    32(6), 1296-1308.
    www.jstor.org/stable/170949
.. _`hitandrun`: https://cran.r-project.org/web/packages/hitandrun/index.html
