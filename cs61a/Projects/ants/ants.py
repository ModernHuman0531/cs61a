"""CS 61A presents Ants Vs. SomeBees."""

import random
from ucb import main, interact, trace
from collections import OrderedDict

################
# Core Classes #
################


class Place:
    """A Place holds insects and has an exit to another Place."""

    def __init__(self, name, exit=None):
        """Create a Place with the given NAME and EXIT.
        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.bees = []        # A list of Bees
        self.ant = None       # An Ant
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        # BEGIN Problem 2
        """
        PESUDOCODE:
        if the Place we're creating that have an exit, then the exit's entrance must be the Place we're creating right now.
        we have to do this because in the constructor we always set the entrance to zero 
        tip:
        self = the Place we're creating right now.
        exit = the Place we need to connect if it exist
        """
        "*** YOUR CODE HERE ***"
        if exit != None:
            exit.entrance = self
        # END Problem 2

    def is_hive(self):
        return False

    def add_insect(self, insect):
        """
        Asks the insect to add itself to the current place. This method exists so
            it can be enhanced in subclasses.
        """
        insect.add_to(self)

    def remove_insect(self, insect):
        """
        Asks the insect to remove itself from the current place. This method exists so
            it can be enhanced in subclasses.
        """
        insect.remove_from(self)

    def __str__(self):
        return self.name


class Insect:
    """An Insect, the base class of Ant and Bee, has health and a Place."""

    damage = 0
    # ADD CLASS ATTRIBUTES HERE
    is_watersafe = False

    def __init__(self, health, place=None):
        """Create an Insect with a health amount and a starting PLACE."""
        self.health = health
        self.place = place  # set by Place.add_insect and Place.remove_insect

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and remove the insect from its place if it
        has no health remaining.
        >>> test_insect = Insect(5)
        >>> test_insect.reduce_health(2)
        >>> test_insect.health
        3
        """
        self.health -= amount
        if self.health <= 0:
            self.death_callback()
            self.place.remove_insect(self)

    def action(self, gamestate):
        """The action performed each turn.
        gamestate -- The GameState, used to access game state information.
        """

    def death_callback(self):
        # overriden by the gui
        pass

    def add_to(self, place):
        """Add this Insect to the given Place
        By default just sets the place attribute, but this should be overriden in the subclasses
            to manipulate the relevant attributes of Place
        """
        self.place = place

    def remove_from(self, place):
        self.place = None

    def __repr__(self):
        cname = type(self).__name__
        return '{0}({1}, {2})'.format(cname, self.health, self.place)


class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    is_doubled = False
    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, health=1):
        """Create an Insect with a HEALTH quantity."""
        super().__init__(health)

    def is_container(self):
        return False

    def can_contain(self, other):
        return False

    def contain_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def remove_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def add_to(self, place):
        if place.ant is None:
            place.ant = self
        elif self.can_contain(place.ant):#The ant we add is container, and the original ant isn't container
            self.contain_ant(place.ant)
            place.ant = self
        elif place.ant.can_contain(self):#The ant we add isn't container, but the original ant is container
            place.ant.contain_ant(self)
        else:
            # BEGIN Problem 8
            assert place.ant is None, 'Two ants in {0}'.format(place)
            # END Problem 8
        Insect.add_to(self, place)

    def remove_from(self, place):
        if place.ant is self:
            place.ant = None
        elif place.ant is None:
            assert False, '{0} is not in {1}'.format(self, place)
        else:
            # queen or container (optional) or other situation
            place.ant.remove_ant(self)
        Insect.remove_from(self, place)

    def buff(self):
        """Double this ants's damage, if it has not already been buffed."""
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        # END Problem EC


class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    # OVERRIDE CLASS ATTRIBUTES HERE
    """Because every HarvestAnt cost same food, it isn't different from 
    the the object, so it will be the class attribution"""
    food_cost = 2

    def action(self, gamestate):
        """Produce 1 additional food for the colony.
        gamestate -- The GameState, used to access game state information.
        """
        # BEGIN Problem 1
        "*** YOUR CODE HERE ***"
        gamestate.food = gamestate.food + 1
        # END Problem 1


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3
    min_range, max_range = -1, float('inf')#If we need to set the parameter in different value, we can put the parameter in the class attribute

    def nearest_bee(self, beehive):
        """Return the nearest Bee in a Place that is not the HIVE (beehive), connected to
        the ThrowerAnt's Place by following entrances.
        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        """PESUDOCODE:
        while is not in the hive:
            check the place:
            if it contains the ants:
                return a random ants
            else:
                update to the next place
        return none
        """
        """
        For problem 4 we must add the max_range and minb_range, but do not change the behavior of this class.
        With this two parameter we can implement this idea into the short_thrower and the long_thrower
        """
        place_to_find = self.place
        #Set range:
        distance = 0
        while place_to_find != beehive:
            bee_be_attacked = bee_selector(place_to_find.bees)
            if bee_be_attacked == None:
                place_to_find = place_to_find.entrance
                distance += 1
            else:#The ant must attack the cloest bee within the range
                if distance < self.min_range or distance > self.max_range:
                    place_to_find = place_to_find.entrance
                    distance += 1
                else:
                    return bee_be_attacked
        return None
        # END Problem 3 and 4

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its health."""
        if target is not None:
            target.reduce_health(self.damage)

    def action(self, gamestate):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(gamestate.beehive))


def bee_selector(bees):
    """Return a random bee from a list of bees, or return None if bees is empty."""
    assert isinstance(bees, list), "bee_selector's argument should be a list but was a %s" % type(bees).__name__
    if bees:
        return random.choice(bees)

##############
# Extensions #
##############


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at most 3 places away."""

    name = 'Short'
    food_cost = 2
    max_range = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = False   # Change to True to view in the GUI
    implemented = True   # Change to True to view in the GUI
    # END Problem 4


class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 5 places away."""

    name = 'Long'
    food_cost = 2
    min_range = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = False   # Change to True to view in the GUI
    implemented = True   # Change to True to view in the GUI
    # END Problem 4


class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""

    name = 'Fire'
    damage = 3
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    health = 3
    # BEGIN Problem 5
    implemented = False   # Change to True to view in the GUI
    implemented = True  # Change to True to view in the GUI
    # END Problem 5

    def __init__(self, health=3):
        """Create an Ant with a HEALTH quantity."""
        super().__init__(health)

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and remove the FireAnt from its place if it
        has no health remaining.
        Make sure to reduce the health of each bee in the current place, and apply
        the additional damage if the fire ant dies.
        """
        # BEGIN Problem 5
        "*** YOUR CODE HERE ***"
        """
        PESUDOCODE:
        Construct the copy of the bee's list in the place of the fire ant and loop it to cause the damage if the Fire ant is attacked.
        If the fire_ants is dead, loop over the bee's list and cause fire ant's damage before the fire ant's is removed
        """
        bee_list = self.place.bees[:]
        """Should create a exception for fire ant, since
            1.The reflected damage of a fire ant should not be doubled
            2.Only the extra damage it deals when  its health is 0
        """
        if amount >= self.health:#The case when fireant die do 'additional' damage
            for bee in bee_list:
                Insect.reduce_health(bee, self.damage + amount)
            Ant.reduce_health(self, amount)
        else:
            for bee in bee_list:#Normal case
                Insect.reduce_health(bee, amount)
            Ant.reduce_health(self, amount)
        # END Problem 5

# BEGIN Problem 6
# The WallAnt class
class WallAnt(Ant):#Because the damage in the Ant class is original set to zero, so we don't have to redefine it
    name = 'Wall'
    food_cost = 4
    implemented = True
    def __init__(self, health = 4):
        super().__init__(health)
    
    
# END Problem 6

# BEGIN Problem 7
# The HungryAnt Class
class HungryAnt(Ant):
    name = 'Hungry'
    food_cost = 4
    implemented = True
    chew_duration = 3
    def __init__(self, health = 1):
        super().__init__(health)
        self.chewing = 0
    """
    Chewing method:
    1.If the ant isn't eating, randomally picking one bee in the same place and eat it, then let the chewing equal to chew_duration
    2.Else, reduce the chewing with 1
    """
    def eaten_bee(self, bee):
        if self.place.bees:
            Insect.reduce_health(bee, bee.health)
            self.chewing = HungryAnt.chew_duration
    def action(self, gamestate):
        if self.chewing == 0:
            bee = bee_selector(self.place.bees)
            self.eaten_bee(bee)
        else:
            self.chewing -= 1
# END Problem 7


class ContainerAnt(Ant):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contained_ant = None

    def is_container(self):
        return True

    def can_contain(self, other):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        """
        PESUDOCODE:
        if other is container or self already contain another ant:
            return False
        else:
            return True
        """
        if other.is_container() == True or self.contained_ant != None:
            return False
        else:
            return True
        # END Problem 8

    def contain_ant(self, ant):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        """
        Sets the bodyguard's cotained_ant attributed to the  passed in ant argument
        """
        self.contained_ant = ant
        # END Problem 8

    def remove_ant(self, ant):
        if self.contained_ant is not ant:
            assert False, "{} does not contain {}".format(self, ant)
        self.contained_ant = None

    def remove_from(self, place):
        # Special handling for container ants (this is optional)
        if place.ant is self:
            # Container was removed. Contained ant should remain in the game
            place.ant = place.ant.contained_ant
            Insect.remove_from(self, place)
        else:
            # default to normal behavior
            Ant.remove_from(self, place)

    def action(self, gamestate):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        if self.contained_ant != None:
            self.contained_ant.action(gamestate)
        # END Problem 8


class BodyguardAnt(ContainerAnt):
    """BodyguardAnt provides protection to other Ants."""

    name = 'Bodyguard'
    food_cost = 4
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 8
    implemented = False   # Change to True to view in the GUI
    implemented = True   # Change to True to view in the GUI
    def __init__(self,health = 2):
        super().__init__(health)
    # END Problem 8

# BEGIN Problem 9
# The TankAnt class
class TankAnt(ContainerAnt):
    name = 'Tank'
    food_cost = 6
    damage = 1
    implemented = True
    def __init__(self, health = 2):
        super().__init__(health)
    def action(self, gamestate):
        ContainerAnt.action(self, gamestate)
        bee_list = self.place.bees[:]
        for bee in bee_list:
            bee.reduce_health(self.damage)
# END Problem 9


class Water(Place):
    """Water is a place that can only hold watersafe insects."""

    def add_insect(self, insect):
        """Add an Insect to this place. If the insect is not watersafe, reduce
        its health to 0."""
        # BEGIN Problem 10
        "*** YOUR CODE HERE ***"
        """
        Don't repeat the code if we  have already write it before.Like the place insect method we have already written in the Place class
        """
        super().add_insect(insect)
        if insect.is_watersafe == False:
            insect.reduce_health(insect.health)
        
        # END Problem 10

# BEGIN Problem 11
# The ScubaThrower class
class ScubaThrower(ThrowerAnt):
    name = 'Scuba'
    implemented = True
    food_cost = 6
    is_watersafe = True
    def __init__(self, health = 1):
        super().__init__(health)
# END Problem 11

# BEGIN Problem EC


class QueenAnt(ScubaThrower):  # You should change this line
# END Problem EC
    """The Queen of the colony. The game is over if a bee enters her place."""

    name = 'Queen'
    food_cost = 7
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem EC
    created_num = 0
    implemented = True   # Change to True to view in the GUI
    # END Problem EC

    def __init__(self, health=1):
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        self.index = QueenAnt.created_num
        QueenAnt.created_num += 1
        super().__init__(health)
        # END Problem EC

    def action(self, gamestate):
        """1. A queen ant throws a leaf, but also doubles the damage of ants
        in her tunnel.
        
        2. Impostor queens do only one thing: reduce their own health to 0.
        """
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        if self.index == 0:#2.
            self.throw_at(self.nearest_bee(gamestate.beehive))# Throw the leaf to the nearest bee
            temp_place = self.place.exit
            while temp_place != None:
                if temp_place.ant != None:
                    if temp_place.ant.is_doubled == False and temp_place.ant.name is not 'Fire' :
                        temp_place.ant.damage *= 2
                        temp_place.ant.is_doubled = True                        
                        #return TankAnt is TankAnt
                        if temp_place.ant.name is 'Bodyguard' or temp_place.ant.name is 'Tank':
                            if temp_place.ant.contained_ant != None:
                                temp_place.ant.contained_ant.damage *= 2
                                temp_place.ant.contained_ant.is_doubled = True
                    """
                    elif temp_place.ant.name is 'Fire' and temp_place.ant.is_doubled == False:
                        if temp_place.ant.health == 0:
                            temp_place.ant.damage *= 2
                            temp_place.ant.is_doubled = True  
                    """
                            
                temp_place = temp_place.exit
        else:
            self.reduce_health(self.health)

        
        # END Problem EC

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and if the True QueenAnt has no health
        remaining, signal the end of the game.
        """
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        """
        We have to differ the real queen with imposter.
        If real health = 0, end the game.
        But if the imposter' health = 0, keep going the game
        """
        Insect.reduce_health(self, amount)
        if self.health == 0:
            if self.index == 0:
                bees_win()

        
        # END Problem EC
    def remove_from(self, place):
        """
        Not allow to remove the true queen.
        If is imposter, remove it as usual.
        """
        if self.index != 0:
            return Ant.remove_from(self,place)

class AntRemover(Ant):
    """Allows the player to remove ants from the board in the GUI."""

    name = 'Remover'
    implemented = False

    def __init__(self):
        super().__init__(0)


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    is_watersafe = True

    def sting(self, ant):
        """Attack an ANT, reducing its health by 1."""
        ant.reduce_health(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Special handling for NinjaAnt
        # BEGIN Problem Optional 1
        return self.place.ant is not None
        # END Problem Optional 1

    def action(self, gamestate):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.
        gamestate -- The GameState, used to access game state information.
        """
        destination = self.place.exit
        # Extra credit: Special handling for bee direction
        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2
        if self.blocked():
            self.sting(self.place.ant)
        elif self.health > 0 and destination is not None:
            self.move_to(destination)

    def add_to(self, place):
        place.bees.append(self)
        Insect.add_to(self, place)

    def remove_from(self, place):
        place.bees.remove(self)
        Insect.remove_from(self, place)

    def slow(self, length):
        """Apply a status lasting LENGTH turns that causes bee to execute
        the previous .action on even-numbered turns."""
        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2

    def scare(self, length):
        """If this Bee has not been scared before, apply a status that
        lasts for LENGTH turns that causes bee to go backwards."""

        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2

    def apply_status(self, status, previous_action, length):
        """Apply STATUS to replace the current .action method for
        duraction LENGTH calls, after which it simply calls PREVIOUS_ACTION."""

        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2


############
# Optional #
############

class NinjaAnt(Ant):
    """NinjaAnt does not block the path and damages all bees in its place.
    This class is optional.
    """

    name = 'Ninja'
    damage = 1
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 1
    implemented = False   # Change to True to view in the GUI
    # END Problem Optional 1

    def action(self, gamestate):
        # BEGIN Problem Optional 1
        "*** YOUR CODE HERE ***"
        # END Problem Optional 1

############
# Statuses #
############


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    food_cost = 4
    # BEGIN Problem Optional 2
    implemented = False   # Change to True to view in the GUI
    # END Problem Optional 2

    def throw_at(self, target):
        if target:
            target.slow(3)


class ScaryThrower(ThrowerAnt):
    """ThrowerAnt that intimidates Bees, making them back away instead of advancing."""

    name = 'Scary'
    food_cost = 6
    # BEGIN Problem Optional 2
    implemented = False   # Change to True to view in the GUI
    # END Problem Optional 2

    def throw_at(self, target):
        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2


class LaserAnt(ThrowerAnt):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    food_cost = 10
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 3
    implemented = False   # Change to True to view in the GUI
    # END Problem Optional 3

    def __init__(self, health=1):
        super().__init__(health)
        self.insects_shot = 0

    def insects_in_front(self, beehive):
        # BEGIN Problem Optional 3
        return {}
        # END Problem Optional 3

    def calculate_damage(self, distance):
        # BEGIN Problem Optional 3
        return 0
        # END Problem Optional 3

    def action(self, gamestate):
        insects_and_distances = self.insects_in_front(gamestate.beehive)
        for insect, distance in insects_and_distances.items():
            damage = self.calculate_damage(distance)
            insect.reduce_health(damage)
            if damage:
                self.insects_shot += 1


##################
# Bees Extension #
##################

class Wasp(Bee):
    """Class of Bee that has higher damage."""
    name = 'Wasp'
    damage = 2


class Hornet(Bee):
    """Class of bee that is capable of taking two actions per turn, although
    its overall damage output is lower. Immune to statuses.
    """
    name = 'Hornet'
    damage = 0.25

    def action(self, gamestate):
        for i in range(2):
            if self.health > 0:
                super().action(gamestate)

    def __setattr__(self, name, value):
        if name != 'action':
            object.__setattr__(self, name, value)


class NinjaBee(Bee):
    """A Bee that cannot be blocked. Is capable of moving past all defenses to
    assassinate the Queen.
    """
    name = 'NinjaBee'

    def blocked(self):
        return False


class Boss(Wasp, Hornet):
    """The leader of the bees. Combines the high damage of the Wasp along with
    status immunity of Hornets. Damage to the boss is capped up to 8
    damage by a single attack.
    """
    name = 'Boss'
    damage_cap = 8
    action = Wasp.action

    def reduce_health(self, amount):
        super().reduce_health(self.damage_modifier(amount))

    def damage_modifier(self, amount):
        return amount * self.damage_cap / (self.damage_cap + amount)


class Hive(Place):
    """The Place from which the Bees launch their assault.
    assault_plan -- An AssaultPlan; when & where bees enter the colony.
    """

    def __init__(self, assault_plan):
        self.name = 'Hive'
        self.assault_plan = assault_plan
        self.bees = []
        for bee in assault_plan.all_bees:
            self.add_insect(bee)
        # The following attributes are always None for a Hive
        self.entrance = None
        self.ant = None
        self.exit = None

    def is_hive(self):
        return True

    def strategy(self, gamestate):
        exits = [p for p in gamestate.places.values() if p.entrance is self]
        for bee in self.assault_plan.get(gamestate.time, []):
            bee.move_to(random.choice(exits))
            gamestate.active_bees.append(bee)


class GameState:
    """An ant collective that manages global game state and simulates time.
    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """

    def __init__(self, strategy, beehive, ant_types, create_places, dimensions, food=2):
        """Create an GameState for simulating a game.
        Arguments:
        strategy -- a function to deploy ants to places
        beehive -- a Hive full of bees
        ant_types -- a list of ant constructors
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.beehive = beehive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.dimensions = dimensions
        self.active_bees = []
        self.configure(beehive, create_places)

    def configure(self, beehive, create_places):
        """Configure the places in the colony."""
        self.base = AntHomeBase('Ant Home Base')
        self.places = OrderedDict()
        self.bee_entrances = []

        def register_place(place, is_bee_entrance):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = beehive
                self.bee_entrances.append(place)
        register_place(self.beehive, False)
        create_places(self.base, register_place, self.dimensions[0], self.dimensions[1])

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        num_bees = len(self.bees)
        try:
            while True:
                self.beehive.strategy(self)         # Bees invade
                self.strategy(self)                 # Ants deploy
                for ant in self.ants:               # Ants take actions
                    if ant.health > 0:
                        ant.action(self)
                for bee in self.active_bees[:]:     # Bees take actions
                    if bee.health > 0:
                        bee.action(self)
                    if bee.health <= 0:
                        num_bees -= 1
                        self.active_bees.remove(bee)
                if num_bees == 0:
                    raise AntsWinException()
                self.time += 1
        except AntsWinException:
            print('All bees are vanquished. You win!')
            return True
        except BeesWinException:
            print('The ant queen has perished. Please try again.')
            return False

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.
        This method is called by the current strategy to deploy ants.
        """
        constructor = self.ant_types[ant_type_name]
        if self.food < constructor.food_cost:
            print('Not enough food remains to place ' + ant_type_name)
        else:
            ant = constructor()
            self.places[place_name].add_insect(ant)
            self.food -= constructor.food_cost
            return ant

    def remove_ant(self, place_name):
        """Remove an Ant from the game."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = ' (Food: {0}, Time: {1})'.format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status


class AntHomeBase(Place):
    """AntHomeBase at the end of the tunnel, where the queen resides."""

    def add_insect(self, insect):
        """Add an Insect to this Place.
        Can't actually add Ants to a AntHomeBase. However, if a Bee attempts to
        enter the AntHomeBase, a BeesWinException is raised, signaling the end
        of a game.
        """
        assert isinstance(insect, Bee), 'Cannot add {0} to AntHomeBase'
        raise BeesWinException()


def ants_win():
    """Signal that Ants win."""
    raise AntsWinException()


def bees_win():
    """Signal that Bees win."""
    raise BeesWinException()


def ant_types():
    """Return a list of all implemented Ant classes."""
    all_ant_types = []
    new_types = [Ant]
    while new_types:
        new_types = [t for c in new_types for t in c.__subclasses__()]
        all_ant_types.extend(new_types)
    return [t for t in all_ant_types if t.implemented]


class GameOverException(Exception):
    """Base game over Exception."""
    pass


class AntsWinException(GameOverException):
    """Exception to signal that the ants win."""
    pass


class BeesWinException(GameOverException):
    """Exception to signal that the bees win."""
    pass


def interactive_strategy(gamestate):
    """A strategy that starts an interactive session and lets the user make
    changes to the gamestate.
    For example, one might deploy a ThrowerAnt to the first tunnel by invoking
    gamestate.deploy_ant('tunnel_0_0', 'Thrower')
    """
    print('gamestate: ' + str(gamestate))
    msg = '<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n'
    interact(msg)

###########
# Layouts #
###########


def wet_layout(queen, register_place, tunnels=3, length=9, moat_frequency=3):
    """Register a mix of wet and and dry places."""
    for tunnel in range(tunnels):
        exit = queen
        for step in range(length):
            if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
                exit = Water('water_{0}_{1}'.format(tunnel, step), exit)
            else:
                exit = Place('tunnel_{0}_{1}'.format(tunnel, step), exit)
            register_place(exit, step == length - 1)


def dry_layout(queen, register_place, tunnels=3, length=9):
    """Register dry tunnels."""
    wet_layout(queen, register_place, tunnels, length, 0)


#################
# Assault Plans #
#################

class AssaultPlan(dict):
    """The Bees' plan of attack for the colony.  Attacks come in timed waves.
    An AssaultPlan is a dictionary from times (int) to waves (list of Bees).
    >>> AssaultPlan().add_wave(4, 2)
    {4: [Bee(3, None), Bee(3, None)]}
    """

    def add_wave(self, bee_type, bee_health, time, count):
        """Add a wave at time with count Bees that have the specified health."""
        bees = [bee_type(bee_health) for _ in range(count)]
        self.setdefault(time, []).extend(bees)
        return self

    @property
    def all_bees(self):
        """Place all Bees in the beehive and return the list of Bees."""
        return [bee for wave in self.values() for bee in wave]