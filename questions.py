from models import PotentiallySubjectiveResponse as PSR

question_options = {
    'clinical_sex': {
        'female': PSR(value='female'),
        'male': PSR(value='male'),
        'intersex': PSR(value='intersex'),
        'mtf_female': PSR(value='mtf_female'),
        'ftm_male': PSR(value='ftm_male'),
        'other': PSR(subjective=True),
    },
    'gender_identity': {
        'male': PSR(value='male'),
        'mostly_male': PSR(value='mostly_male'),
        'both': PSR(value='both'),
        'mostly_female': PSR(value='mostly_female'),
        'female': PSR(value='female'),
        'genderqueer': PSR(value='genderqueer'),
        'neutrois': PSR(value='neutrois'),
        'nonbinary_nos': PSR(value='nonbinary_nos'),
        'other': PSR(subjective=True),
    },
    'sexual_orientation': {
        'kinsey_0': PSR(value='kinsey_0'),
        'kinsey_1': PSR(value='kinsey_1'),
        'kinsey_2': PSR(value='kinsey_2'),
        'kinsey_3': PSR(value='kinsey_3'),
        'kinsey_4': PSR(value='kinsey_4'),
        'kinsey_5': PSR(value='kinsey_5'),
        'kinsey_6': PSR(value='kinsey_6'),
        'pansexual': PSR(value='pansexual'),
        'omnisexual': PSR(value='omnisexual'),
        'other': PSR(subjective=True),
    },
    'race': {
        'white': PSR(value='white'),
        'black': PSR(value='black'),
        'hispanic': PSR(value='hispanic'),
        'native_american_pacific_islander': PSR(value='native_american_pacific_islander'),
        'middle_eastern': PSR(value='middle_eastern'),
        'other': PSR(subjective=True),
    },
    'spirituality': {},
    'occupation': {},
    'education': {},
    'relationship': {},
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
