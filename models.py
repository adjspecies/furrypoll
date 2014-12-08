import datetime
from furrypoll import db

class Touchpoint(db.EmbeddedDocument):
    """ Store a touchpoint of a user's interaction with the survey

    touchpoint_type: One of the following:
        0 - survey created
        -1, -2, -3 - Answers to page 1, 2, or 3
        -4 - survey completed
        -5 - survey cancelled
        -6 - survey marked as coming from a duplicate IP
        1...n - answers to question 1...n
    """
    touchpoint_type = db.IntField()
    timestamp = db.DateTimeField(default=datetime.datetime.now, required=True)

class NumberPerOption(db.EmbeddedDocument):
    option = db.StringField(max_length=30)
    value = db.IntField()

class StringPerOption(db.EmbeddedDocument):
    option = db.StringField(max_length=30)
    value = db.StringField(max_length=30)

class PotentiallySubjectiveResponse(db.EmbeddedDocument):
    subjective = db.BooleanField()
    value = db.StringField(max_length=2000)

class GenderIdentityCoordinates(db.EmbeddedDocument):
    male = db.FloatField()
    female = db.FloatField()
    male_quantized = db.IntField()
    female_quantized = db.IntField()

class Character(db.EmbeddedDocument):
    species_category = db.StringField(max_length=200)
    species_text = db.ListField(db.EmbeddedDocumentField('PotentiallySubjectiveResponse'))
    primary_character = db.BooleanField()
    deprecated_character = db.BooleanField()
    reason = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    # Add year bounds (from when to when)

class Sexuality(db.EmbeddedDocument):
    sex_importance = db.ListField(db.EmbeddedDocumentField('NumberPerOption'))
    interests = db.ListField(db.EmbeddedDocumentField('StringPerOption'))
    other_interests = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')

class ResponseMetadata(db.EmbeddedDocument):
    client_ip = db.StringField(max_length=16, required=True)
    client_ua = db.StringField(required=True)
    touchpoints = db.ListField(db.EmbeddedDocumentField('Touchpoint'))

class Overview(db.EmbeddedDocument):
    birth_month = db.IntField()
    birth_year = db.IntField()
    clinical_sex = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    gender_identity = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    gender_identity_coords = db.EmbeddedDocumentField('GenderIdentityCoordinates')
    sexual_orientation = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    country = db.StringField(max_length=2, default='xx')
    state = db.StringField(max_length=2, default='xx')
    location_size = db.StringField(max_length=20)
    race = db.ListField(db.EmbeddedDocumentField('PotentiallySubjectiveResponse'))
    spirituality = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    politics_economic = db.EmbeddedDocumentField('NumberPerOption')
    politics_social = db.EmbeddedDocumentField('NumberPerOption')
    occupation = db.ListField(db.EmbeddedDocumentField('PotentiallySubjectiveResponse'))
    education = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    relationship = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    partner_is_furry = db.BooleanField()
    long_distance_relationship = db.BooleanField()
    open_relationship_romantic = db.BooleanField()
    open_relationship_sexual = db.BooleanField()
    how_furry = db.IntField()
    how_long_known = db.FloatField()
    how_long_member = db.FloatField()
    who_knows = db.StringField(max_length=30)
    non_furries_general_response = db.StringField(max_length=30)
    non_furries_personal_response = db.StringField(max_length=30)
    non_furries_perception_accuracy = db.StringField(max_length=30)
    how_human = db.EmbeddedDocumentField('PotentiallySubjectiveResponse')
    gender_in_furry = db.StringField(max_length=30)
    gender_in_furry_coords = db.EmbeddedDocumentField('GenderIdentityCoordinates')
    furry_activities = db.ListField(db.EmbeddedDocumentField('NumberPerOption'))
    furry_activities_opinion = db.ListField(db.EmbeddedDocumentField('NumberPerOption'))
    non_furry_activities = db.ListField(db.EmbeddedDocumentField('NumberPerOption'))
    self_described = db.ListField(db.StringField(max_length=30))
    furry_importance = db.ListField(db.EmbeddedDocumentField('NumberPerOption'))
    conventions = db.ListField(db.StringField(max_length=30))
    conventions_other = db.StringField(max_length=1000)
    furry_websites = db.ListField(db.EmbeddedDocumentField('StringPerOption'))
    characters = db.ListField(db.EmbeddedDocumentField('Character'))

class Response(db.Document):
    # survey_id = db.StringField(max_length=255, required=True)
    overview = db.EmbeddedDocumentField('Overview')
    psychographic_battery = db.ListField(db.EmbeddedDocumentField('NumberPerOption'))
    sexuality = db.EmbeddedDocumentField('Sexuality')
    metadata = db.EmbeddedDocumentField('ResponseMetadata')

    meta = {
        'allow_inheritance': True,
        'collection': 'responses'
    }
