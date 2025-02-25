import xlwings as xw

def get_image_size(excel_file):
    try:
        # 엑셀 파일 열기
        wb = xw.Book(excel_file)
        sheet = wb.sheets[1]  # 첫 번째 시트 선택

        image_sizes = {}

        # 시트 내 모든 도형 순회
        for shape in sheet.shapes:
            print(f"Shape Name: {shape.name}, Type: {shape.type}")
            # 도형 타입이 그림인 경우
            if shape.type == 'picture':
                # 이미지 크기 정보 저장 (pt 단위)
                image_sizes[shape.name] = {
                    "width": shape.width,
                    "height": shape.height,
                    "file size" : shape
                }

        wb.close()  # 엑셀 파일 닫기
        return image_sizes

    except Exception as e:
        print(f"Error: {e}")
        return None

# 엑셀 파일 경로
file_path = "ImageExcel.xlsm"

# 이미지 크기 정보 얻기
image_info = get_image_size(file_path)

# 결과 출력
if image_info:
    for name, size in image_info.items():
        print(f"Image Name: {name}")
        print(f"  Width: {size['width']} pt")
        print(f"  Height: {size['height']} pt")

# Output:
print("End of Program")
