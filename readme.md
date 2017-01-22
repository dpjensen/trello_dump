# trelloDump
A set of python scripts that prints important changes to trello boards

# Usage
The script looks for its Trello API keys in ~/.trello. An example config can be found as `example.trello`
```
#by default, looks for the board 'Word'
trelloDump
#specify a board
trelloDump --board personal
```

# Install
```
git clone https://blah_blah_blah
cd trello_dump
sudo pip3 install .
```

# Current state
- This is beta softwre, that contains a large number of hard-coded defualts in it's current state

# TODO
- Create a configurable list of change types to print
- Iterate through multiple locations for config file
- Less hacky way of printing changes from a list
