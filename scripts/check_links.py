#!/usr/bin/env python3
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent

HTTP_TIMEOUT_SECONDS = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

KNOWN_PRIVATE_REPOSITORIES = {
    "https://github.com/GabrielFrigo4/optilaser",
}


@dataclass(frozen=True)
class LinkCheckResult:
    url: str
    status_code: int
    is_valid: bool
    message: str


def extract_urls_from_tex_files(root: Path) -> Set[str]:
    urls: Set[str] = set()
    url_pattern = re.compile(r"https?://[^\s{}<>\"\'\\]+")

    for tex_path in root.glob("**/*.tex"):
        content = tex_path.read_text(encoding="utf-8", errors="ignore")
        for match in url_pattern.finditer(content):
            url = match.group(0).rstrip(".,;")
            urls.add(url)
    return urls


def verify_url(url: str) -> LinkCheckResult:
    if url in KNOWN_PRIVATE_REPOSITORIES:
        return LinkCheckResult(url=url, status_code=200, is_valid=True, message="OK (Privado)")

    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"},
    )
    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            return LinkCheckResult(url=url, status_code=response.getcode(), is_valid=True, message="OK")
    except urllib.error.HTTPError as error:
        if error.code in (403, 999) and "linkedin.com" in url:
            return LinkCheckResult(url=url, status_code=error.code, is_valid=True, message="OK (Bot Protection)")
        return LinkCheckResult(url=url, status_code=error.code, is_valid=False, message=f"HTTP {error.code}")
    except urllib.error.URLError as error:
        return LinkCheckResult(url=url, status_code=0, is_valid=False, message=str(error.reason))
    except Exception as error:
        return LinkCheckResult(url=url, status_code=0, is_valid=False, message=str(error))


def run_link_verification(root: Path) -> Tuple[List[LinkCheckResult], List[LinkCheckResult]]:
    urls = extract_urls_from_tex_files(root)
    successful: List[LinkCheckResult] = []
    failed: List[LinkCheckResult] = []

    print(f"Verificando {len(urls)} links encontrados nos arquivos .tex...\n")

    for url in sorted(urls):
        result = verify_url(url)
        if result.is_valid:
            successful.append(result)
            print(f"  [OK]  {result.status_code:3d}  {result.url}")
        else:
            failed.append(result)
            print(f"  [ERR] {result.status_code:3d}  {result.url} -> {result.message}")

    return successful, failed


def main() -> None:
    _, failed = run_link_verification(REPO_ROOT)
    print("\n" + "=" * 50)
    if failed:
        print(f"Falha: {len(failed)} link(s) com erro.")
        raise SystemExit(1)
    print("Sucesso: Todos os links estão ativos e acessíveis!")


if __name__ == "__main__":
    main()
