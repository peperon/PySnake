import configparser


class LoadGame:

    @staticmethod
    def load():
        snake = []
        parser = configparser.ConfigParser()
        parser.read("./data/saved.sv")
        if len(parser.sections()) == 0:
                raise IOError
        result = {}
        result["level"] = int(parser.get("DEFAULT", "level"))
        result["snake"] = eval(parser.get("DEFAULT", "snake"))
        result["food"] = eval(parser.get("DEFAULT", "food"))
        result["direction"] = int(parser.get("DEFAULT", "direction"))

        return result
