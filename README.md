# COVID19-xray-classifier

Utilizing Deep Learning to detect COVID-19 from x-ray images

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/covidlog.jpg)

**Datasets used:** 

- [COVID-19 normal-covid Images]()

# Usage 1 :Train and Test
## train and evaluate the model:** 
Open the notebook COVID19_classifier_training_and_evaluation.ipynb and run all scripts.
## Results:**
**Classification Report:**
![Classification Report](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/classification_report.png)
**Confusion Matrix Normal Case:**
![Confusion Matrix Normal](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/Confusion_matrix_nor.png.png)
**Confusion Matrix Covid Case:**
![Confusion Matrix Covid](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/Confusion_matrix_nonnor.png)
**Confusion Roc Curve:**
![Roc Curve](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/roc_curve.png)
**Outputs:**
![Sample Output](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/sample_output.png)
![Sample Output1](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/sample_output2.png)
![Sample Output2](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/train_val/helper_images/sample_output_3.png)

# Usage 1 :Flask application
Before running the script, run pip install -r requirements.txt so that you can install all the necessary dependencies.

Run the application : python covid_flask.py


**Upload Images:**

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/upload.png)

**Test Normal Case:**

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/normal.png)

**Test Positive Case:**

![Intro figure](https://github.com/GuesmiAbd/detect_covid_flask/blob/main/images/covid.png)
