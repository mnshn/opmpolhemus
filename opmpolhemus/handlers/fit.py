import numpy as np
import random


def gradOfCost(points, pcl, alpha, beta, gamma):
    xyz = np.array(list(map(lambda x: pcl[x], points)))
    size = np.shape(xyz)[0]
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    dalpha = -2 * (np.sum(z) - beta * np.sum(x) - gamma * np.sum(y) -
                   size * alpha)
    dbeta = -2 * (np.inner(x, z) - beta * np.inner(x, x) -
                  gamma * np.inner(x, y) - alpha * np.sum(x))
    dgamma = -2 * (np.inner(y, z) - beta * np.inner(y, z) -
                   gamma * np.inner(y, y) - alpha * np.sum(y))
    return np.array((dalpha, dbeta, dgamma))


def gradDescent(points, pcl):
    L = 5
    prev = 1
    step = 0
    rate = 10e-4
    mesh = 10e-10
    maxSteps = 10e5
    (alphaI, betaI, gammaI) = np.array(
        (random.uniform(-L, L), random.uniform(-L, L), random.uniform(-L, L)))
    while prev > mesh and step < maxSteps:
        (alphaP, betaP, gammaP) = (alphaI, betaI, gammaI)
        (alphaI, betaI, gammaI) = (alphaI, betaI, gammaI) - rate * gradOfCost(
            points, pcl, alphaI, betaI, gammaI)
        prev = abs(alphaI - alphaP)**2 + abs(betaI - betaP)**2 + abs(gammaI -
                                                                     gammaP)**2
        step += 1
    print(step, prev)
    return [alphaI, betaI, gammaI]


# while prev > mesh and step < maxSteps:
#     (prevX, prevY)=np.array((xI, yI))
#     (xI, yI)=np.array((xI, yI)) - alpha*gradOfTest(prevX, prevY)
#     prev=abs(xI-prevX)**2+abs(yI-prevY)**2
#     step=step + 1
