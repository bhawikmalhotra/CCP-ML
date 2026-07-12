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