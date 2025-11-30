from get_influencer_score import *

run_cases = [(40000, 0.3, 5), (43000, 0.1, 2), (100000, 0.6, 10)]

submit_cases = run_cases + [
    (1, 1, 0),
    (200, 0.8, 6),
    (300000, 0.5, 9),
    (500000, 0.2, 4),
    (750000, 0.7, 14),
]


def test(input1, input2, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(f" * num_followers: {input1}")
        print(f" * average_engagement_percentage: {input2}")
        result = round(get_influencer_score(input1, input2))
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result == expected_output:
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
