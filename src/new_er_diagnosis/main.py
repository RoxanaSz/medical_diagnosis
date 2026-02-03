#!/usr/bin/env python
import sys
import warnings
import json
import re

from datetime import datetime

from new_er_diagnosis.crew import NewErDiagnosis
from new_er_diagnosis.orchestrator import RiskWeightedOrchestrator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def generate_final_response(actions):
    lines = ["Synthesized Clinical Plan:\n"]

    for a in actions:
        lines.append(f"- {a['action']}")

    lines.append(
        "\nThis plan prioritizes interventions that reduce the greatest "
        "potential harm while preserving diagnostic flexibility."
    )

    return "\n".join(lines)

def extract_json(raw: str) -> str:
    if not raw or not raw.strip():
        raise ValueError("Empty agent output")

    # Remove markdown code fences
    raw = re.sub(r"```(?:json)?", "", raw)
    raw = raw.replace("```", "").strip()

    # Extract first JSON object
    start = raw.find("{")
    end = raw.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found")

    return raw[start:end + 1]

def write_to_file(filename, outputs, actions):
    #res = generate_final_response(actions) #to remove
    #print("RES", res)  #to remove

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# ER Chest Pain – Decision Report\n\n")
        f.write("## Agent Outputs\n\n")

        for task_output in outputs:
            f.write(f"### {task_output.agent}\n\n")
            f.write("```json\n")
            f.write(task_output.raw)
            f.write("\n```\n\n")

        f.write("## Orchestrator Output\n\n")
        f.write("```json\n")
        f.write(json.dumps(actions, indent=2))
        f.write("\n```\n")

def run():
    """
    Run the crew.
    """
    try:
        crew_result = NewErDiagnosis().crew().kickoff(inputs={})
        agent_outputs = []

        for task_output in crew_result.tasks_output:
            if not task_output.raw.strip():
                print(f" Empty output from agent: {task_output.agent}")

            cleaned = extract_json(task_output.raw)
            parsed = json.loads(cleaned) #task_output.raw
            parsed["agent_role"] = task_output.agent #.role
            agent_outputs.append(parsed)

        orchestrator = RiskWeightedOrchestrator(
            agent_reliability={
                "Cardiologist": 1.0,
                "Emergency Medicine Physician": 0.9,
                "Internal Medicine Physician (Cost-Aware)": 0.7
            }
        )

        final_actions = orchestrator.synthesize(agent_outputs)   
        write_to_file("final_report.md", crew_result.tasks_output, final_actions)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=FINISH!-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "topic",
        'current_year': str(datetime.now().year)
    }
    try:
        NewErDiagnosis().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        NewErDiagnosis().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "topic",
        "current_year": str(datetime.now().year)
    }

    try:
        NewErDiagnosis().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = NewErDiagnosis().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
