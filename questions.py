question_options = {
    '_birth_year': [2014 - i for i in range(0, 100)],
    'clinical_sex': {
        'female': { 'subjective': False },
        'male': { 'subjective': False },
        'intersex': { 'subjective': False },
        'mtf_female': { 'subjective': False },
        'ftm_male': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'gender_identity': {
        'male': { 'subjective': False },
        'mostly_male': { 'subjective': False },
        'both': { 'subjective': False },
        'mostly_female': { 'subjective': False },
        'female': { 'subjective': False },
        'genderqueer': { 'subjective': False },
        'neutrois': { 'subjective': False },
        'nonbinary_nos': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'sexual_orientation': {
        'kinsey_0': { 'subjective': False },
        'kinsey_1': { 'subjective': False },
        'kinsey_2': { 'subjective': False },
        'kinsey_3': { 'subjective': False },
        'kinsey_4': { 'subjective': False },
        'kinsey_5': { 'subjective': False },
        'kinsey_6': { 'subjective': False },
        'pansexual': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'race': {
        'white': { 'subjective': False },
        'black': { 'subjective': False },
        'asian': { 'subjective': False },
        'hispanic': { 'subjective': False },
        'native_american_pacific_islander': { 'subjective': False },
        'middle_eastern': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'spirituality': {
        'christian_catholic': { 'subjective': False },
        'christian_orthodox': { 'subjective': False },
        'christian_protestant': { 'subjective': False },
        'christian_other': { 'subjective': True },
        'muslim': { 'subjective': False },
        'hindu': { 'subjective': False },
        'jewish': { 'subjective': False },
        'pagan': { 'subjective': False },
        'buddhist': { 'subjective': False },
        'athiest': { 'subjective': False },
        'agnostic': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'occupation': {
        'student': { 'subjective': False },
        'administrative': { 'subjective': False },
        'government_armed_service': { 'subjective': False },
        'sales_support': { 'subjective': False },
        'technical_it': { 'subjective': False },
        'professional': { 'subjective': False },
        'service': { 'subjective': False },
        'vet_animal_related': { 'subjective': False },
        'creative_furry': { 'subjective': False },
        'creative_nonfurry': { 'subjective': False },
        'retired': { 'subjective': False },
        'unemployed': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'education': {
        'some_highschool': { 'subjective': False },
        'ongoing_highschool': { 'subjective': False },
        'graduate_highschool': { 'subjective': False },
        'some_university': { 'subjective': False },
        'ongoing_university': { 'subjective': False },
        'graduate_university': { 'subjective': False },
        'ongoing_postcollege': { 'subjective': False },
        'graduate_postcollege': { 'subjective': False },
        'advanced_degree': { 'subjective': False },
        'other': { 'subjective': True },
    },
    'relationship': {
        'single': { 'subjective': False },
        'casual': { 'subjective': False },
        'long_term_committed': { 'subjective': False },
        'legal_non_marriage': { 'subjective': False },
        'married': { 'subjective': False },
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
