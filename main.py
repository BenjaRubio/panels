from typing import List, Tuple, Dict
import json


def fit_panel(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    count = 0

    columns = roof_width // panel_width
    rows = roof_height // panel_height

    count += columns * rows

    # rotate for remaining space
    remaining_right_width = roof_width - columns * panel_width
    remaining_right_height = roof_height
    right_count = (remaining_right_width // panel_height) * (remaining_right_height // panel_width)

    remaining_bottom_width = panel_width * columns
    remaining_bottom_height = roof_height - panel_height * rows
    bottom_count = (remaining_bottom_width // panel_height) * (remaining_bottom_height // panel_width)

    return count + right_count + bottom_count

def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    count = fit_panel(panel_width, panel_height, roof_width, roof_height)
    rotation_count = fit_panel(panel_height, panel_width, roof_width, roof_height)

    return max(count, rotation_count)

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()