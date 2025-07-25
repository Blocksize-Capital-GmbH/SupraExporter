# Supra Blockchain Metrics Exporter

<div align="center" style="display: flex; justify-content: center; align-items: center; gap: 60px; flex-wrap: wrap;">
  <!-- Blocksize - Professional blockchain infrastructure -->
  <a href="https://blocksize.info" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/Blocksize_Logo/Logo_main_white.svg">
      <img alt="Blocksize" src=".github/assets/Blocksize_Logo/Logo_main.svg" height="48">
    </picture>
  </a>

  <!-- Supra Blockchain -->
  <a href="https://supra.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/Supra_Logos/SVG/SupraLogo-horz-onDark.svg">
      <img alt="Supra" src=".github/assets/Supra_Logos/SVG/SupraLogo-horz-onLight.svg" height="52">
    </picture>
  </a>
</div>

<div align="center">

[![CI Pipeline](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/actions/workflows/main.yml/badge.svg)](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/actions/workflows/main.yml)
[![Docker Image](https://img.shields.io/badge/docker-ghcr.io%2Fblocksize--capital--gmbh%2Fsupraexporter-blue?logo=docker)](https://ghcr.io/blocksize-capital-gmbh/supraexporter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

</div>

A production-ready Prometheus metrics exporter for Supra blockchain nodes. This exporter provides comprehensive monitoring capabilities for both validator and RPC nodes, enabling operators to track node health, block heights, and network participation.

## Features

- **🔍 Validator Monitoring**: Track block height, validator participation, and health status
- **⚡ RPC Node Monitoring**: Monitor RPC endpoint availability and block synchronization
- **📊 Prometheus Integration**: Native Prometheus metrics format for seamless monitoring stack integration
- **🐳 Docker Support**: Production-ready containerized deployment
- **🛡️ Multiple Deployment Modes**: Support for validator-only, RPC-only, or combined monitoring
- **📈 Health Checks**: Automated health status based on block height synchronization
- **🔧 Flexible Configuration**: Environment-based configuration for easy deployment

## Quick Start

### Using Docker (Recommended)

1. **Create a configuration file**:

    ```bash
    cp .env.example .env
    # Edit .env with your node configuration
    ```

2. **Run with Docker Compose**:

    ```bash
    docker compose up -d
    ```

3. **Access metrics**:
    ```bash
    curl http://localhost:7897/debug/metrics/prometheus
    ```

### Development Setup

1. **Prerequisites**:
    - Python 3.10 or higher
    - [Poetry](https://python-poetry.org/docs/#installation) for dependency management

2. **Quick Setup (Recommended)**:

    ```bash
    git clone https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter.git
    cd supra-blockchain-metrics-exporter

    # Run the automated setup script
    ./scripts/dev-setup.sh
    ```

    This script will:
    - Configure Poetry to use in-project virtual environment (`.venv/`)
    - Create `.env` file from `.env.example`
    - Install all dependencies
    - Verify the setup

3. **Manual Setup** (Alternative):

    ```bash
    # Configure Poetry for local development
    poetry config virtualenvs.in-project true --local
    poetry config virtualenvs.create true --local

    # Install dependencies
    poetry install

    # Create configuration
    cp .env.example .env
    # Edit .env with your configuration
    ```

4. **Run the exporter**:

    ```bash
    poetry shell  # Activate virtual environment
    python -m supraexporter.main

    # Or run directly with poetry
    poetry run python -m supraexporter.main
    ```

5. **IDE Setup**:
    - Your IDE should automatically detect the `.venv/` folder
    - Set Python interpreter to `.venv/bin/python` (or `.venv/Scripts/python.exe` on Windows)
    - The virtual environment is isolated and won't affect CI pipelines

#### Poetry Configuration Notes

- **Local Config**: The `--local` flag creates repository-specific Poetry settings that aren't committed to git
- **CI Compatibility**: CI pipelines override Poetry config with custom virtual environment paths
- **Team Flexibility**: Each developer can choose their preferred virtual environment location
- **No Conflicts**: Local Poetry config won't break CI or affect other team members

## Configuration

The exporter is configured via environment variables, typically set in a `.env` file:

### Required Configuration

| Variable             | Description                                             | Example                         |
| -------------------- | ------------------------------------------------------- | ------------------------------- |
| `ROLE`               | Exporter mode: `validator`, `rpc`, or `both`            | `validator`                     |
| `VALIDATOR_LOG_PATH` | Path to validator log file (if ROLE includes validator) | `/home/supra/logs/supra.log`    |
| `NETWORK_PUBKEY`     | Validator public key (if ROLE includes validator)       | `53cfe11e8c05c93c90b54b98...`   |
| `RPC_URL`            | Local RPC endpoint URL (if ROLE includes rpc)           | `http://localhost:27000/rpc/v1` |
| `RPC_LOG_PATH`       | Path to RPC log file (if ROLE includes rpc)             | `/home/supra/rpc/logs/rpc.log`  |

### Optional Configuration

| Variable         | Description                           | Default                                |
| ---------------- | ------------------------------------- | -------------------------------------- |
| `EXPORTER_PORT`  | Port for metrics endpoint             | `9100`                                 |
| `PUBLIC_RPC_URL` | Public RPC URL for health comparison  | `https://rpc-mainnet.supra.com/rpc/v1` |
| `POLL_INTERVAL`  | Metrics collection interval (seconds) | `10`                                   |

### Finding Your Network Public Key

To find your validator's public key, check the validator identity configuration file:

```bash
# Primary method: Check the validator public identity file
cat supra_config/validator_public_identity.toml

# Alternative: Look for public key in validator logs
grep -i "pubkey\|public.*key" /path/to/validator.log

# Or search in other validator configuration files
find supra_config/ -name "*.toml" -exec grep -l "public" {} \;
```

The public key is typically found in the `validator_public_identity.toml` file within your `supra_config` directory.

## Metrics

The exporter provides the following Prometheus metrics:

### Common Metrics

- `supra_public_rpc_block_height`: Latest block height from public RPC

### Validator Metrics (when ROLE=validator or both)

- `supra_validator_block_height`: Block height parsed from validator logs
- `supra_validator_health`: Health status (1 if within 10 blocks of public RPC)
- `supra_block_relative_abundance`: Proportion of block proposals by this validator
- `supra_view_relative_abundance`: Proportion of view changes by this validator

### RPC Metrics (when ROLE=rpc or both)

- `supra_rpc_block_height`: Block height from local RPC endpoint
- `supra_rpc_health`: RPC health status (1 if within 10 blocks of public RPC)

## Deployment

### Production Docker Deployment

1. **Create docker-compose.yml**:

    ```yaml
    version: "3.8"
    services:
        supra-metrics-exporter:
            image: ghcr.io/blocksize-capital-gmbh/supraexporter:latest
            container_name: supra_blockchain_metrics_exporter
            network_mode: host
            restart: unless-stopped
            volumes:
                - ./.env:/app/.env
                - ${VALIDATOR_LOG_PATH}:${VALIDATOR_LOG_PATH}:ro
    ```

2. **Deploy**:
    ```bash
    docker compose up -d
    ```

### Kubernetes Deployment

Example Kubernetes deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: supra-metrics-exporter
spec:
    replicas: 1
    selector:
        matchLabels:
            app: supra-metrics-exporter
    template:
        metadata:
            labels:
                app: supra-metrics-exporter
        spec:
            containers:
                - name: exporter
                  image: ghcr.io/blocksize-capital-gmbh/supraexporter:latest
                  ports:
                      - containerPort: 7897
                  env:
                      - name: ROLE
                        value: "validator"
                      - name: VALIDATOR_LOG_PATH
                        value: "/logs/supra.log"
                      - name: NETWORK_PUBKEY
                        value: "your-pubkey-here"
                  volumeMounts:
                      - name: logs
                        mountPath: /logs
                        readOnly: true
            volumes:
                - name: logs
                  hostPath:
                      path: /path/to/supra/logs
```

### Prometheus Configuration

Add the following to your Prometheus configuration:

```yaml
scrape_configs:
    - job_name: "supra-exporter"
      static_configs:
          - targets: ["localhost:7897"]
      metrics_path: "/debug/metrics/prometheus"
      scrape_interval: 30s
```

## Monitoring & Alerting

### Grafana Dashboard

Import the provided Grafana dashboard (coming soon) or create custom visualizations using the exported metrics.

### Sample Alerts

```yaml
groups:
    - name: supra-validator
      rules:
          - alert: ValidatorUnhealthy
            expr: supra_validator_health == 0
            for: 5m
            labels:
                severity: critical
            annotations:
                summary: "Supra validator is unhealthy"
                description: "Validator has been out of sync for more than 5 minutes"

          - alert: ValidatorBlocksStale
            expr: time() - supra_validator_block_height > 300
            for: 2m
            labels:
                severity: warning
            annotations:
                summary: "Validator blocks are stale"
                description: "No new blocks seen for 5+ minutes"
```

## Development

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=supraexporter --cov-report=html

# Run specific test file
poetry run pytest supraexporter/tests/test_validators.py
```

### Code Quality

The project uses comprehensive code quality tools:

```bash
# Format code
poetry run black supraexporter/
poetry run isort supraexporter/

# Lint code
poetry run flake8 supraexporter/

# Type checking
poetry run mypy supraexporter/

# Run pre-commit hooks
poetry run pre-commit run --all-files
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Validator     │    │    RPC Node      │    │  Public RPC     │
│   Log Files     │    │   (Optional)     │    │   (Reference)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                 Supra Metrics Exporter                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────────┐   │
│  │   Log       │ │    RPC      │ │      Health Check       │   │
│  │  Reader     │ │   Client    │ │     (Public RPC)        │   │
│  └─────────────┘ └─────────────┘ └─────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   Prometheus    │
                    │    Metrics      │
                    │   (HTTP API)    │
                    └─────────────────┘
```

## Troubleshooting

### Common Issues

**Exporter can't read log files:**

- Verify file paths in `.env` configuration
- Check file permissions (exporter needs read access)
- Ensure log files exist and are being written to

**Metrics show stale data:**

- Check if log files are being rotated
- Verify mount points in Docker deployment
- Ensure log paths point to active log files, not archived ones

**Health checks failing:**

- Verify `PUBLIC_RPC_URL` is accessible
- Check if your node is actually in sync
- Review network connectivity

**Docker container exits:**

- Check logs: `docker logs supra_blockchain_metrics_exporter`
- Verify environment variables are properly set
- Ensure required files are mounted and accessible

**Virtual environment issues:**

- Check Poetry config: `poetry config --list`
- Reset local config: `poetry config virtualenvs.in-project false --local`
- Recreate environment: `poetry env remove --all && poetry install`
- Verify Python version: `poetry env info`

### Logs and Debugging

Enable debug logging:

```bash
export LOG_LEVEL=DEBUG
poetry run python -m supraexporter.main
```

Check exporter health:

```bash
curl http://localhost:7897/debug/metrics/prometheus | grep supra_
```

## Security

- The exporter runs with read-only access to log files
- No sensitive data is exposed through metrics
- All network communication uses standard HTTP/HTTPS
- Container runs as non-root user

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/issues)
- **Documentation**: [Project Wiki](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/wiki)
- **Security**: Report security vulnerabilities via our [contact form](https://blocksize.info/contact/)

## Acknowledgments

- Built for the [Supra](https://supra.com/) blockchain ecosystem
- Developed by [Blocksize](https://blocksize.info/) - Professional blockchain infrastructure and staking services
- Uses [Prometheus](https://prometheus.io/) for metrics exposition
- Containerized with [Docker](https://www.docker.com/)

---

<div align="center">

**Made with ❤️ by [Blocksize](https://blocksize.info/) for the [Supra](https://supra.com/) community**

_Need professional staking or infrastructure services? [Get in touch with Blocksize](https://blocksize.info/contact/)_

</div>
