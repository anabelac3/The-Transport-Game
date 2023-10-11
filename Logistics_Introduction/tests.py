from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot




class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            yield (Slider, {'slider1': 50, 'slider2': 50, 'slider3': 50, 'slider4': 0, 'slider5': 0, 'slider6': 0, 'slider7': 0, 'slider8': 0, 'slider9': 0, 'slider10': 0, 'slider11': 0, 'slider12': 0, 'slider13': 0, 'slider14': 0, 'slider15': 0, 'slider16': 0, 'slider17': 0, 'slider18': 0, 'slider19': 0, 'slider20': 0, 'slider21': 0,})
            yield (Results)
            assert self.player.score == 3
            yield (AssignedPosition)
            assert self.player.position == 'A'
        elif self.player.id_in_group == 2:
            yield (Slider, {'slider1': 50, 'slider2': 50, 'slider3': 0, 'slider4': 0, 'slider5': 0, 'slider6': 0, 'slider7': 0, 'slider8': 0, 'slider9': 0, 'slider10': 0, 'slider11': 0, 'slider12': 0, 'slider13': 0, 'slider14': 0, 'slider15': 0, 'slider16': 0, 'slider17': 0, 'slider18': 0, 'slider19': 0, 'slider20': 0, 'slider21': 0,})
            yield (Results)
            assert self.player.score == 2
            yield (AssignedPosition)
            assert self.player.position == 'B'
        elif self.player.id_in_group == 3:
            yield (Slider, {'slider1': 50, 'slider2': 0, 'slider3': 0, 'slider4': 0, 'slider5': 0, 'slider6': 0, 'slider7': 0, 'slider8': 0, 'slider9': 0, 'slider10': 0, 'slider11': 0, 'slider12': 0, 'slider13': 0, 'slider14': 0, 'slider15': 0, 'slider16': 0, 'slider17': 0, 'slider18': 0, 'slider19': 0, 'slider20': 0, 'slider21': 0,})
            yield (Results)
            assert self.player.score == 1
            yield (AssignedPosition)
            assert self.player.position == 'C'



