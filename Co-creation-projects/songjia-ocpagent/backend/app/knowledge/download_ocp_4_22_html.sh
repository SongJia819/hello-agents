#!/usr/bin/env bash

set -uo pipefail

CATALOG_URL="https://docs.redhat.com/en/documentation/openshift_container_platform/4.22"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${OCP_OUTPUT_DIR:-${SCRIPT_DIR}/docs/ocp-4.22}"
CATALOG_FILE="${OUTPUT_DIR}/catalog.html"
FORCE=false
LIMIT=""
SINGLE_PAGE=false

usage() {
    echo "Usage: $0 [--force] [--limit N] [--single-page]" >&2
}

while (($#)); do
    case "$1" in
        --force)
            FORCE=true
            ;;
        --limit)
            shift
            LIMIT="${1:-}"
            if [[ ! "${LIMIT}" =~ ^[1-9][0-9]*$ ]]; then
                echo "--limit must be a positive integer" >&2
                exit 2
            fi
            ;;
        --single-page)
            SINGLE_PAGE=true
            ;;
        --help)
            usage
            exit 0
            ;;
        *)
            usage
            exit 2
            ;;
    esac
    shift
done

if [[ "${SINGLE_PAGE}" == true ]]; then
    DOCUMENT_FORMAT="html-single"
    DOCUMENT_URL_SUFFIX="/index"
else
    DOCUMENT_FORMAT="html"
    DOCUMENT_URL_SUFFIX=""
fi

HTML_DIR="${OUTPUT_DIR}/${DOCUMENT_FORMAT}"
MANIFEST_FILE="${OUTPUT_DIR}/${DOCUMENT_FORMAT}-manifest.tsv"
mkdir -p "${HTML_DIR}"

download_file() {
    local url="$1"
    local destination="$2"
    local partial

    partial="${destination}.part"
    if [[ -s "${partial}" ]]; then
        if curl --fail --location --silent --show-error --continue-at - \
            --connect-timeout 15 --max-time 120 --retry 2 \
            --output "${partial}" "${url}" && [[ -s "${partial}" ]]; then
            mv -f "${partial}" "${destination}"
            return 0
        fi
        rm -f "${partial}"
    fi

    if curl --fail --location --silent --show-error \
        --connect-timeout 15 --max-time 120 --retry 2 \
        --output "${partial}" "${url}"; then
        if [[ -s "${partial}" ]]; then
            mv -f "${partial}" "${destination}"
            return 0
        fi
    fi
    return 1
}

if [[ "${FORCE}" == true || ! -s "${CATALOG_FILE}" ]]; then
    if ! download_file "${CATALOG_URL}" "${CATALOG_FILE}"; then
        echo "Failed to download OCP 4.22 catalog: ${CATALOG_URL}" >&2
        exit 1
    fi
fi

mapfile -t slugs < <(
    sed 's/></>\n</g' "${CATALOG_FILE}" \
        | awk '/<rh-tile compact/{in_tile=1} in_tile {print} /<\/rh-tile>/{in_tile=0}' \
        | grep -oE '/en/documentation/openshift_container_platform/4\.22/html/[a-z0-9_-]+(/index)?' \
        | sed -E 's#^/en/documentation/openshift_container_platform/4\.22/html/##; s#/index$##' \
        | sort -u
)

if ((${#slugs[@]} == 0)); then
    echo "No supported OCP 4.22 document links found in ${CATALOG_FILE}" >&2
    exit 1
fi

if [[ -n "${LIMIT}" ]]; then
    slugs=("${slugs[@]:0:LIMIT}")
fi

manifest_temporary="$(mktemp "${OUTPUT_DIR}/.${DOCUMENT_FORMAT}-manifest.tsv.XXXXXX")"
printf 'slug\turl\tfile\tstatus\n' > "${manifest_temporary}"

completed=0
skipped=0
failed=0
for slug in "${slugs[@]}"; do
    url="https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/${DOCUMENT_FORMAT}/${slug}${DOCUMENT_URL_SUFFIX}"
    output="${HTML_DIR}/${slug}.html"

    if [[ "${FORCE}" != true && -s "${output}" ]]; then
        printf '%s\t%s\t%s\tskipped\n' "${slug}" "${url}" "${DOCUMENT_FORMAT}/${slug}.html" >> "${manifest_temporary}"
        ((skipped += 1))
        continue
    fi

    if download_file "${url}" "${output}"; then
        printf '%s\t%s\t%s\tcompleted\n' "${slug}" "${url}" "${DOCUMENT_FORMAT}/${slug}.html" >> "${manifest_temporary}"
        ((completed += 1))
    else
        printf '%s\t%s\t%s\tfailed\n' "${slug}" "${url}" "${DOCUMENT_FORMAT}/${slug}.html" >> "${manifest_temporary}"
        ((failed += 1))
    fi
done

mv -f "${manifest_temporary}" "${MANIFEST_FILE}"
echo "${DOCUMENT_FORMAT} download complete: discovered=${#slugs[@]} completed=${completed} skipped=${skipped} failed=${failed}"

if ((failed > 0)); then
    exit 1
fi
