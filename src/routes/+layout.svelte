<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import { LightSwitch } from '@skeletonlabs/skeleton';
	
</script>

<AppShell>
	<svelte:fragment slot="header">
		
		<AppBar>
			<svelte:fragment slot="lead">
				<strong class="text-xl uppercase">Function_dev (BETA)</strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
							
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://github.com/Mishikiari/FunctionDev"
					target="_blank"
					rel="noreferrer"
				>
					GitHub
				</a>
				<LightSwitch />
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>

	<slot />
</AppShell>
