import models

responses = {}

for response in models.Response.objects.all():
    if response.sexuality and response.sexuality.dom_or_sub:
        for dom_or_sub in response.sexuality.dom_or_sub:
            if dom_or_sub.option not in responses:
                responses[dom_or_sub.option] = {}
            if dom_or_sub.value not in responses[dom_or_sub.option]:
                responses[dom_or_sub.option][dom_or_sub.value] = 0
            responses[dom_or_sub.option][dom_or_sub.value] += 1

print "option,very submissive, somewhat submissive, neither dom nor sub, somewhat dominant, very dominant"
for interest, levels in responses.items():
    print "{},{},{},{},{},{}".format(
        interest,
        levels[-2],
        levels[-1],
        levels[0],
        levels[1],
        levels[2])
