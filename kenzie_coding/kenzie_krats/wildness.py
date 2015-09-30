__doc__ = """
A basic programming exercise to get Kenzie excited enough to learn to code. Maybe a basis for a game...
This is a little advanced, but hopefully she'll find it interesting.
"""

from random import choice # For telling jokes...


class Animal:
    """All animals have a defense mechanism, and know how to use it"""
    defense = "Runaway"
    def use_my_defense(self):
        print("%s: I'm gonna get you with my %s." % (self.name, self.defense))


class BrownBear(Animal):
    """Brown Bears Use claws, strength and a good sense of smell"""
    defense = "claws"
    name = "Brown Bear"

    def smell(self):
        print("%s: I can smell stuff far away." % self.name)

    def strength(self):
        print("%s: I can lift heavy logs." % self.name)


class PeregrineFalcon(Animal):
    defense = "talons"
    name = "Peregrine Falcon"

    def fly(self):
        print("%s: I fly 247 miles per hour." % self.name)

    def see(self):
        print("%s: I can see really well." % self.name)


class Wolf(Animal):
    defense = "the pack"
    name = "Wolf"

    def runs(self):
        print("%s: I run really far." % self.name)

    def smells(self):
        print("%s: I smell really well." % self.name)

class Person:
    """This can be anyone."""
    def __init__(self, name, legs=2, arms=2, favorite_color=None):
        self.name = name
        self.legs = legs
        self.arms = arms
        self.favorite_color = favorite_color

    def walk(self):
        print("%s: I'm walking" % self.name)

    def greet(self):
        print("Hello, my name is %s." % self.name)


class KrattBrother(Person):
    """This extends person to allow you to put on a creature power suit, and tell bad jokes."""

    def __init__(self, name, favorite_color, jokes):
        self.name = name
        self.favorite_color = favorite_color
        self.jokes = jokes
        super(Person, self).__init__()
        assert(self.name in ['Chris', 'Martin'])

    def tell_a_joke(self):
        print("%s: %s" %(self.name, choice(self.jokes)))

    def put_on_a_powersuit(self, creature):
        self.__class__ = type("Hero", (KrattBrother, creature.powers), {})
        print("%s: Thanks Aviva" % self.name)
        print("%s: Getting Creature Powers." % self.name)
        print("%s: Now I'm a %s." % (self.name, creature.powers.name))

    def take_off_powersuit(self):
        self.__class__ = type("KrattBrother",(KrattBrother,),{})
        print("%s: Now I'm back to normal" % self.name)


class aviva(Person):
    name = "Aviva"
    favorite_color = "Yellow"

    def make_a_disk(self, creature):
        print("%s: I'm making a %s disk for you." % (self.name, creature.name))
        return Disk(creature)


class Disk:

    def __init__(self, creature):
        self.powers = creature


"""
Let's put it all to work.
This is what gets run.
"""

if __name__ == "__main__":
    Chris = KrattBrother("Chris", favorite_color="Green", jokes=["Does a bear poop in the woods?", "Martin is Weird"])
    Chris.greet()
    Martin = KrattBrother("Martin", favorite_color="Blue", jokes=["Yeah, he wipes with a fluffy bunny.", "Chris is Weird"])
    Martin.greet()
    print()

    Chris.tell_a_joke()
    Martin.tell_a_joke()
    print()

    Aviva = aviva("Aviva")
    Aviva.greet()
    Gourmond = Person("Gourmond", favorite_color="Grey")
    Gourmond.greet()
    print()

    BB = Aviva.make_a_disk(BrownBear)
    Chris.put_on_a_powersuit(BB)
    Chris.smell()
    Chris.strength()
    Chris.use_my_defense()
    print()

    PF = Aviva.make_a_disk(Wolf)
    Martin.put_on_a_powersuit(PF)
    Martin.runs()
    Martin.smellsx()
    Martin.use_my_defense()
    print()

    Martin.take_off_powersuit()
    print("Martin's Favorite Color is %s" % Martin.favorite_color)
    print()

    try:
        KrattBrother(Gourmond, Gourmond.favorite_color, jokes=["endangered species are tasty"])
    except AssertionError:
        print("%s can't be a Kratt Brother." % Gourmond.name)
