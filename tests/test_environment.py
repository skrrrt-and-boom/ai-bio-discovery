import anndata
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def test_core_scientific_stack() -> None:
    x = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = np.array([0.0, 2.0, 4.0, 6.0])
    model = LinearRegression().fit(x, y)

    adata = anndata.AnnData(
        X=np.array([[1.0, 0.0], [0.0, 1.0]]),
        obs=pd.DataFrame(index=["cell_1", "cell_2"]),
        var=pd.DataFrame(index=["gene_1", "gene_2"]),
    )

    assert np.isclose(model.predict([[4.0]])[0], 8.0)
    assert adata.shape == (2, 2)

