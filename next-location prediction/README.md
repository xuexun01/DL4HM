## Next-Location Prediction

*@Date: 2022-9-18*
*@Author: xuexun01*

**Context**
[TOC]

### 1. Introduction

&emsp;&emsp;Next-location prediction is about forecasting which location an individual will visit given historical data about their mobility. It may help policymakers organize the public transportation network, urban planners decide a city's future developments, and transportation companies provide citizens with a better service in terms of traffic reduction and ease of mobility.

&emsp;&emsp;**What info should next-location prediction capture?**

* spatial, temporal and social-geographic dimensions of human mobility

    individual spatial patterns & individual temporal patterns

* extenral factors

    e.g. weather conditions

* user preferences

    e.g. POIs, friendships


### 2. Problem definition


### 3. Metrics

&emsp;&emsp;Next-location prediction can be intended as a regression task or a multi-class classification task. Both have their own metric. Regardless of metrics, next-location preditors output a ranking of the probability of each location to be an individual's next destination. 

* regression task

    Haversine distance, equirectangular distance

* multi-class classification task

    accuracy, recall, F1-score, Mean Average Percentage Error, Area Under the Curve


### 4. Related papers

#### 4.1 [DeepMove: Predicting Human Mobility with Attentional Recurrent Networks](./DeepMove%3A%20Predicting%20Human%20Mobility%20with%20Attentional%20Recurrent%20Networks.pdf)

Contribution:

* propose an attentional recurrent model, DeepMove to predict human mobility from long-range and sparse trajectories.

* design two attention mechanisms: embedding encode module and sequential encode module

Model Architecture:

![DeepMove](../images/DeepMove_architecture.png)