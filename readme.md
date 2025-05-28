# Supra Metrics Exporter

A lean, modular, and production-ready Prometheus exporter for the [Supra](https://supra.com/) blockchain.
This exporter collects metrics from:

- 📡 RPC endpoints (e.g. block height)
- 📜 Validator log files (e.g. block authored, view frequency)

Supports all three deployment modes:

- `rpc` – Export only RPC metrics
- `validator` – Export only validator metrics
- `both` – Export all metrics from a single node, if both clients run on same node

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-org/supra-metrics-exporter.git
cd supra-metrics-supraexporter
```

### 2. Setup environment

```bash
cp config.example.env .env
```

Edit `.env` to match your RPC/log file paths and pubkey.

### 3. Install dependencies

```bash
poetry install
```

### 4. Run the exporter

```bash
poetry run python -m supraexporter.main
```

Exporter runs on [http://localhost:9100/metrics](http://localhost:9100/metrics)

---

## 📥 Prometheus Integration

```yaml
- job_name: "supra-supraexporter"
  static_configs:
      - targets: ["localhost:9100"]
```

---

## 📦 Docker Support

---

## 📦 Quick Start

### 🐳 Option 1: Using Docker Compose

1. Create a `.env` file in the project root (see [sample.env](#sampleenv) below).
2. Save the following as `docker-compose.yml`:

```yaml
version: "3.8"

services:
    supra-metrics-exporter:
        image: yourdockerhub/supra-metrics-exporter:latest
        container_name: supra_blockchain_metrics_exporter
        network_mode: host
        restart: unless-stopped
        volumes:
            - ./.env:/app/.env
```

3. Run:

```bash
docker compose up -d
```

Metrics will be available at:

```
http://localhost:${EXPORTER_PORT}
```

---

### 🐳 Option 2: Using Docker CLI

```bash
docker run --network host \
  -v $(pwd)/.env:/app/.env \
  --name supra_exporter \
  -d yourdockerhub/supra-metrics-supraexporter:latest
```

---

## ⚙️ Configuration

All configuration is provided via a `.env` file. Here’s a minimal working example:

---

## ⚙️ Sample `.env`

```dotenv
ROLE=both
EXPORTER_PORT=9100
RPC_URL=http://localhost:8545
PUBLIC_RPC_URL=https://rpc-testnet.supra.com/rpc/v1
VALIDATOR_LOG_PATH=/var/log/supra-validator.log
NETWORK_PUBKEY=0xYOURPUBKEY
```

---

## 📈 Exposed Metrics

| Metric Name                      | Description                             |
| -------------------------------- | --------------------------------------- |
| `supra_rpc_block_height`         | Latest block height from your RPC       |
| `supra_public_rpc_block_height`  | Latest block height from public RPC     |
| `supra_rpc_health`               | 1 if within 10 blocks of public RPC     |
| `supra_validator_block_height`   | Parsed from validator log               |
| `supra_block_relative_abundance` | Ratio of 'Block' lines with your pubkey |
| `supra_view_relative_abundance`  | Ratio of 'View' lines with your pubkey  |
| `supra_validator_health`         | 1 if within 10 blocks of RPC            |

---

## 🔧 Customization

- Extendable to other blockchains
- Swap in your own collectors or parsing logic
- Written in clean, modular Python

---

## 🛡️ License

MIT – free to use, fork, and contribute.

---

## 👥 Maintainers

- Abhinav Taneja ([at@blocksize-capital.com](mailto:at@blocksize-capital.com))
- Axel Lode ([al@blocksize-capital.com](mailto:al@blocksize-capital.com))
