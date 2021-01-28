def print_models(unprinted_designs, completed_models):
    """
    남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트합니다.
    출력한 각 디자인을 completed models로 옮깁니다.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """출력이 끝난 모델 모두 표시"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




