import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Initialize an empty list of user requests and their classifications
requests = []
classes = []

# Define the maximum number of requests to keep in memory
MAX_REQUESTS = 1000

# Define the number of neighbors to use in the k-NN algorithm
N_NEIGHBORS = 5

# Define the k-NN classifier
knn = KNeighborsClassifier(n_neighbors=N_NEIGHBORS)

# Define a function to process a user query and generate a response
def process_query(query):
    # Add the current request to the list of requests
    requests.append(query)

    # Limit the number of requests to MAX_REQUESTS
    if len(requests) > MAX_REQUESTS:
        requests.pop(0)

    # Train the k-NN classifier on the current list of requests and their classifications
    X = np.array(requests).reshape(-1, 1)
    y = np.array(classes)
    knn.fit(X, y)

    # Use the k-NN classifier to classify the current request
    prediction = knn.predict(np.array([query]).reshape(-1, 1))[0]

    # Add the current request and its classification to the list of requests and classifications
    classes.append(prediction)

    # Limit the number of classifications to MAX_REQUESTS
    if len(classes) > MAX_REQUESTS:
        classes.pop(0)

    # Generate a response based on the classification
    if prediction == "greeting":
        response = "Hello! How can I help you today?"
    elif prediction == "farewell":
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm sorry, I didn't understand your query."

    return response
