#!/bin/bash
# Development Environment Setup Script
# This script configures your local development environment without affecting CI

set -e

echo "🔧 Setting up local development environment..."

# Configure Poetry for local development (in-project venv)
echo "📦 Configuring Poetry for local development..."
poetry config virtualenvs.in-project true --local
poetry config virtualenvs.create true --local
poetry config virtualenvs.prefer-active-python true --local

echo "✅ Poetry configured for local development:"
poetry config --list | grep -E "(virtualenvs\.(in-project|create|prefer-active-python))"

# Create/update .env file if needed
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "📄 Creating .env from .env.example..."
        cp .env.example .env
        echo "✅ .env file created"
    else
        echo "⚠️  No .env.example found"
    fi
else
    echo "✅ .env file already exists"
fi

# Install dependencies
echo "📦 Installing project dependencies..."
poetry install

# Verify setup
echo "🔍 Verifying development setup..."
poetry env info

if [ -d ".venv" ]; then
    echo "✅ Virtual environment created at: $(pwd)/.venv"
    echo "🎉 Development environment ready!"
    echo ""
    echo "💡 Tips:"
    echo "   • Your IDE should now detect the .venv folder automatically"
    echo "   • Use 'poetry shell' to activate the virtual environment"
    echo "   • Use 'poetry run python' to run Python with the virtual environment"
    echo "   • CI will continue to use its own virtual environment configuration"
else
    echo "❌ Virtual environment not found at .venv"
    echo "   Check Poetry configuration with: poetry config --list"
fi
