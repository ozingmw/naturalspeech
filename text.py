import tqdm
import os

check = os.listdir('../naturalspeech_dataset/KSS_data/archive/kss/wavs')

with open('../naturalspeech_dataset/KSS_data/archive/transcript.v.1.4.txt', 'r', encoding='UTF-8') as f:
    for line in tqdm.tqdm(f):
        wav_file_path = line.split('|')[0].split('/')[1]
        text = line.split('|')[2]

        if wav_file_path not in check:
            continue

        if wav_file_path[0] == '1':
            with open('./filelists/transcript_refine_test.txt', 'a', encoding='UTF-8') as ff:
                ff.write(f'DUMMY1/{wav_file_path}|{text}\n')
        elif wav_file_path[0] == '2':
            with open('./filelists/transcript_refine_val.txt', 'a', encoding='UTF-8') as ff:
                ff.write(f'DUMMY1/{wav_file_path}|{text}\n')
        else:
            with open('./filelists/transcript_refine_train.txt', 'a', encoding='UTF-8') as ff:
                ff.write(f'DUMMY1/{wav_file_path}|{text}\n')