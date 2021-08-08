import time
import torch
import soundfile as sf
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.tts_inference import Text2Speech
from parallel_wavegan.utils import download_pretrained_model
from parallel_wavegan.utils import load_model
from flask import Flask, send_file, request

sample_rate = 23000
lang = 'Japanese'
model_tag = 'kan-bayashi/jsut_conformer_fastspeech2_accent_with_pause' 
vocoder_tag = "jsut_parallel_wavegan.v1" 

downloader = ModelDownloader()

text2speech = Text2Speech(
    **downloader.download_and_unpack(model_tag),
    device="cpu",
    # Only for Tacotron 2
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=False,
    backward_window=1,
    forward_window=3,
    # Only for FastSpeech & FastSpeech2
    speed_control_alpha=1.0,
)
text2speech.spc2wav = None
vocoder = load_model(download_pretrained_model(vocoder_tag)).eval()
vocoder.remove_weight_norm()


app = Flask(__name__)

@app.route('/audio', methods=['POST'])
def get_audio():
    json_data = request.get_json()
    text = json_data['text']

    with torch.no_grad():
        start_time = time.time()
        wav, c, *_ = text2speech(text)
        wav = vocoder.inference(c)

    rtf = (time.time() - start_time) / (len(wav)/sample_rate)
    print(f"RTF = {rtf:5f}")

    file_name = f"tmp/{start_time}_{text[:10]}.wav"
    sf.write(file_name, wav.view(-1).cpu().numpy(), sample_rate, "PCM_16")

    return send_file(file_name)

