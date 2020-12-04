function create_stream(url, target) {
  const source = new EventSource(url);
  source.onopen = () => console.log("Stream opened!");
  source.onerror = console.error;
  source.onmessage = evt => target.textContent = `${evt.data}`;
  return source;
}
