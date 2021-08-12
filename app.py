import time
import torch
import tempfile
import soundfile as sf
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.tts_inference import Text2Speech
from parallel_wavegan.utils import download_pretrained_model
from parallel_wavegan.utils import load_model
from flask import Flask, send_file, request

SAMPLE_RATE = 24000
MODEL_TAG = 'kan-bayashi/jsut_conformer_fastspeech2_accent_with_pause' 
VOCODER_TAG = "jsut_parallel_wavegan.v1" 

downloader = ModelDownloader()

text2speech = Text2Speech(
    **downloader.download_and_unpack(MODEL_TAG),
    device = "cuda",
    speed_control_alpha = 1.0,
)
text2speech.spc2wav = None
vocoder = load_model(download_pretrained_model(VOCODER_TAG)).to("cuda").eval()
vocoder.remove_weight_norm()


app = Flask(__name__)

@app.route('/audio', methods=['POST'])
def get_audio():
    start_time = time.time()
    json_data = request.get_json()
    text = json_data['text']

    print(text)
    try:
        with torch.no_grad():
            wav, c, *_ = text2speech(text)
            wav = vocoder.inference(c)
    except:
        torch.cuda.empty_cache() 
        return "Speech generation failed", 500

    file_name = f"{tempfile.gettempdir()}/{start_time}_{text[:10]}.wav"
    sf.write(file_name, wav.view(-1).cpu().numpy(), SAMPLE_RATE, "PCM_16")

    return send_file(file_name)

