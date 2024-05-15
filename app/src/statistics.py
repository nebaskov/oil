import os
from loguru import logger
from dotenv import load_dotenv

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

load_dotenv()
DATA_PATH = os.getenv('DATA_PATH')


def read_data(path: str, id_column) -> pd.DataFrame:
    return pd.read_csv(path, index_col=id_column)


def scale_data(ds: pd.DataFrame) -> pd.DataFrame:
    columns = ds.columns
    index = ds.index
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(ds)
    return pd.DataFrame(scaled_data, index=index, columns=columns)


def plot_pca(x: pd.DataFrame, y: pd.Series, n_components: int = 100) -> None:
    test_pca = PCA(n_components=n_components)
    test_pca.fit(x)
    optim_n_comp = 2
    explained_ratio = 0
    for n_comp in range(2, n_components):
        explained_ratio = test_pca.explained_variance_ratio_[:n_comp].sum()
        if explained_ratio > 0.8:
            break
        optim_n_comp += 1
    logger.debug(f'Optimal components number: {optim_n_comp} with explained ration: {explained_ratio}')

    pca = PCA(n_components=optim_n_comp)
    transformed_data = pca.fit_transform(x)
    fig = plt.figure()
    sns.scatterplot(x=transformed_data, y=y)
    fig.suptitle('PCA plot')
    plt.show()
