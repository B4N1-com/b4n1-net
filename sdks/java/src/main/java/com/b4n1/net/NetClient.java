package com.b4n1.net;

/**
 * b4n1-net SDK — sovereign transport, Java wrapper.
 *
 * <p>The JAR ships the engine for each supported platform under {@code bin/}
 * and resolves the one that matches this machine. Every call is a thin spawn
 * into that binary: the SDK never reimplements the wire protocol.
 *
 * <pre>{@code
 * NetClient client = new NetClient();
 * System.out.println(client.version());
 * }</pre>
 *
 * <p>Override the engine with the {@code B4N1NET_BIN_PATH} environment variable.
 */
public final class NetClient {

    /** SDK version; it tracks the engine release. */
    public static final String SDK_VERSION = "0.4.3";

    private final String binary;

    public NetClient() {
        this(null);
    }

    public NetClient(String binaryPath) {
        String resolved = binaryPath != null ? binaryPath : resolveBinary();
        if (resolved == null) {
            throw new IllegalStateException(
                    "b4n1-net engine not found. Set B4N1NET_BIN_PATH.");
        }
        this.binary = resolved;
    }

    /** Absolute path of the engine, or {@code null} when this platform is not bundled. */
    public static String resolveBinary() {
        String override = System.getenv("B4N1NET_BIN_PATH");
        if (override != null && !override.isEmpty() && new java.io.File(override).canExecute()) {
            return override;
        }

        String os = System.getProperty("os.name", "").toLowerCase();
        String arch = System.getProperty("os.arch", "");
        String name;
        if (os.contains("linux")) {
            name = arch.equals("aarch64") ? "b4n1net-linux-arm64" : "b4n1net-linux-amd64";
        } else if (os.contains("mac")) {
            name = arch.equals("aarch64") ? "b4n1net-macos-arm64" : "b4n1net-macos-x64";
        } else if (os.contains("win")) {
            name = "b4n1net-windows-amd64.exe";
        } else {
            return null;
        }

        java.io.File bundled = new java.io.File(System.getProperty("user.dir"), "bin/" + name);
        return bundled.canExecute() ? bundled.getAbsolutePath() : null;
    }

    public String version() {
        return text("--version");
    }

    public String help() {
        return text("help");
    }

    public String licenses() {
        return text("licenses");
    }

    public String status(boolean json) {
        return text(json ? new String[] {"status", "--json"} : new String[] {"status"});
    }

    public String demo(boolean json) {
        return text(json ? new String[] {"demo", "--json"} : new String[] {"demo"});
    }

    public String docs(String section) {
        return section == null
                ? text("docs")
                : text("docs", "--section", section);
    }

    public String serve(String addr, String secret, boolean json) {
        return text(appendSecret(new String[] {"serve", "--addr", addr}, secret, json));
    }

    public String send(String addr, String secret, String message, boolean json) {
        String[] args = appendSecret(new String[] {"send", "--addr", addr}, secret, json);
        if (message == null) {
            return text(args);
        }
        String[] withMessage = java.util.Arrays.copyOf(args, args.length + 2);
        withMessage[args.length] = "--message";
        withMessage[args.length + 1] = message;
        return text(withMessage);
    }

    public String start(String addr, String secret, boolean json) {
        String[] base = addr == null ? new String[] {"start"} : new String[] {"start", "--addr", addr};
        return text(appendSecret(base, secret, json));
    }

    public String stop(boolean json) {
        return text(json ? new String[] {"stop", "--json"} : new String[] {"stop"});
    }

    private static String[] appendSecret(String[] base, String secret, boolean json) {
        java.util.List<String> args = new java.util.ArrayList<>(java.util.Arrays.asList(base));
        if (secret != null) {
            args.add("--secret");
            args.add(secret);
        }
        if (json) {
            args.add("--json");
        }
        return args.toArray(new String[0]);
    }

    private String text(String... args) {
        java.util.List<String> command = new java.util.ArrayList<>();
        command.add(binary);
        command.addAll(java.util.Arrays.asList(args));
        try {
            Process process = new ProcessBuilder(command).redirectErrorStream(true).start();
            String output = new String(
                    process.getInputStream().readAllBytes(),
                    java.nio.charset.StandardCharsets.UTF_8);
            process.waitFor();
            return output.trim();
        } catch (java.io.IOException | InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new IllegalStateException("b4n1-net engine call failed", error);
        }
    }
}
