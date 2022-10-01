## Crowd Flow Prediction

*@Date: 2022-9-20*

*@Author: xuexun*

- [Crowd Flow Prediction](#crowd-flow-prediction)
  - [1. Introduction](#1-introduction)
  - [2. Problem definition](#2-problem-definition)
  - [3. Metrics](#3-metrics)
  - [4. Related papers](#4-related-papers)

### 1. Introduction

&emsp;&emsp;**Crowd flow prediction** is the task of forecasting the incoming and outgoing flows of people on a geographic region, usually spatial tessellation. It has a crucial impact on several aspects of society, from public safety(COVID-19 prevention) to the definition of on-demand services, the management of land use, and traffic optimization.

&emsp;&emsp;Crowd flow prediction requires dealing with both spatial and temporal dependencies. Indeed. a region's out-flow may affect the in-flows of both near and far regions. At the same time, crowd flows are chracterized by temporal closeness, trends, and periodicity. Temporal closeness marks the dependencies between events that are close in time; trends highlight patterns that repeat over time; periodicity captures the repetitive nature of relevant events. Futhermore, exogenous factors such as weather conditions, holidays and the presence of public city events may affect crowd flow patterns.

### 2. Problem definition

&emsp;&emsp;Given an individual's trajectory $T_u$ and a spatial tessellation $\mathcal{G}$ of the geographic space (generally a $i \times j$ grid), the set of locations(tiles) the trajectory intersects in a time interval $\Delta t$ is:

$$
q^t_{T_u} = \{(p_k \rightarrow t) \in \Delta t  \land (p_k \rightarrow (x,y)) \in (i,j) | (i,j)\}
$$

where $(i,j)$ indicates a location on $\mathcal{G}$ and $p_k$ is the user $u$'s current location, identified by the coordinates (x,y). Let $Q$ be the set of locations covered by all the individual trajectories and let $t-1, t ,t+1$ be three consecutive time spans, the incoming flow $in^{(i,j)}_t$ to a location $(i,j)$ is the number of the individuals that are in $(i,j)$ at time $t$ but were not in $(i,j)$ at time $t-1$. Similarly, the outgoing flow $out^{(i,j)}_t$ to location $(i,j)$ is the number of individuals that are in $(i,j)$ at time $t$ and move to another location at time $t+1$:

$$
in^{(i,j)}_t = \sum_{T \in Q}\{t > 1 | (i,j) \notin q^{t-1}_T \land (i,j) \in q^t_T \}
$$
$$
out^{(i,j)}_t = \sum_{T \in Q}\{t > 1 | (i,j) \in q^{t}_T \land (i,j) \notin q^{t+1}_T \}
$$

&emsp;&emsp;We can represent the flows of a region as a tensor $X_t \in R^{2 \times I \times J}$, where one dimension is associated with the in-flow $(X_t)_{1,i,j} = in^{(i,j)}_t$ and the other with the out-flow $(X_t)_{2,i,j} = out^{(i,j)}_t$. Therefore, crowd flow prediction is the task of predicting $X_{t+\Delta}$ given the historical flow ${X_t|1, ... , X_t|t}$. If $\Delta > 1$, the problem is named multi-step crowd flow prediction.

&emsp;&emsp;A variant of crow flow prediction aims at forecasting the entire origin-destination matrix given the hisotical observations of crowd flows.


### 3. Metrics

&emsp;&emsp;The performance of crowd flow predictors is evaluated as the error between the empirical crowd flows and the predicted ones. E.g. Mean Absolute Errpr(MAE), Root Mean Squared Error(RMSE), Mean Absolute Percent Error(MAPE).

### 4. Related papers

