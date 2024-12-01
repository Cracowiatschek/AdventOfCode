
name: str = "Day 1: Historian Hysteria"  # initialize challenge name for framework

class GetDistance:
    def __init__(self):
        self.left_list: list[int] = []
        self.right_list: list[int] = []
        self.distance: int = 0
        self.increases_score: int = 0

    def data_parser(self, data: list[str]) -> None: # get data from input
        for i in data:
            get_places: list[str] = i.split(' ')
            self.left_list.append(int(get_places[0]))  # split data between two lists
            self.right_list.append(int(get_places[-1]))

    @staticmethod
    def get_the_smallest(list_of_places: list[int]) -> int:  # get index for minimal value from list
        minimal_value: int = min(list_of_places)
        return list_of_places.index(minimal_value)

    def get_distance(self) -> None:  #calculate distance between points from left and right list
        self.left_list.sort()
        self.right_list.sort()
        for i in range(len(self.left_list)):
            items: list[int] = [self.left_list[i], self.right_list[i]]
            self.distance += max(items) - min(items)

    def get_increases_score(self) -> None:  # calculate increases score like int from left * conut int at right
        for i in range(len(self.left_list)):
            left_item: int = self.left_list[i]
            item_count_on_right: int = self.right_list.count(left_item)
            self.increases_score += left_item * item_count_on_right


def output(data: list[str]):  # get solution outputs for framework

    solution = GetDistance()
    solution.data_parser(data)
    solution.get_distance()
    solution.get_increases_score()

    return solution.distance, solution.increases_score
