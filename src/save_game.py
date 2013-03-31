import configparser


class SaveGame:

    @staticmethod
    def save(level, snake, food, direction):
        with open("./data/saved.sv", "w") as save_file:
            parser = configparser.ConfigParser()
            parser.set("DEFAULT", "level", str(level))
            parser.set("DEFAULT", "snake", str(snake))
            parser.set("DEFAULT", "food", str(food))
            parser.set("DEFAULT", "direction", str(direction))
            parser.write(save_file)
