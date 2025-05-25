from data import mbti_data, zodiac_data, animal_data

def analyze_personality(mbti, zodiac, animal):
    mbti_desc = mbti_data.get(mbti, "")
    zodiac_desc = zodiac_data.get(zodiac, "")
    animal_desc = animal_data.get(animal, "")

    result = (
        f"{mbti}의 창의성과 {zodiac}의 감성, {animal}의 에너지가 어우러져,\n"
        f"당신은 {mbti_desc} {zodiac_desc} {animal_desc}\n"
        f"항상 새로운 아이디어를 시도하며, 상황에 따라 융통성 있게 대처하는 능력이 뛰어납니다.\n"
        f"이러한 성향 덕분에 다채로운 인간관계를 형성하며, 매 순간을 의미 있게 만들어 갑니다."
    )

    return result
