# trelloDump
A python script that prints recent changes to a trello board.

# Usage
The script looks for its Trello API keys in ~/.trello. An example config can be found as `example.trello`
```
#by default, looks for the board 'Work', and prints relevant changes.
$ trelloDump
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Changes in the past 7 days:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

============Item: Refactor important code, filed under My_list
~~~Item Marked as finished:~~~
		Date: 2017-02-13T19:45:30.652Z
		Done: Refactor important code
~~~Item updated:~~~
		Date: 2017-02-08T23:34:11.908Z
		Mostly done, test suite will need to be re-written
~~~Item created:~~~
		Date: 2017-02-08T19:22:04.606Z
		Filed under: My_list



#You can also specify a board
$ trelloDump --board personal
```
The toml config file also allows you to specify a `date_range` of applicable items, and a `done_name`, to specify the name of your "finished tasks" list.
If an item is moved to the `done_name` board, `trelloDump` prints the task as done.
It currently prints new cards, added comments, and when a card is moved to the `done_name` list.
# Install
```
git clone https://blah_blah_blah
cd trello_dump
sudo pip3 install .
```

# Current state
- This is beta softwre, that contains a large number of hard-coded defualts in it's current state

# TODO
- Create a configurable list of "interesting" actions.
- Less hacky way of printing changes from a list would be nice.
