import json
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, asdict

BASE_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = BASE_DIR / "graph"

# ============================================================================
# SCORING ENGINE: Phase 3-B Path Scoring & Ranking
# ============================================================================

@dataclass
class PathScore:
    """Represents a scored and ranked path"""
    rank: int
    path_sequence: List[str]
    path_label: str
    final_score: float
    components: Dict[str, float]
    explanation: Dict[str, str]

def normalize(value: float, max_value: float) -> float:
    """Normalize value to [0, 1] range"""
    if max_value == 0:
        return 0.0
    return min(value / max_value, 1.0)

def compute_s1_eligibility(
    current_stage: str,
    stream: str,
    required_exams: List[str],
    prerequisites_met: bool
) -> float:
    """
    S1: Eligibility Score
    Can student realistically enter this path?
    
    Eligible → 1.0
    Partially eligible → 0.6
    Not eligible → 0.0
    """
    stage_map = {"10th": 0.0, "12th": 0.5, "UG": 0.8, "PG": 1.0}
    stage_score = stage_map.get(current_stage, 0.0)
    
    # If prerequisites met and in same/related stream
    if prerequisites_met and stage_score >= 0.5:
        return min(stage_score + 0.2, 1.0)
    elif prerequisites_met:
        return 0.6
    else:
        return 0.0

def compute_s2_alignment(graph_distance: int, edge_type_strength: float) -> float:
    """
    S2: Program–Job Alignment
    How directly does program lead to job?
    
    Direct (1 edge) → 1.0
    Indirect (2-3 edges) → 0.7
    Weak (4+ edges) → 0.3
    """
    if graph_distance == 1:
        return 1.0
    elif graph_distance <= 3:
        return 0.7
    else:
        return 0.3
    
    # Could also factor in edge_type_strength
    # return alignment * edge_type_strength

def compute_s3_salary(salary_p75: float, max_salary: float = 50.0) -> float:
    """
    S3: Salary Score
    Uses p75 percentile (aspirational but realistic)
    
    Normalized to [0, 1] capped at 1.0
    """
    return normalize(salary_p75, max_salary)

def compute_s4_demand(forecast_2026: float, max_forecast: float = 100.0) -> float:
    """
    S4: Demand Score
    Uses future demand index (2026 forecast)
    
    Future-proofs recommendations
    """
    return normalize(forecast_2026, max_forecast)

def compute_s5_region_compatibility(
    student_region: str,
    path_region: str,
    student_state: str = None,
    path_state: str = None
) -> float:
    """
    S5: Region Compatibility
    How well does path fit student's region preference?
    
    Same city → 1.0
    Same state → 0.8
    Same country → 0.6
    Relocation needed → 0.4
    """
    if student_region == path_region:
        return 1.0
    elif student_state and student_state == path_state:
        return 0.8
    else:
        # Same country (India)
        return 0.6

def compute_s6_skill_gap(required_skills: int, missing_skills: int) -> float:
    """
    S6: Skill Gap Penalty
    How many skills missing between student and job?
    
    skill_gap_ratio = missing_skills / required_skills
    skill_score = 1 - skill_gap_ratio
    """
    if required_skills == 0:
        return 1.0
    
    skill_gap_ratio = missing_skills / required_skills
    return max(1 - skill_gap_ratio, 0.0)

def compute_s7_robustness(
    num_employers: int,
    num_industries: int,
    num_alternative_programs: int
) -> float:
    """
    S7: Risk / Robustness Score
    How resilient is this path?
    
    Highly robust (multiple options) → 1.0
    Moderate → 0.7
    Fragile (single option) → 0.4
    """
    diversity_score = (num_employers + num_industries + num_alternative_programs) / 9.0
    
    if diversity_score >= 0.67:
        return 1.0
    elif diversity_score >= 0.33:
        return 0.7
    else:
        return 0.4

def score_path(path_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compute final path score using 7 components with fixed weights
    
    FINAL_SCORE = 
        0.20 * S1 (Eligibility)
      + 0.15 * S2 (Alignment)
      + 0.20 * S3 (Salary)
      + 0.20 * S4 (Demand)
      + 0.10 * S5 (Region)
      + 0.10 * S6 (Skill Gap)
      + 0.05 * S7 (Robustness)
    """
    
    # Compute individual scores
    S1 = compute_s1_eligibility(
        context.get("current_stage", "12th"),
        context.get("stream", "Science"),
        path_data.get("required_exams", []),
        path_data.get("prerequisites_met", True)
    )
    
    S2 = compute_s2_alignment(
        path_data.get("graph_distance", 3),
        path_data.get("edge_strength", 1.0)
    )
    
    S3 = compute_s3_salary(
        path_data.get("salary_p75", 15.0),
        context.get("max_salary", 50.0)
    )
    
    S4 = compute_s4_demand(
        path_data.get("demand_2026", 50.0),
        context.get("max_demand", 100.0)
    )
    
    S5 = compute_s5_region_compatibility(
        context.get("region", "Bangalore"),
        path_data.get("region", "Bangalore"),
        context.get("state"),
        path_data.get("state")
    )
    
    S6 = compute_s6_skill_gap(
        path_data.get("required_skills", 5),
        path_data.get("missing_skills", 1)
    )
    
    S7 = compute_s7_robustness(
        path_data.get("num_employers", 3),
        path_data.get("num_industries", 2),
        path_data.get("num_alt_programs", 1)
    )
    
    # Apply fixed weights
    weights = {
        "S1": 0.20,
        "S2": 0.15,
        "S3": 0.20,
        "S4": 0.20,
        "S5": 0.10,
        "S6": 0.10,
        "S7": 0.05
    }
    
    final_score = (
        weights["S1"] * S1 +
        weights["S2"] * S2 +
        weights["S3"] * S3 +
        weights["S4"] * S4 +
        weights["S5"] * S5 +
        weights["S6"] * S6 +
        weights["S7"] * S7
    )
    
    return {
        "final_score": round(final_score, 4),
        "components": {
            "S1_eligibility": round(S1, 4),
            "S2_alignment": round(S2, 4),
            "S3_salary": round(S3, 4),
            "S4_demand": round(S4, 4),
            "S5_region": round(S5, 4),
            "S6_skill_gap": round(S6, 4),
            "S7_robustness": round(S7, 4)
        },
        "weights": weights
    }

def generate_explanation(score_data: Dict[str, Any], path_data: Dict[str, Any]) -> Dict[str, str]:
    """
    Generate human-readable explanation for each component
    """
    S1 = score_data["components"]["S1_eligibility"]
    S2 = score_data["components"]["S2_alignment"]
    S3 = score_data["components"]["S3_salary"]
    S4 = score_data["components"]["S4_demand"]
    S5 = score_data["components"]["S5_region"]
    S6 = score_data["components"]["S6_skill_gap"]
    S7 = score_data["components"]["S7_robustness"]
    
    def interpret_score(score: float, dimension: str) -> str:
        if dimension == "eligibility":
            if score == 1.0:
                return "Excellent - Strong prerequisites met"
            elif score >= 0.6:
                return "Good - Partially eligible, may need prep"
            else:
                return "Poor - Significant prerequisites missing"
        
        elif dimension == "alignment":
            if score == 1.0:
                return "Excellent - Direct program-to-job path"
            elif score >= 0.7:
                return "Good - Common but not direct path"
            else:
                return "Weak - Rare or indirect mapping"
        
        elif dimension == "salary":
            salary_val = path_data.get("salary_p75", 0)
            if score >= 0.8:
                return f"Excellent - High salary (p75 ≈ {salary_val:.1f} LPA)"
            elif score >= 0.5:
                return f"Good - Moderate salary (p75 ≈ {salary_val:.1f} LPA)"
            else:
                return f"Low - Entry-level salary (p75 ≈ {salary_val:.1f} LPA)"
        
        elif dimension == "demand":
            demand_val = path_data.get("demand_2026", 0)
            if score >= 0.8:
                return f"Very high - Strong growth forecast ({demand_val:.0f}%)"
            elif score >= 0.5:
                return f"Moderate - Stable demand ({demand_val:.0f}%)"
            else:
                return f"Low - Slower growth ({demand_val:.0f}%)"
        
        elif dimension == "region":
            if score >= 1.0:
                return f"Perfect - Same city ({path_data.get('region', 'N/A')})"
            elif score >= 0.8:
                return f"Good - Same state"
            elif score >= 0.6:
                return "Acceptable - Within India"
            else:
                return "Fair - Relocation required"
        
        elif dimension == "skill_gap":
            missing = path_data.get("missing_skills", 0)
            required = path_data.get("required_skills", 5)
            if score >= 0.8:
                return f"Low gap - {missing}/{required} skills to acquire"
            elif score >= 0.5:
                return f"Moderate gap - {missing}/{required} skills needed"
            else:
                return f"High gap - {missing}/{required} skills to learn"
        
        elif dimension == "robustness":
            if score >= 1.0:
                return "Highly robust - Multiple employers & industries"
            elif score >= 0.7:
                return "Moderate - Some alternatives available"
            else:
                return "Fragile - Limited alternatives"
    
    return {
        "eligibility": interpret_score(S1, "eligibility"),
        "alignment": interpret_score(S2, "alignment"),
        "salary": interpret_score(S3, "salary"),
        "demand": interpret_score(S4, "demand"),
        "region": interpret_score(S5, "region"),
        "skill_gap": interpret_score(S6, "skill_gap"),
        "robustness": interpret_score(S7, "robustness")
    }

def rank_paths(
    paths: List[Dict[str, Any]],
    context: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Score and rank multiple paths
    
    Returns ranked list with scores, components, and explanations
    """
    scored_paths = []
    
    for i, path in enumerate(paths):
        score_data = score_path(path, context)
        explanation = generate_explanation(score_data, path)
        
        scored_paths.append({
            "path_index": i,
            "path": path.get("path_sequence", []),
            "path_label": path.get("label", "Unknown Path"),
            "final_score": score_data["final_score"],
            "components": score_data["components"],
            "weights": score_data["weights"],
            "explanation": explanation
        })
    
    # Sort by score descending
    scored_paths.sort(key=lambda x: x["final_score"], reverse=True)
    
    # Add rank
    for rank, path in enumerate(scored_paths, 1):
        path["rank"] = rank
    
    return scored_paths

# ============================================================================
# MAIN: Demo with sample paths
# ============================================================================

if __name__ == "__main__":
    # Sample paths to score
    sample_paths = [
        {
            "label": "B.Tech AI & ML → ML Engineer → TCS → Bangalore",
            "path_sequence": ["PROGRAM_BTECH_AI_ML", "JOB_ML_ENGINEER", "EMP_TCS", "REG_BANGALORE"],
            "required_exams": ["EXAM_JEE_MAIN"],
            "prerequisites_met": True,
            "graph_distance": 2,
            "edge_strength": 1.0,
            "salary_p75": 22.0,
            "demand_2026": 85.0,
            "region": "Bangalore",
            "state": "Karnataka",
            "required_skills": 5,
            "missing_skills": 1,
            "num_employers": 5,
            "num_industries": 3,
            "num_alt_programs": 2
        },
        {
            "label": "B.Tech CSE → Data Scientist → Infosys → Delhi",
            "path_sequence": ["PROGRAM_BE", "JOB_DATA_SCIENTIST", "EMP_INFOSYS", "REG_DELHI"],
            "required_exams": ["EXAM_JEE_MAIN"],
            "prerequisites_met": True,
            "graph_distance": 2,
            "edge_strength": 0.85,
            "salary_p75": 25.0,
            "demand_2026": 92.0,
            "region": "Delhi",
            "state": "Delhi",
            "required_skills": 6,
            "missing_skills": 2,
            "num_employers": 4,
            "num_industries": 2,
            "num_alt_programs": 1
        },
        {
            "label": "BBA → Business Analyst → TCS → Bangalore",
            "path_sequence": ["PROGRAM_BBA", "JOB_BUSINESS_ANALYST", "EMP_TCS", "REG_BANGALORE"],
            "required_exams": ["EXAM_12TH_BOARD"],
            "prerequisites_met": True,
            "graph_distance": 2,
            "edge_strength": 0.8,
            "salary_p75": 12.0,
            "demand_2026": 75.0,
            "region": "Bangalore",
            "state": "Karnataka",
            "required_skills": 4,
            "missing_skills": 1,
            "num_employers": 6,
            "num_industries": 4,
            "num_alt_programs": 3
        },
        {
            "label": "MBBS → Medical Doctor → Apollo → Bangalore",
            "path_sequence": ["PROGRAM_MBBS", "JOB_MEDICAL_DOCTOR", "EMP_APOLLO", "REG_BANGALORE"],
            "required_exams": ["EXAM_NEET"],
            "prerequisites_met": True,
            "graph_distance": 2,
            "edge_strength": 1.0,
            "salary_p75": 10.0,
            "demand_2026": 65.0,
            "region": "Bangalore",
            "state": "Karnataka",
            "required_skills": 3,
            "missing_skills": 0,
            "num_employers": 8,
            "num_industries": 2,
            "num_alt_programs": 2
        },
        {
            "label": "LLB → Lawyer → Solo Practice → Delhi",
            "path_sequence": ["PROGRAM_LLB", "JOB_LAWYER"],
            "required_exams": ["EXAM_CLAT"],
            "prerequisites_met": False,
            "graph_distance": 1,
            "edge_strength": 0.7,
            "salary_p75": 15.0,
            "demand_2026": 50.0,
            "region": "Delhi",
            "state": "Delhi",
            "required_skills": 4,
            "missing_skills": 3,
            "num_employers": 1,
            "num_industries": 1,
            "num_alt_programs": 1
        }
    ]
    
    # Student context
    student_context = {
        "current_stage": "12th",
        "stream": "Science",
        "region": "Bangalore",
        "state": "Karnataka",
        "max_salary": 50.0,
        "max_demand": 100.0
    }
    
    # Score and rank
    ranked_paths = rank_paths(sample_paths, student_context)
    
    # Output
    output_file = BASE_DIR / "outputs" / "ranked_paths.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    output_file.write_text(
        json.dumps(ranked_paths, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    print(f"✅ Path Scoring Complete\n")
    print(f"📊 Ranked {len(ranked_paths)} paths\n")
    
    # Print summary
    for path in ranked_paths:
        print(f"#{path['rank']} | {path['path_label']}")
        print(f"    Score: {path['final_score']} | Eligibility: {path['components']['S1_eligibility']}")
        print(f"    Salary: {path['components']['S3_salary']} | Demand: {path['components']['S4_demand']}")
        print()
    
    print(f"💾 Full output saved to: {output_file}")
