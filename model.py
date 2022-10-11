{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bd42586c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "from sklearn import datasets\n",
    "iris=datasets.load_iris()\n",
    "x=iris.data\n",
    "y=iris.target\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "03e17206",
   "metadata": {},
   "outputs": [],
   "source": [
    "#labels for iris dataset\n",
    "labels ={\n",
    " 0: \"setosa\",\n",
    " 1: \"versicolor\",\n",
    " 2: \"virginica\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3a6948bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#split the data set\n",
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.50)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "55317fba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Using decision tree algorithm\n",
    "from sklearn import tree\n",
    "classifier=tree.DecisionTreeClassifier()\n",
    "classifier.fit(x_train,y_train)\n",
    "predictions=classifier.predict(x_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6c3b73f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#export the model\n",
    "pickle.dump(classifier, open('model.pkl','wb'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f8b5c35a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Worlds\n",
      "virginica\n"
     ]
    }
   ],
   "source": [
    "#load the model and test with a custom input\n",
    "model = pickle.load( open('model.pkl','rb'))\n",
    " = [[6.7, 3.3, 5.7, 2.1]]\n",
    "predict = model.predict(x)\n",
    "print(\"Hello Worlds\")\n",
    "print(labels[predict[0]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "22eda948",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[6.7, 3.3, 5.7, 2.1]]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f53245cf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
