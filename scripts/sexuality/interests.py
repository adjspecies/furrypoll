import models

responses = {}

for response in models.Response.objects.all():
    if response.sexuality and response.sexuality.interests:
        for interest in response.sexuality.interests:
            if interest.option not in responses:
                responses[interest.option] = {}
            for value in interest.value:
                if value not in responses[interest.option]:
                    responses[interest.option][value] = 0
                responses[interest.option][value] += 1

print "option,interested,consume media,create media,participate online,participate in person"
for interest, levels in responses.items():
    print "{},{},{},{},{},{}".format(
        interest,
        levels['interested'],
        levels['consume_media'],
        levels['create_media'],
        levels['participate_online'],
        levels['participate_inperson'])
