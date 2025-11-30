from log_scale import *

run_cases = [
    ([1, 10, 100, 1000], 10, [0.0, 1.0, 2.0, 3.0]),
    ([1, 2, 4, 8], 2, [0.0, 1.0, 2.0, 3.0]),
]

submit_cases = run_cases + [
    ([2, 4, 8, 16], 2, [1.0, 2.0, 3.0, 4.0]),
    ([3, 9, 27, 81], 3, [1.0, 2.0, 3.0, 4.0]),
    ([5, 25, 125, 625], 5, [1.0, 2.0, 3.0, 4.0]),
    ([10, 100, 1000, 10000], 10, [1.0, 2.0, 3.0, 4.0]),
    ([20, 400, 8000, 160000], 20, [1.0, 2.0, 3.0, 4.0]),
]


def test(data, base, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(f" * data: {data}")
        print(f" * base: {base}")
        print(f"Expected: {expected_output}")
        scaled_data = log_scale(data, base)
        for i in range(0, len(scaled_data)):
            scaled_data[i] = round(scaled_data[i], 2)
        print(f"Actual:   {scaled_data}")
        if scaled_data == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
