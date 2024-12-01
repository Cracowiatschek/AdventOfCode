
name: str = "Day 1: Historian Hysteria"
def init_data(path):
    return open(path, 'r').read().split("\n")


class GetDistance:
    def __init__(self):
        self.left_list: list[int] = []
        self.right_list: list[int] = []
        self.distance: int = 0
        self.increases_score: int = 0

    def data_parser(self, data: list[str]) -> None:
        for i in data:
            get_places: list[str] = i.split(' ')
            self.left_list.append(int(get_places[0]))
            self.right_list.append(int(get_places[-1]))

    @staticmethod
    def get_the_smallest(list_of_places: list[int]) -> int:
        minimal_value: int = min(list_of_places)
        return list_of_places.index(minimal_value)

    def get_distance(self) -> None:
        self.left_list.sort()
        self.right_list.sort()
        for i in range(len(self.left_list)):
            items: list[int] = [self.left_list[i], self.right_list[i]]
            self.distance += max(items) - min(items)

    def get_increases_score(self) -> None:
        for i in range(len(self.left_list)):
            left_item: int = self.left_list[i]
            item_count_on_right: int = self.right_list.count(left_item)
            self.increases_score += left_item * item_count_on_right


def output(data: list[str]):

    solution = GetDistance()
    solution.data_parser(data)
    solution.get_distance()
    solution.get_increases_score()

    return solution.distance, solution.increases_score
