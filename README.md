# Moonville

## Space Apps Challenge 2013

This is a repository for my (potential) contribution to the [NASA Space Apps Challenge 2013](http://spaceappschallenge.org/). I will not be able to join the competition since the Hackathon (20-21/4) clashes with a lot of other stuff for me. But, I'm hoping to build a rough, playable prototype of a simulation game I will call _Moonville_.

### Overview

I plan to build a "pluggable" game structure in Python (using either [cocos2d](http://cocos2d.org/) or [pyGame](http://www.pygame.org/)) where players can themselves add levels, items and possibly even game mechanics and graphics.

For the Space Apps Challenge weekend I hope to be able to fill the structure wih enough game content to have a playable children's game (5+ years).

## Challenge description for [Bootstraping of Space Industry](http://spaceappschallenge.org/challenge/affordable-rapid-bootstrapping-of-space-industry/).

### Background:

The concept of establishing a presence on the Moon in some form is elusive to many people. How hard is it? Could we do it? Why should we? What resources does the Moon have that could support an industry? We want to raise awareness about both the potential for a lunar industry and the challenges of developing one.

### Challenge Description:

Develop a simulation of a lunar industry through a series of "bootstrapping" stages until it becomes self-sustaining. The strategy is to decide which machines to build first and how many of them, using resources launched from Earth and available from the Moon. A major part of this challenge is learning what the purpose and value of a lunar industry could be and incorporating it into the game.

### Functional Specifications:

The industry consists of a set of devices equivalent to the ["Global Village Construction Set"](http://opensourceecology.org/wiki/Global_Village_Construction_Set) but adapted to lunar industry (no humans present in the early stages; just robots). Players get to launch an initial set of hardware to the Moon, choosing from a set of available devices. Suggested devices: lunar excavators, metal refineries (extract metal from the soil), solar cell makers, 3D printers, communication relays, etc.

The players have monetary budgets, from which they can buy launch mass for the machines they send to the Moon in the initial set and then in subsequent shipments of parts. Users can make money by selling manufactured goods such as propellants to spaceports in orbit or spare parts to other users/entities, which are introduced at varying stages of the game. The game ends when the user runs out of money.

Examples of problems players could encounter

* They run out of power (deficient in solar cell makers)
* They have more parts then their robonauts can assemble (focused on building other things before making more robonauts)
* They don’t have right materials available (chemical plants/refineries for necessary materials weren’t built)

Flexibility could be built into the game, pending approval by the game master

* Players could invent new machines, which are checked them for realism in the physics and chemistry.  There could even be a patent system.  
* Players could identify new income streams
