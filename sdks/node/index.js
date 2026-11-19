'use strict';

/**
 * b4n1-net SDK — sovereign transport, Node wrapper.
 *
 * The package ships the engine for each supported platform under `bin/` and
 * resolves the one that matches this machine. Everything else is a thin,
 * typed-by-convention call into that binary: the SDK never reimplements the
 * wire protocol, so a fix in the engine fixes every language at once.
 *
 * Override the engine: B4N1NET_BIN_PATH=/path/to/b4n1net
 */

const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const BINARIES = {
  'linux-x64': 'b4n1net-linux-amd64',
  'linux-arm64': 'b4n1net-linux-arm64',
  'darwin-x64': 'b4n1net-macos-x64',
  'darwin-arm64': 'b4n1net-macos-arm64',
  'win32-x64': 'b4n1net-windows-amd64.exe',
};

function platformBinaryName() {
  return BINARIES[`${process.platform}-${process.arch}`] || null;
}

/** Absolute path of the engine, or null when this platform is not bundled. */
function getBinary() {
  const override = process.env.B4N1NET_BIN_PATH;
  if (override && fs.existsSync(override)) return override;

  const name = platformBinaryName();
  if (name) {
    const bundled = path.join(__dirname, 'bin', name);
    if (fs.existsSync(bundled)) return bundled;
  }
  return null;
}

/** Run the engine and return { status, stdout, stderr }. Throws when absent. */
function run(args, options = {}) {
  const binary = getBinary();
  if (!binary) {
    throw new Error(
      'b4n1-net engine not found for this platform. Set B4N1NET_BIN_PATH.'
    );
  }
  const result = spawnSync(binary, args, {
    encoding: 'utf8',
    timeout: (options.timeoutSeconds || 30) * 1000,
  });
  if (result.error) throw result.error;
  return { status: result.status, stdout: result.stdout || '', stderr: result.stderr || '' };
}

/** Trimmed stdout — the shape every verb prints. */
function text(args) {
  const r = run(args);
  return (r.stdout || r.stderr).trim();
}

class NetClient {
  constructor(binaryPath) {
    this.binary = binaryPath || getBinary();
    if (!this.binary) {
      throw new Error(
        'b4n1-net engine not found. Set B4N1NET_BIN_PATH or install the binary.'
      );
    }
  }

  version() { return text(['--version']); }
  help() { return text(['help']); }
  licenses() { return text(['licenses']); }
  status(json = false) { return text(json ? ['status', '--json'] : ['status']); }
  demo(json = false) { return text(json ? ['demo', '--json'] : ['demo']); }
  docs(section) {
    return text(section ? ['docs', '--section', section] : ['docs']);
  }
  serve(addr, secret, json = false) {
    const args = ['serve', '--addr', addr];
    if (secret) args.push('--secret', secret);
    if (json) args.push('--json');
    return run(args);
  }
  send(addr, secret, message, json = false) {
    const args = ['send', '--addr', addr];
    if (secret) args.push('--secret', secret);
    if (message) args.push('--message', message);
    if (json) args.push('--json');
    return run(args);
  }
  start(addr, secret, json = false) {
    const args = ['start'];
    if (addr) args.push('--addr', addr);
    if (secret) args.push('--secret', secret);
    if (json) args.push('--json');
    return run(args);
  }
  stop(json = false) { return run(json ? ['stop', '--json'] : ['stop']); }
}

module.exports = { NetClient, getBinary, run, SDK_VERSION: "0.4.1" };
