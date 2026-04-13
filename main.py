# main.py
from clone_repo import clone_repo
from analyzer import extract_structure
from evaluator import evaluate_code

def run(repo_url, problem_statement):
    print("Cloning repo...")
    repo_path = clone_repo(repo_url)

    print("Analyzing structure...")
    structure = extract_structure(repo_path)

    print("Evaluating with LLM...")
    result = evaluate_code(problem_statement, structure)

    print("\n===== FINAL RESULT =====\n")
    print(result)


if __name__ == "__main__":
    repo_url = input("Enter GitHub repo URL: ")
    problem = input("Enter problem statement: ")

    run(repo_url, problem)