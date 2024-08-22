"dinner": content.Schema(
            type = content.Type.OBJECT,
            properties = {
              "main_dish": content.Schema(
                type = content.Type.OBJECT,
                enum = "[]",
                required = """["name", "calories", "category", "ingredients"]""",
                properties = {
                  "name": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "calories": content.Schema(
                    type = content.Type.NUMBER,
                  ),
                  "category": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "how_to_cook": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "meal_time": content.Schema(
                    type = content.Type.STRING,
                  ),
                },
              ),
            },
          ),