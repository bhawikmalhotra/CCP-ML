# Customer Churn Predictor

Dataset ===> WA_Fn-UseC_-Telco-Customer-Churn

Start :-

Dataframe analysis

        - shape             (7043, 21)  
        - col               21

        ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
        'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'],

EDA

- Most of the People not churn                     |    about 73 %  |  Not used
- Gender is equaly distributed                     |    50- 50      |  Not used
- Contract type
    Month-to-month    55.019168
    Two year          24.066449                     |                | Used
    One year          20.914383


- monthly charges                   | related    | used
- tenure                            | related    | used     


useful features 

features = [
    "Partner",
    "Dependents",
    "Contract",
    "Tenure",
    "MonthlyCharges",
    "OnlineSecurity",
    "TechSupport",
    "InternetService",
    "PaymentMethod"
]

target = "Churn"


- After one hot encoding and columns renaming 

[      'tenure', 'MonthlyCharges', 'IsPartner', 'HasDependents',
       'Contract_OneYear', 'Contract_TwoYear', 'NoInternet_OnlineSecurity',
       'HasOnlineSecurity', 'NoInternet_TechSupport', 'HasTechSupport',
       'FiberOptic', 'NoInternet', 'Payment_CreditCard',
       'Payment_ElectronicCheck', 'Payment_MailedCheck']




creating models 

- Logistic Regression                       | Generally Good 80%  ✅  

    Accuracy : 0.808374733853797
    Precision: 0.6666666666666666
    Recall   : 0.5522788203753352
    F1 Score : 0.6041055718475073
    ROC AUC  : 0.7264289854772429

    Train Accuracy: 0.7932197373091942
    Test Accuracy : 0.808374733853797


- Decision tree Classifier                  |    Overfitting ❌ 
    Accuracy : 0.7317246273953159
    Precision: 0.4931506849315068
    Recall   : 0.48257372654155495
    F1 Score : 0.4878048780487805
    ROC AUC  : 0.6520011489850631

    Train Accuracy: 0.9317246273953159
    Test Accuracy : 0.7317246273953159

## Ensebble Learning

- Random Forest                               |  significantly Improved Our Model ✅  , Fixed Overfitting

    Accuracy : 0.808374733853797
    Precision: 0.6666666666666666
    Recall   : 0.5522788203753352
    F1 Score : 0.6041055718475073
    ROC AUC  : 0.7264289854772429

    Train Accuracy: 0.8454029108981186
    Test Accuracy : 0.8062455642299503