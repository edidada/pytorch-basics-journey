"""Minimal end-to-end PyTorch Quickstart smoke test.

Follows the official Learn-the-Basics path (data -> model -> train -> save/load)
but uses synthetic tensors, so it runs offline in CI without downloading datasets.
"""
from pathlib import Path
from tempfile import TemporaryDirectory

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def build_model() -> nn.Module:
    return nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 128),
        nn.ReLU(),
        nn.Linear(128, 10),
    )


def main() -> None:
    torch.manual_seed(0)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"torch={torch.__version__} device={device}")

    # Tensors + Datasets & DataLoaders
    features = torch.randn(128, 1, 28, 28)
    labels = torch.randint(0, 10, (128,))
    loader = DataLoader(TensorDataset(features, labels), batch_size=64, shuffle=True)
    x, y = next(iter(loader))
    assert x.shape == (64, 1, 28, 28)
    print(f"batch: X={tuple(x.shape)} y={tuple(y.shape)}")

    # Build Model + Autograd + Optimization
    model = build_model().to(device)
    print(f"params={sum(p.numel() for p in model.parameters())}")
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
    model.train()
    total = 0.0
    for xb, yb in loader:
        xb, yb = xb.to(device), yb.to(device)
        loss = loss_fn(model(xb), yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total += loss.item()
    print(f"train loss={total / len(loader):.4f}")

    # Save & Load Model
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "model.pth"
        torch.save(model.state_dict(), path)
        restored = build_model().to(device)
        restored.load_state_dict(torch.load(path, weights_only=True))
        restored.eval()
        with torch.no_grad():
            pred = restored(x.to(device)).argmax(dim=1)
        print(f"predictions: {pred[:8].tolist()}")

    print("smoke test OK")


if __name__ == "__main__":
    main()
