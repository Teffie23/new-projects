import vosk
import sys
import queue
import sounddevice as sd
import json
def q_callback(indate,frames,time,status):
    if status:
        print(status,file=sys.stderr)
    q.put(bytes(indate))

model = vosk.Model('model')
samplerate = 16000
device = 1
q=queue.Queue()
def my_listen(callback):
    with sd.RawInputStream(samplerate=samplerate,blocksize=8000,device=device,dtype='int16',
                       channels=1,callback=q_callback):
        rec=vosk.KaldiRecognizer(model,samplerate)
        while True:
            data=q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())['text'])
                #print(rec.Result())
            #else:
            #    print(rec.PartialResult())