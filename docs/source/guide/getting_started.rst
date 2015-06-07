Gettings Started
================

To use vindinium, create a file to execute the client's code, for example, 
``main.py``::

    import vindinium

    # Create a vindinium client
    client = vindinium.Client(
        key='aait3gih',                 # your bot code
        mode='training',                # 'training' or 'arena'
        n_turns=300,                    # only valid for training
        server='http://localhost:9000', # if local, or 'http://vindinium.org'
        open_browser=True               # if true, it open the browser when
                                        #    game starts
    )

    url = client.run(vindinium.bots.MinerBot())
    print 'Replay in:', url


The method ``client.run`` receives a bot instance, see below how to create your
bot.


Creating Bots
-------------

All bots must inherit from ``vindinium.bots.RawBot`` or ``vindinium.bots.BaseBot``,
both contains the same methods, but diverge how the state is processed. For
instance, ``RawBot`` does not process the state, that why the name, while 
``BaseBot`` creates and updates a ``Game`` instance, which contains information
about map, heros and buildings.

It is recommended that you create your bot from ``BaseBot``, e.g.::

    class MyBot(vindinium.bots.BaseBot):
        def start(self):
            print 'Game just started'

        def move(self):
            print 'Game asking for a movement'
            return vindinium.STAY

        def end(self):
            print 'Game finished'


With this, your bot has the access to the following attributes:

- **id**: the hero's id.
- **game**: the game instance.
- **hero**: the hero instance.
- **state**: the raw state.

Notice that, the ``move`` method must return the bot's command:
``vindinium.STAY``, ``vindinium.NORTH``, ``vindinium.LEFT``, 
``vindinium.SOUTH`` or ``vindinium.WEST``.