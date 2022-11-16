class DialogWindow():
    def __init__(self):
        pass

    # select model version and path directory with images
    def select_settings(self):
        # select model version
        model_v = input('select model version "s" - small or "m" - medium: ')
        # path directory with images
        directory = input("directory name with images in img: ")
        path = f'img/{directory}'

        return model_v, directory, path

    # last info about output
    def ready(self, directory):
        print(f'Ready in output/{directory}')