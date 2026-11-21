import { readFileSync, writeFileSync } from 'node:fs';

const json = path => JSON.parse(readFileSync(new URL(path, import.meta.url), 'utf8'));
const conventions = json('./data/conventions.json');
const sources = json('../data/references.json');
const letters = json('./data/letters.json');
const glossary = json('./data/glossary.json');
const presets = [
  ...json('../data/examples.json').map(example => ({ kind: 'attested', ...example })),
  ...json('./data/teaching.json').map(example => ({ kind: 'constructed', ...example })),
];
const data = { conventions, sources, letters, glossary, presets };
const output = '// Generated from the research and teaching data. Run node build-data.mjs.\n'
  + 'globalThis.RomanResearch = ' + JSON.stringify(data, null, 2) + ';\n';
const destination = new URL('./data/research.js', import.meta.url);
if (process.argv.includes('--check')) {
  if (readFileSync(destination, 'utf8') !== output) {
    throw new Error('Run node build-data.mjs to update the browser data.');
  }
} else {
  writeFileSync(destination, output);
}
