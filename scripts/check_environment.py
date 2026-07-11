"""Verify that the core scientific Python environment works end to end."""

import os
from importlib.metadata import version
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".cache" / "matplotlib")
)

import anndata
import numpy as np
import pandas as pd
import scanpy
from sklearn.linear_model import LinearRegression


def main() -> None:
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
    assert scanpy is not None

    packages = ["numpy", "pandas", "scipy", "scikit-learn", "anndata", "scanpy"]
    print("Environment verification passed.")
    print(f"AnnData shape: {adata.shape}")
    print(f"Scanpy import: {version('scanpy')}")
    for package in packages:
        print(f"{package}=={version(package)}")


if __name__ == "__main__":
    main()
