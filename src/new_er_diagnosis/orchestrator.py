from collections import defaultdict

class RiskWeightedOrchestrator:
    
    RISK_WEIGHT = {
    "High": 1.0,
    "Moderate": 0.5,
    "Low": 0.1
    }

    def __init__(self, agent_reliability=None):
        # Optional: down-weight known biased agents
        self.agent_reliability = agent_reliability or {}

    def synthesize(self, agent_outputs):
        action_scores = defaultdict(float)
        action_metadata = defaultdict(list)

        for output in agent_outputs:
            risk_weight = self.RISK_WEIGHT[output["risk_if_missed"]]
            confidence = output["confidence"]
            reliability = self.agent_reliability.get(
                output.get("agent_role"), 1.0
            )

            contribution = confidence * risk_weight * reliability

            for action in output["actions_recommended"]:
                action_scores[action] += contribution
                action_metadata[action].append(output["hypothesis"])

        return self._select_actions(action_scores, action_metadata)

    def _select_actions(self, scores, metadata, threshold=0.4):
        selected = []

        for action, score in scores.items():
            if score >= threshold:
                selected.append({
                    "action": action,
                    "score": round(score, 3),
                    "risk_coverage": metadata[action]
                })

        # sort by descending expected harm reduction
        return sorted(selected, key=lambda x: x["score"], reverse=True)


    # def synthesize2(self, agent_outputs):
    #     hypotheses = normalize(agent_outputs)
    #     ranked = compute_expected_risk(hypotheses)
    #     actions = select_dominant_actions(ranked)
    #     return generate_final_response(actions)

    #     Action_ex = {
    #     "name": str,
    #     "supported_by": ['agent_role'],
    #     "covered_risks": ["High", "Moderate", "Low"]
    #    }
    
    # agent_outputs_ex = [    {
    #     "agent_role": "Cardiologist",
    #     "hypothesis": "...",
    #     "confidence": 0.8,
    #     "actions_recommended": [...],
    #     "risk_if_missed": "High"
    # }    ] 