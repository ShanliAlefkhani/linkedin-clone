from rest_framework import filters
from jobs.models import Job


class Node:
    def __init__(self, value, pk):
        self.left = None
        self.right = None
        self.value = value
        self.pk = pk


def make_bst(array):
    if not array:
        return None

    mid = int((len(array)) / 2)
    root = array[mid]
    root.left = make_bst(array[:mid])
    root.right = make_bst(array[mid + 1:])
    return root


def array_filter(minimum, maximum, root):
    if root is None:
        return
    ans = []
    if minimum <= root.value <= maximum:
        ans.append(array_filter(minimum, maximum, root.left))
        ans.append(root.pk)
        ans.append(array_filter(minimum, maximum, root.right))
    elif root.value < minimum:
        ans.append(array_filter(minimum, maximum, root.right))
    else:
        ans.append(array_filter(minimum, maximum, root.left))
    return ans


class SalaryFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        minimum = request.query_params.get("minimum salary", 0)
        maximum = request.query_params.get("maximum salary", 1000)
        jobs = Job.objects.all()
        array = []
        for job in jobs:
            node = Node(job.salary, job.pk)
            array.append(node)
        array = sorted(array, key=lambda n: n.value)
        root = make_bst(array)
        filtered_array = array_filter(int(minimum), int(maximum), root)
        queryset = Job.objects.filter(pk__in=filtered_array)
        return queryset
