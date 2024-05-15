import os

import pandas as pd
from dotenv import load_dotenv
from brukeropusreader import read_file, opus_data

load_dotenv()
DATA_PATH = os.getenv('DATA_PATH')


def read_data(path: str):
    files = os.listdir(path)
    print(f'{len(files)=}')
    raw_data: dict[str, opus_data.OpusData] = dict()
    for file in files:
        if file in ('.DS_Store', 'dataset.csv'):
            continue
        filename_split: list[str] = os.path.splitext(file)
        sample_name = filename_split[0] + filename_split[1].replace('.', '__')
        raw_data[sample_name] = read_file(os.path.join(path, file))
    clean_data: list[dict] = []
    for name, spectrum_data in raw_data.items():
        sample = dict(zip(
            spectrum_data.get_range('AB'),
            spectrum_data.get('AB')[:len(spectrum_data.get_range('AB'))]
        ))
        s_name, exp_num = name.split('__')
        sample['sample'] = s_name
        sample['exp_num'] = exp_num
        # sample['target'] = int(s_name[-1]) if s_name[-1].isnumeric() else -1
        sample['target'] = s_name[-1]
        clean_data.append(sample)
    df = pd.DataFrame(clean_data)
    print(f'{df.shape=}')
    return df


if __name__ == '__main__':
    dataset = read_data(DATA_PATH)
    dataset.to_csv(os.path.join(DATA_PATH, 'dataset.csv'), index=False)
