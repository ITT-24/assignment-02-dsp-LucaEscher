import pyaudio

# Kopiert von audio-sample.py -------------
CHUNK_SIZE = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Audio sampling rate (Hz)
#  ----------------------------------------

# aus audio-sample.py kopiert
def set_up_stream(FORMAT, CHANNELS, RATE, CHUNK_SIZE):
    p = pyaudio.PyAudio()

    # print info about audio devices
    # let user select audio device
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    print('select audio device:')
    input_device = int(input())

    return p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK_SIZE,
                  input_device_index=input_device)
