"use strict";
const $ = (id) => document.getElementById(id);
const state = {data: null, mode: "platform", platform: "X", query: "", category: "", pending: new Set(), polling: null};
const categories = {Games: "游戏", "Interactive worlds and simulations": "交互世界", "3D films and animations": "影片与动画"};
const statuses = {ok: "已读取", stale: "旧值 · 更新失败", unavailable: "暂无数据", readme_snapshot: "历史快照"};
const number = new Intl.NumberFormat("zh-CN");
const dateFormat = new Intl.DateTimeFormat("zh-CN", {timeZone: "Asia/Shanghai", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false});
const escape = (value) => String(value ?? "").replace(/[&<>"']/g, (c) => ({"&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"}[c]));
const formatDate = (value) => value && !Number.isNaN(Date.parse(value)) ? dateFormat.format(new Date(value)) : "尚无观测";
function safeLink(url, text, className = "") {
  try { const parsed = new URL(url); if (!['http:', 'https:'].includes(parsed.protocol)) return escape(text); }
  catch { return escape(text); }
  return `<a href="${escape(url)}" target="_blank" rel="noopener noreferrer" class="${className}">${escape(text)}</a>`;
}
function matches(work) {
  return (!state.category || work.category === state.category) &&
    (!state.query || `${work.name} ${work.creator}`.toLocaleLowerCase().includes(state.query.toLocaleLowerCase()));
}
function audit(work) {
  if (work.audit.startsWith("Verified")) return {text: "代码已核实", kind: "verified"};
  if (work.audit.startsWith("Pending")) return {text: "代码待核实", kind: "pending"};
  if (work.audit.includes("Outside")) return {text: "不在代码核验范围", kind: ""};
  return {text: "未纳入代码核验", kind: ""};
}
function workMarkup(work) {
  return `<div class="work">${safeLink(work.url, work.name, "work-name")}<div class="creator">${escape(work.creator)}</div><div class="category">${escape(categories[work.category] || work.category)}</div></div>`;
}
function withRanks(items) {
  const ordered = items.sort((a, b) => (b.score ?? -1) - (a.score ?? -1) || a.key.localeCompare(b.key, "en"));
  let last = null, rank = 0;
  return ordered.map((item, position) => {
    if (item.score === null) return {...item, rank: null};
    if (item.score !== last) rank = position + 1;
    last = item.score;
    return {...item, rank};
  });
}
function rankMarkup(rank) { return `<span class="rank-number ${rank && rank <= 3 ? 'top' : ''}">${rank ?? '—'}</span>`; }

function platformRows() {
  const data = state.data, primary = state.platform === "GitHub" ? "stars" : "views";
  const items = withRanks(Object.entries(data.sources).filter(([, s]) => s.platform === state.platform)
    .map(([key, source]) => ({key, source, score: Number.isInteger(source.metrics[primary]) ? source.metrics[primary] : null})));
  const filtered = items.filter(({source}) => source.works.some(id => matches(data.works[id])));
  $("result-count").textContent = `${filtered.length} / ${items.length} 个来源`;
  $("rows").innerHTML = filtered.map(({source, rank, score}) => {
    const works = source.works.map(id => data.works[id]);
    const shared = works.length > 1 ? `<span class="shared">${works.length} 个作品共用此来源</span>` : "";
    const metric = source.metrics;
    const secondary = primary === "stars" ? (metric.forks != null ? `${number.format(metric.forks)} Fork` : "") : (metric.likes != null ? `${number.format(metric.likes)} 赞` : "");
    const detail = Object.entries(metric).map(([key, value]) => `${escape({views: '浏览', likes: '赞', reposts: '转发', replies: '回复', comments: '评论', stars: 'Star', forks: 'Fork'}[key] || key)} ${number.format(value)}`).join(' / ');
    const sourceLabel = source.platform === "GitHub" ? source.identity : (source.scope_notes.join(" / ") || `${source.platform} 原始来源`);
    const status = statuses[source.status] || source.status;
    return `<tr><td>${rankMarkup(rank)}</td><td>${works.map(workMarkup).join("")}<div class="mobile-source">${safeLink(source.url, '查看来源')} · ${escape(status)}<br>${escape(formatDate(source.observed_at))}</div></td>
      <td>${safeLink(source.url, sourceLabel, 'source-link')}${shared}<div class="source-meta"><span class="status ${escape(source.status)}">${escape(status)}</span><time datetime="${escape(source.observed_at || '')}">${escape(formatDate(source.observed_at))}</time></div>
      <details class="source-detail"><summary>数据与核验</summary><p>${detail || '暂无观测数据'}</p>${works.map(w => `<p>${escape(w.name)}：${escape(audit(w).text)}</p>`).join('')}</details></td>
      <td class="score-cell"><div class="score">${score === null ? '—' : number.format(score)}</div><div class="score-label">${primary === 'stars' ? 'Star' : '浏览'}</div><div class="secondary-metrics">${secondary}</div></td></tr>`;
  }).join("");
  const unknown = filtered.filter(item => item.score === null).length;
  $("table-note").textContent = `同一帖子、视频或仓库只计一次。筛选保留原榜名次。${unknown ? `当前有 ${unknown} 个来源暂无数据，不列名次。` : ''}`;
  return filtered.length;
}

function voteRows() {
  const {works, local_votes: votes} = state.data;
  const mine = new Set(votes.mine);
  const items = withRanks(Object.entries(works).map(([id, work]) => ({key: work.name, id, work, score: votes.totals[id] || 0})));
  const filtered = items.filter(({work}) => matches(work));
  $("result-count").textContent = `${filtered.length} / ${items.length} 个作品`;
  $("rows").innerHTML = filtered.map(({id, work, score, rank}) => {
    const check = audit(work), selected = mine.has(id), busy = state.pending.has(id);
    return `<tr><td>${rankMarkup(score ? rank : null)}</td><td>${workMarkup(work)}<div class="mobile-source">${escape(check.text)}</div></td><td><span class="audit ${check.kind}">${escape(check.text)}</span><div class="source-meta">${safeLink(work.url, '查看作品', 'source-link')}</div></td><td class="score-cell"><span class="score">${number.format(score)}</span><span class="score-label"> 票</span><button class="vote-button ${selected ? 'selected' : ''}" data-vote="${id}" aria-label="${selected ? '撤回支持' : '支持'} ${escape(work.name)}" aria-pressed="${selected}" ${busy ? 'disabled' : ''}>${busy ? '正在保存…' : selected ? '已支持 · 撤回' : '👍 支持'}</button></td></tr>`;
  }).join("");
  $("table-note").textContent = "相同票数共享名次；尚无投票的作品暂不列名次。筛选保留原榜名次。测试票数保存在本机。";
  return filtered.length;
}

function render() {
  if (!state.data) return;
  const voting = state.mode === "votes";
  $("work-count").textContent = number.format(Object.keys(state.data.works).length);
  for (const [id, active] of [["platform-mode", !voting], ["vote-mode", voting]]) { $(id).classList.toggle("active", active); $(id).setAttribute("aria-pressed", active); }
  $("platforms").hidden = voting;
  $("vote-notice").hidden = !voting;
  $("refresh").hidden = voting;
  $("refresh").disabled = state.data.refresh.running;
  $("refresh").textContent = state.data.refresh.running ? "正在更新…" : "更新平台数据";
  $("board-title").textContent = voting ? "把一票投给喜欢的作品" : `${state.platform} 热度榜`;
  $("board-description").textContent = voting ? "支持可以撤回，票数随操作更新。尝试搜索一个你喜欢的作品。" : state.platform === 'GitHub' ? "按代码仓库累计 Star 排序，共用仓库的作品合并展示。" : `按所收录${state.platform === 'X' ? '帖子' : '视频'}的累计浏览量排序，表示来源传播量。`;
  $("meta-column").textContent = voting ? "代码核验" : "数据来源";
  $("score-column").textContent = voting ? "本地票数" : state.platform === 'GitHub' ? 'Star' : '浏览量';
  document.querySelectorAll('[data-platform]').forEach(button => {const active = button.dataset.platform === state.platform; button.classList.toggle('active', active); button.setAttribute('aria-pressed', active);});
  $("notice").textContent = voting ? '' : state.data.refresh.message || (state.platform === 'YouTube' ? 'YouTube 当前使用带日期的历史快照，更新按钮不会刷新此平台。' : '部分来源更新失败时显示旧值，请同时查看数据时间。');
  const count = voting ? voteRows() : platformRows();
  if (!count) $("rows").innerHTML = '<tr><td colspan="4" class="empty">没有匹配的作品。试试其他关键词，或选择“全部分类”。</td></tr>';
  schedulePolling();
}

async function api(path, body) {
  const response = await fetch(path, body === undefined ? {} : {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRF-Token': state.data.csrf}, body: JSON.stringify(body)});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || '操作未完成，请重试。');
  return data;
}
function toast(message) { $("toast").textContent = message; $("toast").hidden = false; clearTimeout(toast.timer); toast.timer = setTimeout(() => $("toast").hidden = true, 4000); }
function schedulePolling() {
  if (state.data.refresh.running && !state.polling) state.polling = setTimeout(async () => {
    state.polling = null;
    try { state.data = await api('/api/data'); render(); } catch { toast('服务暂时不可达，请确认本地服务仍在运行。'); }
  }, 2000);
  if (!state.data.refresh.running && state.polling) { clearTimeout(state.polling); state.polling = null; }
}
$("platform-mode").addEventListener('click', () => { state.mode = 'platform'; render(); });
$("vote-mode").addEventListener('click', () => { state.mode = 'votes'; render(); });
$("platforms").addEventListener('click', event => { const button = event.target.closest('[data-platform]'); if (button) { state.platform = button.dataset.platform; render(); }});
$("search").addEventListener('input', event => { state.query = event.target.value.trim(); render(); });
$("category").addEventListener('change', event => { state.category = event.target.value; render(); });
$("rows").addEventListener('click', async event => {
  const button = event.target.closest('[data-vote]');
  if (!button || state.pending.has(button.dataset.vote)) return;
  const id = button.dataset.vote, voted = !state.data.local_votes.mine.includes(id);
  state.pending.add(id); render();
  try { state.data = await api('/api/vote', {work_id: id, voted}); toast(voted ? '已支持，计入本地试投。' : '已撤回支持。'); }
  catch (error) { toast(error.message); }
  finally { state.pending.delete(id); render(); document.querySelector(`[data-vote="${id}"]`)?.focus({preventScroll: true}); }
});
$("refresh").addEventListener('click', async () => {
  $("refresh").disabled = true;
  try { state.data = await api('/api/refresh', {}); render(); }
  catch (error) { toast(error.message); $("refresh").disabled = false; }
});
api('/api/data').then(data => { state.data = data; render(); }).catch(error => {
  $("rows").innerHTML = '<tr><td colspan="4" class="empty">未能加载数据。请确认本地服务已启动，然后刷新页面。</td></tr>';
  $("notice").textContent = error.message;
});
