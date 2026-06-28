def calculate_ats_score(resume_skills, jd_skills):

    matched = []
    missing = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_skills)) * 100)

    return score, matched, missing