# Text Classification Tutorial

This repository shows how to get a baseline model for test classification task. We experimented with following models: 

* Multinomial Naive Bayes
* Bernoulli Naive Bayes 
* Logistic Regression
* SVM


## Jupyter Notebook 

Here you can find a notebook with code to seek for a baseline model.

* [Google Colab](https://colab.research.google.com/drive/18dq83Zs6pCdJiUiiL0h7d4o-vPZbK6vT)
* [static view in this repo](https://github.com/acheshkov/text-classification-tutorial/blob/master/model/notebook.ipynb)

## Docker

This repository also provides an example how to wrap your model in simple web API interface. For this purpose we use Flask and docker container.

You can either use public image `acheshkov/text-clf` from docker hub or build your own. To build own put model file `model.joblib` to `model` folder and execute:

```console
$ docker build -t IMAGE_TAG_NAME .
```


To run container specify port you need:

```console
$ docker run -d -p PORT:80 IMAGE_TAG_NAME
```

or use existing image:

```console
$ docker run -d -p PORT:80 acheshkov/text-clf
```

Since Web API deployed you can call it

```console
$ curl -d '{"text": "any text to classify"}'  https://YOUR_BACKEND:PORT/classify
```