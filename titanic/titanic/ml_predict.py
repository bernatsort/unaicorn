# All the information that we need for running a prediction.
# Correct order in the dataframe: pclass, sex, age, sibsp, parch, fare, embarked, title
def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    # we input everything we need
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    # We're opening our model and then we're running the prediction
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction == 0:
        prediction = 'Not survived'
    elif prediction == 1:
        prediction = 'Survived'
    else:
        prediction =  'Error'
    return prediction
