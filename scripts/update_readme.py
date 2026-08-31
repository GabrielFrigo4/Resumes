#!/usr/bin/env python3
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parent.parent
COMPANIES_DIR = REPO_ROOT / "companies"
README_PATH = REPO_ROOT / "README.md"

TAG_START = "<!-- COMPANIES_TABLE_START -->"
TAG_END = "<!-- COMPANIES_TABLE_END -->"

COMPANY_NAMES = {
    "nubank": "Nubank",
    "ifood": "iFood",
    "uber": "Uber",
    "google": "Google",
    "meta": "Meta",
    "amazon": "Amazon",
    "microsoft": "Microsoft",
}

BRAND_COLORS = {
    "nubank": "8A05BE",
    "ifood": "EA1D2C",
    "uber": "000000",
    "google": "4285F4",
    "meta": "0668E1",
    "amazon": "FF9900",
    "microsoft": "00A4EF",
}


@dataclass(frozen=True)
class CompanyDocument:
    company: str
    title: str
    filename: str
    language: str
    download_url: str
    badge_url: str


def detect_language(tex_content: str) -> str:
    if any(k in tex_content for k in ("brazilian", "portuges", "portuguese")):
        return "🇧🇷 PT-BR"
    if "english" in tex_content:
        return "🇺🇸 EN-US"
    if "Resumo Profissional" in tex_content or "Experiência" in tex_content:
        return "🇧🇷 PT-BR"
    return "🇺🇸 EN-US"


def format_title(stem: str, language: str) -> str:
    parts = stem.split("-")
    if len(parts) == 2 and parts[1].isdigit():
        base, year = parts[0].lower(), parts[1]
        if base == "internship":
            return f"Estágio {year}" if "PT" in language else f"Internship {year}"
        if base == "ifuture":
            return f"iFuture {year}"
        if base == "letter":
            return f"Carta {year}" if "PT" in language else f"Cover Letter {year}"
        return f"{base.capitalize()} {year}"
    return stem.replace("-", " ").title()


def parse_company_document(tex_path: Path) -> CompanyDocument:
    company_raw = tex_path.parent.name.lower()
    company_name = COMPANY_NAMES.get(company_raw, tex_path.parent.name.title())
    brand_color = BRAND_COLORS.get(company_raw, "24292e")

    content = tex_path.read_text(encoding="utf-8", errors="ignore")
    language = detect_language(content)
    title = format_title(tex_path.stem, language)
    pdf_filename = f"{tex_path.stem}.pdf"

    return CompanyDocument(
        company=company_name,
        title=title,
        filename=pdf_filename,
        language=language,
        download_url=f"https://github.com/GabrielFrigo4/Resumes/releases/latest/download/{pdf_filename}",
        badge_url=f"https://img.shields.io/badge/PDF-Baixar-{brand_color}?style=flat-square&logo=adobeacrobatreader",
    )


def collect_company_documents() -> List[CompanyDocument]:
    if not COMPANIES_DIR.exists():
        return []

    documents: List[CompanyDocument] = []
    for company_dir in sorted(COMPANIES_DIR.iterdir()):
        if not company_dir.is_dir() or company_dir.name.startswith("."):
            continue
        for tex_file in sorted(company_dir.glob("*.tex")):
            documents.append(parse_company_document(tex_file))
    return documents


def build_markdown_table(documents: List[CompanyDocument]) -> str:
    if not documents:
        return "_Nenhum documento específico encontrado._"

    rows = [
        "| Empresa | Documento / Vaga | Idioma | Download |",
        "| :--- | :--- | :---: | :---: |",
    ]
    for doc in documents:
        rows.append(
            f"| **{doc.company}** | {doc.title} (`{doc.filename}`) | {doc.language} | "
            f"[![Baixar]({doc.badge_url})]({doc.download_url}) |"
        )
    return "\n".join(rows)


def update_readme_file(table_content: str) -> None:
    if not README_PATH.exists():
        raise FileNotFoundError(f"Arquivo {README_PATH} não encontrado.")

    content = README_PATH.read_text(encoding="utf-8")
    block = f"{TAG_START}\n{table_content}\n{TAG_END}"

    if TAG_START in content and TAG_END in content:
        pattern = re.compile(f"{re.escape(TAG_START)}.*?{re.escape(TAG_END)}", re.DOTALL)
        updated_content = pattern.sub(block, content)
    else:
        anchor = "## 🔗 Links Úteis"
        section = (
            f"## 🏢 Documentos por Empresa (companies)\n\n"
            f"Documentos customizados para processos seletivos específicos:\n\n"
            f"{block}\n\n---\n\n{anchor}"
        )
        updated_content = content.replace(anchor, section) if anchor in content else f"{content}\n\n{section}\n"

    README_PATH.write_text(updated_content, encoding="utf-8")


def main() -> None:
    documents = collect_company_documents()
    table = build_markdown_table(documents)
    update_readme_file(table)
    print("README.md atualizado com sucesso.")


if __name__ == "__main__":
    main()
