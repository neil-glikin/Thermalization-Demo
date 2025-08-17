# Temperature Demo
A demo of the meaning (in some sense) of the microscopic concept of temperature as a statistical distribution

Created to help me talk to my non-physicist but technically-inclined friends about what temperature means

The demonstration is a set of animations using python in a Jupyter notebook.

This demonstration models a physical system as a grid of particles, or sites, each of which has a discrete number of energy "units" on it. Energy units are randomly exchanged from one site to another, and the distribution of enegries naturally approaches a Boltzmann distribution, which is an exponentially decaying probability distribution. The grid itself is visualized as a pixel image, and the distribution of energies as a histogram. Animations let you watch the evolution of both the grid and its energy distribution histogram as sites randomly exchange energy with each other.

The interesting takeaway (from my point of view): Predicting a thermal (Boltzmann) distribution requires no physics whatsoever, aside from energy conservation and some mechanism to exchange it. All you need is combinatorics; the Boltzmann distribution is *the* thermal distribution simply because it's the most likely one! The whole field of statistical mechanics is based off of the emergence of macroscopic properties from microscopic statistics.

Requires ipympl for animations in Jupyter notebooks.
