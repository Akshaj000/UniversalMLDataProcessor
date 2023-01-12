import pandas as pd
import enum

class ScalerEnum(enum.Enum):
    STANDARDAZATION = "Standard"
    NORMALIZATION = "Normalize"

class TypeEnum(enum.Enum):
    REGRESSION = "Regression"
    CLASSIFICATION = "Classification"

class FillNullEnum(enum.Enum):
    MEAN = "mean"
    DROP = "drop"

def preprocessor(
    target: str,
    fill_null: FillNullEnum,
    split_percent: float,
    can_apply_smote: bool,
    scaler: ScalerEnum,
    data = None,

):
    from .data_preprocessing import DataPreprocessing
    if 'Unnamed: 32' in data.columns:
        data.drop(columns=['Unnamed: 32'], inplace=True)
    data_pre_object = DataPreprocessing(data)
    data_pre_object.encode_categorical_columns()
    if fill_null == "mean":
        data_pre_object.handle_null("mean")
    else:
        data_pre_object.drop_null()
    data_pre_object.out_in(target)
    data_pre_object.split(split_percent)
    if can_apply_smote:
        data_pre_object.apply_smote_data()
    if scaler == ScalerEnum.STANDARDAZATION.value:
        data_pre_object.standardize_or_normalize("Standard")
    elif scaler == ScalerEnum.NORMALIZATION.value:
        data_pre_object.standardize_or_normalize("Normalize")
    return data_pre_object


def fit(
    data_pre_object = None,
    type: TypeEnum = None,

): 
    from .regression_class import MachineLearningRegression
    from .classification_class import MacineLearningClassification
    if type is None:
        return False
    if type == TypeEnum.REGRESSION.value:
        models = MachineLearningRegression(data_pre_object)
    elif type == TypeEnum.CLASSIFICATION.value:
        models = MacineLearningClassification(data_pre_object)
    return models.evaluvate()

    