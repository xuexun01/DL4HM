## Flow Generation

*@Date: 2022-10-1*

*@Author: xuexun01*

- [Flow Generation](#flow-generation)
  - [1. Introduction](#1-introduction)
  - [2. Problem definition](#2-problem-definition)
  - [3. Metrics](#3-metrics)
  - [4. Related papers](#4-related-papers)

### 1. Introduction

&emsp;&emsp;Flow genetation consists of generating the flows between a set of geographic locations, given some locations' characterisitics and without any information about the real flows. Flow generation is crucial to many aspects of our society, such as transport planning and spatial economics to reduce inequalities, and the modeling of epidemic spreding patterns.

&emsp;&emsp;Solving flow generation requires capturing the spatial patterns of close and distant flows, dependencies in the mobility network, and the characteristics of the locations.


### 2. Problem definition

&emsp;&emsp;Given a tessellation $\mathcal{G}$ over a region $A$, the flow, $y(g_i, g_j)$, between locations $g_i$ and $g_j$ represents the number of people moving from $g_i$ to $g_j$. The total outflow, $O_i$, from location $g_i$, is the total number of people originating from location $g_i$, $O_i = \sum_j{y(g_i,g_j)}$. Flow generation aims to estimate $y(g_i,g_j)  \forall i,j \in \mathcal{G}, i \neq j$.

### 3. Metrics

&emsp;&emsp;Flow generation is commonly evaluated as the CPC(Common Part of Commuters) between real and generated flows. Other metrics commonly used for this purpose are MAE, RMSE and MAPE.

### 4. Related papers