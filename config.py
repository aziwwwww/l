import platform

is_half = True
exp_root = "logs"
python_exec = "runtime\python" if platform.system() == "Windows" else "python"
infer_device = "cuda"

webui_port_main = 9874
webui_port_uvr5 = 9873
webui_port_infer_tts = 9872
webui_port_subfix = 9871
