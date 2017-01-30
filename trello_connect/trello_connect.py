import urllib3
import certifi
import json

class TrelloConnect():
    """
    A very simple class for connecting to the trello API.
    """

    def __init__(self, token, key, verb):
        self.token = token
        self.key = key
        self.http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )
        self.verbose = verb
        #get member info.
        request = "https://api.trello.com/1/members/me?fields=username&boards=all&board_fields=name&key={}&token={}".format(self.key, self.token)
        if self.verbose:
            print(request)
        resp = self.http.request("GET", request)

        if resp.status != 200:
            raise RuntimeError("Trello returned {}: {}".format(resp.status, resp.data))
        data_dict = json.loads(resp.data.decode("UTF-8"))

        board_dict = {}
        for board in data_dict["boards"]:
            board_dict[board["name"]] = board["id"]
        self.boards = board_dict

    def get_full_card_info(self, cid):
        """
        Returns a dataset on a card, given an ID.
        This returns a large dataset, core application requres at least all history
        """
        request = "https://api.trello.com/1/cards/{}?actions=all&actions_display=true&action_memberCreator_fields=username&members=true&member_fields=username,status&attachments=true&fields=all&checklists=all&list=true&actions_limit=50&key={}&token={}".format(cid, self.key, self.token)
        if self.verbose:
            print(request)
        resp = self.http.request("GET", request)
        data_dict = json.loads(resp.data.decode("UTF-8"))
        return data_dict

    def get_lists(self, board):
        """
        Get the lists in a board
        """
        if board not in self.boards:
            print("The board '{}' could not be found.".format(board))
        request = "https://api.trello.com/1/boards/{}?lists=open&list_fields=all&fields=name,desc&key={}&token={}".format(self.boards[board], self.key, self.token)
        if self.verbose:
            print(request)
        resp = self.http.request("GET", request)
        data_dict = json.loads(resp.data.decode("UTF-8"))
        return data_dict["lists"]

    def get_cards(self, list_id):
        """
        Get the cards in a list
        """
        request = "https://api.trello.com/1/lists/{}?fields=name&cards=open&card_fields=all&key={}&token={}".format(list_id, self.key, self.token)
        if self.verbose:
            print(request)
        resp = self.http.request("GET", request)
        data_dict = json.loads(resp.data.decode("UTF-8"))
        return data_dict
