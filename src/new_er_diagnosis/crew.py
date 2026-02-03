from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# ER chest-pain case

# American College of Cardiology (ACC) and
# American Heart Association (AHA) 
    
# The HEART score is a scoring system for patients presenting with chest pain at the emergency department. 
# Acute Coronary Syndrome (ACS) probability in patients with chest pain varies widely, often requiring 
# risk stratification tools.

#User input

# "45-year-old male presents to ER with acute chest pain radiating to left arm,
# diaphoresis (excessive, abnormal sweating),
# mild shortness of breath. Vitals stable. ECG pending."

# A 45-year-old male presents to the emergency department with acute chest pain
# radiating to the left arm, associated with diaphoresis and mild shortness of
# breath. Vitals are stable. ECG and labs are pending. No known prior cardiac history.

# This is intentionally ambiguous → could be:
# Acute Coronary Syndrome (ACS)
# Pulmonary Embolism
# Aortic Dissection
# GERD (Gastroesophageal reflux disease) / musculoskeletal pain

# Perfect for agent disagreement.

# output_format1t = {
#   "primary_hypothesis": "Acute Coronary Syndrome",
#   "confidence": 0.75,
#   "supporting_evidence": [...],
#   "missing_data": [...],
#   "recommended_actions": [...],
#   "risk_if_wrong": "High mortality"
# }

# output_format2t = {
#   "primary_hypothesis": "Pulmonary Embolism",
#   "confidence": 0.4,
#   "supporting_evidence": [...],
#   "counterarguments": [...],
#   "recommended_actions": [...],
#   "risk_if_wrong": "Moderate–High"
# }

# output_format3t = {
#   "primary_hypothesis": "Non-cardiac chest pain",
#   "confidence": 0.3,
#   "supporting_evidence": [...],
#   "recommended_actions": [...],
#   "risk_if_wrong": "Catastrophic but low probability"
# }

# Hypothesis = {
#   "name": str,
#   "confidence": float,
#   "risk_if_missed": float,   # orchestrator assigns
#   "actions": list,
#   "evidence_strength": float
# }


expected_output = """
JSON schema:
{
  "primary_hypothesis": string,
  "confidence": float (0–1),
  "recommended_actions": [string]
}
No extra text allowed.
"""

expected_output1 = """
A JSON object with the following structure:

{
  "primary_hypothesis": string,
  "confidence": number between 0 and 1,
  "supporting_evidence": [string],
  "recommended_actions": [string],
  "risk_if_wrong": string
}

Do not include explanations outside the JSON.
"""
# expected_output2 = """
# Return a JSON object EXACTLY matching this schema:

# {
#   "primary_hypothesis": "Acute Coronary Syndrome",
#   "confidence": 0.75,
#   "supporting_evidence": ["Chest pain radiating to left arm", "Diaphoresis" ],
#   "missing_data": ["ECG results", "Troponin levels"],
#   "recommended_actions": ["Obtain ECG", "Measure serial troponins"],
#   "risk_if_wrong": "High mortality"
# }

# Rules:
# - Keys must match exactly
# - confidence must be a float between 0 and 1
# - Values must be medically grounded
# """


output_format1="""
{
  "hypothesis": string,
  "confidence": float (0-1),
  "supporting_findings": [string],
  "actions_recommended": [string],
  "risk_if_missed": "Low" | "Moderate" | "High"
}
"""

output_format2="""
{
  "hypothesis": string,
  "confidence": float (0-1),
  "alternative_diagnoses": [string],
  "actions_recommended": [string],
  "risk_if_missed": "Low" | "Moderate" | "High"
}
"""
output_format3="""
{
  "hypothesis": string,
  "confidence": float (0-1),
  "conditions_not_ruled_out": [string],
  "actions_recommended": [string],
  "risk_if_missed": "Low" | "Moderate" | "High"
}
"""

@CrewBase
class NewErDiagnosis():
    """NewErDiagnosis crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def cardiology_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['cardiology_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def pulmonology_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pulmonology_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def internal_medicine_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['internal_medicine_agent'], # type: ignore[index]
            allow_delegation=False,
            verbose=True
        )
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def cardio_task(self) -> Task:
        return Task(
            config=self.tasks_config['cardio_task'], # type: ignore[index]
            expected_output = output_format1 #expected_output2
        )

    @task
    def pulm_task(self) -> Task:
        return Task(
            config=self.tasks_config['pulm_task'], # type: ignore[index]
            expected_output = output_format2
        )
    
    @task
    def internal_task(self) -> Task:
        return Task(
            config=self.tasks_config['internal_task'], # type: ignore[index]
            expected_output = output_format3,
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the NewErDiagnosis crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
