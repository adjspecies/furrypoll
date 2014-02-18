from models import PotentiallySubjectiveResponse as PSR

question_options = {
    'clinical_sex': {
        'female': PSR(subjective=False),
        'male': PSR(subjective=False),
        'intersex': PSR(subjective=False),
        'mtf_female': PSR(subjective=False),
        'ftm_male': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'gender_identity': {
        'male': PSR(subjective=False),
        'mostly_male': PSR(subjective=False),
        'both': PSR(subjective=False),
        'mostly_female': PSR(subjective=False),
        'female': PSR(subjective=False),
        'genderqueer': PSR(subjective=False),
        'neutrois': PSR(subjective=False),
        'nonbinary_nos': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'sexual_orientation': {
        'kinsey_0': PSR(subjective=False),
        'kinsey_1': PSR(subjective=False),
        'kinsey_2': PSR(subjective=False),
        'kinsey_3': PSR(subjective=False),
        'kinsey_4': PSR(subjective=False),
        'kinsey_5': PSR(subjective=False),
        'kinsey_6': PSR(subjective=False),
        'pansexual': PSR(subjective=False),
        'omnisexual': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'race': {
        'white': PSR(subjective=False),
        'black': PSR(subjective=False),
        'hispanic': PSR(subjective=False),
        'native_american_pacific_islander': PSR(subjective=False),
        'middle_eastern': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'spirituality': {
        'christian_catholic': PSR(subjective=False),
        'christian_orthodox': PSR(subjective=False),
        'christian_protestant': PSR(subjective=False),
        'christian_other': PSR(subjective=True),
        'muslim': PSR(subjective=False),
        'hindu': PSR(subjective=False),
        'jewish': PSR(subjective=False),
        'pagan': PSR(subjective=False),
        'buddhist': PSR(subjective=False),
        'athiest': PSR(subjective=False),
        'agnostic': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'occupation': {
        'student': PSR(subjective=False),
        'administrative': PSR(subjective=False),
        'government_armed_service': PSR(subjective=False),
        'sales_support': PSR(subjective=False),
        'technical_it': PSR(subjective=False),
        'professional': PSR(subjective=False),
        'service': PSR(subjective=False),
        'vet_animal_related': PSR(subjective=False),
        'creative_furry': PSR(subjective=False),
        'creative_nonfurry': PSR(subjective=False),
        'retired': PSR(subjective=False),
        'unemployed': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'education': {
        'some_highschool': PSR(subjective=False),
        'ongoing_highschool': PSR(subjective=False),
        'graduate_highschool': PSR(subjective=False),
        'some_university': PSR(subjective=False),
        'ongoing_university': PSR(subjective=False),
        'graduate_university': PSR(subjective=False),
        'ongoing_postcollege': PSR(subjective=False),
        'graduate_postcollege': PSR(subjective=False),
        'advanced_degree': PSR(subjective=False),
        'other': PSR(subjective=True),
    },
    'relationship': {
        'single': PSR(subjective=False),
        'casual': PSR(subjective=False),
        'long_term_committed': PSR(subjective=False),
        'legal_non_marriage': PSR(),
        'married': PSR(),
    },
}

political_views = [
    (
        'social',
        '''Social political views''',
        '''More social restrictions (authoritarian)''',
        '''Fewer social restrictions (anarchist)''',
    ),
    (
        'economic',
        '''Economic political views''',
        '''More economic restrictions (regulated)''',
        '''Fewer economic restrictions (laissez-faire)''',
    )
]

psychographic_battery = [
    (
        'faith_and_spirituality',
        '''Faith and spirituality is a good way of understanding the world''',
    ),
    (
        'friends_look_advice',
        '''My friends look to me for advice about movies, music, video games, or pop culture''',
    ),
    (
        'make_rather_than_buy',
        '''In general, I'd rather make something instead of buying it''',
    ),
    (
        'more_talented_than_peers',
        '''I'm more talented than most people in my peer group''',
    ),
    (
        'value_cutting_edge',
        '''I value having cutting-edge technology''',
    ),
    (
        'rather_patronize_small_businesses',
        '''I'd rather patronize a small business than a big company''',
    ),
    (
        'enjoy_creating_things',
        '''Creativity is one of my strongest attributes''',
    ),
    (
        'ahead_of_pop_culture',
        '''Where pop culture is concerned, I'm ahead of the curve''',
    ),
    (
        'tendency_to_overthink',
        '''I admit, I have a tendency to overthink things''',
    ),
    (
        'mass_media_lcd',
        '''Mass media is too 'lowest common denominator' for my tastes''',
    ),
    (
        'enjoy_leading',
        '''I enjoy being able to lead and influence others''',
    ),
    (
        'focus_on_specific_interests',
        '''I tend to focus on a few specific interests of mine''',
    ),
    (
        'too_reliant_on_tech',
        '''People are too reliant on technology these days''',
    ),
    (
        'filesharing_nbd',
        '''Even if technically illegal, file-sharing of copyrighted material isn't that big a deal''',
    ),
    (
        'citizens_politically_active',
        '''It's important for people to be politically active''',
    ),
    (
        'want_to_be_fashionable',
        '''In general, I want to be considered fashionable''',
    ),
    (
        'exciting_rather_than_predictable',
        '''It's better to have an exciting life than one where every day is predictable''',
    ),
    (
        'learning_for_learnings_sake',
        '''I believe in learning for learning's sake -- it doesn't need to have a purpose''',
    ),
    (
        'routine_is_comforting',
        '''I find a sense of routine comforting''',
    ),
    (
        'advertising_is_useful',
        '''Advertising is a useful source of information''',
    ),
    (
        'other_people_think_important',
        '''What other people think of me is important''',
    ),
    (
        'learn_about_universe',
        '''I like learning about how the universe works''',
    ),
    (
        'find_simpler_option',
        '''When something is confusing, it's better to find a simpler option than to spend time trying to figure it out''',
    ),
    (
        'decisions_moral_code',
        '''My decisions are motivated primarily by my moral code''',
    ),
    (
        'people_more_distant',
        '''People are more distant from each other these days''',
    ),
    (
        'first_to_try_new_things',
        '''I'm often the first person in my group of friends to try something new''',
    ),
    (
        'consider_intellectual',
        '''I consider myself to be an intellectual''',
    ),
    (
        'buy_on_impulse',
        '''I have a tendency to buy things on impulse''',
    ),
    (
        'corporations_soulless',
        '''I find corporations, and corporate products, rather soulless and uninspiring''',
    ),
    (
        'enjoy_traveling',
        '''I enjoy traveling and discovering new things and places''',
    ),
]

sex_importance = [
    (
        'self',
        '''how important is sex to you personally, in the context of the furry subculture?''',
    ),
    (
        'fandom',
        '''how important do you think sex is to the furry subculture?''',
    ),
    (
        'others',
        '''how important do you believe sex is to other furries?''',
    ),
    (
        'public',
        '''how important do you think the public &emdash; among those who are aware of it &emdash; believes sex is to the furry subculture?''',
    ),
]

interests = [
    (
        'fursuit_sex',
        '''Fursuit sex''',
    ),
    (
        'babyfur',
        '''Babyfur, cub, AB/DL, or other age-play''',
    ),
    (
        'zoophilia',
        '''Zoophilia''',
    ),
    (
        'plushophilia',
        '''Plushophilia''',
    ),
    (
        'hyper',
        '''Hyper (over-sized) sexual anatomy''',
    ),
    (
        'macro_micro',
        '''Macro (incredibly large) or micro (incredibly small) characters''',
    ),
    (
        'vorarephilia',
        '''Vorarephilia''',
    ),
    (
        'bondage',
        '''Bondage''',
    ),
    (
        's_m',
        '''Sadism and/or masochism'''
    ),
    (
        'domination',
        '''Domination/submission, or power-play'''
    ),
    (
        'watersports',
        '''Watersports''',
    ),
    (
        'fertility_etc',
        '''Fertility, 'heat', pregnophilia, and other interests related to fertility'''
    )
]
