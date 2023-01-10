class MachineLearningRegression:
    def __init__(self,data_pr,models=None):
        self.data = data_pr.data
        self.train_features = data_pr.train_features
        self.train_target = data_pr.train_target
        self.test_features = data_pr.test_features
        self.test_target = data_pr.test_target
        if models == None:
            from sklearn.linear_model import LinearRegression,Ridge,Lasso
            from sklearn.tree import DecisionTreeRegressor
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.neighbors import KNeighborsRegressor
            models = [LinearRegression(),Ridge(),Lasso(),DecisionTreeRegressor(),RandomForestRegressor(),KNeighborsRegressor()]
        self.model_evaluvation_dict = {str(i).replace("()",""):{'model_object':i} for i in models}
        self.model_prediction = {str(i).replace("()",""):None for i in models}
    def fit(self):
        for model,dic in self.model_evaluvation_dict.items():
            self.model_evaluvation_dict[model]['model_object'].fit(self.train_features,self.train_target)
            self.model_prediction[model] = self.model_evaluvation_dict[model]['model_object'].predict(self.test_features)
    def Score_test_dataset(self):
        from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_absolute_percentage_error
        metrics = {'r2 score':r2_score,'MAE':mean_absolute_error,'MSE':mean_squared_error,'MAPE':mean_absolute_percentage_error}
        for model,dic in self.model_evaluvation_dict.items():
            for metric,obj in metrics.items():
                self.model_evaluvation_dict[model][metric] = obj(self.model_prediction[model],self.test_target)
    def evaluvate(self):
        self.fit()
        self.Score_test_dataset()
        for model in self.model_evaluvation_dict:
            del self.model_evaluvation_dict[model]['model_object']
        return self.model_evaluvation_dict