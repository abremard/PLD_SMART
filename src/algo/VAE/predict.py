import magenta.music as mm
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

from algo.VAE.models.VAE import play, interpolate, download

import tensorflow.compat.v1 as tf

def generate(
    input_mel_midi_data,
    filename,
    temperature = 0.5,
    num_steps=15,
    start_melody=0,
    end_melody=1,
    ):
    
    # Load the pre-trained model.
    mel_2bar_config = configs.CONFIG_MAP['cat-mel_2bar_big']
    mel_2bar = TrainedModel(mel_2bar_config, batch_size=4, checkpoint_dir_or_path='gs://download.magenta.tensorflow.org/models/music_vae/colab2/checkpoints/mel_2bar_big.ckpt')

    # Extract melodies from MIDI files. This will extract all unique 2-bar melodies using a sliding window with a stride of 1 bar.
    mel_input_seqs = [mm.midi_to_sequence_proto(m) for m in input_mel_midi_data]
    extracted_mels = []
    for ns in mel_input_seqs:
        extracted_mels.extend(
            mel_2bar_config.data_converter.from_tensors(
                mel_2bar_config.data_converter.to_tensors(ns)[1]))
        
    start_mel = extracted_mels[start_melody]
    end_mel = extracted_mels[end_melody]

    mel_2bar_interp = interpolate(mel_2bar, start_mel, end_mel, filename=filename, num_steps=num_steps, temperature=temperature)
    