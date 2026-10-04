#!/usr/bin/env node
// Instalador das ExpertSA Skills para o Google Antigravity.
// Uso: npx github:dbadaniel/ExpertSA-Skills [skill...] [--project | --legacy | --cli | --dir <pasta>] [--list]
'use strict';
const fs = require('fs');
const path = require('path');
const os = require('os');

const REPO_ROOT = path.resolve(__dirname, '..');
const HOME = os.homedir();
const TARGETS = {
  global: { dir: path.join(HOME, '.gemini', 'config', 'skills'), label: 'global (Antigravity 2.0 e IDE)' },
  legacy: { dir: path.join(HOME, '.gemini', 'antigravity', 'skills'), label: 'global legado (Antigravity IDE antigo)' },
  cli: { dir: path.join(HOME, '.gemini', 'antigravity-cli', 'skills'), label: 'global (Antigravity CLI)' },
  project: { dir: path.join(process.cwd(), '.agents', 'skills'), label: 'deste projeto' },
};

function availableSkills() {
  return fs.readdirSync(REPO_ROOT, { withFileTypes: true })
    .filter((d) => d.isDirectory() && !d.name.startsWith('.') && fs.existsSync(path.join(REPO_ROOT, d.name, 'SKILL.md')))
    .map((d) => d.name);
}

function description(skill) {
  const md = fs.readFileSync(path.join(REPO_ROOT, skill, 'SKILL.md'), 'utf8');
  const m = md.match(/^description:\s*(.+)$/m);
  return m ? m[1].trim().slice(0, 110) + (m[1].length > 110 ? '…' : '') : '';
}

function help() {
  console.log(`
ExpertSA Skills — instalador para Google Antigravity

  npx github:dbadaniel/ExpertSA-Skills                 instala todas as skills (global)
  npx github:dbadaniel/ExpertSA-Skills elementor-wsp-mcp   instala só essa skill

Opções:
  --project      instala em ./.agents/skills (só este projeto)
  --legacy       instala em ~/.gemini/antigravity/skills (IDE antigo)
  --cli          instala em ~/.gemini/antigravity-cli/skills (Antigravity CLI)
  --dir <pasta>  instala numa pasta específica
  --list         lista as skills disponíveis
  --help         mostra esta ajuda

Rodar de novo atualiza a skill para a versão mais recente.
`);
}

function main() {
  const args = process.argv.slice(2);
  if (args.includes('--help') || args.includes('-h')) return help();

  const skills = availableSkills();
  if (args.includes('--list')) {
    console.log('\nSkills disponíveis:\n');
    for (const s of skills) console.log(`  ${s}\n    ${description(s)}\n`);
    return;
  }

  let target = TARGETS.global;
  const dirIdx = args.indexOf('--dir');
  if (dirIdx !== -1) {
    if (!args[dirIdx + 1]) { console.error('Erro: --dir precisa de um caminho.'); process.exit(1); }
    target = { dir: path.resolve(args[dirIdx + 1]), label: 'pasta escolhida' };
  } else if (args.includes('--project')) target = TARGETS.project;
  else if (args.includes('--legacy')) target = TARGETS.legacy;
  else if (args.includes('--cli')) target = TARGETS.cli;

  const requested = args.filter((a, i) => !a.startsWith('-') && args[i - 1] !== '--dir');
  const unknown = requested.filter((s) => !skills.includes(s));
  if (unknown.length) {
    console.error(`Skill não encontrada: ${unknown.join(', ')}\nDisponíveis: ${skills.join(', ')}`);
    process.exit(1);
  }
  const toInstall = requested.length ? requested : skills;

  fs.mkdirSync(target.dir, { recursive: true });
  console.log(`\nInstalando em ${target.dir} (${target.label}):\n`);
  for (const s of toInstall) {
    const dest = path.join(target.dir, s);
    const existed = fs.existsSync(dest);
    fs.rmSync(dest, { recursive: true, force: true });
    fs.cpSync(path.join(REPO_ROOT, s), dest, { recursive: true });
    console.log(`  ✓ ${s} ${existed ? '(atualizada)' : '(instalada)'}`);
  }

  // Aviso de cópia duplicada no caminho legado, que o IDE também lê.
  if (target === TARGETS.global) {
    const dups = toInstall.filter((s) => fs.existsSync(path.join(TARGETS.legacy.dir, s)));
    if (dups.length) {
      console.log(`\n  Atenção: também existe uma cópia antiga em ${TARGETS.legacy.dir}`);
      console.log(`  (${dups.join(', ')}). Apague essa pasta para o Antigravity não carregar a versão velha.`);
    }
  }

  console.log('\nPronto. Reinicie o Antigravity (ou abra uma conversa nova) para carregar as skills.');
  if (toInstall.includes('elementor-wsp-mcp')) {
    console.log('Lembre de conectar o WSP MCP no Antigravity: veja o README da skill.\n');
  }
}

main();
