import models

russians = {
    'n': 0.0,
    'russians': 0.0,
}

for response in models.Response.objects.all():
    touchpoints = map(lambda tp: tp.touchpoint_type, response.metadata.touchpoints)
    if -4 in touchpoints:
        russians['n'] += 1.0
        if response.overview is not None:
            if response.overview.country == 'ru':
                russians['russians'] += 1.0

print "2015: {:3.2f}%".format(russians['russians'] / russians['n'] * 100)
