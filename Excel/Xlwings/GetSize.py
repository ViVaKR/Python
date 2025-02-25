import xlwings as xw
import os

def get_image_info(excel_file):

    try:
        wb = xw.Book(excel_file)
        image_sizes = {}

        for sheet in wb.sheets:
            for shape in sheet.shapes:
                # 도형 타입이 그림인 경우
                if shape.type.casefold()  == 'picture':
                    image_api = shape.api
                    print(image_api)
                    # 이미지 크기 정보 저장 (pt 단위)
                    image_sizes[shape.name] = {
                    "sheet": sheet.name,
                    "width": shape.width,
                    "height": shape.height
                }

        wb.close()  # 엑셀 파일 닫기
        return image_sizes

    except Exception as e:
        print(f"Error: {e}")
        return None

# 엑셀 파일 경로
file_path = "ImageExcel.xlsm"

# 이미지 정보 얻기
image_info = get_image_info(file_path)

# 결과 출력
if image_info:
    for name, size in image_info.items():
        print(f"\nSheet Name: {size['sheet']}")
        print(f"Image Name: {name}")
        print(f"  Width: {size['width']} pt")
        print(f"  Height: {size['height']} pt")
