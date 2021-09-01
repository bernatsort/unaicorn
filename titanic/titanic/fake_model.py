def fake_predict(user_age):
    if user_age > 10:
        prediction = 'survived'
    else:
        prediction = 'died'
    return prediction
