import datetime
from furrypoll import db

class Response(db.Document):
    survey_id = db.StringField(max_length=255, required=True)
    overview = db.EmbeddedDocumentField(Overview)
    psychographic_battery = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    sexuality = db.EmbeddedDocumentField(Sexuality)
    metadata = db.EmbeddedDocumentField(ResponseMetadata)

class Overview(db.EmbeddedDocument):
    birth_month = db.IntField()
    birth_year = db.IntField()
    clinical_sex = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    gender_identity = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    sexual_orientation = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    country = db.StringField(max_length=2, default='xx')
    state_province = db.StringField(max_length=2, default='xx')
    location_size = db.StringField(max_length=20)
    race = db.ListField(db.EmbeddedDocumentField(PotentiallySubjectiveResponse))
    spirituality = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    political_views = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    occupation = db.ListField(db.EmbeddedDocumentField(PotentiallySubjectiveResponse))
    education = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    relationship = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    partner_is_furry = db.BooleanField()
    how_furry = db.IntField()
    how_long_known = db.FloatField()
    how_long_member = db.FloatField()
    who_knows = db.StringField(max_length=30)
    non_furries_general_response = db.StringField(max_length=30)
    non_furries_personal_response = db.StringField(max_length=30)
    non_furries_perception_accuracy = db.StringField(max_length=30)
    how_human = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)
    gender_in_furry = db.StringField(max_length=30)
    furry_activities = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    furry_activities_opinion = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    non_furry_activities = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    self_described = db.ListField(db.StringField(max_length=30))
    furry_importance = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    conventions = db.ListField(db.StringField(max_length=30))
    furry_websites = db.ListField(db.EmbeddedDocumentField(StringPerOption))
    characters = db.ListField(db.EmbeddedDocumentField(Character))

class Character(db.EmbeddedDocument):
    species = db.ListField(db.EmbeddedDocumentField(PotentiallySubjectiveResponse))
    reason = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)

class Sexuality(db.EmbeddedDocument):
    sex_importance = db.ListField(db.EmbeddedDocumentField(NumberPerOption))
    interests = db.ListField(db.EmbeddedDocumentField(StringPerOption))
    other_interests = db.EmbeddedDocumentField(PotentiallySubjectiveResponse)

class NumberPerOption(db.EmbeddedDocument):
    option = db.StringField(max_length=30)
    value = db.IntField()

class StringPerOption(db.EmbeddedDocument):
    option = db.StringField(max_length=30)
    value = db.StringField(max_length=30)

class PotentiallySubjectiveResponse(db.EmbeddedDocument):
    subjective = db.BooleanField(default=False)
    value = db.StringField(max_length=2000)

class ResponseMetadata(db.EmbeddedDocument):
    client_ip = db.StringField(max_length=16, required=True)
    client_ua = db.StringField(required=True)
    touchpoints = db.ListField(db.EmbeddedDocumentField(Touchpoint))

class Touchpoint(db.EmbeddedDocument):
    touchpoint_type = db.StringField(max_length=1) # (c)reated, (r)esponse to page, (s)ubmit, (x)canceled.
    timestamp = db.DateTimeField(default=datetime.datetime.now, required=True)
