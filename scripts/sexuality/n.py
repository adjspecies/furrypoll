import models

n = 0

for response in models.Response.objects.all():
    touchpoints = map(lambda tp: tp.touchpoint_type, response.metadata.touchpoints)
    if -3 in touchpoints:
        n += 1

print "n = {}".format(n)
