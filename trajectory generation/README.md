## Trajectory Generation

*@Date: 2022-10-1*

*@Author: xuexun01*

- [Trajectory Generation](#trajectory-generation)
  - [1. Introduction](#1-introduction)
  - [2. Problem definition](#2-problem-definition)
  - [3. Metrics](#3-metrics)
  - [4. Related papers](#4-related-papers)

### 1. Introduction

&emsp;&emsp;The goal of generative models of individual human mobility is to generate synthetic trajecoties with realistic mobility patterns. The generated synthetic trajectories must reproduce a set of spatial and temporal mobility patterns, such as the distribution of characteristic distances traveled and the predictability of human whereabouts. The trajectory generation is crucial in many applications, such as:

* the performance analysis of networking protocols such as mobile ad hoc networks
* urban planning, what-if analysis, computational epidemiology, epidemic diffusion.
* protect geo-privacy of trajectory data

&emsp;&emsp;Solving trajectory generation requires capturing, simultaneously, the temporal and spatial patterns of individual human mobility. A realistic generative model should reproduce the temporal statistics observed empirically, including the number and sequence of visited locations together with the time and duration of the visits. In particular, the biggest hurdle consists of the simultaneous description of an individual's routine and sporadic out-of-routine mobility patterns. Regarding spatial patterns, a generative model should reproduce the tendency of individuals to move preferably within short distance, the heterogeneity of characteristic distances and their scales, the tendency of individuals to split into returners and explorers, the routinary and predictable nature of human displacements, and the fact that individuals visit a number of locations that are constant in time.


### 2. Problem definition

&emsp;&emsp;A generative mobility model $M$ is any algorithm able to generate a set of $n$ synthetic trajectories $\mathcal{T}_M = {T_{a_1}, ..., T_{a_n}}$, which describe the movements, during a certain period of time, of $n$ independent agents $a_1, ..., a_n$. The synthetic trajectory generated for a single agent $a_i$ should be in the form of *next-location prediction Definition*, i.e., a time-ordered sequence $T_{a_i} = <p_1, p_2, ..., p_k>$ composed by spatio-temporal points, describing the $k$ locations visited by $a_i$. The realism of $M$ is evaluated with respect to:

* A set of spatial patterns


### 3. Metrics

&emsp;&emsp;The distance between the distribution measures the preformances of trajectory generators of standard mobility metrics computed on a real dataset and the generated dataset, such as **haversine distance**, **equirectangular distance**.

### 4. Related papers