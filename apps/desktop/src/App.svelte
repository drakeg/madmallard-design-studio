<script lang="ts">
let tool = $state("Select");
let zoom = $state(100);
const tools = ["Select", "Frame", "Rectangle", "Ellipse", "Text"];
</script>
<div class="app">
<header><strong>◆ Mad Mallard Design Studio</strong><span>Untitled Design · Sprint 0</span><button disabled>Export</button></header>
<nav aria-label="Design tools">{#each tools as t}<button class:active={tool===t} onclick={() => tool=t}>{t}</button>{/each}</nav>
<div class="workspace">
<aside><h3>Layers</h3><p>▤ Frame 1</p><p>▢ Rectangle 1</p><p>▤ Headline</p><h3>Assets</h3><p>Coming soon</p></aside>
<main><div class="artboard"><div class="shape"></div><h1>Design without limits.</h1><p>Your local-first creative workspace.</p></div></main>
<aside><h3>Properties</h3><p>Tool: {tool}</p><p>Zoom: {zoom}%</p><input aria-label="Zoom" type="range" min="25" max="200" bind:value={zoom}/><p>Interactive editing arrives in Sprint 1.</p></aside>
</div><footer>Rust + Tauri 2 + Svelte 5 · Local-first preview</footer>
</div>
<style>
:global(*){box-sizing:border-box}:global(body){margin:0;background:#171c26;color:#e7eaf0;font-family:system-ui,sans-serif}:global(button){background:#2c3444;border:1px solid #414c61;color:inherit;border-radius:6px;padding:8px 12px;cursor:pointer}.app{height:100vh;display:flex;flex-direction:column}header{display:flex;justify-content:space-between;align-items:center;padding:12px 20px;border-bottom:1px solid #3b4558}nav{display:flex;gap:8px;padding:10px 16px;border-bottom:1px solid #3b4558}.active{background:#4568d2}.workspace{flex:1;min-height:0;display:grid;grid-template-columns:210px 1fr 230px}aside{padding:18px;border-right:1px solid #3b4558;font-size:13px;color:#b7c1d1}aside:last-child{border-left:1px solid #3b4558;border-right:0}h3{text-transform:uppercase;letter-spacing:1px;font-size:12px}main{background:#242c39;display:grid;place-items:center;padding:25px}.artboard{background:#f8fafc;color:#141b2b;width:min(750px,100%);aspect-ratio:8/5;padding:12%;box-shadow:0 12px 45px #0007}.shape{width:75px;height:75px;border-radius:16px;background:#5378dc;transform:rotate(-12deg)}h1{font-size:clamp(24px,3vw,46px)}.artboard p{color:#667085}footer{padding:9px 16px;border-top:1px solid #3b4558;font-size:11px;color:#a9b4c5}
</style>