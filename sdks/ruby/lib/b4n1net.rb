# frozen_string_literal: true

# b4n1-net SDK — sovereign transport, Ruby wrapper.
#
# The gem ships the engine for each supported platform under bin/ and resolves
# the one that matches this machine. Every call is a thin spawn into that
# binary: the SDK never reimplements the wire protocol.
#
#   require "b4n1net"
#   client = B4n1Net::Client.new
#   puts client.version
#   puts client.demo
#
# Override the engine with B4N1NET_BIN_PATH.

require "open3"

module B4n1Net
  SDK_VERSION = "0.4.4"

  BINARIES = {
    ["linux", "x86_64"] => "b4n1net-linux-amd64",
    ["linux", "aarch64"] => "b4n1net-linux-arm64",
    ["darwin", "x86_64"] => "b4n1net-macos-x64",
    ["darwin", "arm64"] => "b4n1net-macos-arm64",
    ["mingw32", "x86_64"] => "b4n1net-windows-amd64.exe"
  }.freeze

  # Absolute path of the engine, or nil when this platform is not bundled.
  def self.binary
    override = ENV["B4N1NET_BIN_PATH"]
    return override if override && File.executable?(override)

    name = BINARIES[[RbConfig::CONFIG["host_os"].split("-").first, RbConfig::CONFIG["host_cpu"]]]
    return nil unless name

    bundled = File.expand_path(File.join(__dir__, "..", "bin", name))
    File.executable?(bundled) ? bundled : nil
  end

  class Client
    def initialize(binary_path = nil)
      @binary = binary_path || B4n1Net.binary
      raise "b4n1-net engine not found. Set B4N1NET_BIN_PATH." unless @binary
    end

    def version = text("--version")
    def help = text("help")
    def licenses = text("licenses")
    def status(json: false) = text("status", *(json ? ["--json"] : []))
    def demo(json: false) = text("demo", *(json ? ["--json"] : []))
    def docs(section: nil) = text("docs", *(section ? ["--section", section] : []))

    def serve(addr:, secret: nil, json: false)
      args = ["serve", "--addr", addr]
      args += ["--secret", secret] if secret
      args << "--json" if json
      text(*args)
    end

    def send(addr:, secret: nil, message: nil, json: false)
      args = ["send", "--addr", addr]
      args += ["--secret", secret] if secret
      args += ["--message", message] if message
      args << "--json" if json
      text(*args)
    end

    def start(addr: nil, secret: nil, json: false)
      args = ["start"]
      args += ["--addr", addr] if addr
      args += ["--secret", secret] if secret
      args << "--json" if json
      text(*args)
    end

    def stop(json: false) = text("stop", *(json ? ["--json"] : []))

    private

    def text(*args)
      stdout, stderr, _status = Open3.capture3(@binary, *args)
      (stdout.empty? ? stderr : stdout).strip
    end
  end
end
