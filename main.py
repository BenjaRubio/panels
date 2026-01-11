from typing import List, Tuple, Dict
import json


def rotate_panel(panel_width: int, panel_height: int) -> Tuple[int, int]:
    return panel_height, panel_width

def fit_panel(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    count = 0
    remaining_width = roof_width
    remaining_height = roof_height
    rotated = False

    while True:
      if remaining_height < panel_height:
        if not rotated:
          panel_width, panel_height = rotate_panel(panel_width, panel_height)
          rotated = True
          continue
        else:
          break
      
      remaining_height -= panel_height
      remaining_width = roof_width
      while remaining_width >= panel_width:
        remaining_width -= panel_width
        count += 1

    return count

def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    count = fit_panel(panel_width, panel_height, roof_width, roof_height)
    rotation_count = fit_panel(*rotate_panel(panel_width, panel_height), roof_width, roof_height)

    print(f"Count: {count}, Rotation count: {rotation_count}")

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