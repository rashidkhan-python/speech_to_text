from faster_whisper import WhisperModel
from datetime import datetime,time
import torch
import pandas as pd

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

audio_path =  r"C:\Users\Rashid\Desktop\speech_to_text\Code\voice.wav"  # wav/flac/m4a work too

def whisper_transcribe(audio_path,model='base',verbose=False):
# CPU-friendly setup: small model, INT8 compute for speed/memory
    model = WhisperModel("base", device="cpu", compute_type="int8")

    segments,info = model.transcribe(
        audio_path,
        beam_size=5,
        language='en',
        vad_filter=True)
    return segments

def whisper_transcription_segments_df(audio_path,model='base'):
    result = whisper_transcribe(audio_path,model)
    all_seg_df= pd.DataFrame([{"id":seg.id,
                   "seek":seg.seek, 
                   "start": seg.start,
                   "end":seg.end,
                   "text":seg.text,
                   "temperature":seg.temperature,
                   "avg_logprob":seg.avg_logprob,
                   "compression_ratio":seg.compression_ratio,
                   "no_speech_prob":seg.id} for seg in result]).set_index("id")
    return all_seg_df
if __name__ == '__main__':

    model = 'base'
    # file_name = 'voice.wav'
    # output  = whisper_transcribe(file_name,model)


    raw_data = r"C:\Users\Rashid\Desktop\speech_to_text\data\raw"
    interim_data = r"C:\Users\Rashid\Desktop\speech_to_text\data\interim"
    processed_data = r"C:\Users\Rashid\Desktop\speech_to_text\data\processed"


    clipped_wav_file = rf"{processed_data}/freakonomic_chunk.wav"
    output  = whisper_transcribe(clipped_wav_file,model)
    print(output)
    seg_df = whisper_transcription_segments_df(clipped_wav_file,model)
