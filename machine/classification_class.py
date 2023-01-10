class MacineLearningClassification:
    def __init__(self,data_pr,models=None):
        self.data = data_pr.data
        self.train_features = data_pr.train_features
        self.train_target = data_pr.train_target
        self.test_features = data_pr.test_features
        self.test_target = data_pr.test_target
        if models==None:
            from sklearn.linear_model import LogisticRegression
            from sklearn.tree import DecisionTreeClassifier
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.naive_bayes import BernoulliNB,GaussianNB
            from sklearn.neighbors import KNeighborsClassifier
            models = [LogisticRegression(),DecisionTreeClassifier(),RandomForestClassifier(),BernoulliNB(),GaussianNB(),KNeighborsClassifier()]
        self.model_evaluvation_dict = {str(i).replace("()",""):{'model_object':i} for i in models}
        self.model_prediction = {str(i).replace("()",""):None for i in models}
    def fit(self):
        for model,dic in self.model_evaluvation_dict.items():
            self.model_evaluvation_dict[model]['model_object'].fit(self.train_features,self.train_target)
            self.model_prediction[model] = self.model_evaluvation_dict[model]['model_object'].predict(self.test_features)
    def Score_test_data(self):
        for model,dic in self.model_evaluvation_dict.items():
            self.model_evaluvation_dict[model]['score on test data'] = self.model_evaluvation_dict[model]['model_object'].score(self.test_features,self.test_target)*100
    def create_confusion_matrix(self):
        from sklearn.metrics import confusion_matrix
        for model,dic in self.model_evaluvation_dict.items():
            self.model_evaluvation_dict[model]['confusion matrix for test data'] = confusion_matrix(self.test_target,self.model_prediction[model]).tolist()
    def create_f1_precision_recall(self):
        from sklearn.metrics import f1_score,recall_score,precision_score
        for model,dic in self.model_evaluvation_dict.items():
            self.model_evaluvation_dict[model]['f1 score for test data'] = f1_score(self.test_target,self.model_prediction[model],average='macro')*100
            self.model_evaluvation_dict[model]['precision for test data'] = precision_score(self.test_target,self.model_prediction[model],average='macro')*100
            self.model_evaluvation_dict[model]['recall for test data'] = recall_score(self.test_target,self.model_prediction[model],average='macro')*100
    def evaluvate(self):
        self.fit()
        self.Score_test_data()
        self.create_confusion_matrix()
        self.create_f1_precision_recall()
        for model in self.model_evaluvation_dict:
            del self.model_evaluvation_dict[model]['model_object']
        return self.model_evaluvation_dict