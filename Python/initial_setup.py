from setup_ai import install_ai
from setup_maps_events import install_maps_events
from setup_other import install_talk
from setup_params_text import install_params_text


def setup_all():
    install_ai()
    print("AI installed.")
    install_maps_events()
    print("Maps and events installed.")
    install_params_text()
    print("Params and text installed.")
    install_talk()
    print("Talk installed.")
    print("Installation complete.")


if __name__ == '__main__':
    setup_all()
