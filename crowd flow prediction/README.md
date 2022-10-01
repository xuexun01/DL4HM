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

### 3. Metrics

&emsp;&emsp;The performance of crowd flow predictors is evaluated as the error between the empirical crowd flows and the predicted ones. E.g. Mean Absolute Errpr(MAE), Root Mean Squared Error(RMSE), Mean Absolute Percent Error(MAPE).

### 4. Related papers
