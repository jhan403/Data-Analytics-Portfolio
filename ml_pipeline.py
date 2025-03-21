import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        data = pd.read_csv(self.filepath)
        data = data.dropna()  # Drop all null values
        return data

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, X):
        return self.scaler.fit_transform(X)

class Model:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

class Evaluator:
    @staticmethod
    def evaluate(y_test, y_pred):
        return accuracy_score(y_test, y_pred)

class MLPipeline:
    def __init__(self, data_loader, preprocessor, model, evaluator):
        self.data_loader = data_loader
        self.preprocessor = preprocessor
        self.model = model
        self.evaluator = evaluator

    def run(self):
        data = self.data_loader.load_data()
        X = data.drop(columns=['id', 'diagnosis'], axis=1)
        y = data['diagnosis']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_train = self.preprocessor.preprocess(X_train)
        X_test = self.preprocessor.preprocess(X_test)
        
        self.model.train(X_train, y_train)
        y_pred = self.model.predict(X_test)
        
        accuracy = self.evaluator.evaluate(y_test, y_pred)
        print(f'Accuracy: {accuracy}')

    def predict_batch(self, records):
        records_df = pd.DataFrame(records)
        records_df = records_df.dropna()  # Drop all null values
        records_preprocessed = self.preprocessor.preprocess(records_df)
        predictions = self.model.predict(records_preprocessed)
        return predictions

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run ML pipeline on a dataset.')
    parser.add_argument('--file', type=str, default='benign_malignant_tumor.csv', help='Path to the dataset file')
    parser.add_argument('--batch', type=str, help='Batch of records to predict in JSON format')
    args = parser.parse_args()
    
    data_loader = DataLoader(args.file)
    preprocessor = Preprocessor()
    model = Model()
    evaluator = Evaluator()
    
    pipeline = MLPipeline(data_loader, preprocessor, model, evaluator)
    pipeline.run()
    
    if args.batch:
        batch_data = pd.read_csv(args.batch)
        batch_data = batch_data.dropna()  # Drop all null values from batch data
        batch_X = batch_data.drop(columns=['id', 'diagnosis'], axis=1)
        batch_X = preprocessor.preprocess(batch_X)
        batch_predictions = model.predict(batch_X)
        print(f'Batch Predictions: {batch_predictions}')