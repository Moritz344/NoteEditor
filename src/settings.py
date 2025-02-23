import json

def get_data_from_json() -> str:
    with open("data.json","r") as file:
            data = json.load(file)
            font = data["preferences"]["font"]
            colorscheme = data["preferences"]["colorscheme"]
            standard_font_size = data["other"]["standard_font_size"]
            min_font_size = data["other"]["min_font_size"]
            max_font_size = data["other"]["max_font_size"]
            background_color = data["other"]["background_color"]
            path = data["other"]["path"]
            files = data["other"]["files"]
            project_name=data["other"]["project_name"]


            return font,colorscheme,standard_font_size,max_font_size,min_font_size,path,background_color,files,project_name
            
font,colorscheme,standard_font_size,max_font_size,min_font_size,path,background_color,files,project_name = get_data_from_json()

