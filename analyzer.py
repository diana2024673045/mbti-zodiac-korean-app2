from data import mbti_analysis, zodiac_analysis, animal_analysis

def analyze_personality(mbti, zodiac, animal):
    mbti_text = mbti_analysis.get(mbti, "해당 MBTI에 대한 정보가 없습니다.")
    zodiac_text = zodiac_analysis.get(zodiac, "해당 별자리에 대한 정보가 없습니다.")
    animal_text = animal_analysis.get(animal, "해당 띠에 대한 정보가 없습니다.")

    analysis_result = f"""분석 결과:
- MBTI: {mbti_text}
- 별자리: {zodiac_text}
- 띠: {animal_text}
"""

    combined_interpretation = (
        f"{mbti}의 특징과 {zodiac}의 감성, {animal}의 기질이 어우러져, "
        f"당신은 매우 독특하고 다채로운 성격의 소유자입니다. "
        f"내면의 힘과 외향적인 매력을 함께 지닌 당신은 사람들에게 깊은 인상을 남기며, "
        f"상황에 따라 유연하게 대처할 수 있는 능력이 있습니다."
    )

    return f"{analysis_result}\n\n종합 해석:\n{combined_interpretation}"
