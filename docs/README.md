<p><img src="./docs/gml_logo.jpg" alt="gml logo" title="GML &amp; tracks" /></p>     
--------------------------------------------------------------------------------

# Gradual Machine Learning(GML) framework
English | [简体中文](./README-zh_CN.md)                

gml is a Python package that provides for Gradual Machine Learning


  - [Introuduction](#introuduction)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API](#api)
  - [FAQ](#faq)
  - [Contributing](#contributing)
  - [Related Efforts](#related-efforts)
  - [The Team](#the-team)
  - [License](#license)


## Introuduction
   ### Goal
   In order to support more and more applications of gradual machine learning and help researchers quickly complete model deployment and testing, this project aims to develop a general gradual machine learning platform. Gradual machine learning mainly includes three major steps: easy instance labeling, feature extraction and influence modeling, and gradual inference. According to the different steps of gradual machine learning, multiple unified algorithms are designed and implemented. Currently, several types of factor graphs such as single-factor non-parameterize, binary-factor non-parameterize, and single-factor parameterize are supported, and support factor graph parameter learning algorithm based on stochastic gradient descent and batch gradient descent
   ### Flowchat
   <p><img src="./docs/flowchat.jpg" alt="gml flowchat" title="flowchat &amp; tracks" /></p>    


## Installation
    pip install gradual-ml
## Usage
 Before using this framework, you need to prepare your data according to the following [Data structure description](./docs/data_structures.md) .

After preparing the data, you can use this framework as follows.
First you need to prepare a configuration file [example](./examples/example.config),and set some [parameters](./docs/parameter_description.md)
``` python 
[para]
top_m = 2000  
top_k = 10
top_n = 1
update_proportion = -1   
optimization_threshold = -1
balance = False
learning_epoches = 500
inference_epoches = 500
learning_method = sgd
n_process = 1
out = False
```
Then, call GML as follows:
  ```python            
  with open('variables.pkl', 'rb') as v:
      variables = pickle.load(v)
  with open('features.pkl', 'rb') as f:
      features = pickle.load(f)
  graph = GML.initial("alsa.config", variables, features)
  graph.inference()
  ```
Here is an [example](examples/example.py) you can refer.

