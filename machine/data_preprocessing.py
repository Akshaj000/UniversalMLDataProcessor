class DataPreprocessing:
    def __init__(self,data):
        self.data = data
        from warnings import filterwarnings
        filterwarnings("ignore")
        self.objects=DataPreprocessing.initialize()
        self.input = None
        self.output = None
        self.features = list(data.columns)
        self.output_name = None
        self.train_features,self.train_target,self.test_target,self.test_features = None,None,None,None
    def drop_null(self):
        self.data.dropna(axis=0,inplace=True)
    def initialize():
        from sklearn import preprocessing,model_selection,decomposition
        return {
                'Standard scaler':preprocessing.StandardScaler,
                'Min Max Scalar':preprocessing.MinMaxScaler,
                'PCA':decomposition.PCA,
                'train test split':model_selection.train_test_split,
               }
    def out_in(self,output_name):
        self.input = self.data.drop(output_name,axis=1)
        self.output = self.data[output_name]
        self.features.remove(output_name)
        self.output_name = output_name
    def apply_count_vectorize(self,col,count_vect_obj=None):
        if count_vect_obj ==None:
            from sklearn.feature_extraction.text import CountVectorizer
            self.objects['Countvec_'+col] = CountVectorizer()
            self.data[col] = self.objects['Countvec_'+col].fit_transform(self.data[col])
        else:
            self.objects['Countvec_'+col] = count_vect_obj
            self.data[col] = self.objects['Countvec_'+col].fit_transform(self.data[col])
    def split(self,test_percent,rs = 42):
         self.train_features,self.test_features,self.train_target,self.test_target = self.objects['train test split'](self.input,self.output,test_size=test_percent,random_state=rs)
    def get_object_column(self):
        import numpy as np
        edit_col = [i for i in self.features if self.data[i].dtype == np.object_]
        return edit_col
    def encode_categorical_columns(self):
        import numpy as np
        from sklearn.preprocessing import LabelEncoder
        label_encoder_objects ={}
        edit_columns = self.get_object_column()
        for col in edit_columns:
            label_object = LabelEncoder()
            self.data[col]=label_object.fit_transform(self.data[col])
            label_encoder_objects[col+"_encoder_object"] = label_object
        self.objects['Label_Encoder'] = label_encoder_objects
    def change_columns(self,columns):
        self.data = self.data[columns]
    def apply_smote_data(self):
        from imblearn.over_sampling import SMOTE
        smote_object = SMOTE()
        self.train_features,self.train_target = smote_object.fit_resample(self.train_features,self.train_target)
        self.objects['Smote object'] = smote_object
    def standardize_or_normalize(self,scale_type=None):
        if scale_type == "Standard":
            from pandas import DataFrame as df
            scale_object  = self.objects['Standard scaler']()
            self.train_features=df(data = scale_object.fit_transform(self.train_features),columns = self.features)
            self.test_features = df(data = scale_object.fit_transform(self.test_features),columns = self.features)
        elif scale_type == "Normalize":
            from pandas import DataFrame as df
            scale_object  = self.objects['Min Max Scalar']()
            self.train_features=df(data = scale_object.fit_transform(self.train_features),columns = self.features)
            self.test_features = df(data = scale_object.fit_transform(self.test_features),columns = self.features)