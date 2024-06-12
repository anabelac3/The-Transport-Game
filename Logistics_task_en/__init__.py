import random
import string

from otree.api import *

author = 'Your name here'
doc = """
Your app description
"""


def slider_field(label):
    return models.IntegerField(min=0, max=100, label=label)


class C(BaseConstants):
    NAME_IN_URL = 'Logistics_task_en'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 20
    POSITIONS = ['A', 'B', 'C']


class Subsession(BaseSubsession):
    resources_AB = models.IntegerField()
    resources_AC = models.IntegerField()
    resources_BC = models.IntegerField()
    resources_ABC = models.IntegerField()


class Group(BaseGroup):
    proposed_coalition_player_A = models.StringField(
        widget=widgets.RadioSelect,
    )
    proposed_coalition_player_B = models.StringField(
        widget=widgets.RadioSelect,
    )
    proposed_coalition_player_C = models.StringField(
        widget=widgets.RadioSelect,
    )
    allocation_A_to_A = models.IntegerField()
    allocation_A_to_B = models.IntegerField()
    allocation_A_to_C = models.IntegerField()
    allocation_B_to_A = models.IntegerField()
    allocation_B_to_B = models.IntegerField()
    allocation_B_to_C = models.IntegerField()
    allocation_C_to_A = models.IntegerField()
    allocation_C_to_B = models.IntegerField()
    allocation_C_to_C = models.IntegerField()
    selected_coalition_name_player_A = models.StringField()
    selected_coalition_name_player_B = models.StringField()
    selected_coalition_name_player_C = models.StringField()
    selected_coalition_allocation_A_player_A = models.IntegerField()
    selected_coalition_allocation_B_player_A = models.IntegerField()
    selected_coalition_allocation_C_player_A = models.IntegerField()
    selected_coalition_allocation_A_player_B = models.IntegerField()
    selected_coalition_allocation_B_player_B = models.IntegerField()
    selected_coalition_allocation_C_player_B = models.IntegerField()
    selected_coalition_allocation_A_player_C = models.IntegerField()
    selected_coalition_allocation_B_player_C = models.IntegerField()
    selected_coalition_allocation_C_player_C = models.IntegerField()
    coalition_formed = models.BooleanField(default=False)  # seyit last problem
    formed_coalition_name = models.StringField()
    payoff_A = models.IntegerField()
    payoff_B = models.IntegerField()
    payoff_C = models.IntegerField()


class Player(BasePlayer):
    completion_code = models.StringField()
    score = models.IntegerField()
    position = models.StringField()
    resources = models.IntegerField()
    goal = models.StringField(blank=True)
    comment = models.StringField(blank=True)
    comment_email = models.StringField(blank=True)
    age = models.IntegerField()  # blank=True)
    mturk_id = models.StringField()
    gender = models.IntegerField(
        choices=[
            [0, 'Female'],
            [1, 'Male'],
            [2, 'Other'],
            [3, 'Prefer not to say'],
        ],
        widget=widgets.RadioSelect(),
        # blank=True,
    )
    pcuse = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    comprehension_position = models.IntegerField(widget=widgets.RadioSelect())
    comprehension_position_fail = models.IntegerField()
    comprehension_resources = models.IntegerField(widget=widgets.RadioSelect())
    comprehension_resources_fail = models.IntegerField()
    comprehension_bonus = models.IntegerField(
        choices=[
            [0, '10000 euros'],
            [1, '9000 euros'],
            [2, '8000 euros'],
        ],
        widget=widgets.RadioSelect(),
    )
    comprehension_bonus_fail = models.IntegerField()
    comprehension_coalitions = models.IntegerField(widget=widgets.RadioSelect())
    comprehension_coalitions_fail = models.IntegerField()
    proposed_coalition = models.StringField(max_length=3)
    selected_coalition = models.StringField()
    selected_coalition_name = models.StringField(max_length=3)
    selected_coalition_allocation_A = models.IntegerField()
    selected_coalition_allocation_B = models.IntegerField()
    selected_coalition_allocation_C = models.IntegerField()
    allocate_to_player_A = models.IntegerField(blank=True, null=True)
    allocate_to_player_B = models.IntegerField(blank=True, null=True)
    allocate_to_player_C = models.IntegerField(blank=True, null=True)
    money = models.IntegerField()
    question_order = models.StringField()
    manipulation_check1 = models.IntegerField(
        choices=[
            [0, 'On the basis of performance on a slider task'],
            [1, 'By a random draw'],
        ],
        widget=widgets.RadioSelect(),
    )
    manipulation_check2 = models.IntegerField(
        choices=[
            [0, 'Parties with more seats contributed more'],
            [1, 'They did not contribute to it at all. The budget was fixed.'],
        ],
        widget=widgets.RadioSelect(),
    )
    manipulation_check2control = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    manipulation_check2controlbudget = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    seats_deserve = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    budget_deserve = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    motivation_max = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Maximize your own outcomes",
    )
    motivation_harm = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Minimize harm to the other bargainers",
    )
    motivation_deserve = models.IntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Make sure that every bargainer got what they deserved",
    )

    pt_1 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I sometimes find it difficult to see things from someone else's point of view."
    )

    pt_2 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I try to look at everybody's side of a disagreement before I make a decision."
    )
    pt_3 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I try to understand my friends better by imagining how things look from their perspective."
    )

    pt_4 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="If I'm sure I'm right about something, I don't waste much time listening to other people's arguments."
    )
    pt_5 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I believe that there are two sides to every question and try to look at them both."
    )

    pt_6 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="When I'm upset at someone, I usually try to 'put myself in their shoes’ for a while."
    )

    pt_7 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Before criticizing somebody, I try to imagine how I would feel if I were in their place."
    )

    ec_1 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I often have tender, concerned feelings for people less fortunate than me."
    )

    ec_2 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Sometimes I don't feel very sorry for other people when they are having problems."
    )
    ec_3 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="When I see someone being taken advantage of, I feel kind of protective towards them."
    )

    ec_4 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Other people's misfortunes do not usually disturb me a great deal."
    )
    ec_5 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="When I see someone being treated unfairly, I sometimes don't feel very much pity for them."
    )

    ec_6 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I am often touched by what other people go through."
    )

    attention_check = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="This is an attention check, please select 5"
    )

    ec_8 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I would describe myself as a pretty soft-hearted person."
    )

    apt_1 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I tried to take other players’ perspectives."
    )

    apt_2 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I tried to imagine how other players felt."
    )
    apt_3 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I made an effort to see the world through the other players’ eyes."
    )

    apt_4 = models.PositiveIntegerField(
        choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
        ],
        widget=widgets.RadioSelectHorizontal,
        label="I sought to understand players’ viewpoints."
    )

    device = models.IntegerField(
        choices=[
            [1, "Desktop/laptop with a mouse"],
            [2, "Desktop/laptop without a mouse"],
            [3, "Tablet"],
            [4, "Mobile phone"],
            [5, "Other"],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )
    browser = models.IntegerField(
        choices=[
            [1, "Chrome"],
            [2, "Internet Explorer or Microsoft Edge"],
            [3, "Safari"],
            [4, "Firefox"],
            [5, "Opera"],
            [6, "Other"],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )
    # tslider1 = slider_field(False)
    # tslider2 = slider_field(False)
    # tslider3 = slider_field(False)
    # tslider4 = slider_field(False)
    # tslider5 = slider_field(False)
    # tslider6 = slider_field(False)
    # tslider7 = slider_field(False)
    # tslider8 = slider_field(False)
    # tslider9 = slider_field(False)
    # tslider10 = slider_field(False)
    # tslider11 = slider_field(False)
    # tslider12 = slider_field(False)
    # tslider13 = slider_field(False)
    # tslider14 = slider_field(False)
    # tslider15 = slider_field(False)
    # tslider16 = slider_field(False)
    # tslider17 = slider_field(False)
    # tslider18 = slider_field(False)
    # tslider19 = slider_field(False)
    # tslider20 = slider_field(False)
    # tslider21 = slider_field(False)
    # slider1 = slider_field(False)
    # slider2 = slider_field(False)
    # slider3 = slider_field(False)
    # slider4 = slider_field(False)
    # slider5 = slider_field(False)
    # slider6 = slider_field(False)
    # slider7 = slider_field(False)
    # slider8 = slider_field(False)
    # slider9 = slider_field(False)
    # slider10 = slider_field(False)
    # slider11 = slider_field(False)
    # slider12 = slider_field(False)
    # slider13 = slider_field(False)
    # slider14 = slider_field(False)
    # slider15 = slider_field(False)
    # slider16 = slider_field(False)
    # slider17 = slider_field(False)
    # slider18 = slider_field(False)
    # slider19 = slider_field(False)
    # slider20 = slider_field(False)
    # slider21 = slider_field(False)
    # slider22 = slider_field(False)
    # slider23 = slider_field(False)
    # slider24 = slider_field(False)
    # slider25 = slider_field(False)
    # slider26 = slider_field(False)
    # slider27 = slider_field(False)
    # slider28 = slider_field(False)
    # slider29 = slider_field(False)
    # slider30 = slider_field(False)
    # slider31 = slider_field(False)
    # slider32 = slider_field(False)
    # slider33 = slider_field(False)
    # slider34 = slider_field(False)
    # slider35 = slider_field(False)
    # slider36 = slider_field(False)
    # slider37 = slider_field(False)
    # slider38 = slider_field(False)
    # slider39 = slider_field(False)
    # slider40 = slider_field(False)
    # slider41 = slider_field(False)
    # slider42 = slider_field(False)
    # slider43 = slider_field(False)
    # slider44 = slider_field(False)
    # slider45 = slider_field(False)
    # slider46 = slider_field(False)
    # slider47 = slider_field(False)
    # slider48 = slider_field(False)
    # slider49 = slider_field(False)
    # slider50 = slider_field(False)
    # slider51 = slider_field(False)
    # slider52 = slider_field(False)
    # slider53 = slider_field(False)
    # slider54 = slider_field(False)
    # slider55 = slider_field(False)
    # slider56 = slider_field(False)
    # slider57 = slider_field(False)
    # slider58 = slider_field(False)
    # slider59 = slider_field(False)
    # slider60 = slider_field(False)
    # slider61 = slider_field(False)
    # slider62 = slider_field(False)
    # slider63 = slider_field(False)


def creating_session(subsession: Subsession):
    session = subsession.session  # Seyit
    subsession.resources_AB = (
            session.config['resources_player_A']
            + session.config['resources_player_B']
    )
    subsession.resources_AC = (
            session.config['resources_player_A']
            + session.config['resources_player_C']
    )
    subsession.resources_BC = (
            session.config['resources_player_B']
            + session.config['resources_player_C']
    )
    subsession.resources_ABC = (
            session.config['resources_player_A']
            + session.config['resources_player_B']
            + session.config['resources_player_C']
    )
    for p in subsession.get_players():
        p.participant.end_game = False
    for p in subsession.get_players():
        p.participant.grouped = False
    for p in subsession.get_players():
        p.participant.leftover = False
    for p in subsession.get_players():
        p.participant.kicked = False
    for p in subsession.get_players():
        p.completion_code = 'DS' + ''.join(random.choices(string.digits, k=4))


def vars_for_template(player: Player):
    session = player.session  # Seyit
    subsession = player.subsession  # Pradeep
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


def offer_summary(player: Player):
    offers = (
        player.allocate_to_player_A,
        player.allocate_to_player_B,
        player.allocate_to_player_C,
    )
    offers_int = map(int, offers)
    offers_str = map(str, offers_int)
    return "-".join(offers_str)


def selected_list(player: Player):
    group = player.group  # Seyit
    return [p for p in group.get_players() if p.selected == player.id]


def leftover_check(player: Player):
    participant = player.participant  # Seyit
    group = player.group  # Seyit
    other_players = player.get_others_in_group()
    for p in other_players:
        if p.participant.kicked == True:
            participant.leftover = True
        if p.participant._current_page_name == 'Funnel' and group.coalition_formed == False:
            participant.leftover = True
        if (
                p.participant._current_page_name == 'Demographics'
                and group.coalition_formed == False
        ):
            participant.leftover = True
        if (
                p.participant._current_page_name == 'PC_use'
                and group.coalition_formed == False
        ):
            participant.leftover = True
        if (
                p.participant._current_page_name == 'Debriefing'
                and group.coalition_formed == False
        ):
            participant.leftover = True
        if p.participant._current_page_name == 'Kicked' and group.coalition_formed == False:
            participant.leftover = True


def comprehension_position_choices(player: Player):
    session = player.session  # Seyit
    choices = [
        [0, 'Company A'],
        [1, 'Company B'],
        [2, 'Company C'],
    ]
    return choices


def comprehension_position_error_message(player: Player, value):
    session = player.session  # Seyit
    if (player.position == 'A' and value != 0) or (player.position == 'B' and value != 1) or (
            player.position == 'C' and value != 2):
        player.comprehension_position_fail = 1
        return "This is incorrect. You are representing Company {}. Please enter the correct answer.".format(
            player.position)

def comprehension_resources_choices(player: Player):
    session = player.session  # Seyit
    choices = [
        [0, 'My company transports 4 tons'],
        [1, 'My company transports 3 tons'],
        [2, 'My company transports 2 tons'],
    ]
    return choices


def comprehension_resources_error_message(player: Player, value):
    session = player.session  # Seyit
    if (player.position == 'A' and value != 0) or (player.position == 'B' and value != 1) or (
            player.position == 'C' and value != 2):
        player.comprehension_resources_fail = 1
        return "This is not correct. You are transporting {} tons. Please enter the correct answer.".format(player.resources)


def comprehension_coalitions_choices(player: Player):
    session = player.session  # Seyit
    choices = []
    if not session.config['grand_coalition']:
        choices = [
            [0, 'AB, AC '],
            [1, 'AB, BC'],
            [2, 'AC, BC'],
            [3, 'AB, AC, BC'],
        ]
    elif session.config['grand_coalition']:
        choices = [
            [0, 'AB, AC '],
            [1, 'AB, BC'],
            [2, 'AC, BC'],
            [3, 'AB, AC, BC'],
            [4, 'AB, AC, BC, ABC'],
        ]
    return choices


def comprehension_coalitions_error_message(player: Player, value):
    session = player.session  # Seyit
    if session.config['grand_coalition'] == False and value != 3:
        if value == 0:
            player.comprehension_coalitions_fail = 0
        if value == 1:
            player.comprehension_coalitions_fail = 1
        if value == 2:
            player.comprehension_coalitions_fail = 2
        return "This is incorrect. There are 3 possible coalitions: AB, AC and BC. Please enter the correct answer."
    if session.config['grand_coalition'] == True and value != 4:
        if value == 0:
            player.comprehension_coalitions_fail = 1
        return "This is incorrect. There are 4 possible coalitions: AB, AC, BC and ABC. Please enter the correct answer."


def comprehension_bonus_error_message(player: Player, value):
    if value != 1:
        player.comprehension_bonus_fail = 1
        return "This is not correct. You are negotiating an amount of 9000 euros. Please enter the correct answer."


def waiting_too_long(player):  # Seyit timer
    participant = player.participant

    import time
    # print('Timer waited time =', (time.time() - participant.wait_page_arrival), 'seconden voor player', player.id_in_group)
    # assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
    return (time.time() - participant.wait_page_arrival) > 5 * 60  # tijd in seconden waarna de wait_page er mee stopt


def group_by_arrival_time_method(subsession, waiting_players):  # Seyit timer
    # print('\nWe zitten nu in group_by_arrival_time_method')
    # print('Hoeveel zijn er aan het wachten?: ', len(waiting_players))

    if len(waiting_players) >= 3:
        return waiting_players[:3]

    for player in waiting_players:
        # print('En de nummers van de players zijn: ', player.id_in_group)
        if waiting_too_long(player):
            # print('Ik wacht te lang en ik ben player: ', player.id_in_group, '\n')
            player.participant.leftover = True


# FUNCTIONS
# PAGES
# FUNCTIONS
# PAGES
class Waitforgroup(WaitPage):
    title_text = "Matching you with participants"
    body_text = "Please wait a few minutes for other participants."
    group_by_arrival_time = True
    startwp_timer = 5 * 60
    use_task = False

    # #@staticmethod
    # def get_players_for_group(player: Player, waiting_players):
    #     positions = iter(C.POSITIONS)
    #     active_players = [
    #         p for p in waiting_players if p.participant._current_page_name == 'Waitforgroup'
    #     ]
    #     if len(active_players) >= C.PLAYERS_PER_GROUP:
    #         if not session.config['earned']:
    #             for p in active_players:
    #                 p.position = next(positions)
    #                 if p.position == 'A':
    #                     p.resources = session.config['resources_player_A']
    #                 elif p.position == 'B':
    #                     p.resources = session.config['resources_player_B']
    #                 elif p.position == 'C':
    #                     p.resources = session.config['resources_player_C']
    #         return active_players
    # Seyit

    # @staticmethod
    # def group_by_arrival_time_method(subsession, waiting_players): # Seyit, vervanging van hierboven
    #     print('in group_by_arrival_time_method')
    #     m_players = [p for p in waiting_players if p.participant.category == 'M']
    #     f_players = [p for p in waiting_players if p.participant.category == 'F']

    #     if len(m_players) >= 2 and len(f_players) >= 2:
    #         print('about to create a group')
    #         return [m_players[0], m_players[1], f_players[0], f_players[1]]
    #     print('not enough players yet to create a group')

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False


class Groupingconfirmation(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        participant.grouped = True
        leftover_check(player)


class Sliderinstructions(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)

    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)


class Slider(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['slider_time']

    form_model = 'player'

    # @staticmethod
    def get_form_fields(player: Player):
        return ['slider{}'.format(i) for i in range(1, 22)]


class EndRound1(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False


class Slider2(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['slider_time']

    form_model = 'player'

    # @staticmethod
    def get_form_fields(player: Player):
        return ['slider{}'.format(i) for i in range(22, 43)]


class EndRound2(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False


class Slider3(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['slider_time']

    form_model = 'player'

    # @staticmethod
    def get_form_fields(player: Player):
        return ['slider{}'.format(i) for i in range(43, 64)]

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        player.score = 0
        leftover_check(player)
        sliders = [
            player.slider1,
            player.slider2,
            player.slider3,
            player.slider4,
            player.slider5,
            player.slider6,
            player.slider7,
            player.slider8,
            player.slider9,
            player.slider10,
            player.slider11,
            player.slider12,
            player.slider13,
            player.slider14,
            player.slider15,
            player.slider16,
            player.slider17,
            player.slider18,
            player.slider19,
            player.slider20,
            player.slider21,
            player.slider22,
            player.slider23,
            player.slider24,
            player.slider25,
            player.slider26,
            player.slider27,
            player.slider28,
            player.slider29,
            player.slider30,
            player.slider31,
            player.slider32,
            player.slider33,
            player.slider34,
            player.slider35,
            player.slider36,
            player.slider37,
            player.slider38,
            player.slider39,
            player.slider40,
            player.slider41,
            player.slider42,
            player.slider43,
            player.slider44,
            player.slider45,
            player.slider46,
            player.slider47,
            player.slider48,
            player.slider49,
            player.slider50,
            player.slider51,
            player.slider52,
            player.slider53,
            player.slider54,
            player.slider55,
            player.slider56,
            player.slider57,
            player.slider58,
            player.slider59,
            player.slider60,
            player.slider61,
            player.slider62,
            player.slider63,
        ]
        for slider in sliders:
            if slider == 50:
                player.score += 1
        participant.score = player.score


class Waitforparticipants(WaitPage):

    # @staticmethod
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and player.round_number == 1
                and session.config['earned'] == True
                and participant.grouped == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    title_text = "Position assignment"
    body_text = "You will be randomly assigned a position"
    startwp_timer = 5 * 60

    # @staticmethod
    # @staticmethod
    def after_all_players_arrive(group: Group):
        session = group.session  # Seyit
        scores = []
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        p3 = group.get_player_by_id(3)
        for p in group.get_players():
            try:  # Seyit
                p.score
            except:
                p.score = 0
            summary = (p.id_in_group, p.score)
            scores.append(summary)
        sorted_scores = sorted(scores, key=lambda tup: tup[1], reverse=True)
        A = sorted_scores[0]
        B = sorted_scores[1]
        C = sorted_scores[2]
        if A[0] == 1:
            p1.position = 'A'
            p1.resources = session.config['resources_player_A']
        elif A[0] == 2:
            p2.position = 'A'
            p2.resources = session.config['resources_player_A']
        elif A[0] == 3:
            p3.position = 'A'
            p3.resources = session.config['resources_player_A']
        if B[0] == 1:
            p1.position = 'B'
            p1.resources = session.config['resources_player_B']
        elif B[0] == 2:
            p2.position = 'B'
            p2.resources = session.config['resources_player_B']
        elif B[0] == 3:
            p3.position = 'B'
            p3.resources = session.config['resources_player_B']
        if C[0] == 1:
            p1.position = 'C'
            p1.resources = session.config['resources_player_C']
        elif C[0] == 2:
            p2.position = 'C'
            p2.resources = session.config['resources_player_C']
        elif C[0] == 3:
            p3.position = 'C'
            p3.resources = session.config['resources_player_C']


class PositionAssignment(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                participant.end_game == False
                and participant.kicked == False
                and participant.leftover == False
                and session.config['earned'] == True
                and player.round_number == 1
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)

    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)


class AssignedPosition(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Seyit
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class InstructionsCoalitions(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class ComprehensionCheck(Page):
    form_model = 'player'
    form_fields = ['comprehension_position']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Seyit
        if (
                session.config['comprehension_check'] == True
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def vars_for_template(player: Player):
        vars = vars_for_template(player)
        vars.update({'position_label': "Which company do you represent?"})
        return vars

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class ComprehensionCheck1(Page):
    form_model = 'player'
    form_fields = ['comprehension_resources']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Seyit
        if (
                session.config['comprehension_check'] == True
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def vars_for_template(player: Player):
        vars = vars_for_template(player)
        vars.update({'resources_label': "How many tons does your company transport to Paris every day?"})
        return vars

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class ComprehensionCheck2(Page):
    form_model = 'player'
    form_fields = ['comprehension_bonus']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Seyit
        if (
                session.config['comprehension_check'] == True
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class ComprehensionCheck3(Page):
    form_model = 'player'
    form_fields = ['comprehension_coalitions']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Pradeep
        if (
                session.config['comprehension_check'] == True
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class ManipulationCheck2control(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False
    form_model = 'player'
    form_fields = ['manipulation_check2control']

class ManipulationCheck2controlBudget(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['manipulation_check2controlbudget']

class BargainingStarts(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and player.round_number == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class NewRound(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and player.round_number > 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        group = player.group  # Seyit
        for player in group.get_players():
            prev_player = player.in_round(1)
            player.position = prev_player.position
            player.resources = prev_player.resources
            player.completion_code = prev_player.completion_code
        leftover_check(player)
        if timeout_happened:
            participant.kicked = True

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']


class PhaseI(Page):
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    form_model = 'player'
    form_fields = [
        'proposed_coalition',
        'allocate_to_player_A',
        'allocate_to_player_B',
        'allocate_to_player_C',
    ]

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        group = player.group  # Seyit
        for p in group.get_players():
            try:  # Seyit
                p.proposed_coalition
            except:
                p.proposed_coalition = ''
                p.allocate_to_player_A = 0
                p.allocate_to_player_B = 0
                p.allocate_to_player_C = 0

            if p.proposed_coalition == 'BC':
                p.allocate_to_player_A = 0
            if p.proposed_coalition == 'AC':
                p.allocate_to_player_B = 0
            if p.proposed_coalition == 'AB':
                p.allocate_to_player_C = 0
            if p.position == 'A':
                group.proposed_coalition_player_A = p.proposed_coalition
                try:  # seyit last problem
                    group.allocation_A_to_A = p.allocate_to_player_A
                except:
                    group.allocation_A_to_A = 0
                try:
                    group.allocation_A_to_B = p.allocate_to_player_B
                except:
                    group.allocation_A_to_B = 0
                try:
                    group.allocation_A_to_C = p.allocate_to_player_C
                except:
                    group.allocation_A_to_C = 0
            elif p.position == 'B':
                group.proposed_coalition_player_B = p.proposed_coalition
                try:  # seyit last problem
                    group.allocation_B_to_A = p.allocate_to_player_A
                except:
                    group.allocation_B_to_A = 0
                try:
                    group.allocation_B_to_B = p.allocate_to_player_B
                except:
                    group.allocation_B_to_B = 0
                try:
                    group.allocation_B_to_C = p.allocate_to_player_C
                except:
                    group.allocation_B_to_C = 0
            elif p.position == 'C':
                group.proposed_coalition_player_C = p.proposed_coalition
                try:  # seyit last problem
                    group.allocation_C_to_A = p.allocate_to_player_A
                except:
                    group.allocation_C_to_A = 0
                try:
                    group.allocation_C_to_B = p.allocate_to_player_B
                except:
                    group.allocation_C_to_B = 0
                try:
                    group.allocation_C_to_C = p.allocate_to_player_C
                except:
                    group.allocation_C_to_C = 0
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Seyit
        return session.config['timeout_time']


class WaitForOffers(WaitPage):
    title_text = "Waiting for offers from other participants"
    body_text = "Wait until all participants have submitted offers. This may take some time."
    startwp_timer = 5 * 60

    # @staticmethod
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False


class OffersMade(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class PhaseII(Page):
    form_model = 'player'
    form_fields = ['selected_coalition']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def vars_for_template(player: Player):
        session = player.session  # Seyit
        group = player.group  # Seyit
        vars = vars_for_template(player)
        offers = dict()
        for p in group.get_players():
            pc = p.proposed_coalition
            if pc and player.position in p.proposed_coalition:
                summary = (
                    pc,
                    offer_summary(p),
                    p.allocate_to_player_A,
                    p.allocate_to_player_B,
                    p.allocate_to_player_C,
                    p.id_in_group,
                )
                summary_wo_id = summary[:-1]
                offers[summary_wo_id] = summary
        if session.config['select_none']:
            offers['tuple'] = (
                "Select this option if you do not wish to select one of the above offers. You will not be able to form a coalition this round.",
                "No",
                99,
                99,
                99,
                'None',
            )
        vars.update({"offers": sorted(offers.values())})
        return vars

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class WaitForSelection(WaitPage):
    title_text = "Waiting for selection"
    body_text = "Wait until all participants have chosen a proposal. This may take some time."
    startwp_timer = 5 * 60

    # @staticmethod
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and participant.grouped == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    # @staticmethod
    def after_all_players_arrive(group: Group):
        session = group.session  # Seyit
        players = group.get_players()
        myloop = 0
        for p in players:
            myloop += 1
            try:  # Seyit xxxxx
                p.selected_coalition
            except:
                p.selected_coalition = 'None'

            if p.selected_coalition != 'None':
                cs = p.selected_coalition  # Seyit
                try:  # Seyit xxxxx
                    p.selected_coalition_name = group.get_player_by_id(cs).proposed_coalition
                except:
                    p.selected_coalition_name = 'None'
                try:  # Seyit xxxxx
                    p.selected_coalition_allocation_A = group.get_player_by_id(cs).allocate_to_player_A
                except:
                    p.selected_coalition_allocation_A = 0
                try:  # Seyit xxxxx
                    p.selected_coalition_allocation_B = group.get_player_by_id(cs).allocate_to_player_B
                except:
                    p.selected_coalition_allocation_B = 0
                try:  # Seyit xxxxx
                    p.selected_coalition_allocation_C = group.get_player_by_id(cs).allocate_to_player_C
                except:
                    p.selected_coalition_allocation_C = 0
            elif p.selected_coalition == 'None':
                p.selected_coalition_name = 'None'
                p.selected_coalition_allocation_A = 0  # None Seyit xxxxx
                p.selected_coalition_allocation_B = 0  # None Seyit xxxxx
                p.selected_coalition_allocation_C = 0  # None Seyit xxxxx
            if p.position == 'A':
                group.selected_coalition_name_player_A = p.selected_coalition_name
                group.selected_coalition_allocation_A_player_A = p.selected_coalition_allocation_A
                group.selected_coalition_allocation_B_player_A = p.selected_coalition_allocation_B
                group.selected_coalition_allocation_C_player_A = p.selected_coalition_allocation_C
            elif p.position == 'B':
                group.selected_coalition_name_player_B = p.selected_coalition_name
                group.selected_coalition_allocation_A_player_B = p.selected_coalition_allocation_A
                group.selected_coalition_allocation_B_player_B = p.selected_coalition_allocation_B
                group.selected_coalition_allocation_C_player_B = p.selected_coalition_allocation_C
            elif p.position == 'C':
                group.selected_coalition_name_player_C = p.selected_coalition_name
                group.selected_coalition_allocation_A_player_C = p.selected_coalition_allocation_A
                group.selected_coalition_allocation_B_player_C = p.selected_coalition_allocation_B
                group.selected_coalition_allocation_C_player_C = p.selected_coalition_allocation_C
        list_AB = []
        list_AC = []
        list_BC = []
        list_ABC = []
        list_none = []
        for p in players:
            if p.selected_coalition_name == "AB":
                list_AB.append(p.position)
            if p.selected_coalition_name == "AC":
                list_AC.append(p.position)
            if p.selected_coalition_name == "BC":
                list_BC.append(p.position)
            if p.selected_coalition_name == "ABC":
                list_ABC.append(p.position)
            if p.selected_coalition_name == None:
                list_none.append(p.position)
        if (
                len(list_AB) == 2
                and group.selected_coalition_allocation_A_player_A
                == group.selected_coalition_allocation_A_player_B
        ):
            if (
                    group.selected_coalition_allocation_B_player_A
                    == group.selected_coalition_allocation_B_player_B
            ):
                print("AB is formed")
                group.coalition_formed = True
                group.formed_coalition_name = "AB"
                group.payoff_A = group.selected_coalition_allocation_A_player_A
                group.payoff_B = group.selected_coalition_allocation_B_player_B
                group.payoff_C = 0
        elif (
                len(list_AC) == 2
                and group.selected_coalition_allocation_A_player_A
                == group.selected_coalition_allocation_A_player_C
        ):
            if (
                    group.selected_coalition_allocation_C_player_A
                    == group.selected_coalition_allocation_C_player_C
            ):
                print("AC is formed")
                group.coalition_formed = True
                group.formed_coalition_name = "AC"
                group.payoff_A = group.selected_coalition_allocation_A_player_A
                group.payoff_B = 0
                group.payoff_C = group.selected_coalition_allocation_C_player_C
        elif (
                len(list_BC) == 2
                and group.selected_coalition_allocation_B_player_B
                == group.selected_coalition_allocation_B_player_C
        ):
            print("First part for B works")
            if (
                    group.selected_coalition_allocation_C_player_B
                    == group.selected_coalition_allocation_C_player_C
            ):
                print("BC is formed")
                group.coalition_formed = True
                group.formed_coalition_name = "BC"
                group.payoff_A = 0
                group.payoff_B = group.selected_coalition_allocation_B_player_B
                group.payoff_C = group.selected_coalition_allocation_C_player_C
        elif (
                len(list_ABC) == 3
                and group.selected_coalition_allocation_A_player_A
                == group.selected_coalition_allocation_A_player_B
                == group.selected_coalition_allocation_A_player_C
        ):
            if (
                    group.selected_coalition_allocation_B_player_A
                    == group.selected_coalition_allocation_B_player_B
                    == group.selected_coalition_allocation_B_player_C
            ):
                if (
                        group.selected_coalition_allocation_C_player_A
                        == group.selected_coalition_allocation_C_player_B
                        == group.selected_coalition_allocation_C_player_C
                ):
                    group.coalition_formed = True
                    group.formed_coalition_name = "ABC"
                    group.payoff_A = group.selected_coalition_allocation_A_player_A
                    group.payoff_B = group.selected_coalition_allocation_B_player_B
                    group.payoff_C = group.selected_coalition_allocation_C_player_C
        else:
            group.coalition_formed = False
            group.payoff_A = 0
            group.payoff_B = 0
            group.payoff_C = 0
        for p in players:
            if p.position == "A":
                p.money = group.payoff_A
                p.payoff = group.payoff_A * session.config['payoff_conversion']
            if p.position == "B":
                p.money = group.payoff_B
                p.payoff = group.payoff_B * session.config['payoff_conversion']
            if p.position == "C":
                p.money = group.payoff_C
                p.payoff = group.payoff_C * session.config['payoff_conversion']


class OffersSelected(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.end_game == False
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class PhaseIII_Success(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        group = player.group  # Seyit
        try:  # Seyit
            group.coalition_formed
        except:
            group.coalition_formed = 0
        if (
                participant.end_game == False
                and group.coalition_formed == 1
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def get_timeout_seconds(player: Player):  # Seyit xxxxx
        session = player.session
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):  # Seyit xxxxx
        participant = player.participant
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)

    # @staticmethod
    def vars_for_template(player: Player):
        group = player.group  # Seyit
        offers_dict = dict()
        vars = vars_for_template(player)
        prop_name_A = group.proposed_coalition_player_A
        prop_name_B = group.proposed_coalition_player_B
        prop_name_C = group.proposed_coalition_player_C
        prop_A_to_A = group.allocation_A_to_A
        prop_A_to_B = group.allocation_A_to_B
        prop_A_to_C = group.allocation_A_to_C
        prop_B_to_A = group.allocation_B_to_A
        prop_B_to_B = group.allocation_B_to_B
        prop_B_to_C = group.allocation_B_to_C
        prop_C_to_A = group.allocation_C_to_A
        prop_C_to_B = group.allocation_C_to_B
        prop_C_to_C = group.allocation_C_to_C
        sel_name_A = group.selected_coalition_name_player_A
        sel_name_B = group.selected_coalition_name_player_B
        sel_name_C = group.selected_coalition_name_player_C
        sel_A_to_A = group.selected_coalition_allocation_A_player_A
        sel_A_to_B = group.selected_coalition_allocation_B_player_A
        sel_A_to_C = group.selected_coalition_allocation_C_player_A
        sel_B_to_A = group.selected_coalition_allocation_A_player_B
        sel_B_to_B = group.selected_coalition_allocation_B_player_B
        sel_B_to_C = group.selected_coalition_allocation_C_player_B
        sel_C_to_A = group.selected_coalition_allocation_A_player_C
        sel_C_to_B = group.selected_coalition_allocation_B_player_C
        sel_C_to_C = group.selected_coalition_allocation_C_player_C
        proposed_by_A = 0
        proposed_by_B = 0
        proposed_by_C = 0
        selected_by_A = 0
        selected_by_B = 0
        selected_by_C = 0
        offer_A = [
            group.proposed_coalition_player_A,
            group.allocation_A_to_A,
            group.allocation_A_to_B,
            group.allocation_A_to_C,
            proposed_by_A,
            proposed_by_B,
            proposed_by_C,
            selected_by_A,
            selected_by_B,
            selected_by_C,
        ]
        offer_B = [
            group.proposed_coalition_player_B,
            group.allocation_B_to_A,
            group.allocation_B_to_B,
            group.allocation_B_to_C,
            proposed_by_A,
            proposed_by_B,
            proposed_by_C,
            selected_by_A,
            selected_by_B,
            selected_by_C,
        ]
        offer_C = [
            group.proposed_coalition_player_C,
            group.allocation_C_to_A,
            group.allocation_C_to_B,
            group.allocation_C_to_C,
            proposed_by_A,
            proposed_by_B,
            proposed_by_C,
            selected_by_A,
            selected_by_B,
            selected_by_C,
        ]
        offers = (offer_A, offer_B, offer_C)
        for offer in offers:
            if (
                    offer[0] == prop_name_A
                    and offer[1] == prop_A_to_A
                    and offer[2] == prop_A_to_B
                    and offer[3] == prop_A_to_C
            ):
                offer[4] = 1
            if (
                    offer[0] == prop_name_B
                    and offer[1] == prop_B_to_A
                    and offer[2] == prop_B_to_B
                    and offer[3] == prop_B_to_C
            ):
                offer[5] = 1
            if (
                    offer[0] == prop_name_C
                    and offer[1] == prop_C_to_A
                    and offer[2] == prop_C_to_B
                    and offer[3] == prop_C_to_C
            ):
                offer[6] = 1
            if (
                    offer[0] == sel_name_A
                    and offer[1] == sel_A_to_A
                    and offer[2] == sel_A_to_B
                    and offer[3] == sel_A_to_C
            ):
                offer[7] = 1
            if (
                    offer[0] == sel_name_B
                    and offer[1] == sel_B_to_A
                    and offer[2] == sel_B_to_B
                    and offer[3] == sel_B_to_C
            ):
                offer[8] = 1
            if (
                    offer[0] == sel_name_C
                    and offer[1] == sel_C_to_A
                    and offer[2] == sel_C_to_B
                    and offer[3] == sel_C_to_C
            ):
                offer[9] = 1
            offer_dict = (
                offer[0],
                offer[1],
                offer[2],
                offer[3],
                offer[4],
                offer[5],
                offer[6],
                offer[7],
                offer[8],
                offer[9],
            )
            offers_dict[offer_dict] = offer_dict
        vars.update({"offers_dictionary": sorted(offers_dict.values())})
        return vars

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session  # Seyit
        group = player.group  # Seyit
        for p in group.get_players():
            if p.position == 'A':
                p.payoff = group.payoff_A * session.config['payoff_conversion']
            if p.position == 'B':
                p.payoff = group.payoff_B * session.config['payoff_conversion']
            if p.position == 'C':
                p.payoff = group.payoff_C * session.config['payoff_conversion']


class Payoff(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def vars_for_template(player: Player):
        session = player.session  # Seyit
        vars = vars_for_template(player)
        timers = session.config['timers']
        vars.update({"timers": timers})
        return vars


class Email(Page):
    form_model = 'player'
    form_fields = ['comment_email']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        session = player.session  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False

class PhaseIII_Failure(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == False
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        else:
            return False

    # @staticmethod
    def vars_for_template(player: Player):
        group = player.group  # Seyit
        offers_dict = dict()
        vars = vars_for_template(player)
        prop_name_A = group.proposed_coalition_player_A
        prop_name_B = group.proposed_coalition_player_B
        prop_name_C = group.proposed_coalition_player_C
        prop_A_to_A = group.allocation_A_to_A
        prop_A_to_B = group.allocation_A_to_B
        prop_A_to_C = group.allocation_A_to_C
        prop_B_to_A = group.allocation_B_to_A
        prop_B_to_B = group.allocation_B_to_B
        prop_B_to_C = group.allocation_B_to_C
        prop_C_to_A = group.allocation_C_to_A
        prop_C_to_B = group.allocation_C_to_B
        prop_C_to_C = group.allocation_C_to_C
        sel_name_A = group.selected_coalition_name_player_A
        sel_name_B = group.selected_coalition_name_player_B
        sel_name_C = group.selected_coalition_name_player_C
        sel_A_to_A = group.selected_coalition_allocation_A_player_A
        sel_A_to_B = group.selected_coalition_allocation_B_player_A
        sel_A_to_C = group.selected_coalition_allocation_C_player_A
        sel_B_to_A = group.selected_coalition_allocation_A_player_B
        sel_B_to_B = group.selected_coalition_allocation_B_player_B
        sel_B_to_C = group.selected_coalition_allocation_C_player_B
        sel_C_to_A = group.selected_coalition_allocation_A_player_C
        sel_C_to_B = group.selected_coalition_allocation_B_player_C
        sel_C_to_C = group.selected_coalition_allocation_C_player_C
        proposed_by_A = 0
        proposed_by_B = 0
        proposed_by_C = 0
        selected_by_A = 0
        selected_by_B = 0
        selected_by_C = 0
        offer_A = [
            group.proposed_coalition_player_A,
            group.allocation_A_to_A,
            group.allocation_A_to_B,
            group.allocation_A_to_C,
            proposed_by_A,
            proposed_by_B,
            proposed_by_C,
            selected_by_A,
            selected_by_B,
            selected_by_C,
        ]
        offer_B = [
            group.proposed_coalition_player_B,
            group.allocation_B_to_A,
            group.allocation_B_to_B,
            group.allocation_B_to_C,
            proposed_by_A,
            proposed_by_B,
            proposed_by_C,
            selected_by_A,
            selected_by_B,
            selected_by_C,
        ]
        offer_C = [
            group.proposed_coalition_player_C,
            group.allocation_C_to_A,
            group.allocation_C_to_B,
            group.allocation_C_to_C,
            proposed_by_A,
            proposed_by_B,
            proposed_by_C,
            selected_by_A,
            selected_by_B,
            selected_by_C,
        ]
        offers = (offer_A, offer_B, offer_C)
        for offer in offers:
            if (
                    offer[0] == prop_name_A
                    and offer[1] == prop_A_to_A
                    and offer[2] == prop_A_to_B
                    and offer[3] == prop_A_to_C
            ):
                offer[4] = 1
            if (
                    offer[0] == prop_name_B
                    and offer[1] == prop_B_to_A
                    and offer[2] == prop_B_to_B
                    and offer[3] == prop_B_to_C
            ):
                offer[5] = 1
            if (
                    offer[0] == prop_name_C
                    and offer[1] == prop_C_to_A
                    and offer[2] == prop_C_to_B
                    and offer[3] == prop_C_to_C
            ):
                offer[6] = 1
            if (
                    offer[0] == sel_name_A
                    and offer[1] == sel_A_to_A
                    and offer[2] == sel_A_to_B
                    and offer[3] == sel_A_to_C
            ):
                offer[7] = 1
            if (
                    offer[0] == sel_name_B
                    and offer[1] == sel_B_to_A
                    and offer[2] == sel_B_to_B
                    and offer[3] == sel_B_to_C
            ):
                offer[8] = 1
            if (
                    offer[0] == sel_name_C
                    and offer[1] == sel_C_to_A
                    and offer[2] == sel_C_to_B
                    and offer[3] == sel_C_to_C
            ):
                offer[9] = 1
            offer_dict = (
                offer[0],
                offer[1],
                offer[2],
                offer[3],
                offer[4],
                offer[5],
                offer[6],
                offer[7],
                offer[8],
                offer[9],
            )
            offers_dict[offer_dict] = offer_dict
        vars.update({"offers_dictionary": sorted(offers_dict.values())})
        return vars

    # @staticmethod
    def get_timeout_seconds(player: Player):
        session = player.session  # Pradeep
        return session.config['timeout_time']

    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        if timeout_happened:
            participant.kicked = True
        leftover_check(player)


class ManipulationCheck1(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['manipulation_check1']


class ManipulationCheck2(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['manipulation_check2']


class SeatsDeserveA(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['seats_deserve']


class Motivations(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['motivation_max', 'motivation_harm', 'motivation_deserve']


class IRI_PT_dutch(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['pt_1', 'pt_2', 'pt_3', 'pt_4', 'pt_5', 'pt_6', 'pt_7']


class IRI_EC_dutch(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['ec_1', 'ec_2', 'ec_3', 'ec_4', 'ec_5', 'ec_6', 'attention_check', 'ec_8']


class Adapted_PT_dutch(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['apt_1', 'apt_2', 'apt_3', 'apt_4']


class PC_use(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['pcuse']


class BudgetDeserveA(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['budget_deserve']


class Device(Page):
    form_model = 'player'
    form_fields = ['device']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False


class Browser(Page):
    form_model = 'player'
    form_fields = ['browser']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        else:
            return False


class Funnel(Page):
    form_model = 'player'
    form_fields = ['comment']

    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False


class Demographics(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['age', 'gender']


class Debriefing(Page):
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
                and participant.leftover == False
        ):
            return True
        # elif (
        #         subsession.round_number == C.NUM_ROUNDS
        #         and participant.end_game == False
        # ):
        #     return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                # and player.round_number == 1
        ):
            return True
        else:
            return False
    def before_next_page(player: Player):
        participant = player.participant  # Seyit
        participant.end_game = True

class Leftover(Page):
    form_model = 'player'
    form_fields = ['comment_snr2']
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if (
                participant.grouped == False
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
                and player.round_number == 1
        ):
            return True
        else:
            return False

    # @staticmethod
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)

    # @staticmethod
    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        participant.leftover = True


class ID(Page):
    # @staticmethod
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        subsession = player.subsession  # Seyit
        group = player.group  # Seyit
        if (
                participant.end_game == False
                and group.coalition_formed == True
                and participant.kicked == False
        ):
            return True
        elif (
                subsession.round_number == C.NUM_ROUNDS
                and participant.end_game == False
                and participant.kicked == False
        ):
            return True
        elif (
                participant.leftover == True
                and participant.kicked == False
                and participant.end_game == False
        ):
            return True
        else:
            return False

    # @staticmethod
    # @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant  # Seyit
        participant.end_game = True


class Kicked(Page):
    # @staticmethod
    # @staticmethod
    def is_displayed(player: Player):
        participant = player.participant  # Seyit
        if participant.kicked == True:
            return True
        else:
            return False

    # @staticmethod
    # @staticmethod
    def vars_for_template(player: Player):
        return vars_for_template(player)


page_sequence = [
    Waitforgroup,
    Groupingconfirmation,
    # Sliderinstructions,
    # Slider,
    # EndRound1,
    # Slider2,
    # EndRound2,
    # Slider3,
    Waitforparticipants,
    # PositionAssignment,
    AssignedPosition,
    InstructionsCoalitions,
    ComprehensionCheck,
    ComprehensionCheck1,
    ComprehensionCheck2,
    ComprehensionCheck3,
    BargainingStarts,
    NewRound,
    PhaseI,
    WaitForOffers,
    OffersMade,
    PhaseII,
    WaitForSelection,
    OffersSelected,
    PhaseIII_Success,
    Payoff,
    PhaseIII_Failure,
    # SeatsDeserveA,
    Leftover,
    IRI_PT_dutch,
    IRI_EC_dutch,
    Adapted_PT_dutch,
    # ManipulationCheck2control,
    # ManipulationCheck2controlBudget,
    # Motivations,
    # ManipulationCheck2,
    # Device,
    # Browser,
    # Funnel,
    Demographics,
    # Email,
    # PC_use,
    Debriefing,
    # ID,
    Kicked,
]
