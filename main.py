from os import system
import eel
import exportFunctions






def start_eel():
    app = "chrome"
    
    eel.init("web/build", [".tsx", ".ts", ".jsx", ".js", ".html"])

    eel_kwargs = dict(
        host="localhost",
        port=8080,
        # size=(1280, 800),
    )
    page_name = "index.html"

    eel_cmdline_args = "--kiosk"

    try:
        eel.start(page_name, mode=app, **eel_kwargs, cmdline_args=[eel_cmdline_args])
    except:
        raise


if __name__ == "__main__":
    # system("taskkill /im chrome.exe /f") # Podemos colocar isso para fechar o chrome antes de rodar o eel
    eel.spawn(start_eel)  # Inicializando eel em outro thread
    data_points_normal = exportFunctions.get_random_data_points(2)
    data_points_JSON = exportFunctions.get_random_data_points_JSON(5)

    print(data_points_normal)
    print(data_points_JSON)

    while True:
        eel.sleep(1)
