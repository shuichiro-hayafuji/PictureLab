<script>
    const ans = (async()=>{
        const res = await fetch(`/api`);
        return await res.json();
    })()
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<hr>
{#await ans}
    <p>...loading</p>
{:then data}
    <h3>{data.message}</h3>
    <h3>{data.status}</h3>
{:catch error}
    <p>An error occured!</p>
{/await}
