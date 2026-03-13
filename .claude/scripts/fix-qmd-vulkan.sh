#!/usr/bin/env bash
# fix-qmd-vulkan.sh
# Re-applies Vulkan GPU fix for QMD after npm updates.
# Run this any time `npm update -g @tobilu/qmd` wipes the patch.
#
# What this does:
#   1. Installs the prebuilt Vulkan binary for node-llama-cpp
#   2. Patches llm.js to prefer Vulkan over CUDA (CUDA toolkit not installed)

set -e

QMD_DIR="$APPDATA/npm/node_modules/@tobilu/qmd"
LLM_JS="$QMD_DIR/dist/llm.js"

echo "=== QMD Vulkan Fix ==="

# Step 1: Install Vulkan prebuilt binary
echo "[1/2] Installing @node-llama-cpp/win-x64-vulkan..."
NODE_LLAMA_VERSION=$(node -e "console.log(require('$QMD_DIR/node_modules/node-llama-cpp/package.json').version)")
echo "      node-llama-cpp version: $NODE_LLAMA_VERSION"
npm install --prefix "$QMD_DIR" "@node-llama-cpp/win-x64-vulkan@$NODE_LLAMA_VERSION" --no-save

# Step 2: Patch GPU preference order in llm.js
echo "[2/2] Patching llm.js GPU preference order..."
if grep -q '"cuda","metal","vulkan"' "$LLM_JS"; then
    sed -i 's/\["cuda","metal","vulkan"\]/["vulkan","metal","cuda"]/g' "$LLM_JS"
    echo "      Patched: cuda>metal>vulkan → vulkan>metal>cuda"
elif grep -q '"vulkan","metal","cuda"' "$LLM_JS"; then
    echo "      Already patched — no changes needed."
else
    echo "      WARNING: Expected pattern not found. Check llm.js manually."
    echo "      Look for the GPU preference array near 'getLlamaGpuTypes'"
    exit 1
fi

# Step 3: Patch ensureRerankModel to unload generate model before loading reranker
# (all 3 models can't fit in 3GB VRAM simultaneously; expansion is done before rerank)
echo "[3/3] Patching ensureRerankModel for VRAM management..."
if grep -q 'Free VRAM used by the generate' "$LLM_JS"; then
    echo "      Already patched — no changes needed."
elif grep -q 'this.rerankModelLoadPromise = (async () => {' "$LLM_JS"; then
    # Insert generate model disposal before the load promise
    sed -i 's/this\.rerankModelLoadPromise = (async () => {/\/\/ Free VRAM used by the generate (expansion) model before loading reranker.\n        if (this.generateModel) {\n            await this.generateModel.dispose();\n            this.generateModel = null;\n        }\n        this.rerankModelLoadPromise = (async () => {/' "$LLM_JS"
    echo "      Patched: generate model unloads before reranker loads"
else
    echo "      WARNING: Expected pattern not found. Apply manually."
fi

# Step 3: Restart daemon
echo "[3/3] Restarting QMD daemon..."
qmd mcp stop 2>/dev/null || true
sleep 2
qmd mcp --http --port 8182 --daemon
sleep 3
qmd status | grep -E "GPU:|MCP:"

echo ""
echo "Done. Run 'qmd query \"test\" -c codex' to verify."
