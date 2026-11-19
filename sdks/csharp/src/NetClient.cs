using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;

namespace B4n1Net;

/// <summary>
/// b4n1-net SDK — sovereign transport, .NET wrapper.
///
/// The package ships the engine for each supported platform under <c>bin/</c>
/// and resolves the one that matches this machine. Every call is a thin spawn
/// into that binary: the SDK never reimplements the wire protocol.
///
/// Override the engine with the <c>B4N1NET_BIN_PATH</c> environment variable.
/// </summary>
public sealed class NetClient
{
    /// <summary>SDK version; it tracks the engine release.</summary>
    public const string SdkVersion = "0.4.0";

    private readonly string _binary;

    public NetClient(string? binaryPath = null)
    {
        _binary = binaryPath ?? ResolveBinary()
            ?? throw new InvalidOperationException(
                "b4n1-net engine not found. Set B4N1NET_BIN_PATH.");
    }

    /// <summary>Absolute path of the engine, or null when this platform is not bundled.</summary>
    public static string? ResolveBinary()
    {
        var overridePath = Environment.GetEnvironmentVariable("B4N1NET_BIN_PATH");
        if (!string.IsNullOrEmpty(overridePath) && File.Exists(overridePath))
        {
            return overridePath;
        }

        var name = RuntimeInformation.IsOSPlatform(OSPlatform.Linux)
            ? (RuntimeInformation.ProcessArchitecture == Architecture.Arm64
                ? "b4n1net-linux-arm64"
                : "b4n1net-linux-amd64")
            : RuntimeInformation.IsOSPlatform(OSPlatform.OSX)
                ? (RuntimeInformation.ProcessArchitecture == Architecture.Arm64
                    ? "b4n1net-macos-arm64"
                    : "b4n1net-macos-x64")
                : RuntimeInformation.IsOSPlatform(OSPlatform.Windows)
                    ? "b4n1net-windows-amd64.exe"
                    : null;
        if (name == null)
        {
            return null;
        }

        var bundled = Path.Combine(AppContext.BaseDirectory, "bin", name);
        return File.Exists(bundled) ? bundled : null;
    }

    public string Version() => Text("--version");

    public string Help() => Text("help");

    public string Licenses() => Text("licenses");

    public string Status(bool json = false) => Text(WithJson(new[] { "status" }, json));

    public string Demo(bool json = false) => Text(WithJson(new[] { "demo" }, json));

    public string Docs(string? section = null) =>
        section == null ? Text("docs") : Text("docs", "--section", section);

    public string Serve(string addr, string? secret = null, bool json = false) =>
        Text(WithJson(WithSecret(new[] { "serve", "--addr", addr }, secret), json));

    public string Send(string addr, string? secret = null, string? message = null, bool json = false)
    {
        var args = new List<string>(WithSecret(new[] { "send", "--addr", addr }, secret));
        if (message != null)
        {
            args.Add("--message");
            args.Add(message);
        }
        return Text(WithJson(args.ToArray(), json));
    }

    public string Start(string? addr = null, string? secret = null, bool json = false)
    {
        var args = new List<string> { "start" };
        if (addr != null)
        {
            args.Add("--addr");
            args.Add(addr);
        }
        return Text(WithJson(WithSecret(args.ToArray(), secret), json));
    }

    public string Stop(bool json = false) => Text(WithJson(new[] { "stop" }, json));

    private static string[] WithSecret(string[] baseArgs, string? secret)
    {
        if (secret == null)
        {
            return baseArgs;
        }
        var args = new List<string>(baseArgs) { "--secret", secret };
        return args.ToArray();
    }

    private static string[] WithJson(string[] baseArgs, bool json)
    {
        if (!json)
        {
            return baseArgs;
        }
        var args = new List<string>(baseArgs) { "--json" };
        return args.ToArray();
    }

    private string Text(params string[] args)
    {
        var start = new ProcessStartInfo(_binary)
        {
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
        };
        foreach (var arg in args)
        {
            start.ArgumentList.Add(arg);
        }

        using var process = Process.Start(start)
            ?? throw new InvalidOperationException("could not start the b4n1-net engine");
        var output = process.StandardOutput.ReadToEnd();
        var error = process.StandardError.ReadToEnd();
        process.WaitForExit();
        return (output.Length > 0 ? output : error).Trim();
    }
}
