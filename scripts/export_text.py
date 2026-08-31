#!/usr/bin/env python3
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
RESUME_DIR = REPO_ROOT / "resume"

LATEX_ACCENTS: Dict[str, str] = {
    r"\~{a}": "ã",
    r"\~{A}": "Ã",
    r"\~{o}": "õ",
    r"\~{O}": "Õ",
    r"\'{a}": "á",
    r"\'{e}": "é",
    r"\'{i}": "í",
    r"\'{o}": "ó",
    r"\'{u}": "ú",
    r"\'{c}": "ç",
    r"\'{A}": "Á",
    r"\'{E}": "É",
    r"\'{I}": "Í",
    r"\'{O}": "Ó",
    r"\'{U}": "Ú",
    r"\'{C}": "Ç",
    r"\^{a}": "â",
    r"\^{e}": "ê",
    r"\^{o}": "ô",
    r"\`{a}": "à",
    r"\`{A}": "À",
    r"\&": "&",
    r"\$": "$",
    r"\%": "%",
    r"\_": "_",
    r"\#": "#",
    r"--": "–",
    r"---": "—",
    r"``": '"',
    r"''": '"',
}


def unescape_latex(text: str) -> str:
    cleaned = text
    for latex_seq, char in LATEX_ACCENTS.items():
        cleaned = cleaned.replace(latex_seq, char)
    return cleaned


def extract_braced_group(text: str, start_index: int) -> Tuple[Optional[str], int]:
    idx = text.find("{", start_index)
    if idx == -1:
        return None, len(text)

    depth = 1
    cursor = idx + 1
    while cursor < len(text) and depth > 0:
        if text[cursor] == "{":
            depth += 1
        elif text[cursor] == "}":
            depth -= 1
        cursor += 1

    if depth == 0:
        return text[idx + 1 : cursor - 1], cursor
    return None, len(text)


def extract_command_args(text: str, command_pos: int, arg_count: int) -> Tuple[List[str], int]:
    args: List[str] = []
    cursor = command_pos
    for _ in range(arg_count):
        arg, next_pos = extract_braced_group(text, cursor)
        if arg is None:
            break
        args.append(arg)
        cursor = next_pos
    return args, cursor


def clean_text(raw: str) -> str:
    text = unescape_latex(raw)

    while True:
        match = re.search(r"\\href\b", text)
        if not match:
            break
        args, end_idx = extract_command_args(text, match.end(), 2)
        if len(args) == 2:
            url, label = args[0], clean_text(args[1])
            replacement = f"{label} ({url})" if url and not url.startswith("mailto:") else label
            text = text[: match.start()] + replacement + text[end_idx:]
        else:
            break

    while True:
        match = re.search(r"\\(textbf|textit|emph|textsc|small|Huge|huge|large|Large)\b", text)
        if not match:
            break
        cmd = match.group(1)
        args, end_idx = extract_command_args(text, match.end(), 1)
        if len(args) == 1:
            replacement = clean_text(args[0])
            text = text[: match.start()] + replacement + text[end_idx:]
        else:
            text = text[: match.start()] + text[match.end() :]

    text = re.sub(r"\\textbullet\s*", "", text)
    text = re.sub(r"\\vspace\{[^}]*\}", "", text)
    text = re.sub(r"\\\s*", " ", text)
    text = re.sub(r"[{}\\]", "", text)
    text = text.replace("$|$", "|").replace("$", "")
    return re.sub(r"[ \t]+", " ", text).strip()


def parse_resume(tex_path: Path) -> str:
    content = tex_path.read_text(encoding="utf-8", errors="ignore")
    output_lines: List[str] = []

    header_match = re.search(r"\\begin\{center\}(.*?)\\end\{center\}", content, re.DOTALL)
    if header_match:
        header_text = header_match.group(1)
        name_match = re.search(r"\\Huge\s*([^}\\]+)", header_text)
        name = name_match.group(1).strip() if name_match else "GABRIEL FRIGO"

        output_lines.append("=" * 60)
        output_lines.append(clean_text(name).upper())
        output_lines.append("=" * 60)

        for line in header_text.splitlines():
            cleaned = clean_text(line)
            if cleaned and not cleaned.upper() == clean_text(name).upper():
                output_lines.append(cleaned)
        output_lines.append("")

    sections = list(re.finditer(r"\\section\{([^}]+)\}", content))

    for idx, match in enumerate(sections):
        title = match.group(1)
        start_pos = match.end()
        end_pos = sections[idx + 1].start() if idx + 1 < len(sections) else len(content)
        sec_content = content[start_pos:end_pos]

        output_lines.append(f"\n--- {clean_text(title).upper()} ---")

        subheadings_iter = list(re.finditer(r"\\resumeSubheading\b", sec_content))
        if subheadings_iter:
            for s_idx, s_match in enumerate(subheadings_iter):
                args, end_cmd = extract_command_args(sec_content, s_match.end(), 4)
                if len(args) == 4:
                    t, d, r, loc = [clean_text(a) for a in args]
                    output_lines.append(f"\n• {t} | {d}")
                    if r or loc:
                        role_loc = f"  {r}" + (f" - {loc}" if loc else "")
                        output_lines.append(role_loc)

                block_end = (
                    subheadings_iter[s_idx + 1].start()
                    if s_idx + 1 < len(subheadings_iter)
                    else len(sec_content)
                )
                block_content = sec_content[end_cmd:block_end]

                for item_match in re.finditer(r"\\resumeItem\b", block_content):
                    item_args, _ = extract_command_args(block_content, item_match.end(), 1)
                    if item_args:
                        output_lines.append(f"    - {clean_text(item_args[0])}")
        else:
            items = list(re.finditer(r"\\resumeItem\b", sec_content))
            if items:
                for item_match in items:
                    item_args, _ = extract_command_args(sec_content, item_match.end(), 1)
                    if item_args:
                        output_lines.append(f"• {clean_text(item_args[0])}")
            else:
                summary_cleaned = clean_text(sec_content)
                if summary_cleaned:
                    output_lines.append(summary_cleaned)

    return "\n".join(output_lines).strip() + "\n"


def main() -> None:
    for src in (RESUME_DIR / "resume-pt.tex", RESUME_DIR / "resume-en.tex"):
        if src.exists():
            dst = src.with_suffix(".txt")
            dst.write_text(parse_resume(src), encoding="utf-8")
            print(f"Exportado: {dst.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
