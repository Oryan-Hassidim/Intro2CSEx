from collections import Counter
from itertools import combinations
import os
from typing import Optional, List


class Node:
    def __init__(self, data: Optional[str], positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def is_leaf(self):
        return self.positive_child is None and self.negative_child is None

    def __eq__(self, __o: object) -> bool:
        return (self is __o or
                (isinstance(__o, Node)
                 and self.data == __o.data
                 and self.positive_child == __o.positive_child
                 and self.negative_child == __o.negative_child))

    def __str__(self) -> str:
        left = str(self.positive_child) if self.positive_child else None
        right = str(self.negative_child) if self.negative_child else None
        val = repr(self.data)
        if left and right:
            return f'({str(left)} {val} {str(right)})'
        elif left:
            return f'({str(left)} {val})'
        elif right:
            return f'({val} {str(right)})'
        return f'({val})'

    def __repr__(self) -> str:
        left = repr(self.positive_child) if self.positive_child else None
        right = repr(self.negative_child) if self.negative_child else None
        val = repr(self.data)
        if left is None and right is None:
            return f'Node({val})'
        return f'Node({val}, {left}, {right})'


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms

    def __repr__(self):
        return f'Record({repr(self.illness)}, {repr(self.symptoms)})'


Records = List[Record]

# region funcions


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


def validate_type(val, _type, message=None):
    if not isinstance(val, _type):
        raise TypeError(
            message if message else f'Expected {_type} got {_type(val)}')


def validate_elements_type(iterable, type):
    for element in iterable:
        validate_type(element, type)


def validate_min(val, min, message=None):
    if val < min:
        raise ValueError(
            message if message else f'Expected {min} or greater, got {val}')


def validate_max(val, max, message=None):
    if val > max:
        raise ValueError(
            message if message else f'Expected {max} or less, got {val}')


def validate_equals(val1, val2, message):
    if val1 != val2:
        raise ValueError(message)


def get_leaves_and_pathes(node: Node, so_far=None):
    if so_far is None:
        so_far = []

    if node.is_leaf():
        yield (node.data, so_far)

    if node.positive_child:
        so_far.append(True)
        yield from get_leaves_and_pathes(node.positive_child, so_far)
        so_far.pop()

    if node.negative_child:
        so_far.append(False)
        yield from get_leaves_and_pathes(node.negative_child, so_far)
        so_far.pop()

# endregion


class Diagnoser:
    """
    Diagnoser class for diagnosing illnesses by symptoms. Implemented with binary tree.
    """

    def __init__(self, root: Node):
        """
        Initializes Diagnoser with root node.
        """
        self.root = root

    def diagnose(self, symptoms):
        """
        Diagnoses illness by symptoms.
        """
        node = self.root
        while not node.is_leaf():
            node = node.positive_child if node.data in symptoms else node.negative_child
        return node.data

    def calculate_success_rate(self, records):
        """
        Calculates success rate of diagnosis.
        """
        validate_min(len(records), 1)
        count = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                count += 1
        return count / len(records)

    def all_illnesses(self):
        """
        Returns all illnesses sorted by frequency.
        """
        times = Counter(i
                        for i, _ in get_leaves_and_pathes(self.root)
                        if i is not None)
        return [i for i, _ in times.most_common()]

    def paths_to_illness(self, illness):
        """
        Returns all paths to a given illness.
        """
        return [path.copy()
                for ill, path in get_leaves_and_pathes(self.root)
                if ill == illness]

    @staticmethod
    def minimize_core(node: Node, remove_empty):
        if node.is_leaf():
            return node
        node.negative_child = Diagnoser.minimize_core(
            node.negative_child, remove_empty)
        node.positive_child = Diagnoser.minimize_core(
            node.positive_child, remove_empty)
        if (not node.is_leaf()
                and node.negative_child == node.positive_child):
            return node.negative_child
        if node.is_leaf() or not remove_empty:
            return node
        if node.negative_child.data is None:
            return node.positive_child
        if node.positive_child.data is None:
            return node.negative_child
        return node

    def minimize(self, remove_empty=False):
        """
        Minimizes the root of the diagnoser.
        """
        self.root = self.minimize_core(self.root, remove_empty)

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return f"Diagnoser({repr(self.root)})"


def build_tree_core(records: Records, symptoms, yes: set, no: set):
    """
    helper function to build_tree function.
    """
    if len(symptoms) == 0:
        # is a leaf
        records = Counter(record.illness
                          for record in records
                          if yes.issubset(record.symptoms)
                          and no.isdisjoint(record.symptoms))
        return Node(records.most_common(1)[0][0] if records else None)

    symptom = symptoms.pop()

    is_in = symptom in yes
    yes.add(symptom)
    yes_node = build_tree_core(records, symptoms, yes, no)
    if not is_in:
        yes.remove(symptom)

    is_in = symptom in no
    no.add(symptom)
    no_node = build_tree_core(records, symptoms, yes, no)
    if not is_in:
        no.remove(symptom)

    symptoms.append(symptom)
    return Node(symptom, yes_node, no_node)


def build_tree(records, symptoms):
    """
    Builds tree from records, followed by given symptoms list.
    """
    validate_type(records, list)
    validate_type(symptoms, list)
    validate_elements_type(symptoms, str)
    validate_elements_type(records, Record)
    return Diagnoser(build_tree_core(records, symptoms[::-1], set(), set()))


def optimal_tree(records, symptoms, depth):
    validate_min(depth, 0, "Expected depth greater than or equals 0")
    validate_max(depth, len(symptoms),
                 "Expected depth less than or equals length of symptoms")
    validate_equals(len(symptoms), len(set(symptoms)),
                    "There is duplicated value in symptoms")
    validate_elements_type(records, Record)
    validate_elements_type(symptoms, str)
    return max((build_tree(records, list(combination))
                for combination in combinations(symptoms, depth)),
               key=lambda tree: tree.calculate_success_rate(records))


if __name__ == "__main__":
    pass
    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # covid-19   cold

    #flu_leaf = Node("covid-19", None, None)
    #cold_leaf = Node("cold", None, None)
    #inner_vertex = Node("fever", flu_leaf, cold_leaf)
    #healthy_leaf = Node("healthy", None, None)
    #root = Node("cough", inner_vertex, healthy_leaf)

    #diagnoser = Diagnoser(root)

    # diagnoser2 = Diagnoser(
    #    Node("Cough",
    #         Node("Headache",
    #              Node("Covid-19"),
    #              Node("Cold")
    #              ),
    #         Node("Headache",
    #              Node("Cold"),
    #              Node("Healthy")
    #              )
    #         ))

    # Simple test
    #diagnosis = diagnoser.diagnose(["cough"])
    # if diagnosis == "cold":
    #    print("Test passed")
    # else:
    #    print("Test failed. Should have printed cold, printed: ", diagnosis)

    # Add more tests for sections 2-7 here.
    #folder = "Data"
    # for file in os.listdir(folder):
    #    if file.endswith(".txt"):
    #        records = parse_data(os.path.join(folder, file))
    #        success_rate = diagnoser.calculate_success_rate(records)
    #        print(f'Success rate of {file} is {success_rate}')
    # print()

    #print("All illnesses: ", diagnoser.all_illnesses())
    # print()

    #print("Paths to covid-19: ", diagnoser.paths_to_illness("covid-19"))
    #print("Paths to cold: ", diagnoser.paths_to_illness("cold"))
    #print("Paths to Cold: ", diagnoser2.paths_to_illness("Cold"))
    # print()

    # Build a tree from the data.
    #records = parse_data("Data/small_data.txt")
    #symptoms = ["congestion", "fever", "irritability", "headache"]
    #tree = build_tree(records, symptoms)
    #print(repr(tree).replace("Node(", "\nNode("), end="\n\n")
    # tree.minimize()
    #print(repr(tree).replace("Node(", "\nNode("), end="\n\n")
    # tree.minimize(True)
    #print(repr(tree).replace("Node(", "\nNode("), end="\n\n")
    # print()

    #record1 = Record("influenza", ["cough", "fever"])
    #record2 = Record("cold", ["cough"])
    #records = [record1, record2]

    #print(build_tree(records, ["fever"]))
    #print(optimal_tree(records, ["cough", "fever"], 1))
    # print()

    # for file in os.listdir(folder):
    #    if file.endswith(".txt"):
    #        records = parse_data(os.path.join(folder, file))
    #        symptoms = {symp for record in records for symp in record.symptoms}
    #        symptoms = list(symptoms)
    #        diagnoser = optimal_tree(records, symptoms, len(symptoms) // 2)
    #        # print(diagnoser)
    #        diagnoser.minimize(True)
    #        success_rate = diagnoser.calculate_success_rate(records)
    #        print(f'Success rate of {file} is {success_rate}')
    #        print(repr(diagnoser).replace("Node(", "\nNode("),
    #              end="\n\n")
    #d = Diagnoser(Node("Cold"))
    # print(d.paths_to_illness("Cold"))
    # print(d.calculate_success_rate([]))
    #recs = [Record("1", ["2", "3"]), 2]
    # try:
    #    build_tree(recs, ["1"])
    # except TypeError:
    #    print("TypeError")
    # try:
    #    optimal_tree(recs, ["1"], 1)
    # except TypeError:
    #    print("TypeError")
    #recs = [Record("1", ["2", "3"]), Record("4", ["5"])]
    # try:
    #    build_tree(recs, ["1", 2])
    # except TypeError:
    #    print("TypeError")
    # try:
    #    optimal_tree(recs, ["1"], -1)
    # except ValueError:
    #    print("ValueError")
    # try:
    #    optimal_tree(recs, ["1"], 2)
    # except ValueError:
    #    print("ValueError")
    # try:
    #    optimal_tree(recs, ["1", "1"], 1)
    # except ValueError:
    #    print("ValueError")
    # try:
    #    optimal_tree(recs, ["1", 2], 1)
    # except TypeError:
    #    print("TypeError")


#Diagnoser(
#    Node('congestion',
#            Node('fever',
#                Node('irritability',
#                    Node('headache',
#                        Node(None),
#                        Node(None)),
#                    Node('headache',
#                        Node(None),
#                        Node(None))),
#                Node('irritability',
#                    Node('headache',
#                        Node(None),
#                        Node(None)),
#                    Node('headache',
#                        Node('cold'),
#                        Node(None)))),
#            Node('fever',
#                Node('irritability',
#                    Node('headache',
#                        Node('meningitis'),
#                        Node('meningitis')),
#                    Node('headache',
#                        Node('covid-19'),
#                        Node('strep'))),
#                Node('irritability',
#                    Node('headache',
#                        Node('meningitis'),
#                        Node(None)),
#                    Node('headache',
#                        Node('mono'),
#                        Node('healthy'))))))

#Diagnoser(
#    Node('congestion',
#         Node('fever',
#              Node(None),
#              Node('irritability',
#                   Node(None),
#                   Node('headache',
#                        Node('cold'),
#                        Node(None)))),
#         Node('fever',
#              Node('irritability',
#                   Node('meningitis'),
#                   Node('headache',
#                        Node('covid-19'),
#                        Node('strep'))),
#              Node('irritability',
#                   Node('headache',
#                        Node('meningitis'),
#                        Node(None)),
#                   Node('headache',
#                        Node('mono'),
#                        Node('healthy'))))))

#Diagnoser(
#    Node('congestion',
#         Node('cold'),
#         Node('fever',
#              Node('irritability',
#                   Node('meningitis'),
#                   Node('headache',
#                        Node('covid-19'),
#                        Node('strep'))),
#              Node('irritability',
#                   Node('meningitis'),
#                   Node('headache',
#                        Node('mono'),
#                        Node('healthy'))))))
