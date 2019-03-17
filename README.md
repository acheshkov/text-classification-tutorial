# Text Classification Tutorial

This repository shows how to get a baseline model for test classification task. We experimented with following models: 

* Multinomial Naive Bayes
* Bernoulli Naive Bayes 
* Logistic Regression
* SVM


## Jupyter Notebook 

* [Google Colab](https://colab.research.google.com/drive/18dq83Zs6pCdJiUiiL0h7d4o-vPZbK6vT)
* [static view in this repo](https://github.com/acheshkov/text-classification-tutorial/blob/master/model/notebook.ipynb)

## Docker

This repository also provides an example how to wrap your model in simple web API interface. For this purpose we use Flask and docker container.

To build image 

```console
$ docker build -t IMAGE_TAG_NAME .
```

To run container specify port you need

```console
$ docker run -d -p PORT:80 IMAGE_TAG_NAME
```

Since Web API deployed you can call it

```console
$ curl -d '{"text": "any text to classify"}'  https://YOUR_BACKEND:PORT/classify
```