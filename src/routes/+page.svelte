<script lang="ts"  src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.3.0/math.js" >
import Markdown from 'svelte-markdown';
import { parse, evaluate, derivative } from 'mathjs';
import { clipboard } from '@skeletonlabs/skeleton';
import { Stepper, Step } from '@skeletonlabs/skeleton';
import { setInitialClassState } from '@skeletonlabs/skeleton';
import { LightSwitch } from '@skeletonlabs/skeleton';
import { ConicGradient } from '@skeletonlabs/skeleton';
import type { ConicStop } from '@skeletonlabs/skeleton';
import { InputChip } from '@skeletonlabs/skeleton';
import { onMount } from 'svelte';
import { createEventDispatcher } from 'svelte';	
import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';

const dispatch = createEventDispatcher();

function onStepHandler(e: {detail: {state: {current: number, total: number}, step: number}}): void {
	console.log('event:step', e);
}
function onCompleteHandler(e: Event): void { console.log('event:complete', e); }
let searchTerm = '';
	let isDarkMode = false;
	function search() {
	  console.log('Ricerca:', searchTerm);
	}
	function toggleTheme() {
	  isDarkMode = !isDarkMode;
	  document.body.classList.toggle('dark');
	}
  let ShowStepper = true;
	let functioz = "";
	let currentMessage = '';
	let currentX = '';
	let derivatamath = '';
	let derivatamathLeft = '';
	let derivatamathRight = '';	
	let x = '';
	let graph = false;
	
function showGraph(){
	if (graph==false){
		graph = true;
		const desmosIframe = document.querySelector('#desmos-iframe');
		const desmosURL = `https://www.desmos.com/calculator?lang=en&new1=${encodeURIComponent(currentMessage)}`;
   		desmosIframe.src = desmosURL;
	} else{
		graph = false;
	}
}

function calculateDerivative() {
 derivatamath = '';
 derivatamathLeft = '';
 derivatamathRight = '';
 try {
    const parsedExpression = parse(currentMessage);

    derivatamath = derivative(parsedExpression, 'x').toString();
    
    const evalLeft = evaluate(derivatamath, { x });

    const evalRight = evaluate(derivatamath, { x, delta: 0.00001 });

    derivatamathLeft = evalLeft;
    derivatamathRight = evalRight;
 } catch (error) {
    derivatamath = 'Errore nel calcolo della derivata: ' + error.message;
 }
}

	function Xvalue(){
		x= currentX;
	}
	function StepperStat() {
		ShowStepper = false;

		function onCompleteHandler(e: Event): void {
			console.log("event:complete", e);
			showStepper = false;
		}
	}
	
</script>

{#if ShowStepper == true}
	{#each [0] as item}
		<Stepper on:complete={onCompleteHandler} on:complete={StepperStat}>
			<Step>
				<svelte:fragment slot="header">Get Started!</svelte:fragment>
				Function_dev helps you solve functions.
			</Step>
			<Step stepTerm="Complete">
				<svelte:fragment slot="header">Insert function</svelte:fragment>
				Just insert your function.
			</Step>
		</Stepper>
	{/each}
{/if}
<br />
		  <br />
<div class="input-group input-group-divider grid-cols-[auto_1fr_auto] rounded-container-token">
	<button class="input-group-shim">f(x)=</button>
	<textarea
		bind:value={currentMessage}
		class="bg-transparent border-0 ring-0"
		name="prompt"
		id="prompt"
		placeholder="Enter any function..."
		rows="1"
	/>
	<button class="variant-filled-primary" on:click={calculateDerivative}>solve</button>
	
</div>
<br />
<div class="input-group input-group-divider grid-cols-[auto_1fr_auto] rounded-container-token">
	<button class="input-group-shim">x₀=</button>
	<textarea
		bind:value={currentX}
		class="bg-transparent border-0 ring-0"
		name="prompt"
		id="prompt"
		placeholder="Enter any function..."
		rows="1"
	/>
	<button class="variant-filled-primary" on:click={Xvalue}>add</button>
	
</div>
<br />  
<Accordion autocollapse>

	<AccordionItem open>
		<svelte:fragment slot="lead"><strong>Derivative</strong></svelte:fragment>
		<svelte:fragment slot="summary"><strong>f'(x)=</strong></svelte:fragment>
		<svelte:fragment slot="content"><p>{derivatamath}</p><button type="button" class="btn variant-filled" on:click={showGraph}>Show graph</button>
{#if graph==true}
 <center> <iframe  src="https://www.desmos.com/calculator?lang=en"  width="800" height="500" style="border: 4px solid #ccc" frameborder=10></iframe></center>
{/if}

</svelte:fragment>
	</AccordionItem>
	<AccordionItem>
		<svelte:fragment slot="lead"><strong>Right Derivative</strong></svelte:fragment>
		<svelte:fragment slot="summary"><strong>f'+(x)=</strong></svelte:fragment>
		<svelte:fragment slot="content">{derivatamathRight}</svelte:fragment>
	</AccordionItem>
		<AccordionItem open>
		<svelte:fragment slot="lead"><strong>Left Derivative</strong></svelte:fragment>
		<svelte:fragment slot="summary"><strong>f'-(x)=</strong></svelte:fragment>
		<svelte:fragment slot="content"><p>{derivatamathLeft}</p></svelte:fragment>
	</AccordionItem>
</Accordion>

<p>{currentX}</p>
<p>{x}</p>
