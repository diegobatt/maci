import numpy as np
import numpy.random

from sklearn.mixture import GaussianMixture, BayesianGaussianMixture
import scipy.stats as ss
import matplotlib.pyplot as plt


plt.style.use('ggplot')

n = 100000
mu = np.array([1, 4, 7])
sigma = np.array([1, 0.5, 1])
K = mu.shape[0]
weights = np.ones(K, dtype=np.float64) / 3.0
mixture_idx = numpy.random.choice(
    len(weights), size=n, replace=True, p=weights)
samples = numpy.fromiter(
    (ss.norm.rvs(mu[i], sigma[i]) for i in mixture_idx),
    dtype=np.float64)
samples = np.append(samples,[12.5]* 500)

x_axis = np.linspace(samples.min(), samples.max(), 400)
y_axis = np.zeros_like(x_axis)

for l, s, w in zip(mu, sigma, weights):
    y_axis += ss.norm.pdf(x_axis, loc=l, scale=s) * w

y_axis_gmm = np.zeros_like(x_axis)
gmm = GaussianMixture(7)
gmm.fit(samples.reshape(-1,1))
for l, s, w in zip(gmm.means_.flatten(), gmm.covariances_.flatten(), gmm.weights_):
    y_axis_gmm += ss.norm.pdf(x_axis, loc=l, scale=s) * w

y_axis_bgmm = np.zeros_like(x_axis)
bgmm = BayesianGaussianMixture(7)
bgmm.fit(samples.reshape(-1,1))
y_axis_bgmm = np.exp(bgmm.score_samples(x_axis.reshape(-1,1)))
# for l, s, w in zip(bgmm.means_.flatten(), bgmm.covariances_.flatten(), bgmm.weights_):
#     y_axis_bgmm += ss.norm.pdf(x_axis, loc=l, scale=s) * w

plt.plot(x_axis, y_axis, label='Densidad real')
plt.hist(samples, normed=True, bins="fd", label='Muestras')
# plt.plot(x_axis, y_axis_gmm, label='Estimacion ML')
plt.plot(x_axis, y_axis_bgmm, label='Estimacion bayesiana')
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.xlim([-2, 10])
# plt.ylim([0, 0.43])
plt.legend()
plt.savefig('figures/bayes_soluciones')
plt.show()
