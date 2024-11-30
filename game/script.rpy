init python:
    import sys
    import os

    # Add the scripts folder to Python path
    sys.path.append(os.path.join(renpy.config.gamedir, "scripts"))

    # Import the DataHandler class
    from data_handler import DataHandler

    # Initialize the data handler
    base_path = renpy.config.gamedir
    data_handler = DataHandler(base_path)

    # Load JSON data
    characters_data = data_handler.load_json("characters.json")
    dialogues_data = data_handler.load_json("dialogues.json")
    reservations_data = data_handler.load_json("reservations.json")
    rooms_data = data_handler.load_json("rooms.json")

label start:
    "Welcome to the Ren'Py JSON Demo!"

    python:
        # Character introduction
        for character in characters_data["characters"]:
            name = character["name"]
            age = character["age"]
            height = character["height"]
            weight = character["weight"]
            measurements = character["measurements"]  # Bust, Waist, Hip
            cup_size = character["cup_size"]
            smoking = "흡연자" if character["smoking"] else "비흡연자"
            skills = character["skills"]
            performance = character["performance"]
            location = character["current_location"]

            # Display character details using Ren'Py text
            renpy.say(None, f"이름: {name}")
            renpy.say(None, f"나이: {age}세")
            renpy.say(None, f"키: {height}cm, 몸무게: {weight}kg")
            renpy.say(None, f"쓰리사이즈: {measurements[0]}-{measurements[1]}-{measurements[2]} (컵: {cup_size})")
            renpy.say(None, f"흡연 여부: {smoking}")
            renpy.say(None, f"현재 위치: {location}")
            renpy.say(None, "능력치:")
            renpy.say(None, f"- 대화: {skills['conversation']}")
            renpy.say(None, f"- 서비스: {skills['service']}")
            renpy.say(None, "퍼포먼스:")
            renpy.say(None, f"- 종합 점수: {performance['overall']}")
            renpy.say(None, f"- 인기도: {performance['popularity']}")

    return
