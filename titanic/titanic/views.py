from django.shortcuts import render

# import fake_model.py
    # from this folder (.)
from . import fake_model
# import ml_predict.py
from . import ml_predict

# function for any single page that I want to have in my website.

def home(request):
    return render(request, 'index.html')
# second page
def result(request):
    # In our function result, we want to get the info from the Form in index.html
    # Now we're able to get that information and we're able to provide it to our result.html.
    # we cast this into an integer because in our function fake_predict it treats as it is an integer and here as it is a string

    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = int(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])

    # Add a string to the user_input_age variable
    # user_input_age += ' is the age!'

    # prediction = fake_model.fake_predict(user_input_age)

    prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked,title)
    return render(request, 'result.html', {'prediction': prediction})
