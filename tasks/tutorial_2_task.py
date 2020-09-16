from tutorial.functions import generate_dataset
from tutorial.functions import preprocess_data
from tutorial.functions import train_model
from tutorial.functions import make_predictions
from tutorial.functions import score_model
from tutorial.utils import save_json

def generate_train_predict(dataset_name, model_name):
    # Reading the data
    data = generate_dataset(dataset_name)

    # Processing the data
    features, labels = preprocess_data(data)
    
    # Training the model
    model = train_model(features, labels, model_name)
    
    # Making predictions
    predictions = make_predictions(model, features)
    
    # Calculating the accuracy of the model
    accuracy = calculate_accuracy(predictions, labels)
    
    # Saving the prediction and score as results
    result = {}
    result['predictions'] = predictions.tolist()
    result['accuracy'] = accuracy
    save_json(result, 'result.json')
