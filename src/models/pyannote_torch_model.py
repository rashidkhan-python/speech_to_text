import os
from dotenv import load_dotenv
from pyannote.audio import Pipeline
import numpy as np
import pandas as pd
import torch

def get_token():

    load_dotenv()
    token = os.getenv('hf_token')
    
    return token

def speech_diarization(token,audio_file):
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=token)
    pipeline = pipeline.to(device)
    diarization = pipeline(audio_file,num_speakers=2)
    
    return diarization

def diarization_to_df(diarization):
    
    seg_info_list = []
    for turn, track, speaker in diarization.itertracks(yield_label=True):
        seg_info = {'start': np.round(turn.start,2),
                    'end' : np.round(turn.end,2),
                    'speaker' : speaker}
        seg_df = pd.DataFrame.from_dict({track : seg_info},orient = 'index')
        seg_info_list.append(seg_df)

    all_seg_info_df = pd.concat(seg_info_list,axis=0)
    all_seg_info_df = all_seg_info_df.reset_index()

    return all_seg_info_df

def pyannote_to_df(audio_file,token):

    diarization = speech_diarization(token,audio_file)
    dia_df = diarization_to_df(diarization)
    
    return dia_df