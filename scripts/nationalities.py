import models

nationalities = {
    'n': 0.0,
    'nationalities': {},
}

for response in models.Response.objects.all():
    touchpoints = map(lambda tp: tp.touchpoint_type, response.metadata.touchpoints)
    if -4 in touchpoints:
        nationalities['n'] += 1.0
        if response.overview is not None:
            if response.overview.country is not None and response.overview.country != 'xx':
                if response.overview.country not in nationalities['nationalities']:
                    nationalities['nationalities'][response.overview.country] = 0.0
                nationalities['nationalities'][response.overview.country] += 1.0

print "2015: {}".format(nationalities['n'])
result = result = sorted(nationalities['nationalities'].items(), key=lambda x: x[1], reverse=True)
for i in result[:9]:
    print "{}: {:3.2f}%".format(i[0], i[1] / nationalities['n'] * 100)
