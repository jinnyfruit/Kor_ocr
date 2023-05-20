import pytesseract
from PIL import Image

# Tesseract 실행 파일 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def ocr_image(image_path):
    image = Image.open(image_path)
    languages = pytesseract.image_to_string(image, config='--psm 0 --oem 1 -l osd')
    detected_languages = []
    for line in languages.splitlines():
        if line.strip():
            line_parts = line.split(':')
            if len(line_parts) == 2:
                key, value = line_parts
                if key.strip() == 'Script':
                    detected_languages.append(value.strip())

    print("Detected Languages:", detected_languages)

    if 'Hangul' in detected_languages or 'Korean' in detected_languages:
        print("Korean")
        text = pytesseract.image_to_string(image, config='--psm 6 -l kor', temp_dir='/tmp')
        return text

    if 'Latin' in detected_languages or 'English' in detected_languages:
        print("English")
        text = pytesseract.image_to_string(image, lang='eng', temp_dir='/tmp')
        return text

    print("No language detected")
    text = pytesseract.image_to_string(image, temp_dir='/tmp')
    return text


# 이미지 파일 경로
image_path = "/Users/jinnyfruit/PycharmProjects/Openeyes/Backend/static/downloads/test2.png"

# 이미지에서 텍스트 추출
result = ocr_image(image_path)

# 추출된 텍스트 출력
print(result)
