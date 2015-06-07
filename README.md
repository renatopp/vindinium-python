# vindinium-python

An awesome python client for Vindinium.

Vindinium is an online and continuous competition where you control a bot in a turn-based game, consult [the site](http://vindinium.org) to know more. Note: this client is based on the [ornicar's client](https://github.com/ornicar/vindinium-starter-python).

This library provides several base and simple bots, helper structures and common algorithms that allow you to create bots in an easy and fast way, focusing on the strategy and specific techniques of your bot.

The library has the following features:

- Bots:
  - RawBot: a bot that does nothing.
  - BaseBot: a bot that process the state and create and update a Game object.
  - RandomBot: a bot that perform random movements.
  - MinerBot: a bot that looks for mines continuously.
  - AggressiveBot: a bot that only goes after other bots.

- Models (used by base bot to create the game structure):
  - Game: stores all other models.
  - Map: stores static information about the map.
  - Mine: represents a mine in the map.
  - Hero: represents a hero in the game.
  - Tavern: represents a tavern in the game.

- AI algorithms (in general, already specialized for vindinium):
  - AStar: the A* algorithm.

Note: this client fix the inconsistent axis of the server, so you don't have to worry about that (if you're using the game model).

## Installation (automatic)

    pip install vindinium

or

    easy_install vindinium

## Dependences

- [python-requests](http://docs.python-requests.org/en/latest/)

## Usage

    import vindinium

    # Create a vindinium client
    client = vindinium.Client(
        key='aait3gih',
        mode='training',
        n_turns=300,
        server='http://localhost:9000',
        open_browser=True
    )

    # Run the random bot once
    print 'Running...'
    url = client.run(vindinium.bots.MinerBot())
    print 'Replay in:', url

[Check out the documentation to know more](http://pythonhosted.org/vindinium/).