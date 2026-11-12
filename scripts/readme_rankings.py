"""Generate bilingual README previews and self-contained SVGs, without network I/O."""
from html import escape
import unicodedata
import xml.etree.ElementTree as ET

START = "<!-- rankings-preview:start -->"
END = "<!-- rankings-preview:end -->"
ASSETS = "assets/rankings"
LANGUAGES = {"en": "README.md", "zh-CN": "README.zh-CN.md"}
COLORS = {
    "light": {"background": "#ffffff", "text": "#24292f", "muted": "#57606a", "border": "#d0d7de", "track": "#eef2f6"},
    "dark": {"background": "#0d1117", "text": "#e6edf3", "muted": "#9da7b1", "border": "#30363d", "track": "#21262d"},
}
ACCENTS = {"x": ("#0969da", "#58a6ff"), "github": ("#8250df", "#bc8cff"),
           "bilibili": ("#087f8c", "#39c5cf"), "youtube": ("#b42318", "#ff7b72"),
           "readers": ("#1a7f37", "#3fb950")}


def tr(language, en, zh):
    return zh if language == "zh-CN" else en


def md_label(value):
    return escape(str(value), quote=False).replace("\\", "\\\\").replace("[", "&#91;").replace("]", "&#93;").replace("|", "&#124;").replace("\n", " ")


def md_link(label, url):
    return f"[{md_label(label)}](<{url}>)"


def wrapped(value, width, size):
    """Conservative font-width estimate; preserve every character, including CJK."""
    lines, line, used = [], "", 0
    for char in str(value):
        unit = 1 if unicodedata.east_asian_width(char) in {"W", "F"} else (0.3 if char.isspace() else 0.62)
        if line and (used + unit) * size > width:
            # Prefer word boundaries, while still supporting long IDs and CJK.
            cut = line.rfind(" ")
            if cut > len(line) // 2:
                lines.append(line[:cut])
                line = line[cut + 1:]
                used = sum(1 if unicodedata.east_asian_width(c) in {"W", "F"} else (0.3 if c.isspace() else 0.62) for c in line)
            else:
                lines.append(line)
                line, used = "", 0
        line += char
        used += unit
    if line:
        lines.append(line)
    return lines or [""]


def svg_card(title, subtitle, rows, empty, language, theme, mobile, accent):
    width = 480 if mobile else 840
    palette = COLORS[theme]
    color = ACCENTS[accent][theme == "dark"]
    content = []

    def text(x, y, value, size=20, fill=None, weight=400, anchor="start"):
        content.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill or palette["text"]}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>')

    text(24, 39, title, 26, weight=650)
    y = 66
    for line in wrapped(subtitle, width - 48, 16):
        text(24, y, line, 16, palette["muted"])
        y += 22
    y += 20
    if rows:
        maximum = max(row["value"] for row in rows)
        for row in rows:
            text(24, y, str(row["rank"]).zfill(2), 19, palette["muted"], 600)
            text(width - 24, y, f'{row["value"]:,}', 22, weight=650, anchor="end")
            for line in wrapped(row["label"], width - 66 - 24 - (135 if mobile else 160), 20):
                text(66, y, line, weight=550)
                y += 26
            bar_y, bar_width = y - 10, width - 90
            content.append(f'<rect x="66" y="{bar_y}" width="{bar_width}" height="8" rx="4" fill="{palette["track"]}"/>')
            if maximum and row["value"]:
                content.append(f'<rect x="66" y="{bar_y}" width="{bar_width * row["value"] / maximum:.2f}" height="8" rx="4" fill="{color}"/>')
            y += 22
            for line in wrapped(row.get("note", ""), width - 90, 15):
                if line:
                    text(66, y, line, 15, palette["muted"])
                    y += 21
            y += 26
        height = y - 12
    else:
        heading, detail = empty
        for line in wrapped(heading, width - 48, 22):
            text(24, y, line, 22, weight=600)
            y += 29
        y += 5
        for line in wrapped(detail, width - 48, 17):
            text(24, y, line, 17, palette["muted"])
            y += 24
        height = y + 8
    description = "; ".join(f'{r["rank"]}. {r["label"]}: {r["value"]:,}. {r.get("note", "")}' for r in rows) if rows else " ".join(empty)
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description" lang="{language}">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="description">{escape(subtitle + ". " + description)}</desc>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Noto Sans CJK SC",Arial,sans-serif}</style>',
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="{palette["background"]}" stroke="{palette["border"]}"/>',
        f'<rect x="1" y="8" width="5" height="{height - 16}" rx="2" fill="{color}"/>',
        *content, '</svg>', "",
    ])


def svg_pair(first, second, language, mobile):
    """Place compact cards beside each other, or stack them on narrow screens."""
    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    cards = [ET.fromstring(first), ET.fromstring(second)]
    heights = [int(card.attrib["height"]) for card in cards]
    gap = 16 if mobile else 24
    width = 480 if mobile else 480 * 2 + gap
    height = sum(heights) + gap if mobile else max(heights)
    root = ET.Element(f"{{{namespace}}}svg", {
        "width": str(width), "height": str(height), "viewBox": f"0 0 {width} {height}",
        "role": "img", "aria-labelledby": "title description", "lang": language,
    })
    ET.SubElement(root, f"{{{namespace}}}title", id="title").text = tr(language, "X and GitHub popularity", "X 与 GitHub 热度榜")
    ET.SubElement(root, f"{{{namespace}}}desc", id="description").text = tr(language, "Independent rankings and scales for each platform.", "各平台独立排名，横条使用各自的数值尺度。")
    for index, (prefix, card) in enumerate(zip(("x", "github"), cards)):
        for node in card.iter():
            if "id" in node.attrib:
                node.set("id", prefix + "-" + node.attrib["id"])
            if "aria-labelledby" in node.attrib:
                node.set("aria-labelledby", " ".join(prefix + "-" + name for name in node.attrib["aria-labelledby"].split()))
        card.set("x", "0" if mobile else str(index * (480 + gap)))
        card.set("y", str(heights[0] + gap) if mobile and index else "0")
        if not mobile:
            # Equal-height panels without stretching text or bars.
            card.set("height", str(height))
            card.set("viewBox", f"0 0 480 {height}")
            background, accent, *_ = card.findall(f"{{{namespace}}}rect")
            background.set("height", str(height - 1))
            accent.set("height", str(height - 16))
        root.append(card)
    return ET.tostring(root, encoding="unicode") + "\n"


def picture(stem, alt):
    prefix = f"{ASSETS}/{stem}"
    return "\n".join([
        '<picture>',
        f'  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="{prefix}-dark-mobile.svg">',
        f'  <source media="(max-width: 600px)" srcset="{prefix}-light-mobile.svg">',
        f'  <source media="(prefers-color-scheme: dark)" srcset="{prefix}-dark.svg">',
        f'  <img src="{prefix}-light.svg" alt="{escape(alt, quote=True)}" width="840">',
        '</picture>',
    ])


def observed(entry, language):
    stamp = entry.get("observed_at")
    stamp = stamp.replace("T", " ").removesuffix("Z") + " UTC" if stamp else tr(language, "Time unknown", "时间未知")
    status = entry.get("status", "unavailable")
    labels = {
        "ok": ("Fetched", "已采集"), "stale": ("Cached; refresh failed", "缓存；刷新失败"),
        "readme_snapshot": ("README snapshot", "README 快照"),
        "unavailable": ("Unavailable", "暂不可用"), "closed": ("Voting issue closed", "投票帖已关闭"),
    }
    return stamp + " · " + tr(language, *labels.get(status, (status, status)))


def source_label(entry, works, language):
    if len(entry["works"]) > 1:
        count = len(entry["works"])
        if entry["platform"] == "GitHub":
            name = entry["identity"].split("/")[-1]
            return name + tr(language, f" · shared by {count} works", f" · 共用仓库（{count} 件作品）")
        return tr(language, f"Shared video / post · {count} works", f"共用视频／帖子 · {count} 件作品")
    name = works[entry["works"][0]]["name"]
    notes = " ".join(entry.get("scope_notes", [])).lower()
    if "comparison" in notes or "overview" in notes:
        name += tr(language, " · overview / comparison", " · 总览／比较视频")
    return name


def replace_preview(readme, section):
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(START) > readme.index(END):
        raise ValueError("README must contain exactly one ordered pair of rankings-preview markers")
    before, remaining = readme.split(START)
    _, after = remaining.split(END)
    return before + START + "\n" + section + "\n" + END + after


def render_homepages(root, works, platform_rows, registry, votes, vote_rows):
    """Consume the same ordered rows as the full rankings; update only marked blocks."""
    assets, readmes = {}, {}
    for language, filename in LANGUAGES.items():
        verified = sum(work.get("audit", "").startswith("Verified /") for work in works.values())
        measured = sum(len(rows) for rows in platform_rows.values())
        lines = [tr(language, "## Rankings at a glance", "## 榜单速览"), "",
                 tr(language, f"**{len(works)} works** · **{verified} with verified code** · **{measured} measured sources**",
                    f"**{len(works)} 件作品** · **{verified} 件代码已核实** · **{measured} 个来源已有热度数据**"), "",
                 tr(language, "[Full popularity rankings](POPULARITY.md) · [Reader votes](COMMUNITY-RANKING.md) · [Ranking rules](RANKING-RULES.md)",
                    "[完整平台热度榜](POPULARITY.md) · [读者投票榜](COMMUNITY-RANKING.md) · [排名规则](RANKING-RULES.md)"), "",
                 tr(language, "### Platform popularity", "### 平台热度"), "",
                 tr(language, "Platforms rank independently by cumulative views or stars. Each shared source counts once. Dates belong to observations; cached values are not live. Missing data is not zero.",
                    "各平台按累计浏览量或 Star 独立排名，共用来源只计一次。图中日期为实际观测时间，缓存数值并非实时数据；缺失不计零。"), ""]

        def add_card(stem, title, subtitle, rows, empty, accent, show=True):
            for theme in COLORS:
                for mobile in (False, True):
                    suffix = "-mobile" if mobile else ""
                    path = f"{ASSETS}/{stem}-{theme}{suffix}.svg"
                    assets[path] = svg_card(title, subtitle, rows, empty, language, theme, mobile, accent)
            alt = title + ". " + subtitle + ". "
            alt += "; ".join(f'{r["rank"]}. {r["label"]}: {r["value"]:,}; {r.get("note", "")}' for r in rows) if rows else " ".join(empty)
            if show:
                lines.extend([picture(stem, alt), ""])
            return alt

        pair_alts, pair_links = [], []
        for platform, entries in platform_rows.items():
            if platform == "Bilibili":
                lines += ["<details>", "<summary>" + tr(language, "Bilibili and YouTube rankings", "展开 Bilibili、YouTube 榜单") + "</summary>", ""]
            primary = "stars" if platform == "GitHub" else "views"
            top = entries[:3]
            rows = [{"rank": rank, "label": source_label(entry, works, language), "value": entry["metrics"][primary], "note": observed(entry, language)}
                    for rank, (_, entry) in top]
            unit = tr(language, "Repository stars", "仓库 Star") if primary == "stars" else tr(language, "Source views", "来源浏览量")
            subtitle = unit + tr(language, f" · {len(entries)} measured sources", f" · {len(entries)} 个来源有数据")
            empty = (tr(language, "No measured sources yet", "暂无可用热度数据"),
                     tr(language, "Unmeasured sources remain in the catalog.", "尚未获得数据的作品仍保留在清单中。"))
            paired = platform in {"X", "GitHub"}
            alt = add_card(f"{platform.lower()}-{language}", platform + tr(language, " · Top 3", " · 前三条"), subtitle, rows, empty, platform.lower(), show=not paired)
            platform_links = [f"**{platform}**", ""] if paired else []
            for rank, (_, entry) in top:
                links = " · ".join(md_link(works[i]["name"], works[i]["url"]) for i in entry["works"])
                source = md_link(tr(language, "source", "来源"), entry["url"])
                count_unit = tr(language, "stars", "Star") if primary == "stars" else tr(language, "views", "次浏览")
                platform_links.append(f"- **{rank}.** {links} — {entry['metrics'][primary]:,} {count_unit} · {source}")
            platform_links += ["", md_link(tr(language, f"Full {platform} ranking", f"查看完整 {platform} 榜单"), f"POPULARITY.md#{platform.lower()}"), ""]
            if paired:
                pair_alts.append(alt)
                pair_links.extend(platform_links)
                if platform == "GitHub":
                    for theme in COLORS:
                        for mobile in (False, True):
                            suffix = "-mobile" if mobile else ""
                            first = assets[f"{ASSETS}/x-{language}-{theme}-mobile.svg"]
                            second = assets[f"{ASSETS}/github-{language}-{theme}-mobile.svg"]
                            assets[f"{ASSETS}/platforms-{language}-{theme}{suffix}.svg"] = svg_pair(first, second, language, mobile)
                    lines += [picture(f"platforms-{language}", " ".join(pair_alts)), "", *pair_links]
            else:
                lines.extend(platform_links)
        lines += ["</details>", "", tr(language, "Up to three sources per platform; equal values share a rank, with stable ordering within ties. Overview and comparison-video views belong to the whole video.",
                    "每个平台预览最多三条来源，同数值同名次，组内保持稳定顺序。总览或比较视频的播放量属于整段视频。"), "",
                  tr(language, "### Reader choice", "### 读者选择"), ""]

        status = votes.get("status", "not_initialized")
        top_votes = [(rank, work_id) for rank, (_, work_id) in vote_rows if votes["works"][work_id]["votes"] > 0][:5]
        if status in {"not_initialized", "unavailable"}:
            top_votes = []
        reader_rows = [{"rank": rank, "label": works[i]["name"], "value": votes["works"][i]["votes"]} for rank, i in top_votes]
        subtitle = tr(language, "Top 5 by reader votes · independent of platform popularity", "读者票数前五 · 独立于平台热度")
        if status == "not_initialized":
            empty = (tr(language, "Voting is not open yet", "尚未开放投票"),
                     tr(language, "Once enabled, support a work with a thumbs-up on its GitHub ballot comment.", "启用后，在作品的 GitHub 投票评论上点 👍。"))
        elif status == "unavailable":
            empty = (tr(language, "Vote totals are unavailable", "暂时无法获取票数"),
                     tr(language, "No successful observation yet; check the voting issue.", "尚无成功统计记录，可前往投票帖查看。"))
        elif status == "closed":
            empty = (tr(language, "Voting issue is closed", "投票帖已关闭"),
                     tr(language, "No positive votes in the saved observation.", "已保存的统计中暂无获得投票的作品。"))
        else:
            empty = (tr(language, "No votes in this snapshot yet", "当前快照中暂无作品获得投票"),
                     tr(language, "Support your favorite work in the GitHub voting issue.", "可前往 GitHub 投票帖支持喜欢的作品。"))
        add_card(f"readers-{language}", tr(language, "Reader choice", "读者选择"), subtitle, reader_rows, empty, "readers")
        if status != "not_initialized":
            lines += [tr(language, "Vote snapshot: ", "票数快照：") + observed(votes, language), ""]
        for rank, work_id in top_votes:
            entry = votes["works"][work_id]
            action = tr(language, "View ballot", "查看投票评论") if status == "closed" else tr(language, "Vote", "投票")
            lines.append(f"- **{rank}.** {md_link(works[work_id]['name'], works[work_id]['url'])} — **{entry['votes']:,}** 👍 · {md_link(action, entry['url'])}")
        if top_votes:
            lines.append("")
        if registry.get("issue_url"):
            lines += [md_link(tr(language, "View voting issue", "查看投票帖"), registry["issue_url"]), ""]
        lines += [tr(language, "[Full reader ranking](COMMUNITY-RANKING.md) · [Voting rules](RANKING-RULES.md)", "[完整读者榜](COMMUNITY-RANKING.md) · [投票规则](RANKING-RULES.md)"), "",
                  tr(language, "Only works with at least one vote appear here. Add 👍 to a work's designated bot comment; removing it withdraws the vote. One account can support multiple works.",
                     "这里仅展示至少获得一票的作品。在指定机器人评论上点 👍 即投票，取消即可撤票，每个账号可支持多个作品。")]
        # Validate both READMEs before writing any generated assets or marked sections.
        readmes[filename] = replace_preview((root / filename).read_text(), "\n".join(lines))
    for path, content in assets.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    for filename, content in readmes.items():
        (root / filename).write_text(content)
