import random
from data import mbti_data, zodiac_data, animal_data

def analyze_personality(mbti, zodiac, animal):
    mbti_desc = mbti_data.get(mbti, "")
    zodiac_desc = zodiac_data.get(zodiac, "")
    animal_desc = animal_data.get(animal, "")

    templates = [
        f"{mbti}의 창의성과 {zodiac}의 감성, {animal}의 에너지가 어우러져,\n"
        f"당신은 {mbti_desc} {zodiac_desc} {animal_desc}\n"
        f"항상 새로운 아이디어를 시도하며, 상황에 따라 융통성 있게 대처하는 능력이 뛰어납니다.\n"
        f"이러한 성향 덕분에 다채로운 인간관계를 형성하며, 매 순간을 의미 있게 만들어 갑니다.",

        f"{mbti}의 독특한 특성과 {zodiac}의 섬세한 감성, 그리고 {animal}의 활발한 기운이 만나,\n"
        f"당신은 {mbti_desc} {zodiac_desc} {animal_desc}\n"
        f"새로운 도전에 두려움 없이 맞서며, 주변 사람들에게 긍정적인 영향을 끼칩니다.\n"
        f"이런 면모로 인해 다양한 상황 속에서 뛰어난 적응력을 보입니다.",

        f"{mbti} 특유의 창의력과 {zodiac}의 균형 잡힌 감성, {animal}의 강한 에너지가 조화를 이루어,\n"
        f"당신은 {mbti_desc} {zodiac_desc} {animal_desc}\n"
        f"항상 새로운 기회를 찾아 도전하며, 유연한 사고로 문제를 해결합니다.\n"
        f"이러한 특징 덕분에 많은 사람들과 깊은 유대감을 형성합니다."
    ]

    return random.choice(templates)
