<script lang="ts">
  type Shape = { id: number; kind: 'Rectangle' | 'Ellipse'; x: number; y: number; width: number; height: number; color: string };
  let tool = $state<'Select' | 'Rectangle' | 'Ellipse'>('Select');
  let zoom = $state(100);
  let shapes = $state<Shape[]>([{ id: 1, kind: 'Rectangle', x: 100, y: 90, width: 140, height: 100, color: '#5378dc' }]);
  let selectedId = $state<number | null>(1);
  let nextId = 2;
  const tools = ['Select', 'Rectangle', 'Ellipse'] as const;
  const selected = $derived(shapes.find(s => s.id === selectedId));

  function addShape(kind: 'Rectangle' | 'Ellipse') {
    const id = nextId++;
    shapes.push({ id, kind, x: 70 + (id * 24) % 280, y: 60 + (id * 18) % 170, width: 130, height: 90, color: kind === 'Ellipse' ? '#e07c57' : '#5378dc' });
    selectedId = id;
    tool = 'Select';
  }
  function onCanvasClick(event: MouseEvent) {
    if (event.target !== event.currentTarget) return;
    if (tool !== 'Select') addShape(tool);
    else selectedId = null;
  }
  function onKeydown(event: KeyboardEvent) {
    if (!selected || event.target instanceof HTMLInputElement) return;
    const delta = event.shiftKey ? 10 : 1;
    if (event.key === 'ArrowLeft') selected.x -= delta;
    else if (event.key === 'ArrowRight') selected.x += delta;
    else if (event.key === 'ArrowUp') selected.y -= delta;
    else if (event.key === 'ArrowDown') selected.y += delta;
    else if (event.key === 'Delete' || event.key === 'Backspace') { shapes = shapes.filter(s => s.id !== selectedId); selectedId = null; }
    else return;
    event.preventDefault();
  }
</script>
<svelte:window onkeydown={onKeydown}/>
<div class="app">
  <header><strong>◆ Mad Mallard Design Studio</strong><span>Untitled Design · Sprint 1</span><button disabled>Export</button></header>
  <nav aria-label="Design tools">{#each tools as t}<button class:active={tool===t} onclick={() => tool=t}>{t}</button>{/each}</nav>
  <div class="workspace">
    <aside><h3>Layers</h3>{#each [...shapes].reverse() as shape (shape.id)}<button class:active={selectedId===shape.id} class="layer" onclick={() => {selectedId=shape.id;tool='Select';}}>{shape.kind} {shape.id}</button>{/each}<h3>Assets</h3><p>Coming soon</p></aside>
    <main><div class="viewport"><div class="artboard" role="presentation" onclick={onCanvasClick} style:transform={`scale(${zoom/100})`}>
      {#each shapes as shape (shape.id)}<button class="shape" class:selected={selectedId===shape.id} aria-label={`${shape.kind} ${shape.id}`} style:left={`${shape.x}px`} style:top={`${shape.y}px`} style:width={`${shape.width}px`} style:height={`${shape.height}px`} style:background={shape.color} style:border-radius={shape.kind==='Ellipse'?'50%':'4px'} onclick={(e) => {e.stopPropagation();selectedId=shape.id;tool='Select';}}></button>{/each}
    </div></div><p class="hint">Choose a shape tool and click the canvas to add it. Select a shape, then use arrow keys to move it.</p></main>
    <aside><h3>Properties</h3><p>Tool: {tool}</p><label for="zoom">Zoom: {zoom}%</label><input id="zoom" type="range" min="25" max="200" bind:value={zoom}/>{#if selected}<h3>Selected {selected.kind}</h3><label>X <input type="number" bind:value={selected.x}/></label><label>Y <input type="number" bind:value={selected.y}/></label><label>Width <input type="number" min="1" bind:value={selected.width}/></label><label>Height <input type="number" min="1" bind:value={selected.height}/></label><label>Fill <input type="color" bind:value={selected.color}/></label>{:else}<p>No selection</p>{/if}</aside>
  </div><footer>Rust + Tauri 2 + Svelte 5 · Interactive canvas prototype</footer>
</div>
<style>
:global(*){box-sizing:border-box}:global(body){margin:0;background:#171c26;color:#e7eaf0;font-family:system-ui,sans-serif}:global(button){background:#2c3444;border:1px solid #414c61;color:inherit;border-radius:6px;padding:8px 12px;cursor:pointer}:global(button:focus-visible){outline:2px solid #8fb5ff}.app{height:100vh;display:flex;flex-direction:column}header{display:flex;justify-content:space-between;align-items:center;padding:12px 20px;border-bottom:1px solid #3b4558}nav{display:flex;gap:8px;padding:10px 16px;border-bottom:1px solid #3b4558}.active{background:#4568d2}.workspace{flex:1;min-height:0;display:grid;grid-template-columns:210px minmax(0,1fr) 230px}aside{padding:18px;border-right:1px solid #3b4558;font-size:13px;color:#b7c1d1;overflow:auto}aside:last-child{border-left:1px solid #3b4558;border-right:0}h3{text-transform:uppercase;letter-spacing:1px;font-size:12px}.layer{display:block;width:100%;text-align:left;margin:6px 0}main{background:#242c39;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:auto;padding:25px}.viewport{width:720px;height:450px;display:grid;place-items:center;flex-shrink:0}.artboard{position:relative;background:#f8fafc;width:720px;height:450px;box-shadow:0 12px 45px #0007;transform-origin:center}.shape{position:absolute;border:2px solid transparent;padding:0}.shape.selected{outline:3px solid #3e9bff;outline-offset:3px}.hint{font-size:12px;color:#b7c1d1}aside label{display:block;margin:12px 0}aside input[type=number]{display:block;width:100%;padding:6px;background:#232b39;border:1px solid #64718a;border-radius:4px;color:white}footer{padding:9px 16px;border-top:1px solid #3b4558;font-size:11px;color:#a9b4c5}
</style>
