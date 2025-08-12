import requests 
import tempfile
from pydub import AudioSegment

def record_to_wave(RECORD_SECONDS, WAVE_OUTPUT_FILENAME):

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate = RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print(" *recording")

    frames = []

    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print(" *done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wave_file = wave.open(WAVE_OUTPUT_FILENAME,'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(p.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

def download_audio(audio_url, file_name=None):
    doc = requests.get(audio_url)

    if file_name:
        my_file = file_name
        with open(my_file, 'wb') as f:
            f.write(doc.content)
    else:
        temporary_file = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
        my_file = temporary_file.name
        temporary_file.write(doc.content)
        temporary_file.close()

    return my_file

def transform_mp3_to_wave(mp3_file,mp3_output=None):

    sound = AudioSegment.from_mp3(mp3_file)

    if mp3_output:
        my_file = mp3_output
        sound.export(mp3_output, format='wav')

    else:
        temporary_file = tempfile.NamedTemporaryFile(suffix='.wav',delete=False)
        my_file = temporary_file.name
        sound.export(my_file,format='wav')
    return my_file

def audio_chunks_wav(inputFile, outputFile,start_frame=0, end_frame=60000):
    sound = AudioSegment.from_wav(inputFile)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)

    #Extracting 60sec from the recording
    excerpt = sound[start_frame : (start_frame + end_frame)]
    excerpt.export(outputFile,format='wav')


if __name__ == '__main__':

    # records_sec = 60
    file_name = 'voice.wav'
    record_to_wave(records_sec,file_name)

    audio_url  =r"https://dts.podtrac.com/redirect.mp3/tracking.swap.fm/track/0bDcdoop59bdTYSfajQW/pdst.fm/e/stitcher.simplecastaudio.com/2be48404-a43c-4fa8-a32c-760a3216272e/episodes/db82e72d-a274-4a68-990a-87dd2155cb2e/audio/128/default.mp3?aid=rss_feed&amp;awCollectionId=2be48404-a43c-4fa8-a32c-760a3216272e&amp;awEpisodeId=db82e72d-a274-4a68-990a-87dd2155cb2e&amp;feed=Y8lFbOT4"

    raw_data = r"C:\Users\Rashid\Desktop\speech_to_text\data\raw"
    interim_data = r"C:\Users\Rashid\Desktop\speech_to_text\data\interim"
    processed_data = r"C:\Users\Rashid\Desktop\speech_to_text\data\processed"
    
    temporary_file_name = download_audio(audio_url,rf"{raw_data}/freakonomic.mp3")


    mp3_file = rf"{raw_data}/freakonomic.mp3"
    wav_file = rf"{interim_data}/freakonomic.wav"
    clipped_wav_file = rf"{processed_data}/freakonomic_chunk.wav"

    transform_mp3_to_wave(mp3_file=mp3_file,mp3_output=wav_file)

    source = wav_file
    audio_chunks_wav(source,rf"{processed_data}/freakonomic_chunk.wav")
    