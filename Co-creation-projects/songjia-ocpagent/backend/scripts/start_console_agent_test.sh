#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd "${script_dir}/../.." && pwd)"
env_file="${project_root}/backend/.env"

if [[ ! -f "${env_file}" ]]; then
  echo "Environment file not found: ${env_file}" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "${env_file}"
set +a

show_value() {
  local key="$1"
  printf '%s=%s\n' "${key}" "${!key-<unset>}"
}

echo "Loaded environment: ${env_file}"
echo "Effective non-sensitive configuration:"
for key in OCP_AGENT_LLM_THINK LLM_MODEL_ID LLM_BASE_URL LLM_TIMEOUT HOST PORT LOG_LEVEL; do
  show_value "${key}"
done
echo "Sensitive configuration values are redacted."

if [[ "${CONSOLE_AGENT_TEST_DRY_RUN:-false}" == "true" ]]; then
  exit 0
fi

cd "${project_root}"
export PYTHONPATH="${project_root}/backend${PYTHONPATH:+:${PYTHONPATH}}"
exec "${PYTHON_BIN:-python}" -m app.console_agent_test
