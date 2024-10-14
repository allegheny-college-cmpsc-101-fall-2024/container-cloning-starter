"""Remove the duplicate values that are inside of two lists."""

from typing import Any
from typing import List
from typing import Tuple


def remove_duplicates(list_one: List[Any], list_two: List[Any]) -> Tuple[List[Any], List[Any]]:
    """Remove from both lists the duplicate elements that are found in both of the lists."""
    # TODO: There is at least one defect in this function requiring fixing.
    # TODO: Refer to pages 100 and 101 in your text book for more details.
    # iterate through the first list
    for element in list_one:
        # determine if the current item is in the second list
        if element in list_two:
            # remove the element in common from both of the lists
            list_one.remove(element)
            list_two.remove(element)
    # return both of the modified lists that no longer contain
    # the elements that they have in common
    return (list_one, list_two)


def test_remove_duplicates() -> bool:
    """Implement test cases for the remove_duplicates function."""
    # define two lists with some duplicate items to be tested
    list_one = [1, 2, 3, 4]
    list_two = [1, 2, 5, 6]
    # TODO: add comment to describe the purpose of these lines of code
    expected_list_one = [3, 4]
    expected_list_two = [5, 6]
    # TODO: add comment to describe the purpose of these lines of code
    test_case_passed = True
    # TODO: add comment to describe the purpose of these lines of code
    (actual_list_one, actual_list_two) = remove_duplicates(list_one, list_two)
    # TODO: add comment to describe the purpose of these lines of code
    if expected_list_one == actual_list_one and expected_list_two == actual_list_two:
        print("Expected output correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]")
    # TODO: add comment to describe the purpose of these lines of code
    else:
        print("Expected output not correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]")
        print(f"   actual_list_one: {actual_list_one}")
        print(f"   actual_list_two: {actual_list_two}")
        test_case_passed = False
    # TODO: add comment to describe the purpose of these lines of code
    return test_case_passed


if __name__ == "__main__":
    # call the test case for the function under test
    test_case_status = test_remove_duplicates()
    # print the status of the test case
    if not test_case_status:
        print("The test case did not pass!")
    else:
        print("The test case passed!")
