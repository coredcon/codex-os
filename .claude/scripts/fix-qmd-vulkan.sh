#!/usr/bin/env bash
# fix-qmd-vulkan.sh
# Re-applies Vulkan GPU fix for QMD after npm updates.
# Run this any time `npm update -g @tobilu/qmd` wipes the patch.
#
# What this does:
#   1. Installs the prebuilt Vulkan binary for node-llama-cpp
#   2. Patches llm.js to force Vulkan GPU (no CUDA toolkit installed)
#   3. Patches ensureRerankModel to free VRAM before loading reranker
#
# Tested on: 1.0.7 (getLlamaGpuTypes array), 2.0.1 (getLlama options object)

set -e

QMD_DIR="C:/Users/aspor/AppData/Roaming/npm/node_modules/@tobilu/qmd"
LLM_JS="$QMD_DIR/dist/llm.js"

echo "=== QMD Vulkan Fix ==="

# Step 1: Install Vulkan prebuilt binary
echo "[1/3] Installing @node-llama-cpp/win-x64-vulkan..."
NODE_LLAMA_VERSION=$(node -e "console.log(require('$QMD_DIR/node_modules/node-llama-cpp/package.json').version)")
echo "      node-llama-cpp version: $NODE_LLAMA_VERSION"
npm install --prefix "$QMD_DIR" "@node-llama-cpp/win-x64-vulkan@$NODE_LLAMA_VERSION" --no-save

# Step 2: Patch GPU — handles both API styles
echo "[2/3] Patching llm.js for Vulkan GPU..."

# Style A: >=2.0.1 — getLlama({ build: "autoAttempt", ... }) options object
if grep -q 'gpu: "vulkan"' "$LLM_JS"; then
    echo "      Already patched (style A: getLlama options) — no changes needed."
elif grep -q 'build: "autoAttempt"' "$LLM_JS"; then
    sed -i 's/build: "autoAttempt",/build: "autoAttempt",\n                gpu: "vulkan", \/\/ Patched: GTX 1060 uses Vulkan (no CUDA toolkit)/g' "$LLM_JS"
    echo "      Patched (style A): added gpu: \"vulkan\" to getLlama options"
# Style B: <2.0.1 — getLlamaGpuTypes preference array
elif grep -q '"cuda","metal","vulkan"' "$LLM_JS"; then
    sed -i 's/\["cuda","metal","vulkan"\]/["vulkan","metal","cuda"]/g' "$LLM_JS"
    echo "      Patched (style B): cuda>metal>vulkan → vulkan>metal>cuda"
elif grep -q '"vulkan","metal","cuda"' "$LLM_JS"; then
    echo "      Already patched (style B) — no changes needed."
else
    echo "      WARNING: No known GPU pattern found. Check llm.js manually."
    echo "      Search for 'getLlama' or 'getLlamaGpuTypes' to find the right spot."
    exit 1
fi

# Step 3: Patch ensureRerankModel to unload generate model before loading reranker
# (all 3 models can't fit in 3GB VRAM simultaneously; expansion is done before rerank)
echo "[3/3] Patching ensureRerankModel for VRAM management..."
if grep -q 'Free VRAM used by the generate' "$LLM_JS"; then
    echo "      Already patched — no changes needed."
elif grep -q 'this.rerankModelLoadPromise = (async () => {' "$LLM_JS"; then
    sed -i 's/this\.rerankModelLoadPromise = (async () => {/\/\/ Free VRAM used by the generate (expansion) model before loading reranker.\n        if (this.generateModel) {\n            await this.generateModel.dispose();\n            this.generateModel = null;\n        }\n        this.rerankModelLoadPromise = (async () => {/' "$LLM_JS"
    echo "      Patched: generate model unloads before reranker loads"
else
    echo "      WARNING: rerankModelLoadPromise pattern not found. Apply manually."
fi

# Step 4: Restart daemon
echo "[4/4] Restarting QMD daemon..."
qmd mcp stop 2>/dev/null || true
sleep 2
qmd mcp --http --port 8182 --daemon
sleep 3
qmd status | grep -E "GPU:|MCP:"

echo ""
echo "Done. Run 'qmd query \"test\" -c codex' to verify."
