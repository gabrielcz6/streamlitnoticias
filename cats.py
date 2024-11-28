import logging
import torch

logging.basicConfig(level=logging.DEBUG)

try:
    logging.debug("Instanciando el modelo o clase de PyTorch...")
    # Aquí va la instanciación de tu clase de PyTorch, por ejemplo:
    model_path = r"C:\Users\Gabriel\Desktop\PROYECTOS 2024 PROGRAMACION\LANGCHAIN\Streamlit-Demo-Apps\streamlitTalkToCSV_Excel\mi_modelo.pth"
    modelo = torch.load(model_path)
except Exception as e:
    logging.error("Error al instanciar la clase de PyTorch:", exc_info=True)