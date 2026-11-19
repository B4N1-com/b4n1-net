<?php

declare(strict_types=1);

/**
 * b4n1-net SDK — sovereign transport, PHP wrapper.
 *
 * The package ships the engine for each supported platform under bin/ and
 * resolves the one that matches this machine. Every call is a thin spawn into
 * that binary: the SDK never reimplements the wire protocol.
 *
 *   require 'vendor/autoload.php';
 *   $client = new B4n1Net\Client();
 *   echo $client->version();
 *
 * Override the engine with B4N1NET_BIN_PATH.
 */

namespace B4n1Net;

final class Client
{
    public const SDK_VERSION = '0.4.1';

    private const BINARIES = [
        'Linux-x86_64' => 'b4n1net-linux-amd64',
        'Linux-aarch64' => 'b4n1net-linux-arm64',
        'Darwin-x86_64' => 'b4n1net-macos-x64',
        'Darwin-arm64' => 'b4n1net-macos-arm64',
    ];

    private string $binary;

    public function __construct(?string $binaryPath = null)
    {
        $binary = $binaryPath ?? self::resolveBinary();
        if ($binary === null || !is_executable($binary)) {
            throw new \RuntimeException(
                'b4n1-net engine not found. Set B4N1NET_BIN_PATH.'
            );
        }
        $this->binary = $binary;
    }

    /** Absolute path of the engine, or null when this platform is not bundled. */
    public static function resolveBinary(): ?string
    {
        $override = getenv('B4N1NET_BIN_PATH');
        if ($override !== false && $override !== '' && is_executable($override)) {
            return $override;
        }

        $key = PHP_OS_FAMILY . '-' . php_uname('m');
        $name = self::BINARIES[$key] ?? null;
        if ($name === null) {
            return null;
        }
        $bundled = dirname(__DIR__) . '/bin/' . $name;
        return is_executable($bundled) ? $bundled : null;
    }

    public function version(): string { return $this->text('--version'); }
    public function help(): string { return $this->text('help'); }
    public function licenses(): string { return $this->text('licenses'); }
    public function status(bool $json = false): string { return $this->text('status', ...($json ? ['--json'] : [])); }
    public function demo(bool $json = false): string { return $this->text('demo', ...($json ? ['--json'] : [])); }
    public function docs(?string $section = null): string
    {
        return $this->text('docs', ...($section !== null ? ['--section', $section] : []));
    }

    public function serve(string $addr, ?string $secret = null, bool $json = false): string
    {
        $args = ['serve', '--addr', $addr];
        if ($secret !== null) { $args = [...$args, '--secret', $secret]; }
        if ($json) { $args[] = '--json'; }
        return $this->text(...$args);
    }

    public function send(string $addr, ?string $secret = null, ?string $message = null, bool $json = false): string
    {
        $args = ['send', '--addr', $addr];
        if ($secret !== null) { $args = [...$args, '--secret', $secret]; }
        if ($message !== null) { $args = [...$args, '--message', $message]; }
        if ($json) { $args[] = '--json'; }
        return $this->text(...$args);
    }

    public function start(?string $addr = null, ?string $secret = null, bool $json = false): string
    {
        $args = ['start'];
        if ($addr !== null) { $args = [...$args, '--addr', $addr]; }
        if ($secret !== null) { $args = [...$args, '--secret', $secret]; }
        if ($json) { $args[] = '--json'; }
        return $this->text(...$args);
    }

    public function stop(bool $json = false): string { return $this->text('stop', ...($json ? ['--json'] : [])); }

    /** @param string ...$args */
    private function text(string ...$args): string
    {
        $command = escapeshellarg($this->binary);
        foreach ($args as $arg) {
            $command .= ' ' . escapeshellarg($arg);
        }
        $output = [];
        $status = 0;
        exec($command . ' 2>&1', $output, $status);
        return trim(implode("\n", $output));
    }
}
