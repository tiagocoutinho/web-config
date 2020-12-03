var target = document.getElementById("target");
var source = new EventSource("stream/");
source.onopen = () => console.log("Stream opened!");
source.onerror = console.error;
source.onmessage = evt => target.textContent = `${evt.data}`;
