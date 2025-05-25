from data import (
    mbti_summary, zodiac_summary, animal_summary
)

def analyze_personality(mbti, zodiac, animal):
    summary_mbti = mbti_summary.get(mbti, "")
    summary_zodiac = zodiac_summary.get(zodiac, "")
    summary_animal = animal_summary.get(animal, "")

    combined = (
        f"{mbti}의 특성과 {zodiac}의 감성, {animal}의 기질이 조화를 이루어, "
        f"당신은 {summary_mbti} {summary_zodiac} {summary_animal} "
        f"이러한 성향 덕분에 다양한 상황에 유연하게 대응하며 매력적인 인상을 남깁니다."
    )

    return combined
