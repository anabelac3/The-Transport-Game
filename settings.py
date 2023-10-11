from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'Logistics_game_dutch',
        'display_name': "Logistics game",
        'num_demo_participants': 3,
        'app_sequence': ['Logistics_Introduction', 'Logistics_task'],
        'resources_player_A': 4,
        'resources_player_B': 3,
        'resources_player_C': 2,
        'decision_point': 5,
        'grand_coalition': True,
        'total_payoff': 9000,
        'payoff_conversion': 0.000555555556,
        'base_fee': 5.00,
        'select_none': False,
        'timeout_time': 5 * 60,
        'slider_time': 2, # is not used
        'timers': True,
        'incentives': True,
        'earned': True,
        'relation': True,
        'comprehension_check': True,
    },
]
# see the end of this file for the inactive session configs

PARTICIPANT_FIELDS = [
    'fields',
    'end_game',
    'leftover',
    'kicked',
    'question_order',
    'grouped',
    'score',
    'wait_page_arrival' # Seyit timer
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'nl'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {'name': 'live_demo', 'display_name': 'Room for live demo',},
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = environ.get('OTREE_PRODUCTION') in {None, '', '0'}
DEBUG = False
#DEBUG = True

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = '0*$*1p0=l)_xqy=)xds**ee$j4+h$qv049&#vd5x7avz*3=nm0'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = [
    'otree',
]

EXTENSION_APPS = [
]
