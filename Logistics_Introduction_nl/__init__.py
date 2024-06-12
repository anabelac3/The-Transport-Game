from otree.api import *


author = 'Your name here'
doc = """
Your app description
"""


def slider_field(label):
    return models.IntegerField(min=0, max=100, default=0, label=label,)


class C(BaseConstants):
    NAME_IN_URL = 'Logistics_Introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    POSITIONS = ['A', 'B', 'C']


class Subsession(BaseSubsession):
    resources_AB = models.IntegerField()
    resources_AC = models.IntegerField()
    resources_BC = models.IntegerField()
    resources_ABC = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(
        choices=[
                  [1, 'Ja'],
                  [0, 'Nee'],
              ],)
    tscore = models.IntegerField()
    score = models.IntegerField()
    position = models.StringField()
    resources = models.IntegerField()
    practice = models.IntegerField(
        blank=True,
        label="TEST",
    )
    tslider1 = slider_field(False)
    tslider2 = slider_field(False)
    tslider3 = slider_field(False)
    tslider4 = slider_field(False)
    tslider5 = slider_field(False)
    tslider6 = slider_field(False)
    tslider7 = slider_field(False)
    tslider8 = slider_field(False)
    tslider9 = slider_field(False)
    tslider10 = slider_field(False)
    tslider11 = slider_field(False)
    tslider12 = slider_field(False)
    tslider13 = slider_field(False)
    tslider14 = slider_field(False)
    tslider15 = slider_field(False)
    tslider16 = slider_field(False)
    tslider17 = slider_field(False)
    tslider18 = slider_field(False)
    tslider19 = slider_field(False)
    tslider20 = slider_field(False)
    tslider21 = slider_field(False)
    slider1 = slider_field(False)
    slider2 = slider_field(False)
    slider3 = slider_field(False)
    slider4 = slider_field(False)
    slider5 = slider_field(False)
    slider6 = slider_field(False)
    slider7 = slider_field(False)
    slider8 = slider_field(False)
    slider9 = slider_field(False)
    slider10 = slider_field(False)
    slider11 = slider_field(False)
    slider12 = slider_field(False)
    slider13 = slider_field(False)
    slider14 = slider_field(False)
    slider15 = slider_field(False)
    slider16 = slider_field(False)
    slider17 = slider_field(False)
    slider18 = slider_field(False)
    slider19 = slider_field(False)
    slider20 = slider_field(False)
    slider21 = slider_field(False)


# FUNCTIONS
def creating_session(subsession):
    session = subsession.session
    subsession.resources_AB = (
        session.config['resources_player_A'] + session.config['resources_player_B']
    )
    subsession.resources_AC = (
        session.config['resources_player_A'] + session.config['resources_player_C']
    )
    subsession.resources_BC = (
        session.config['resources_player_B'] + session.config['resources_player_C']
    )
    subsession.resources_ABC = (
        session.config['resources_player_A']
        + session.config['resources_player_B']
        + session.config['resources_player_C']
    )


def vars_for_template(player: Player):
    session = player.session
    subsession = player.subsession
    group = player.group
    participant = player.participant
    resources_player_A = session.config['resources_player_A']
    resources_player_B = session.config['resources_player_B']
    resources_player_C = session.config['resources_player_C']
    decision_point = session.config['decision_point']
    total_payoff = session.config['total_payoff']
    base_fee = session.config['base_fee']
    payoff_conversion = session.config['payoff_conversion']
    max_bonus = total_payoff * payoff_conversion
    timeout_time = session.config['timeout_time']
    timeout_time_minutes = timeout_time / 60
    comprehension_check = session.config['comprehension_check']
    incentives = session.config['incentives']
    earned = session.config['earned']
    relation = session.config['relation']
    timers = session.config['timers']
    slider_time = session.config['slider_time']
    possible_coalitions_A = []
    possible_coalitions_B = []
    possible_coalitions_C = []
    possible_coalitions_all = []
    select_none = session.config['select_none']
    if subsession.resources_AB >= session.config['decision_point']:
        possible_coalitions_A.append('AB')
        possible_coalitions_B.append('AB')
        possible_coalitions_all.append('AB')
    if subsession.resources_AC >= session.config['decision_point']:
        possible_coalitions_A.append('AC')
        possible_coalitions_C.append('AC')
        possible_coalitions_all.append('AC')
    if subsession.resources_BC >= session.config['decision_point']:
        possible_coalitions_B.append('BC')
        possible_coalitions_C.append('BC')
        possible_coalitions_all.append('BC')
    if (
        subsession.resources_ABC >= session.config['decision_point']
        and session.config['grand_coalition']
    ):
        possible_coalitions_A.append('ABC')
        possible_coalitions_B.append('ABC')
        possible_coalitions_C.append('ABC')
        possible_coalitions_all.append('ABC')
    return {
        'possible_coalitions_A': possible_coalitions_A,
        'possible_coalitions_B': possible_coalitions_B,
        'possible_coalitions_C': possible_coalitions_C,
        'possible_coalitions_all': possible_coalitions_all,
        'resources_player_A': resources_player_A,
        'resources_player_B': resources_player_B,
        'resources_player_C': resources_player_C,
        'total_payoff': total_payoff,
        'base_fee': base_fee,
        'payoff_conversion': payoff_conversion,
        'select_none': select_none,
        'decision_point': decision_point,
        'max_bonus': max_bonus,
        'timeout_time': timeout_time,
        'timeout_time_minutes': timeout_time_minutes,
        'comprehension_check': comprehension_check,
        'incentives': incentives,
        'earned': earned,
        'relation': relation,
        'timers': timers,
        'slider_time': slider_time,
    }


# chris comment: what's the purpose of passing 'False' as the label?
def practice_error_message(player: Player, value):
    if value != 6000:
        return 'U hebt een verkeerd getal ingevuld. Probeer het nog een keer.'


def leftover_check(player: Player): # Seyit xxxxx
    participant = player.participant
    group = player.group
    other_players = player.get_others_in_group()
    for p in other_players:
        if p.participant.kicked == True:
            participant.leftover = False #True # Seyit 17 May


# PAGES
class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # Seyit - timer is weggehaald
    # @staticmethod
    # def get_timeout_seconds(player: Player):
    #     session = player.session
    #     return session.config['timeout_time']

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     participant = player.participant
    #     if timeout_happened:
    #         participant.kicked = True
    #     if player.consent == 0:
    #         participant.kicked = True
    #     leftover_check(player) # Seyit xxxxx


class Overview(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True
        else:
            return False # Seyit xxxxx

    @staticmethod
    def get_timeout_seconds(player: Player): # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    @staticmethod
    def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        leftover_check(player) # Seyit xxxxx


class GeneralInstructions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True
        else:
            return False # Seyit xxxxx

    @staticmethod
    def get_timeout_seconds(player: Player): # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    @staticmethod
    def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        leftover_check(player) # Seyit xxxxx


class InstructionsSeats(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True


class InstructionsPhases(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True


class Testinstructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        subsession = player.subsession
        group = player.group
        participant = player.participant
        return session.config['earned']

    # chris comment: duplicate method?????
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True

    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)


class PracticeFields(Page):
    form_model = 'player'
    form_fields = ['practice']

    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True
        else:
            return False # Seyit xxxxx

    @staticmethod
    def get_timeout_seconds(player: Player): # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    @staticmethod
    def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        if player.consent == 0:
            participant.kicked = True
        leftover_check(player) # Seyit xxxxx


class Groupassignment(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True
        else:
            return False # Seyit xxxxx

    @staticmethod
    def get_timeout_seconds(player: Player): # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    @staticmethod
    def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        if player.consent == 0:
            participant.kicked = True
        leftover_check(player) # Seyit xxxxx

        import time
        participant.wait_page_arrival = time.time() # Seyit timer


class Kicked(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == True:
            return True
        else:
            return False

    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)


class Instructions_Coalitions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True
        else:
            return False # Seyit xxxxx

    @staticmethod
    def get_timeout_seconds(player: Player): # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    @staticmethod
    def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        if player.consent == 0:
            participant.kicked = True
        leftover_check(player) # Seyit xxxxx


class Bonus(Page):
        @staticmethod
        def vars_for_template(player: Player):
            return vars_for_template(player)

        @staticmethod
        def is_displayed(player: Player):
            participant = player.participant
            if participant.kicked == False:
                return True
            else:
                return False # Seyit xxxxx

        @staticmethod
        def get_timeout_seconds(player: Player): # Seyit xxxxx
            session = player.session
            return session.config['timeout_time']

        @staticmethod
        def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
            participant = player.participant
            if timeout_happened:
                participant.kicked = True
            if player.consent == 0:
                participant.kicked = True
            leftover_check(player) # Seyit xxxxx


class Instructions_Phases(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.kicked == False:
            return True
        else:
            return False # Seyit xxxxx

    @staticmethod
    def get_timeout_seconds(player: Player): # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    @staticmethod
    def before_next_page(player: Player, timeout_happened): # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        if player.consent == 0:
            participant.kicked = True
        leftover_check(player) # Seyit xxxxx


page_sequence = [
    InformedConsent,
    Overview,
    GeneralInstructions,
    Instructions_Coalitions,
    Bonus,
    Instructions_Phases,
    PracticeFields,
    Groupassignment,
    Kicked,
]
