## Deep Learning for Human Mobility

*@Date: 2022-9-16*

*@Author: xuexun01*

This repository is constructed referring to the paper *A survey on Deep learning for Human Mobility*.

- [Deep Learning for Human Mobility](#deep-learning-for-human-mobility)
    - [1. Introduction](#1-introduction)
    - [2. Task taxonomy](#2-task-taxonomy)
    - [3. Deep learning models used in human mobility](#3-deep-learning-models-used-in-human-mobility)


***

#### 1. Introduction

&emsp;&emsp;**Human Mobility** studys mainly about individual and collective mobility patterns, or the generation model that can capture and simulate the spatiotemporal structures and regularities in human trahectories.

&emsp;&emsp;Nowadays, the significance of human mobility field is increasing day by day. It's beneficial to the applications such as disease spreading, urban planning, traffic forecasting, and more are. Meanwhile, the proliferation of digital mobility data ,the surge of computing power and the emerging of effective deep learning method, triggered the applicaiton of deep learning to human mobility.

&emsp;&emsp;However, predicting mobility is not trivial beacuse of three challenges:

* the complex sequential transition regularities exhibited with time-dependent and high-order nature.
* the multi-level periodicity of human mobility.
* the heterogeneity and sparsity of the collected trajectory data.

&emsp;&emsp;The traditional method used in human mobility are mostly pattern-based methods (discover pre-defined mobility patterns and then predict future locations based on these extracted patterns), or model-based method(leverage sequential statistical models to capture the transition regularities of human movements and learn the model parameters from the given training corpus). Notably, they require a considerable effort in feature enginnering and cannot capture long-range temporal and spatial dependencies. In addition, traitional methods still have shortcomings when facing the above challenges. Therefore, deep learning methods are considered.

#### 2. Task taxonomy

&emsp;&emsp;We focus on two categories of tasks: predictive and generative, at present. The following  are the details:

* *next-location prediction*
* *crowd flow prediction*
* *trajectory generation*
* *flow generation*

&emsp;&emsp;**Next-location prediction** is about forecasting which location an individual will visit given historical data about their mobility. And more infos you can get from [here](https://github.com/xuexun01/DL4HM/tree/main/next-location%20prediction).

&emsp;&emsp;**Crowd flow prediction** is the task of forecasting the incoming and outgoing flows of people on a geographic region. And more infos, [here](https://github.com/xuexun01/DL4HM/tree/main/crowd%20flow%20prediction).

&emsp;&emsp;**Trajectory generation** deals with generating synthetic trajectories that can reproduce, realistically, the individual statistical patterns of human mobility. And more details, [here](https://github.com/xuexun01/DL4HM/tree/main/trajectory%20generation).

&emsp;&emsp;**Flow generation** deals with generating realistic flows among locations, given their characteristics and the distance among them, and without any knowledge about the real flows. More details click [here](https://github.com/xuexun01/DL4HM/tree/main/flow%20generation).

#### 3. Deep learning models used in human mobility

|Models|Particularity|
|---|---|
|FCs|commonly used to capture the impact on individual or collective mobility of external feature, weak ability to capture feature|
|RNNs, LSTMs, and GRUs|can efficiently deal with sequential data, but suffer from the vanishing gradient problem|
|CNNs|used to capture spatial patterns in the data|
|Attention mechanisms|widely used for next-location prediction and crowd flow prediction to capture user preferences and highlight relevant historical patterns|
|Generative Models|used to generation realistic trajectories|