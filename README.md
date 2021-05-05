# COVID19-xray-classifier

Utilizing Deep Learning to detect COVID-19 from x-ray images

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/covidlog.jpg)

**Datasets used:** 

- [COVID-19 normal-covid Images]()

# Usage 1 :Train and Test
**train and evaluate the model:** 
Open the notebook COVID19_classifier_training_and_evaluation.ipynb and run all scripts.
**Results:**
![Classification Report]()
![Confusion Matrix Normal]()
![Confusion Matrix Covid]()
![Roc Curve]()
![Sample Output]()
![Sample Output1]()
![Sample Output2]()

# Usage 1 :Flask application
Before running the script, run pip install -r requirements.txt so that you can install all the necessary dependencies.

Run the application : python covid_flask.py


**Upload Images:**

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/upload.png)

**Test Normal Case:**

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/normal.png)

**Test Positive Case:**

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/covid.png)
