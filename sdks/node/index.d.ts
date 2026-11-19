export declare const SDK_VERSION: string;

export interface RunResult {
  status: number | null;
  stdout: string;
  stderr: string;
}

export declare function getBinary(): string | null;
export declare function run(args: string[], options?: { timeoutSeconds?: number }): RunResult;

export declare class NetClient {
  constructor(binaryPath?: string);
  binary: string;
  version(): string;
  help(): string;
  licenses(): string;
  status(json?: boolean): string;
  demo(json?: boolean): string;
  docs(section?: string): string;
  serve(addr: string, secret?: string, json?: boolean): RunResult;
  send(addr: string, secret?: string, message?: string, json?: boolean): RunResult;
  start(addr?: string, secret?: string, json?: boolean): RunResult;
  stop(json?: boolean): RunResult;
}
